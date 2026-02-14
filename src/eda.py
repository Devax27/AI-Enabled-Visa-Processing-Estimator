import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():

    df = pd.read_csv("data/VisaFile.csv", encoding="latin1", low_memory=False)

    df.columns = (
        df.columns.str.strip()
                .str.lower()
                .str.replace(" ", "_")
    )
    df = df.dropna(subset=["work_city"])

    if "full_time_position_y_n" in df.columns:
        
        print("Missing before:", df["full_time_position_y_n"].isnull().sum())

        # Strip spaces and convert to uppercase
        df["full_time_position_y_n"] = (
            df["full_time_position_y_n"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        # Replace common variations
        df["full_time_position_y_n"] = df["full_time_position_y_n"].replace({
            "YES": "Y",
            "NO": "N"
        })

        # Fill missing with mode
        df["full_time_position_y_n"] = df["full_time_position_y_n"].replace("NAN", np.nan)
        df["full_time_position_y_n"] = df["full_time_position_y_n"].fillna(
            df["full_time_position_y_n"].mode()[0]
        )

        # Now safe mapping
        df["full_time_position_y_n"] = df["full_time_position_y_n"].map({
            "Y": 1,
            "N": 0
        })

        print("Missing after:", df["full_time_position_y_n"].isnull().sum())



        df["case_received_date"] = pd.to_datetime(df["case_received_date"],format="mixed", errors="coerce")
        df["decision_date"] = pd.to_datetime(df["decision_date"],format="mixed", errors="coerce")

        df = df.dropna(subset=["case_received_date", "decision_date"])

        df["processing_time_days"] = (
            df["decision_date"] - df["case_received_date"]
        ).dt.days

        df = df[df["processing_time_days"] >= 0]

        categorical_cols = ["visa_class", "visa_status", "work_state"]

        df_encoded = pd.get_dummies(df,columns=categorical_cols,drop_first=True)

        print("Shape before encoding:", df.shape)
        print("Shape after encoding:", df_encoded.shape)
        
        df.head()
        df.shape

        df["processing_time_days"].describe()

        plt.figure(figsize=(8,5))
        sns.histplot(df["processing_time_days"], bins=50)
        plt.xlabel("Processing Time (days)")
        plt.title("Distribution of Visa Processing Time")
        plt.savefig(os.path.join(OUTPUT_DIR, "processing_time_distribution.png"))
        plt.close()

        df = df[df["processing_time_days"] <= 365]
        fig = px.histogram(
        df,
        x="processing_time_days",
        nbins=40,
        title="Interactive Processing Time Distribution"
        )

        fig.write_html("outputs/interactive_processing_time.html")

        num_cols = df.select_dtypes(include=["int64", "float64"]).columns
        num_cols

        df[num_cols].hist(
            figsize=(14, 10),
            bins=30,
            edgecolor="black"
        )
        plt.suptitle("Distribution of Numerical Features", fontsize=16)
        plt.savefig(os.path.join(OUTPUT_DIR, "numerical_distribution.png"))
        plt.close()

        plt.close()

        df.select_dtypes(include="object").columns

        top_categories = (
            df.groupby("visa_status")["processing_time_days"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 5))
        sns.barplot(x=top_categories.values, y=top_categories.index)
        plt.xlabel("Average Processing Time (Days)")
        plt.ylabel("visa_status")
        plt.title("Average Processing Time by Case Status")
        plt.savefig(os.path.join(OUTPUT_DIR, "visa_status_avg_processing.png"))
        plt.close()




        plt.figure(figsize=(10, 5))
        sns.boxplot(
            x="visa_status",
            y="processing_time_days",
            data=df
        )
        plt.xticks(rotation=45)
        plt.title("Processing Time Distribution by Case Status")
        plt.savefig(os.path.join(OUTPUT_DIR, "visa_status_boxplot.png"))
        plt.close()



        plt.figure(figsize=(10, 8))
        sns.heatmap(
            df[num_cols].corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Heatmap")
        plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
        plt.close()



        df["month"] = df["case_received_date"].dt.month

        monthly_avg = df.groupby("month")["processing_time_days"].mean()

        plt.figure(figsize=(9, 5))
        monthly_avg.plot(marker="o")
        plt.xlabel("Month")
        plt.ylabel("Avg Processing Time (Days)")
        plt.title("Monthly Trend in Visa Processing Time")
        plt.grid(True)
        plt.savefig(os.path.join(OUTPUT_DIR, "monthly_trend.png"))
        plt.close()




        # “Processing time varies seasonally, likely due to application volume.”

        pairplot = sns.pairplot(
            df[num_cols].sample(2000),
            diag_kind="kde"
        )
        pairplot.savefig(os.path.join(OUTPUT_DIR, "pairplot.png"))
        plt.close()



        # To avoid memory issues.
        print("Remaining missing values:")
        print(df.isnull().sum().sort_values(ascending=False).head(10))


        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False)
        plt.title("Missing Values Heatmap")
        plt.savefig(os.path.join(OUTPUT_DIR, "missing_values_heatmap.png"))
        plt.close()




        # ## Extended EDA Summary
        # 
        # - Numerical features show right-skewed distributions
        # - Processing time varies significantly across case categories
        # - Strong seasonality observed in monthly trends
        # - Outliers exist and require capping before ML modeling
        # - Correlation analysis helps reduce redundant features

        df.columns

        pivot_df = (
            df.groupby(["visa_status", "work_city"])["processing_time_days"]
            .mean()
            .reset_index()
        )

        top_countries = (
            pivot_df["work_city"]
            .value_counts()
            .head(5)
            .index
        )

        filtered = pivot_df[pivot_df["work_city"].isin(top_countries)]

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=filtered,
            x="visa_status",
            y="processing_time_days",
            hue="work_city"
        )
        plt.xticks(rotation=45)
        plt.title("Average Processing Time by Visa Type and Country")
        plt.savefig(os.path.join(OUTPUT_DIR, "work_city_analysis.png"))
        plt.close()

        pivot_df = (
            df.groupby(["visa_status", "work_state"])["processing_time_days"]
            .mean()
            .reset_index()
        )

        top_countries = (
            pivot_df["work_state"]
            .value_counts()
            .head(5)
            .index
        )

        filtered = pivot_df[pivot_df["work_state"].isin(top_countries)]

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=filtered,
            x="visa_status",
            y="processing_time_days",
            hue="work_state"
        )
        plt.xticks(rotation=45)
        plt.title("Average Processing Time by Visa Type and Country")
        plt.savefig(os.path.join(OUTPUT_DIR, "work_state_analysis.png"))
        plt.close()




        # ## Feature Insights
        # - Processing time varies significantly across visa categories
        # - Certain regions consistently show longer average processing times
        # - Seasonal features (month, year) influence processing duration
        # - Extreme outliers exist and must be handled before modeling
        # - Some categorical features have high variance and are strong ML candidates
if __name__ == "__main__":
    main()


