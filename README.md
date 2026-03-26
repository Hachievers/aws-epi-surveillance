# AWS Epidemiological Surveillance Pipeline

A fully serverless, cloud-native disease surveillance system built on AWS that simulates how real outbreak reports are collected, stored, queried, and analyzed for epidemiological insight.

This project demonstrates how API ingestion, event-driven storage, serverless querying, and Python analytics combine to form a real-time digital public health surveillance pipeline.

---

## Project Overview

This system simulates disease case reporting (mpox) and processes the data through:

API → Lambda → S3 → Athena → Python Visualization



You will see how outbreak data flows from ingestion to epidemic curve visualization **without managing a single server**.

---

## Architecture

*Insert architecture diagram here*

---

## AWS Services Used

- **Amazon API Gateway** — receives case reports  
- **AWS Lambda** — processes and stores data  
- **Amazon S3** — raw JSON storage  
- **Amazon Athena** — SQL querying on S3 data  

---

## What This Simulates

- Digital disease reporting  
- Outbreak monitoring  
- Geographic spread analysis  
- Vaccination coverage analysis  
- Epidemic curve generation  

---

## Step-by-Step Deployment

### 1️⃣ Create S3 Bucket

Create a bucket:epi-surveillance-data-adekunle



Leave all defaults.

---

### 2️⃣ Create Lambda Function

**Runtime:** Python 3.11  

**Lambda code:**

```python
import json
import boto3
from datetime import datetime
import uuid

s3 = boto3.client('s3')
BUCKET = 'your-bucket-name'

def lambda_handler(event, context):
    data = json.loads(event['body'])
    now = datetime.utcnow()

    key = f"raw/disease={data['disease']}/year={now.year}/month={now.month}/day={now.day}/{uuid.uuid4()}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data)
    )

    return {"statusCode": 200, "body": "stored"}
```

Give Lambda permission to write to S3.

---

### 3️⃣ Create API

In API Gateway:

Type: HTTP API

Route: POST /report

Integration: Lambda

Copy your Invoke URL.


---
### 4️⃣ Generate Synthetic Data

Run(bash):

```python generate_epi_data.py```

This sends 300 case reports into your pipeline.


---
### 5️⃣ Create Athena Table

```CREATE EXTERNAL TABLE epi_db.epi_reports (
  patient_id string,
  age int,
  location string,
  symptoms array<string>,
  vaccinated boolean,
  timestamp string
)
PARTITIONED BY (disease string, year string, month string, day string)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-bucket-name/raw/';
```

Then run:
```MSCK REPAIR TABLE epi_db.epi_reports;```


---
### 6️⃣ Query Epidemic Curve

```SELECT
  date(
    date_parse(substr("timestamp",1,19),'%Y-%m-%dT%H:%i:%s')
  ) AS report_date,
  COUNT(*) AS cases
FROM epi_db.epi_reports
GROUP BY 1
ORDER BY 1;
```

Download results as epi_raw.csv


### 7️⃣ Visualize in Python

Run(bash):

```python visualize_epi.py```

You will see:

Epidemic curve
Cases by location
Vaccination distribution
Age distribution

Insert visualization images here





