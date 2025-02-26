from google.cloud import bigquery
import pandas as pd

# Authenticate Google client
client = bigquery.Client.from_service_account_json("houseprediction.json")

# Query house price data
query = """
SELECT * FROM `houseprediction-452100.house_prices.train_data`
LIMIT 10;
"""
df = client.query(query).to_dataframe()

# Show data
print(df.head())