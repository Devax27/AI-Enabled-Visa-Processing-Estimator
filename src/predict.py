import joblib
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict_processing_time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "models", "visa_model.pkl"))
model_features = joblib.load(os.path.join(BASE_DIR, "models", "model_features.pkl"))
rmse = joblib.load(os.path.join(BASE_DIR, "models", "model_rmse.pkl"))

# -------------------------------
# PREPROCESS INPUT
# -------------------------------
def preprocess_input(data):
    df = pd.DataFrame(columns=model_features)

    # Basic inputs
    df.loc[0, "year"] = data.get("year", 0)
    df.loc[0, "month"] = data.get("month", 0)
    df.loc[0, "quarter"] = data.get("quarter", 0)
    df.loc[0, "prevailing_wage_submitted"] = data.get("wage", 0)

    # -------------------------------
    # OPTIONAL: VISA STATUS ENCODING
    # -------------------------------
    status = data.get("visa_status")

    if status == "Denied" and "visa_status_denied" in df.columns:
        df.loc[0, "visa_status_denied"] = 1

    elif status == "Withdrawn" and "visa_status_withdrawn" in df.columns:
        df.loc[0, "visa_status_withdrawn"] = 1

    # -------------------------------
    # OPTIONAL: UNIT ENCODING
    # -------------------------------
    unit_map = {
        "Year": "prevailing_wage_submitted_unit_year",
        "Month": "prevailing_wage_submitted_unit_month",
        "Week": "prevailing_wage_submitted_unit_week",
        "Hour": "prevailing_wage_submitted_unit_hour"
    }

    unit = data.get("unit")

    if unit in unit_map and unit_map[unit] in df.columns:
        df.loc[0, unit_map[unit]] = 1

    # -------------------------------
    # CLEANING
    # -------------------------------
    df = df.fillna(0).infer_objects(copy=False)
    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    return df


# -------------------------------
# PREDICTION FUNCTION
# -------------------------------
def predict_processing_time(input_data):
    try:
        df = preprocess_input(input_data)

        prediction = float(model.predict(df)[0])

        confidence = max(rmse * 0.25, prediction * 0.1)

        lower = prediction - confidence
        upper = prediction + confidence

        return {
            "predicted_status": input_data.get("visa_status", "Unknown"),
            "estimated_processing_days": round(prediction, 2),
            "confidence_range": f"{round(lower)} - {round(upper)} days"
        }

    except Exception as e:
        return {"error": str(e)}
