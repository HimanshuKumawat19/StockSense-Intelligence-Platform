# Company Symbol Reference — StockSense Intelligence Platform

## Overview

This document lists the official stock ticker symbols used in the StockSense dataset. These symbols identify publicly traded companies and are used when fetching market data from the Marketstack API.

Each symbol uniquely represents a company on a stock exchange and acts as the primary identifier when querying financial data.

---

## What Is a Stock Symbol?

A **stock symbol (ticker)** is a short code assigned to a publicly traded company.

Example:

```
AAPL → Apple Inc.
```

Instead of typing full company names, financial systems use symbols to request market data efficiently.

---

## Selected Companies for Dataset

The following companies were selected for training and testing machine learning models because they:

* have high trading volume
* are financially stable
* belong to different industries
* provide realistic market patterns

---

## Symbol Table

| Symbol | Company Name         | Sector             | Exchange |
| ------ | -------------------- | ------------------ | -------- |
| AAPL   | Apple Inc.           | Technology         | NASDAQ   |
| MSFT   | Microsoft Corp.      | Technology         | NASDAQ   |
| GOOGL  | Google               | Technology         | NASDAQ   |
| AMZN   | Amazon.com Inc.      | Consumer Tech      | NASDAQ   |
| NVDA   | NVIDIA Corp.         | Semiconductors     | NASDAQ   |
| META   | Meta Platforms Inc.  | Social Media       | NASDAQ   |
| TSLA   | Tesla Inc.           | Automotive/AI      | NASDAQ   |
| JPM    | JPMorgan Chase & Co. | Banking            | NYSE     |
| V      | Visa Inc.            | Financial Services | NYSE     |
| WMT    | Walmart Inc.         | Retail             | NYSE     |

---

## Why These Symbols Were Chosen

This set ensures:

* sector diversity
* volatility variation
* realistic financial behavior
* strong liquidity
* reliable data consistency

Using multiple sectors improves machine learning generalization and prevents overfitting to one company’s behavior.

---

## Symbol Usage in System

Symbols are used in:

### Data Fetching

```
GET /eod?symbols=AAPL
```

### Storage

Symbols act as a unique identifier:

```
PRIMARY KEY = (symbol, date)
```

### Model Training

Symbols allow multi-company training datasets:

```
Dataset = combined rows of all symbols
```

---

## Naming Convention Rules

All symbols follow exchange standards:

* uppercase letters
* no spaces
* unique per company

Examples:

```
AAPL ✔
TSLA ✔
Apple ✖
```

---

## Future Expansion

Additional companies can be added by inserting their symbol into the data pipeline configuration:

```
symbols = "AAPL,MSFT,GOOGL"
```

No schema changes required.

---

## Notes

* Symbols remain constant even if company name changes
* Historical data remains tied to symbol
* Delisted stocks may stop updating

---

## Summary

Stock symbols serve as the core identifier for all financial data operations in the StockSense platform. Proper symbol management ensures:

* accurate data retrieval
* consistent storage
* scalable dataset growth
* reliable ML training

---

**Document Version:** 1.0
**Maintained By:** StockSense Data System
**Last Updated:** {{auto_update_on_commit}}
