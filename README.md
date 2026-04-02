🌍 AI-Enabled Visa Processing Time Estimator

An AI-powered, end-to-end machine learning system that predicts visa processing time, explains predictions using Explainable AI (SHAP), and provides an intelligent chatbot for user interaction.

🔗 Live Demo
🌐 Streamlit Web App

👉 https://ai-enabled-visa-processing-estimator.streamlit.app

📌 Project Overview

Visa applicants often face uncertainty regarding processing timelines.
This project solves that problem using Machine Learning + Explainable AI + Interactive UI.

The system takes inputs like:

Visa Type
Case Status
Work City
Case Received Date

…and predicts:

✔ Estimated processing time
✔ Confidence interval
✔ Explanation of prediction

✨ Key Features
🚀 ML-based visa processing prediction
📊 SHAP Explainability (Why prediction happened)
🤖 AI Chatbot Assistant (Agentic AI)
📉 Confidence interval estimation
📈 Interactive insights dashboard
📄 Report generation
🌐 Multi-page Streamlit web app
☁️ Fully deployed on cloud
🤖 AI Assistant (Unique Feature)

The system includes an AI-powered chatbot using OpenAI API.

It can:

Answer visa-related questions
Explain delays
Provide recommendations
Handle fallback responses if API fails

💡 This makes the project interactive + intelligent (Agentic AI system)

🧠 Explainable AI (SHAP)

The project uses SHAP to:

Show feature impact on predictions
Identify important factors (visa type, city, time)
Improve transparency and trust
🧠 Machine Learning Pipeline

End-to-end pipeline:

Data ingestion
Data cleaning & preprocessing
Feature engineering (date + categorical encoding)
Model training (multiple models)
Hyperparameter tuning
Model evaluation
Model serialization
Deployment
🏗️ System Architecture
User Input
   ↓
Streamlit UI (Frontend)
   ↓
Prediction Engine (ML Model)
   ↓
SHAP Explainability
   ↓
AI Chatbot (OpenAI API)
   ↓
Final Output
🛠️ Technology Stack
🔹 Languages
Python
SQL
🔹 Machine Learning
Scikit-learn
XGBoost
CatBoost
🔹 Data Processing
Pandas
NumPy
🔹 Explainability
SHAP
🔹 Frontend
Streamlit
🔹 Visualization
Plotly
Matplotlib
🔹 AI Integration
OpenAI API
🔹 Deployment
Streamlit Community Cloud
🔹 Tools
Git
GitHub
VS Code
📊 Model Details

Models tested:

Linear Regression
Random Forest
Gradient Boosting
XGBoost (Final Model ✅)

✔ Selected for best performance and generalization

📂 Project Structure
frontend/
├── app.py
├── pages/
│   ├── 1_Predict.py
│   ├── 2_Insights.py
│   ├── 3_Report.py
│   ├── 4_About.py
│   └── 5_AI_Assistant.py   🤖

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
⚙️ Installation & Setup
# Clone repo
git clone https://github.com/your-username/AI-Enabled-Visa-Processing-Estimator.git

# Navigate
cd AI-Enabled-Visa-Processing-Estimator

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run frontend/app.py
🔐 Security Practices
API keys are stored using .streamlit/secrets.toml
Sensitive data is excluded using .gitignore
API keys are rotated if exposed
📈 Future Improvements
Real-time visa API integration
Advanced analytics dashboard
Model performance optimization
User authentication system
Mobile-responsive UI
💼 Resume Highlight

Built an AI-powered visa processing estimator using XGBoost with SHAP-based explainability and an integrated chatbot, deployed as a multi-page Streamlit application.

📄 License

For educational and research purposes.

🙌 Acknowledgements

Developed as part of a virtual internship to demonstrate real-world ML deployment and system design.

👨‍💻 Author

Devansh Gupta
