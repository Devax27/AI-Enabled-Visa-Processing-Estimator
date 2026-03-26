import streamlit as st
import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "VisaFile.csv")


st.title("📊 Visa Insights")

df = pd.read_csv(DATA_PATH)


st.subheader("Top Visa Types")
st.bar_chart(df["VISA_CLASS"].value_counts().head(10))

st.subheader("Visa Status Distribution")
st.bar_chart(df["VISA_STATUS"].value_counts())

st.subheader("Top Cities")
st.bar_chart(df["WORK_CITY"].value_counts().head(10))