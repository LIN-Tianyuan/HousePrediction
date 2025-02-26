# HousePrediction
Build, deploy, monitor, and automate training of house price prediction model
（With Google Big Query）
## Google Big Query
### 1. Install Google Cloud SDK
```bash
pip install google-cloud-bigquery
```
### 2. Authentication Google Cloud
Go to Google Cloud IAM & Admin

Create a Service Account

Download the JSON Key and save it as “xxx.json”

### 3. Install db-dtypes
```bash
pip install db-dtypes
```

### 4. Error
Error 1:
```bash
The project houseprediction has not enabled BigQuery.
```
Need use project id.
```python
query = """
SELECT * FROM `houseprediction-452100.house_prices.train_data`
LIMIT 10;
"""
```
Error 2:
```bash
User does not have bigquery.jobs.create permission in project houseprediction-452100.
```
```bash
Create service account:
Grant this service account access to project:
BigQuery User/BigQuery Data Viewer/BigQuery Admin
```
## Notice

```bash
which python
```