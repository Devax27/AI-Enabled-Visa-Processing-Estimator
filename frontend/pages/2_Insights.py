import streamlit as st
import pandas as pd

st.title("📊 Visa Insights")

df = pd.read_csv("../data/VisaFile.csv")

st.subheader("Top Visa Types")
st.bar_chart(df["VISA_CLASS"].value_counts().head(10))

st.subheader("Visa Status Distribution")
st.bar_chart(df["VISA_STATUS"].value_counts())

st.subheader("Top Cities")
st.bar_chart(df["WORK_CITY"].value_counts().head(10))