# Real-Time Stock Market Insights & Reporting Pipeline

The project implements a real-time data pipeline that extracts stock data from vantage API, streams it through Apache kafka, processes it with Apache Spark, and loads it into a postgres database. The project integrates modern data engineering tools to ensure scalability, reliability, and performance.

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
- Python 3.10+ (Installed on your computer)
- Docker & Docker Compose (Installed on your computer)
- Kafka cluster (local or cloud)
- Spark 3.x
- PostgreSQL 17+
- Power BI Desktop (Installed on your computer) or Power BI Service

---

## Architecture Diagram Guide (Draw.io)

### 1. Creating the Diagram
- Open **https://draw.io** and start a new blank diagram.
- Download icons for:
  - Power BI  
  - Kafka  
  - API  
  - Docker  
  - Spark  
  - PostgreSQL  
- Import icons by copying and pasting them into the canvas.

### 2. Structuring the Pipeline
Arrange components in a left‑to‑right flow:

**Data Source → Ingestion → Processing → Storage → Visualization**

- Position each tool icon in the correct stage.
- Connect components by dragging arrows from one element to the next.

### Styling Connections
- Change line colour (e.g., black) for clarity.
- Optional animation:
  - Select all arrows (Ctrl + Click)
  - Enable **Flow Animation** in the Style panel.

---

## API Integration (RapidAPI)

### 1. Create an Account
- Visit **https://rapidapi.com**
- Sign up or log in.

### 2. Generate an API Key
- Open the **Console**.
- Create a new application or use the default.
- Copy your API key.

### 3. Secure the Key
- Store it in environment variables or config files.
- Avoid hardcoding it in your source code.

---

## Data Source Setup (Alpha Vantage API)

### Steps
- Search for **Alpha Vantage** on RapidAPI.
- Subscribe if required.
- Test endpoints using Python + `requests`.

### Example API Call

```python
import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "AAPL",
    "interval": "5min"
}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

```

## Running the Project (High-Level)
### Clone the Repository

```bash

  git clone https://github.com/BinahUtuedor/Real-Time-Stock-Market-Analysis

```
---
### Install dependencies

```bash
  cd real-time-stock-market-analysis
  pip install -r requirements.txt

```
---
### Start services using Docker:

```bash
   docker-compose up -d
```
---
## Configure kafka
- Visit: localhost:8085 and configure a new cluster with credentials:
- cluster name: Stock_Market_analysis
- Bootstrap Servers: kafka
- Port: 9092

---

### Run Kafka producers:

```bash
   python producer/main.py
```
This sends data to the pyspark consumer

---

### Stop services running on Docker:

```bash
   docker-compose down
```

**To removes everything created by a Docker Compose project including all associated volumes, run:**

```bash
docker-compose down -v

```
---
## PostgreSQL and Power BI Integration Guide

This guide provides a complete workflow for connecting to PGAdmin, configuring access to the PostgreSQL server, creating the `stock_data` database and `stocks` table, streaming data into the database, and finally connecting PostgreSQL to Power BI for visualisation.

---

## PGAdmin Access

### Logging into PGAdmin
1. Open your browser and go to **http://localhost:5050**.
2. Log in using the credentials defined in the `docker-compose.yml` file:

   - **Email:** `admin@admin.com`  
   - **Password:** `admin`

---

## Registering the PostgreSQL Server in PGAdmin

### Creating the Server Connection
1. In PGAdmin, right‑click **Servers** → **Register** → **Server**.
2. Under the **General** tab:
   - **Name:** `stock_data`

3. Under the **Connection** tab, enter the PostgreSQL configuration from the Compose file:
   - **Hostname/address:** `postgres`
   - **Port:** `5432`
   - **Username:** `admin`
   - **Password:** `admin`

4. Click **Save**.

## Database and Table Setup
The `stock_data` database and `stocks` table may be created automatically by your pipeline. If they are not present:

### Creating the Database
1. Expand the server.
2. Right‑click **Databases** → **Create** → **Database**.
3. Enter the name: `stock_data`.
4. Click **Save**.

### Creating the Table
1. Expand the `stock_data` database.
2. Go to **Schemas → public → Tables**.
3. Right‑click **Tables** → **Query Tool**.
4. Run the SQL below to create the table:

```sql
CREATE TABLE stocks (
    date TIMESTAMP WITHOUT TIME ZONE,
    symbol VARCHAR(10),
    open VARCHAR(10),
    low VARCHAR(10),
    high VARCHAR(10),
    close VARCHAR(10)
);
```
- This creates an empty stocks table ready for ingestion.

---

## Streaming Data into PostgreSQL
To populate the table with live or batch data:

```python
python producer/main.py
```

- Rebuild containers whenever application code changes:

```python
docker compose up --build
```
## Connecting PostgreSQL to Power BI
### Steps in Power BI Desktop
- Launch Power BI Desktop.
- On the Home tab, select Get Data.
- Click More.
- Search for PostgreSQL Database and select it.
- Click Connect.

### Connection Parameters
- In the connection dialog:
- Server: localhost:5434
- Database: stock_data
- Click OK.
- If prompted for credentials:
- Username: admin
- Password: admin
- Click Connect.
- If an encryption support message appears, click OK to proceed.

---
## Contact
- For questions or collaboration, feel free to reach out.