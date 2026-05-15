# Predictive Maintenance API

A deployed end-to-end machine learning API that predicts equipment failure using industrial sensor data.

## Live Demo

* Live API: [https://ml-api-am9f.onrender.com/](https://ml-api-am9f.onrender.com/)
* Swagger Docs: [https://ml-api-am9f.onrender.com/docs](https://ml-api-am9f.onrender.com/docs)
* GitHub Repository: https://github.com/Dnasam/predictive-maintenance-api

---

# Project Overview

This project simulates how machine learning models are operationalized in backend systems.

The system:

* trains a machine learning model using equipment sensor data
* predicts machine failure probability
* exposes predictions through a FastAPI REST API
* supports real-time inference requests
* is deployed publicly using Render

---

# Problem Statement

Modern manufacturing environments rely heavily on continuous machine operations, where unexpected equipment failures can lead to production delays, increased maintenance costs, and operational inefficiencies.

Traditional maintenance approaches are often reactive, meaning issues are addressed only after machine breakdowns occur. This creates avoidable downtime and impacts productivity.

This project explores how machine learning can be used to shift from reactive maintenance to predictive maintenance by analyzing real-time sensor readings and identifying patterns associated with potential machine failures before they occur.

The system uses industrial sensor parameters such as:

air temperature
process temperature
rotational speed
torque
tool wear

to predict whether a machine is likely to fail under given operating conditions.

The objective is to simulate how ML-powered monitoring systems can support smarter maintenance decisions in industrial environments.

---

# Tech Stack

| Category            | Technologies  |
| ------------------- | ------------- |
| Programming         | Python        |
| Machine Learning    | Scikit-learn  |
| Data Processing     | Pandas, NumPy |
| Backend API         | FastAPI       |
| Model Serialization | Joblib        |
| Deployment          | Render        |
| Database (Local)    | PostgreSQL    |
| Version Control     | Git, GitHub   |

---

# Machine Learning Workflow

## Dataset

Used the AI4I Predictive Maintenance Dataset containing industrial machine sensor readings.

## Preprocessing Steps

* Removed unnecessary identifier columns
* Selected relevant numerical features
* Performed train-test split
* Prepared structured input data for model training

## Models Trained

### Logistic Regression

* Used as a simple baseline model
* Easy to interpret and fast to train

### Random Forest Classifier

* Better handling of non-linear relationships
* Improved recall and prediction performance
* Selected as final model

## Final Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~97%     |
| Random Forest       | ~98%     |

---

# API Architecture

```text
User Request
      ↓
FastAPI Backend
      ↓
Trained ML Model (.pkl)
      ↓
Prediction Response
```

---

# API Endpoints

## Root Endpoint

```http
GET /
```

Returns API status.

---

## Prediction Endpoint

```http
POST /predict
```

### Sample Request

```json
{
  "air_temperature": 298.1,
  "process_temperature": 308.6,
  "rotational_speed": 1551,
  "torque": 42.8,
  "tool_wear": 0
}
```

### Sample Response

```json
{
  "prediction": "No Failure",
  "confidence": 0.03
}
```

---

# Project Structure

```text
predictive-maintenance-api/
│
├── data/
│   └── ai4i2020.csv
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── app.py
│   └── __init_.py
|   └── train_model.py
|   └── .gitignore
│
├── requirements.txt
├── runtime.txt
├── README.md

```

---

# Local Setup Instructions

## 1. Clone Repository

```bash
git clone (https://github.com/Dnasam/predictive-maintenance-api)
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run FastAPI Server

```bash
uvicorn src.app:app --reload
```

---

## 6. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Deployment

The API is deployed publicly using Render.

Deployment includes:

* FastAPI backend
* trained ML model
* public REST endpoints
* Swagger documentation

---

# Key Learnings


* how machine learning models are deployed as APIs
* how FastAPI handles request/response workflows
* model serialization using Joblib
* REST API development and testing
* GitHub-based deployment workflows
* basics of PostgreSQL integration

---

# Future Improvements

Potential future enhancements:

* Docker containerization
* Cloud PostgreSQL integration
* Authentication and API keys
* Frontend dashboard
* CI/CD automation
* Model monitoring and logging

---


