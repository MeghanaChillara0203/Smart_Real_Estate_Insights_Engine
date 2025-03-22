from fastapi import FastAPI
import joblib
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load the trained Random Forest model
model = joblib.load("../model/final_rent_price_model.pkl")

# Define the input schema for the API
@app.post("/predict/")
def predict(features: dict):
    try:
        # Convert input dictionary to DataFrame
        df = pd.DataFrame([features])

        # Ensure feature order matches training data
        prediction = model.predict(df)

        # Return the predicted rent price
        return {"predicted_rent": float(prediction[0])}

    except Exception as e:
        return {"error": str(e)}

# Health Check Route
@app.get("/")
def home():
    return {"message": "Rent Prediction API is Running!"}
