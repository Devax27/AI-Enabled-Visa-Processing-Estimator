import streamlit as st
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

st.title("📊 Model Insights")

st.markdown("### Correlation Heatmap")

image_path = os.path.join(BASE_DIR, "outputs", "correlation_heatmap.png")

if os.path.exists(image_path):
    st.image(image_path, caption="Feature Correlation Heatmap")
else:
    st.warning("Run EDA first to generate insights.")

st.markdown("""
### Key Insights:

- Visa type strongly affects processing time  
- Seasonal patterns impact delays  
- High application volume increases waiting time  
- Location plays a major role  
""")