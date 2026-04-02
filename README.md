# 🌍 AI Visa Processing Time Estimator

An AI-powered system that predicts visa processing time using Machine Learning, explains results using SHAP, and provides an interactive chatbot for user guidance.

---

## 🚀 Live Demo

👉 https://ai-enabled-visa-processing-estimator.streamlit.app

---

## 💡 Overview

Visa applicants often face uncertainty about processing timelines.
This project solves that problem by using Machine Learning to estimate visa processing time based on:

* Visa type
* Case status
* Work city
* Application date

The system provides:

✔ Estimated processing time
✔ Confidence range
✔ Explanation of prediction (SHAP)
✔ AI chatbot for queries

---

## ✨ Features

* 🔮 ML-based visa processing prediction
* 📊 SHAP explainability (feature impact)
* 🤖 AI chatbot assistant
* 📈 Interactive insights dashboard
* 🌐 Multi-page Streamlit web app
* ☁️ Deployed on cloud

---

## 🧠 How It Works

User Input → ML Model → Prediction → SHAP Explanation → Chatbot Insight

---

## 🛠️ Tech Stack

**Machine Learning:**

* Scikit-learn
* XGBoost
* CatBoost

**Data Processing:**

* Pandas
* NumPy

**Frontend:**

* Streamlit

**Visualization:**

* Plotly
* Matplotlib

**Explainability:**

* SHAP

**AI Integration:**

* OpenAI API

---

## 📂 Project Structure

frontend/
├── app.py
├── pages/
│   ├── 1_Predict.py
│   ├── 2_Insights.py
│   ├── 3_Report.py
│   ├── 4_About.py
│   └── 5_AI_Assistant.py

src/
├── train.py
├── predict.py

models/
├── visa_model.pkl
├── model_features.pkl
├── model_rmse.pkl

data/
├── VisaFile_small.csv

requirements.txt
README.md

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/AI-Enabled-Visa-Processing-Estimator.git
cd AI-Enabled-Visa-Processing-Estimator

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run frontend/app.py
```

---

## 🤖 AI Assistant

The application includes a chatbot powered by OpenAI API that:

* Answers visa-related questions
* Explains delays
* Provides recommendations

Fallback logic ensures the chatbot works even when API limits are reached.

---

## 📊 Model Details

Models evaluated:

* Linear Regression
* Random Forest
* Gradient Boosting
* XGBoost (Final Model ✅)

XGBoost was selected for its better performance and generalization.

---

## 📌 Why This Project Stands Out

Most ML projects only focus on prediction.
This project goes further:

✔ Predicts outcomes
✔ Explains results (SHAP)
✔ Interacts with users (Chatbot)
✔ Deployed as a real-world application

---

## 🔐 Security

* API keys stored securely using `.streamlit/secrets.toml`
* Sensitive data excluded using `.gitignore`
* Keys rotated if exposed

---

## 📈 Future Improvements

* Real-time visa data integration
* Improved model accuracy
* User authentication system
* Mobile-friendly UI

---

## 👨‍💻 Author

Devansh Gupta
