from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, FloatType
from pyspark.sql.functions import from_json, col
import os


# Directory where Spark will store its checkpoint data. Crucial in streaming fault tolerance
checkpoint_dir = "/tmp/checkpoint/kafka_to_postgres"
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)



# The schema structure matching the new data coming from kafka 
kafka_data_schema = StructType([
    StructField("date", StringType(), True),
    StructField("high", StringType(), True),
    StructField("low", StringType(), True),
    StructField("open", StringType(), True),
    StructField("close", StringType(), True),
    StructField("symbol", StringType(), True)
])

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "stock_analysis") \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", "false") \
    .load() # start reading the kafka topic as a stream


# convert the 'value' column (which is a JSON string) into structured columns
parsed_df = df.selectExpr('CAST(value AS STRING)') \
            .select(from_json(col("value"), kafka_data_schema).alias("data")) \
            .select("data.*")


processed_df = parsed_df.select([
    col("date").cast(TimestampType()).alias("date"),
    col("high").alias("high"),
    col("low").alias("low"),
    col("open").alias("open"),
    col("close").alias("close"),
    col("symbol").alias("symbol")
])

#display the results to the terminal (console output mode)
query = processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .option("checkpointLocation", checkpoint_dir) \
    .start()

#wait for the termination of the query
query.awaitTermination()

