import os
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import RandomizedSearchCV


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor
from catboost import CatBoostRegressor


# --------------------------------
# Paths
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "VisaFile.csv")
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# --------------------------------
# Load and Prepare Data
# --------------------------------

def load_data():

    df = pd.read_csv(DATA_PATH, encoding="latin1", low_memory=False)

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert date columns
    df["case_received_date"] = pd.to_datetime(
        df["case_received_date"], format="mixed", errors="coerce"
    )

    df["decision_date"] = pd.to_datetime(
        df["decision_date"], format="mixed", errors="coerce"
    )

    df = df.dropna(subset=["case_received_date", "decision_date"])

    # Target variable
    df["processing_time_days"] = (
        df["decision_date"] - df["case_received_date"]
    ).dt.days

    df = df[df["processing_time_days"] >= 0]

    # --------------------------------
    # Feature Engineering
    # --------------------------------

    df["year"] = df["case_received_date"].dt.year
    df["month"] = df["case_received_date"].dt.month
    df["quarter"] = df["case_received_date"].dt.quarter

    df["season"] = df["month"].apply(
        lambda x: "Peak" if x in [1, 2, 12] else "Off-Peak"
    )

    # --------------------------------
    # DROP HIGH CARDINALITY COLUMNS
    # --------------------------------

    df = df.drop(columns=[
        "case_received_date",
        "decision_date",
        "case_number",
        "employer_name",
        "job_title",
        "work_city"
    ], errors="ignore")

    # --------------------------------
    # One-hot encoding
    # --------------------------------

    df = pd.get_dummies(df, drop_first=True)

    print("Dataset shape after encoding:", df.shape)

    return df


# --------------------------------
# Model Evaluation
# --------------------------------

def evaluate_model(name, model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"\n{name}")
    print("MAE:", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2:", round(r2, 3))

    return rmse


# --------------------------------
# Training Pipeline
# --------------------------------

def main():

    print("Loading dataset...")

    df = load_data()

    X = df.drop("processing_time_days", axis=1)
    y = df["processing_time_days"]
    feature_names = X.columns


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # --------------------------------
    # Models
    # --------------------------------

    models = {

        "Linear Regression": LinearRegression(),

        "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            max_depth=12,
            random_state=42
        ),

        "XGBoost":
        XGBRegressor(
            n_estimators=400,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            random_state=42
        ),

        "CatBoost":
        CatBoostRegressor(
            iterations=400,
            learning_rate=0.05,
            depth=6,
            verbose=0
        )
    }

    best_model = None
    best_score = float("inf")
    best_rmse = None

    # --------------------------------
    # Train Models
    # --------------------------------

    for name, model in models.items():

        if name == "Linear Regression":

            model.fit(X_train_scaled, y_train)
            score = evaluate_model(name, model, X_test_scaled, y_test)

        else:

            model.fit(X_train, y_train)
            score = evaluate_model(name, model, X_test, y_test)

        if score < best_score:

            best_score = score
            best_model = model
            best_rmse = score

    print("\nBest Model Selected:", type(best_model).__name__)
    
    # --------------------------------
    # Hyperparameter Tuning for XGBoost
    # --------------------------------

    print("\nStarting Hyperparameter Tuning for XGBoost...")

    xgb_params = {
        "n_estimators": [200, 300, 400, 500],
        "max_depth": [4, 6, 8, 10],
        "learning_rate": [0.01, 0.03, 0.05, 0.1],
        "subsample": [0.6, 0.8, 1.0],
        "colsample_bytree": [0.6, 0.8, 1.0]
    }

    xgb_model = XGBRegressor(random_state=42)

    random_search = RandomizedSearchCV(
        estimator=xgb_model,
        param_distributions=xgb_params,
        n_iter=20,
        scoring="neg_root_mean_squared_error",
        cv=3,
        verbose=2,
        n_jobs=-1
    )

    random_search.fit(X_train, y_train)

    best_xgb = random_search.best_estimator_

    print("\nBest Hyperparameters Found:")
    print(random_search.best_params_)

    # Evaluate tuned model
    print("\nEvaluating Tuned XGBoost Model")

    rmse_tuned = evaluate_model(
        "Tuned XGBoost",
        best_xgb,
        X_test,
        y_test
    )
    from sklearn.metrics import r2_score

    train_pred = best_model.predict(X_train)
    test_pred = best_model.predict(X_test)

    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)

    print("\nOverfitting Check")
    print("Train R2:", round(train_r2, 3))
    print("Test R2:", round(test_r2, 3))

    # Replace best model if tuned one is better
    if rmse_tuned < best_rmse:
        best_model = best_xgb
        best_rmse = rmse_tuned
        print("\nTuned model selected as final model.")


    # --------------------------------
    # Feature Importance
    # --------------------------------

    if hasattr(best_model, "feature_importances_"):

        importances = best_model.feature_importances_

        feature_names = X.columns

        importance_df = pd.DataFrame({
            "feature": feature_names,
            "importance": importances
        }).sort_values(by="importance", ascending=False)

        print("\nTop 10 Important Features:")
        print(importance_df.head(10))

        plt.figure(figsize=(10,6))

        sns.barplot(
            x="importance",
            y="feature",
            data=importance_df.head(15)
        )

        plt.title("Top 15 Feature Importance")

        plt.tight_layout()

        plt.savefig(os.path.join(OUTPUT_DIR, "feature_importance.png"))

        plt.close()

    # --------------------------------
    # SHAP Explainability
    # --------------------------------

    print("\nGenerating SHAP Explainability...")

    # Convert all features to numeric for SHAP
    X_train_shap = X_train.astype(float)
    X_test_shap = X_test.astype(float)

    # Use TreeExplainer (best for XGBoost)
    explainer = shap.TreeExplainer(best_model)

    # To avoid memory issues use sample
    sample_data = X_test_shap.sample(2000, random_state=42)

    shap_values = explainer.shap_values(sample_data)

    # Summary plot
    shap.summary_plot(shap_values, sample_data, show=False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "shap_summary.png"))
    plt.close()

    # Feature importance plot
    shap.summary_plot(shap_values, sample_data, plot_type="bar", show=False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "shap_feature_importance.png"))
    plt.close()

    # --------------------------------
    # Save Model + RMSE
    # --------------------------------

    joblib.dump(best_model, os.path.join(MODEL_DIR, "visa_model.pkl"))
    joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))
    joblib.dump(best_rmse, os.path.join(MODEL_DIR, "model_rmse.pkl"))
    joblib.dump(feature_names, os.path.join(MODEL_DIR, "model_features.pkl"))


    print("\nModel saved successfully!")
    print("RMSE saved for confidence interval prediction")


if __name__ == "__main__":
    main()
