import requests
import pandas as pd
import json

API_KEY = "860972832ec6b6fb41a84e2352919cad"

url = "https://api.marketstack.com/v2/eod"

params = {
    "access_key": API_KEY,
    "symbols": "AAPL",
    "limit": 5   # small sample for inspection
}

response = requests.get(url, params=params)
data = response.json()

# -----------------------------
# RAW JSON STRUCTURE
# -----------------------------
print("\n===== FULL JSON STRUCTURE =====\n")
print(json.dumps(data, indent=2))


# -----------------------------
# EXTRACT DATA LIST
# -----------------------------
rows = data["data"]

# -----------------------------
# FLATTEN NESTED JSON
# -----------------------------
df = pd.json_normalize(rows)

# -----------------------------
# SAVE CSV
# -----------------------------
df.to_csv("full_stock_data.csv", index=False)
print("\nCSV Saved → full_stock_data.csv")


# -----------------------------
# ALL COLUMN NAMES
# -----------------------------
print("\n===== ALL COLUMN NAMES =====\n")
for col in df.columns:
    print(col)


# -----------------------------
# DATA TYPES
# -----------------------------
print("\n===== COLUMN DATA TYPES =====\n")
print(df.dtypes)


# -----------------------------
# SAMPLE ROW PREVIEW
# -----------------------------
print("\n===== SAMPLE ROW =====\n")
print(df.iloc[0])


# -----------------------------
# FULL DATA OVERVIEW
# -----------------------------
print("\n===== DATAFRAME INFO =====\n")
print(df.info())

print("\n===== STATISTICS =====\n")
print(df.describe(include="all"))
