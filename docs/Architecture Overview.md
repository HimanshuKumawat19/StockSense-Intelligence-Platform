

`MarketStack API
        ↓
Data Update Service (Python + Cron)
        ↓
PostgreSQL Database
        ↓
Training Service (XGBoost)
        ↓
Model Storage (S3 / Local Disk)
        ↓
FastAPI (Inference API)
        ↓
Client / User
`


The system follows a cyclic ML production workflow:

- Data → Training → Deployment → Monitoring → Retraining
    

---

# 🚀 Tech Stack

|Layer|Technology|
|---|---|
|Data Source|MarketStack API|
|Backend Language|Python|
|ML Model|XGBoost|
|API Framework|FastAPI|
|Database|PostgreSQL|
|Containerization|Docker|
|Deployment|AWS EC2|
|Reverse Proxy (Optional)|Nginx|
|Model Storage|S3 or EC2 disk|

---

# 📂 Project Structure

stock-predictor/
│
├── data_service/
│   ├── fetch_data.py
│   └── cron_job.sh
│
├── training_service/
│   ├── train.py
│   ├── feature_engineering.py
│   └── evaluate.py
│
├── inference_api/
│   ├── main.py
│   ├── model_loader.py
│   └── schemas.py
│
├── models/
│   ├── model_v1.pkl
│   ├── scaler.pkl
│   └── metadata.json
│
├── docker-compose.yml
└── README.md

---

# 🔁 System Workflow

## 1️⃣ Initial Setup

1. Fetch historical stock data
    
2. Store in PostgreSQL
    
3. Generate technical indicators
    
4. Train XGBoost model
    
5. Save model artifact
    
6. Deploy FastAPI service
    

---

## 2️⃣ Daily Automated Update

Scheduled job runs after market close:

- Fetch latest stock data
    
- Append to database
    
- Recompute features
    
- Retrain model
    
- Save new model version if performance improves
    

---

## 3️⃣ User Prediction Flow

When user sends request:

`POST /predict?ticker=AAPL`

System:

1. Loads latest trained model
    
2. Fetches latest features from DB
    
3. Runs prediction
    
4. Logs input + prediction
    
5. Returns JSON response
    

Example response:

`{`
  `"ticker": "AAPL",`
  `"prediction": "UP",`
  `"confidence": 0.63,`
  `"model_version": "v3"`
`}`


---

# 📊 Logging & Monitoring

The system logs:

### Input Log

- Timestamp
    
- Ticker
    
- Feature values
    
- Model version
    

### Prediction Log

- Predicted direction
    
- Confidence score
    
- Actual next-day result
    
- Accuracy metrics
    

This enables:

- Model performance tracking
    
- Drift detection
    
- Model rollback if necessary
    

---

# 🧠 Model Strategy

- Problem Type: Binary Classification (Up/Down)
    
- Model: XGBoost
    
- Features:
    
    - RSI
        
    - EMA
        
    - MACD
        
    - Volatility
        
    - Lag values
        
- Evaluation Metrics:
    
    - Accuracy
        
    - Precision
        
    - Recall
        
    - F1 Score
        

Expected realistic performance:

- 55–60% directional accuracy (good for daily stocks)
    

---

# 🐳 Docker Deployment

Run services using:

`docker-compose up --build`

Services:

- Data Update Service
    
- Training Service
    
- FastAPI Inference Service
    
- PostgreSQL (if not using RDS)
    

---

# ☁ AWS Deployment

Recommended setup:

- EC2 Instance (Docker Host)
    
- RDS PostgreSQL (optional but recommended)
    
- S3 (optional for model storage)
    
- Nginx (reverse proxy)
    

---

# 🔐 Environment Variables

Create `.env` file:

`MARKETSTACK_API_KEY=your_key DATABASE_URL=postgresql://user:pass@host:5432/db MODEL_PATH=/models/model.pkl`

---

# ⚠ Limitations

- Stock markets are noisy and non-stationary
    
- Short-term prediction accuracy is limited
    
- Model retraining frequency affects stability
    
- External news/events not included (can be extended)