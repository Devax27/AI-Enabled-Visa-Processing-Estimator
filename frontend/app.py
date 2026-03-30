import streamlit as st

st.set_page_config(page_title="Visa AI", page_icon="🌍", layout="centered")

# -----------------------
# SAFE UI ENHANCEMENT
# -----------------------
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(120deg, #eef2f7, #ffffff);
}

/* Title */
h1 {
    color: #1a365d;
    text-align: center;
    font-weight: 700;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #4a5568;
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    background: linear-gradient(90deg, #2563eb, #1e40af);
    color: white;
    font-weight: 600;
}

/* Inputs */
.stTextInput input, .stSelectbox div {
    border-radius: 10px !important;
}

/* Spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.title("🌍 Visa Processing Time Estimator")
st.markdown("<p class='subtitle'>AI-powered prediction & insights system</p>", unsafe_allow_html=True)

st.divider()

# -----------------------
# CONTENT
# -----------------------
st.markdown("""
### 🚀 What this app does

- Predict visa processing time  
- Show confidence range  
- Provide insights dashboard  
- Generate downloadable reports  

---

### 📌 How to use

1. Go to **Predict page**  
2. Enter details  
3. Get instant prediction  
4. Download report  
""")

st.success("Use sidebar to navigate →")