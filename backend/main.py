# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# --- 1. SETUP ---
# Create FastAPI app instance
app = FastAPI(title="Health Insurance Fraud Detection API", version="1.0")

# Configure CORS (Cross-Origin Resource Sharing)
# This allows our React frontend (running on a different port) to communicate with this API
origins = [
    "http://localhost:3000", # The default port for React app
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- 2. LOAD SAVED ARTIFACTS ---
# Load the preprocessor and the model once when the application starts
preprocessor = joblib.load('backend/preprocessor.joblib')
model = joblib.load('backend/model.joblib')


# --- 3. DEFINE INPUT DATA SCHEMA ---
# Pydantic model to define the structure and data types for incoming request data
# These fields MUST match the columns used for training the model
class ClaimInput(BaseModel):
    claim_amount: float
    age: int
    gender: str
    location_policyholder: str
    location_hospital: str
    procedure_code: str


# --- 4. CREATE API ENDPOINT ---
@app.post("/predict")
def predict_fraud(claim_input: ClaimInput):
    """
    Receives claim data, preprocesses it, and returns a fraud prediction.
    """
    # Convert the incoming Pydantic model to a pandas DataFrame
    # This is necessary because our preprocessor was trained on a DataFrame
    input_df = pd.DataFrame([claim_input.model_dump()])

    # Preprocess the input data using the loaded preprocessor
    processed_input = preprocessor.transform(input_df)

    # Make a prediction using the loaded model
    prediction = model.predict(processed_input)
    prediction_proba = model.predict_proba(processed_input)

    # Extract the probability of fraud (the second class)
    fraud_probability = prediction_proba[0][1]

    # Return the results in a JSON response
    return {
        "is_fraudulent": bool(prediction[0]),
        "fraud_probability": float(fraud_probability)
    }