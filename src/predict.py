import os
import joblib
import pandas as pd

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "visa_model.pkl")
RMSE_PATH = os.path.join(BASE_DIR, "..", "models", "model_rmse.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "..", "models", "model_features.pkl")

# -----------------------------
# Load Model Artifacts
# -----------------------------

model = joblib.load(MODEL_PATH)
rmse = joblib.load(RMSE_PATH)
model_features = joblib.load(FEATURES_PATH)

print("Model loaded successfully.")


# -----------------------------
# Prediction Function
# -----------------------------

def predict_processing_time(input_data):

    # Convert user input to dataframe
    df = pd.DataFrame([input_data])

    # Create empty dataframe with all training features
    full_df = pd.DataFrame(columns=model_features)

    # Add user input
    full_df = pd.concat([full_df, df], ignore_index=True)

    # Fill missing columns
    full_df = full_df.fillna(0)

    # Convert everything to numeric
    full_df = full_df.astype(float)

    # Prediction
    prediction = float(model.predict(full_df)[0])


    # Confidence interval using RMSE
    confidence = max(rmse * 0.25, prediction * 0.1)

    lower = prediction - confidence
    upper = prediction + confidence
    
    return {
        "estimated_processing_days": round(prediction, 2),
        "confidence_range": f"{round(lower)} - {round(upper)} days"
    }


# -----------------------------
# Test Example
# -----------------------------

if __name__ == "__main__":

    sample_input = {
        "year": 2023,
        "month": 5,
        "quarter": 2
    }

    result = predict_processing_time(sample_input)

    print("\nPrediction Result:")
    print(result)

