import pandas as pd
import numpy as num

df = pd.read_csv("data/VisaFile.csv", encoding="latin1",low_memory=False)

#for standardize the column
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
#Removing the duplicate rows
df = df.drop_duplicates()
# print(df.head())
# print(df.shape)
#For Handle Missing Values
df.isnull().sum().sort_values(ascending=False)
#Drop column for too many missing values
threshold = 0.4 * len(df)   # 40% rule
df = df.dropna(axis=1, thresh=threshold)
print(df.shape)
#For Filling the remaining missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("unknown")
    else:
        df[col] = df[col].fillna(df[col].median())
        

df = df.drop(columns=["processing_time_days"], errors="ignore")
# print(df.head())

df["case_received_date"] = pd.to_datetime(
    df["case_received_date"].astype(str),
    format="mixed",
    errors="coerce"
)

df["decision_date"] = pd.to_datetime(
    df["decision_date"].astype(str),
    format="mixed",
    errors="coerce"
)


df = df.dropna(subset=["case_received_date", "decision_date"])

#create processing_time
print(df.head())
df["processing_time_days"] = (
    df["decision_date"] - df["case_received_date"]
).dt.days

df = df[df["processing_time_days"] >= 0]
print(df.shape)
print(df[["case_received_date", "decision_date", "processing_time_days"]].head())