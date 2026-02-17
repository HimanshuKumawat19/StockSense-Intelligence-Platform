import requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://api.marketstack.com/v2/eod"

params = {
    "access_key": API_KEY,
    "symbols": "AAPL",
    "limit": 100   # change if needed
}

response = requests.get(url, params=params)
data = response.json()

# extract rows
rows = data["data"]

# convert to dataframe
df = pd.DataFrame(rows)

# save csv
df.to_csv("stock_data.csv", index=False)

print("CSV saved successfully as stock_data.csv")

# inspect one row (schema example)
print("\nCOLUMNS PRESENT IN DATA:\n")
print(df.columns.tolist())

print("\nEXAMPLE ROW DATA:\n")
print(df.iloc[0])
