import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_model():
    return joblib.load(os.path.join(BASE_DIR, "models", "visa_model.pkl"))

def load_features():
    return joblib.load(os.path.join(BASE_DIR, "models", "model_features.pkl"))

def load_rmse():
    return joblib.load(os.path.join(BASE_DIR, "models", "model_rmse.pkl"))

def preprocess_input(data, model_features):
    df = pd.DataFrame(columns=model_features)

    date = pd.to_datetime(data.get("case_received_date"))

    df.loc[0, "year"] = date.year
    df.loc[0, "month"] = date.month
    df.loc[0, "quarter"] = (date.month - 1)//3 + 1
    df.loc[0, "day"] = date.day
    df.loc[0, "weekday"] = date.weekday()

    # categorical encoding safely
    visa_col = f"visa_class_{data.get('visa_type').lower()}"
    status_col = f"visa_status_{data.get('visa_status').lower()}"
    city_col = f"work_city_{data.get('city').lower()}"

    if visa_col in df.columns:
        df.loc[0, visa_col] = 1

    if status_col in df.columns:
        df.loc[0, status_col] = 1

    if city_col in df.columns:
        df.loc[0, city_col] = 1

    df = df.fillna(0)
    return df


def predict_processing_time(input_data):
    try:
        model = load_model()
        features = load_features()
        rmse = load_rmse()

        df = preprocess_input(input_data, features)

        pred = float(model.predict(df)[0])

        conf = max(rmse * 0.25, pred * 0.1)

        # ✅ FINAL FIX (no negative values)
        lower = max(0, pred - conf)
        upper = pred + conf

        return {
            "predicted_status": input_data.get("visa_status"),
            "estimated_processing_days": round(pred, 2),
            "confidence_range": f"{round(lower)} - {round(upper)} days"
        }

    except Exception as e:
        return {"error": str(e)}