import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px

# --------------------------------
# Path Handling
# --------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "VisaFile.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():

    # --------------------------------
    # Load Data
    # --------------------------------
    df = pd.read_csv(DATA_PATH, encoding="latin1", low_memory=False)

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.dropna(subset=["work_city"])

    # --------------------------------
    # Clean full_time_position_y_n
    # --------------------------------
    if "full_time_position_y_n" in df.columns:

        print("Missing before:", df["full_time_position_y_n"].isnull().sum())

        df["full_time_position_y_n"] = (
            df["full_time_position_y_n"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        df["full_time_position_y_n"] = df["full_time_position_y_n"].replace({
            "YES": "Y",
            "NO": "N",
            "NAN": np.nan
        })

        df["full_time_position_y_n"] = df["full_time_position_y_n"].fillna(
            df["full_time_position_y_n"].mode()[0]
        )

        df["full_time_position_y_n"] = df["full_time_position_y_n"].map({
            "Y": 1,
            "N": 0
        })

        print("Missing after:", df["full_time_position_y_n"].isnull().sum())

    # --------------------------------
    # Date Processing
    # --------------------------------
    df["case_received_date"] = pd.to_datetime(
        df["case_received_date"], format="mixed", errors="coerce"
    )
    df["decision_date"] = pd.to_datetime(
        df["decision_date"], format="mixed", errors="coerce"
    )

    df = df.dropna(subset=["case_received_date", "decision_date"])

    df["processing_time_days"] = (
        df["decision_date"] - df["case_received_date"]
    ).dt.days

    df = df[df["processing_time_days"] >= 0]

    # --------------------------------
    # Outlier Capping (IQR per visa_status)
    # --------------------------------
    def cap_series(series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        return series.clip(lower, upper)

    df["processing_time_days"] = (
        df.groupby("visa_status")["processing_time_days"]
        .transform(cap_series)
    )

    # --------------------------------
    # INDUSTRY-LEVEL FEATURE ENGINEERING
    # --------------------------------

    # Time-based features
    df["year"] = df["case_received_date"].dt.year
    df["month"] = df["case_received_date"].dt.month
    df["quarter"] = df["case_received_date"].dt.quarter

    df["season"] = df["month"].apply(
        lambda x: "Peak" if x in [1, 2, 12] else "Off-Peak"
    )

    # Historical aggregated signals

    # City historical average
    country_avg = df.groupby("work_city")["processing_time_days"].mean()
    df["country_avg"] = df["work_city"].map(country_avg)

    # Visa status historical average
    visa_avg = df.groupby("visa_status")["processing_time_days"].mean()
    df["visa_avg"] = df["visa_status"].map(visa_avg)

    # State historical average
    state_avg = df.groupby("work_state")["processing_time_days"].mean()
    df["state_avg"] = df["work_state"].map(state_avg)

    # Monthly application volume (Backlog proxy)
    df["monthly_volume"] = (
        df.groupby(["year", "month"])["processing_time_days"]
        .transform("count")
    )

    print("Industry-level features added:",
          ["year", "quarter", "season",
           "country_avg", "visa_avg",
           "state_avg", "monthly_volume"])

    # --------------------------------
    # Encoding (ML Preparation)
    # --------------------------------
    categorical_cols = ["visa_class", "visa_status", "work_state", "season"]

    df_encoded = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    print("Shape before encoding:", df.shape)
    print("Shape after encoding:", df_encoded.shape)

    # --------------------------------
    # EDA Visualizations
    # --------------------------------

    # Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(df["processing_time_days"], bins=50)
    plt.title("Distribution of Visa Processing Time")
    plt.savefig(os.path.join(OUTPUT_DIR, "processing_time_distribution.png"))
    plt.close()

    # Interactive Histogram
    fig = px.histogram(
        df,
        x="processing_time_days",
        nbins=40,
        title="Interactive Processing Time Distribution"
    )
    fig.write_html(
        os.path.join(OUTPUT_DIR, "interactive_processing_time.html")
    )

    # Correlation Heatmap
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    plt.figure(figsize=(10, 8))
    sns.heatmap(df[num_cols].corr(), annot=True,
                cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
    plt.close()

    # Monthly Trend
    monthly_avg = df.groupby("month")["processing_time_days"].mean()

    plt.figure(figsize=(9, 5))
    monthly_avg.plot(marker="o")
    plt.title("Monthly Trend in Visa Processing Time")
    plt.grid(True)
    plt.savefig(os.path.join(OUTPUT_DIR, "monthly_trend.png"))
    plt.close()

    # Season vs Processing
    plt.figure(figsize=(8, 5))
    sns.barplot(x="season",
                y="processing_time_days",
                data=df)
    plt.title("Peak vs Off-Peak Processing Time")
    plt.savefig(os.path.join(OUTPUT_DIR, "season_vs_processing.png"))
    plt.close()

    print("Remaining missing values:", df.isnull().sum().sum())


if __name__ == "__main__":
    main()

