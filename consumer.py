from kafka import KafkaConsumer
import json
import time


# ---- Configure matching Produccer -----

consumer = KafkaConsumer(
    'stock_analysis',  # topic name
    bootstrap_servers='localhost:9094',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group', # Define a consumer group
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Starting kafka consumer. Waiting foor messages on topic 'stock_analyis'...")

# Read messages from Kafka
for message in consumer:
    data = message.value
    print("Received message:")    
    # Print the received data
    print(f"  value (Deserialized): {data}")

consumer.close()
print("kafka consumer closed.")
