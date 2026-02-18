import requests
import pandas as pd
import json
import os
import time
from dotenv import load_dotenv

# -----------------------------
# LOAD API KEY
# -----------------------------
load_dotenv()
API_KEY = os.getenv("API_KEY")

# -----------------------------
# API CONFIG
# -----------------------------
URL = "https://api.marketstack.com/v2/eod"
SYMBOL = "AAPL"
LIMIT = 1000   # max allowed per request

all_rows = []
offset = 0

print("\nFetching data...\n")

# -----------------------------
# PAGINATION LOOP
# -----------------------------
while True:
    params = {
        "access_key": API_KEY,
        "symbols": SYMBOL,
        "limit": LIMIT,
        "offset": offset
    }

    response = requests.get(URL, params=params)
    data = response.json()

    # Debug safety
    if "data" not in data:
        print("Error:", data)
        break

    rows = data["data"]

    # Stop if no more data
    if not rows:
        break

    all_rows.extend(rows)

    print(f"Fetched {len(rows)} rows (Total: {len(all_rows)})")

    offset += LIMIT

    # avoid hitting rate limit
    time.sleep(1)


print("\nTotal rows collected:", len(all_rows))


# -----------------------------
# FLATTEN JSON → DATAFRAME
# -----------------------------
df = pd.json_normalize(all_rows)

# -----------------------------
# SORT BY DATE (old → new)
# -----------------------------
df = df.sort_values("date")


# -----------------------------
# SAVE CSV
# -----------------------------
df.to_csv("AAPL_full_data.csv", index=False)
print("\nCSV Saved → AAPL_full_data.csv")


# -----------------------------
# PRINT FULL JSON SAMPLE
# -----------------------------
print("\n===== SAMPLE JSON ROW =====\n")
print(json.dumps(all_rows[0], indent=2))


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
# SAMPLE ROW
# -----------------------------
print("\n===== SAMPLE ROW =====\n")
print(df.iloc[0])


# -----------------------------
# DATAFRAME INFO
# -----------------------------
print("\n===== DATAFRAME INFO =====\n")
print(df.info())


# -----------------------------
# STATISTICS
# -----------------------------
print("\n===== STATISTICS =====\n")
print(df.describe(include="all"))
