import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ✅ LOAD MODEL
def load_model():
    return joblib.load(os.path.join(BASE_DIR, "models", "visa_model.pkl"))

def load_features():
    return joblib.load(os.path.join(BASE_DIR, "models", "model_features.pkl"))

def load_rmse():
    return joblib.load(os.path.join(BASE_DIR, "models", "model_rmse.pkl"))


def preprocess_input(data, model_features):
    df = pd.DataFrame(columns=model_features)

    # ✅ Basic feature
    df.loc[0, "year"] = data.get("year", 0)

    # ✅ CASE_RECEIVED_DATE → derived features
    date = pd.to_datetime(data.get("case_received_date"))

    if "month" in df.columns:
        df.loc[0, "month"] = date.month
    if "day" in df.columns:
        df.loc[0, "day"] = date.day
    if "weekday" in df.columns:
        df.loc[0, "weekday"] = date.weekday()

    # ✅ VISA STATUS
    status = data.get("visa_status", "").lower()

    if status == "denied" and "VISA_STATUS_denied" in df.columns:
        df.loc[0, "VISA_STATUS_denied"] = 1
    elif status == "withdrawn" and "VISA_STATUS_withdrawn" in df.columns:
        df.loc[0, "VISA_STATUS_withdrawn"] = 1
    elif status == "certified" and "VISA_STATUS_certified" in df.columns:
        df.loc[0, "VISA_STATUS_certified"] = 1

    # ✅ VISA CLASS
    visa = data.get("visa_type", "")
    col_name = f"VISA_CLASS_{visa}"
    if col_name in df.columns:
        df.loc[0, col_name] = 1

    # ✅ WORK CITY
    city = data.get("city", "")
    city_col = f"WORK_CITY_{city}"
    if city_col in df.columns:
        df.loc[0, city_col] = 1

    # Fill missing
    df = df.fillna(0)

    return df


def predict_processing_time(input_data):
    try:
        model = load_model()
        model_features = load_features()
        rmse = load_rmse()

        df = preprocess_input(input_data, model_features)

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