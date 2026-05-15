'''from fastapi import FastAPI
from pydantic import BaseModel
import joblib
#import psycopg2

# -------------------------
# Load model (GLOBAL)
# -------------------------
model = joblib.load("models/model.pkl")

# -------------------------
# Database connection (MOVE UP)
# -------------------------
conn = psycopg2.connect(
    dbname="predictive_maintenance",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# -------------------------
# Initialize app
# -------------------------
app = FastAPI()

# -------------------------
# Request schema
# -------------------------
class MachineData(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float

# -------------------------
# Routes
# -------------------------
@app.get("/")
def home():
    return {"message": "Predictive Maintenance API is running"}

@app.post("/predict")
def predict(data: MachineData):
    input_data = [[
        data.air_temperature,
        data.process_temperature,
        data.rotational_speed,
        data.torque,
        data.tool_wear
    ]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # -------------------------
    # Insert into database
    # -------------------------
    print("Saving to DB...")
    cursor.execute(
        """
        INSERT INTO predictions (
            air_temperature,
            process_temperature,
            rotational_speed,
            torque,
            tool_wear,
            prediction,
            confidence
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            data.air_temperature,
            data.process_temperature,
            data.rotational_speed,
            data.torque,
            data.tool_wear,
            int(prediction),
            float(probability)
        )
    )

    conn.commit()

    return {
        "prediction": "Failure" if prediction == 1 else "No Failure",
        "confidence": round(probability, 2)
    }
'''

from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model
model = joblib.load("models/model.pkl")

# Initialize app
app = FastAPI()

# Request schema
class MachineData(BaseModel):
    air_temperature: float
    process_temperature: float
    rotational_speed: float
    torque: float
    tool_wear: float

# Home route
@app.get("/")
def home():
    return {"message": "Predictive Maintenance API is running"}

# Prediction route
@app.post("/predict")
def predict(data: MachineData):

    input_data = [[
        data.air_temperature,
        data.process_temperature,
        data.rotational_speed,
        data.torque,
        data.tool_wear
    ]]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": "Failure" if prediction == 1 else "No Failure",
        "confidence": round(probability, 2)
    }