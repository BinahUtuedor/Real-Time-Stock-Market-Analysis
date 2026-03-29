# Real-Time Stock Market Insights & Reporting Pipeline

The project implements a real-time data pipeline that extracts stock data from vantage API, streams it through Apache kafka, processes it with Apache Spark, and loads it into a postgres database.

All components are containerised with Docker for easy deployment.

---

## Key Objectives

| Objective | Description |
|-----------|-------------|
| **Scalable Data Pipeline** | High-performance, fault-tolerant pipeline using Kafka + Spark |
| **Real-Time Analytics** | Process streaming stock market data as it arrives |
| **Faster Decision-Making** | Reduce latency and improve responsiveness |
| **Actionable Insights** | Deliver real-time insights through Power BI dashboards |
| **Operational Reliability** | Monitor, alert, and containerize for consistent deployment |

---

## Data Pipeline Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Data ingestion, API integration, utilities |
| **Apache Kafka** | Real‑time data streaming and buffering |
| **Apache Spark** | Distributed stream processing & analytics |
| **PostgreSQL** | Curated storage and historical reporting |
| **Docker** | Containerization and portable deployment |
| **Power BI** | Interactive dashboards and visualization |

---

## Data Pipeline Architecture
The pipeline follows a modern real-time data architecture:

![Data Pipeline Architecture](./img/real_time_pipeline.jpg)

---

## Data Pipeline Work Flow
- `API → produces JSON events into kafka.`
- `kafka UI →inspect topics/messages.`
- `Spark → consumes from kafka, writes to postgres.`
- `Postgres → stores results for analytics.`
- `pgAdmin → manage Postgres visually.`
- `Power BI → external (connects to Postgres database).`

---

## Expected Outcomes

- **Scalable Streaming Pipeline**  
  Continuous, low-latency data processing from multiple sources  

- **Real-Time Insights**  
  Dashboards showing stock trends, trading volumes, and sentiment  

- **Operational Efficiency**  
  Reduced processing delays and improved reliability  

- **Improved Client Satisfaction**  
  Faster, data-driven decision-making capabilities  

---

## Sample Use Cases
- Real-time stock price monitoring
- Trading volume analysis
- Sentiment-driven trading signals
- Market anomaly detection

---

## Getting Started
### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Kafka cluster (local or cloud)
- Spark 3.x
- PostgreSQL 17+
- Power BI Desktop or Power BI Service

---

### Installation

```bash
git clone https://github.com/BinahUtuedor/Real-Time-Stock-Market-Analysis
cd real-time-stock-market-analysis
pip install -r requirements.txt

```

### Running the Project (High-Level)

```bash
1. Start services using Docker:
   docker-compose up -d

2. Run Kafka producers:
   python producer/main.py

```

