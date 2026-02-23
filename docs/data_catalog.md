# 📊 Data Catalog — Stock Market EOD Dataset

## 1. Dataset Overview

**Dataset Name:** StockSense EOD Market Dataset
**Source:** Marketstack API
**Update Frequency:** Daily (End-of-Day)
**Granularity:** One row per symbol per trading day
**Primary Use:** Machine Learning + Financial Analysis

---

## 2. Table Schema

**Table Name:** `stock_prices`

| Column         | Type   | Nullable | Description            | ML Usage        |
| -------------- | ------ | -------- | ---------------------- | --------------- |
| open           | float  | No       | Opening price of stock | ✔               |
| high           | float  | No       | Highest price of day   | ✔               |
| low            | float  | No       | Lowest price of day    | ✔               |
| close          | float  | No       | Closing price          | ✔               |
| volume         | float  | No       | Total traded shares    | ✔               |
| adj_high       | float  | No       | Adjusted high price    | ✔               |
| adj_low        | float  | No       | Adjusted low price     | ✔               |
| adj_close      | float  | No       | Adjusted closing price | ⭐ Primary       |
| adj_open       | float  | No       | Adjusted opening price | ✔               |
| adj_volume     | float  | No       | Adjusted volume        | ✔               |
| split_factor   | float  | No       | Stock split ratio      | Optional        |
| dividend       | float  | No       | Dividend paid          | Optional        |
| name           | string | No       | Company name           | Metadata        |
| exchange_code  | string | No       | Exchange code          | Metadata        |
| asset_type     | string | No       | Asset category         | Metadata        |
| price_currency | string | No       | Price currency         | Metadata        |
| symbol         | string | No       | Ticker symbol          | Identifier      |
| exchange       | string | No       | Exchange name          | Metadata        |
| date           | string | No       | Trading date           | ⭐ Primary Index |
|                |        |          |                        |                 |

---

## 3. Primary Keys

Composite key:

```
(symbol, date)
```

Reason:

* multiple companies
* multiple dates

---

## 4. Column Categories

### Price Features

Used for modeling:

```
open
high
low
close
adj_close
volume
```

---

### Adjusted Price Features

Used for historical consistency:

```
adj_open
adj_high
adj_low
adj_close
adj_volume
```

---

### Corporate Action Columns

```
split_factor
dividend
```

Purpose:
Explain sudden price shifts.

---

### Metadata Columns

Not used for prediction but useful for filtering:

```
name
exchange_code
asset_type
price_currency
symbol
exchange
```

---

## 5. Data Constraints

| Rule                   | Description               |
| ---------------------- | ------------------------- |
| Price ≥ 0              | Prices must be positive   |
| Volume ≥ 0             | Volume cannot be negative |
| Date unique per symbol | No duplicates allowed     |
| Split factor ≥ 1       | Split ratios valid        |

---

## 6. Data Quality Checks

Validation rules applied during ingestion:

* remove duplicate rows
* ensure chronological order
* validate numeric ranges
* verify missing values
* detect outliers

---

## 7. Recommended Columns for ML Models

Minimum feature set:

```
adj_close
volume
high
low
open
```

Extended feature set:

```
returns
moving averages
volatility
momentum indicators
```

---

## 8. Indexing Strategy

Recommended indexes for database:

```
INDEX(symbol)
INDEX(date)
INDEX(symbol, date)
```

This ensures fast queries.

---

## 9. Data Retention Policy

| Policy             | Value     |
| ------------------ | --------- |
| Historical storage | unlimited |
| Update frequency   | daily     |
| Backup frequency   | weekly    |

---

## 10. Known Limitations

* Dataset does not include news sentiment
* No intraday data
* Limited historical data (free tier)
* No macroeconomic indicators

---
