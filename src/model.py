import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =====================================================
# Reproducibility
# =====================================================
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# =====================================================
# Paths
# =====================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "VisaFile.csv")
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

os.makedirs(MODEL_DIR, exist_ok=True)


# =====================================================
# Data Loading + Cleaning
# =====================================================
def load_data():

    df = pd.read_csv(DATA_PATH, encoding="latin1", low_memory=False)

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.dropna(subset=["work_city"])

    # Clean full_time_position_y_n
    if "full_time_position_y_n" in df.columns:
        df["full_time_position_y_n"] = (
            df["full_time_position_y_n"]
            .astype(str)
            .str.strip()
            .str.upper()
            .replace({"YES": "Y", "NO": "N", "NAN": np.nan})
        )

        df["full_time_position_y_n"] = df["full_time_position_y_n"].fillna(
            df["full_time_position_y_n"].mode()[0]
        )

        df["full_time_position_y_n"] = df["full_time_position_y_n"].map({
            "Y": 1,
            "N": 0
        })

    # Date parsing
    df["case_received_date"] = pd.to_datetime(
        df["case_received_date"],
        format="mixed",
        errors="coerce"
    )

    df["decision_date"] = pd.to_datetime(
        df["decision_date"],
        format="mixed",
        errors="coerce"
    )

    df = df.dropna(subset=["case_received_date", "decision_date"])

    df["processing_time_days"] = (
        df["decision_date"] - df["case_received_date"]
    ).dt.days

    df = df[df["processing_time_days"] >= 0]

    # =====================================================
    # Industry-Level Feature Engineering
    # =====================================================

    df["year"] = df["case_received_date"].dt.year
    df["month"] = df["case_received_date"].dt.month
    df["quarter"] = df["case_received_date"].dt.quarter

    df["season"] = df["month"].apply(
        lambda x: "Peak" if x in [1, 2, 12] else "Off-Peak"
    )

    df["monthly_volume"] = (
        df.groupby(["year", "month"])["processing_time_days"]
        .transform("count")
    )

    df["state_avg"] = (
        df.groupby("work_state")["processing_time_days"]
        .transform("mean")
    )

    return df


# =====================================================
# Main Training Pipeline
# =====================================================
def main():

    print("Loading and preparing data...")
    df = load_data()

    # ------------------------------
    # Development Mode (Faster Training)
    # ------------------------------
    df = df.sample(60000, random_state=RANDOM_STATE)

    # Drop high-cardinality column
    X = df.drop(
        ["processing_time_days",
         "case_received_date",
         "decision_date",
         "work_city"],   # important optimization
        axis=1
    )

    y = df["processing_time_days"]

    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns
    categorical_features = X.select_dtypes(include=["object"]).columns

    # Numeric pipeline (no scaling for tree models)
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ])

    # Categorical pipeline
    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    # ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    # RandomForest (Faster Dev Mode)
    model = RandomForestRegressor(
        n_estimators=20,
        random_state=RANDOM_STATE,
        n_jobs=-1
    )

    # Full Pipeline
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=RANDOM_STATE
    )

    print("Training model...")
    pipeline.fit(X_train, y_train)

    print("Evaluating model...")
    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("\n==============================")
    print("Model Performance:")
    print("MAE:", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2 Score:", round(r2, 4))
    print("==============================\n")

    # Save model
    model_path = os.path.join(MODEL_DIR, "rf_pipeline.joblib")
    joblib.dump(pipeline, model_path)

    print("Model saved successfully at:", model_path)


if __name__ == "__main__":
    main()
