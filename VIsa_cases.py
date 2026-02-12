import os
import pandas as pd
import numpy as np

DATA_PATH = "data/VisaFile.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        "Dataset not found. Please place VisaFile.csv inside the data/ folder."
    )


def load_data(path):
    return pd.read_csv(path, encoding="latin1", low_memory=False)


def clean_columns(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
    )
    return df


def handle_missing_values(df):
    df = df.drop_duplicates()

    threshold = 0.4 * len(df)
    df = df.dropna(axis=1, thresh=threshold)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("unknown")
        else:
            df[col] = df[col].fillna(df[col].median())

    return df


def process_dates(df):
    df["case_received_date"] = pd.to_datetime(df["case_received_date"],format="mixed", errors="coerce")
    df["decision_date"] = pd.to_datetime(df["decision_date"],format="mixed", errors="coerce")

    df = df.dropna(subset=["case_received_date", "decision_date"])

    df["processing_time_days"] = (
        df["decision_date"] - df["case_received_date"]
    ).dt.days

    return df[df["processing_time_days"] >= 0]


def main():
    df = load_data(DATA_PATH)
    df = clean_columns(df)
    df = handle_missing_values(df)
    df = process_dates(df)

    print("Final dataset shape:", df.shape)
    # print(df[
    #     ["case_received_date", "decision_date", "processing_time_days"]
    # ].head())
    print(df.head())


if __name__ == "__main__":
    main()
