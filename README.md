# 🌍 AI-Enabled Visa Processing Time Estimator

An AI-powered web application that predicts visa processing time using machine learning and provides interactive insights through a multi-page dashboard.

---

## 🔗 Live Demo

### 🌐 Streamlit Web App  
https://ai-enabled-visa-processing-estimator.streamlit.app/  

---

## 📌 Project Overview

Visa applicants often face uncertainty regarding processing timelines and delays.  
This project builds a machine learning-based system to estimate visa processing time using historical visa data.

The system processes user inputs such as visa type, case status, working city, and case received date to generate predictions along with a confidence range.

In addition, the application provides an interactive dashboard for data insights and allows users to download a summary report.

---

## ✨ Key Features

### 🔹 Visa Processing Time Prediction
- Predicts processing time using trained ML model  
- Takes real-world inputs (visa type, status, city, date)  
- Provides estimated processing days  

### 🔹 Confidence Range Estimation
- Displays lower and upper bounds  
- Helps users understand prediction uncertainty  

### 🔹 Multi-Page Web Application
- Home page overview  
- Prediction interface  
- Insights dashboard  
- Report download page  

### 🔹 Interactive Insights Dashboard
- Visa type distribution  
- Visa status trends  
- Top working cities  
- Data-driven visualizations  

### 🔹 PDF Report Generation
- Generates downloadable summary report  
- Useful for documentation and analysis  

---

## 🧠 Machine Learning Pipeline

The system follows a complete ML pipeline:

- Data ingestion from real dataset  
- Data preprocessing and cleaning  
- Feature engineering (date-based + categorical encoding)  
- Handling high-dimensional data  
- Model training and evaluation  
- Model serialization and deployment  

---

## 🏗️ System Architecture

User  
 │  
 ▼  
Streamlit Web App (Frontend)  
 │  
 ▼  
Prediction Engine (Local ML Model)  
 │  
 ▼  
Trained Model (XGBoost / Scikit-learn)  

The application directly uses a trained machine learning model for real-time predictions without relying on external APIs.

---

## 🛠️ Technology Stack

### 🔹 Languages
- Python  
- SQL  

### 🔹 Machine Learning
- Scikit-learn  
- XGBoost  

### 🔹 Data Processing
- Pandas  
- NumPy  

### 🔹 Frontend
- Streamlit  

### 🔹 Visualization
- Plotly  
- Matplotlib  

### 🔹 Deployment
- Streamlit Community Cloud  
- AWS EC2  

### 🔹 Tools
- Git  
- GitHub  
- VS Code  

---

## 📊 Model Details

Multiple models were evaluated:

- Linear Regression (baseline)  
- Random Forest (ensemble)  
- Gradient Boosting  
- XGBoost (final model)  

XGBoost was selected due to better performance and stability.

---

## 📂 Project Structure

frontend/  
├── app.py  
├── pages/  
│   ├── 1_Predict.py  
│   ├── 2_Insights.py  
│   ├── 3_Report.py  
│   └── 4_About.py  

src/  
├── train_model.py  
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

1. Clone repository  
git clone https://github.com/your-username/AI-Enabled-Visa-Processing-Estimator.git  

2. Navigate to project  
cd AI-Enabled-Visa-Processing-Estimator  

3. Create virtual environment  
python -m venv venv  
venv\Scripts\activate  

4. Install dependencies  
pip install -r requirements.txt  

5. Run application  
streamlit run frontend/app.py  

---

## 📈 Future Improvements

- Real-time visa data integration  
- Advanced analytics dashboard  
- Improved model accuracy with more features  
- User authentication system  
- Mobile-friendly interface  

---

## 📄 License

This project is for educational and research purposes.

---

## 🙌 Acknowledgements

This project was developed as part of a virtual internship to demonstrate the application of machine learning in real-world problem solving and deployment.

---

## 👨‍💻 Author

Devansh Gupta
