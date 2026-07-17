
# 🧠 BurnSafe AI - Employee Burnout Prediction & Risk Assessment

## 📌 Overview

BurnSafe AI is a Machine Learning based application that predicts employee burnout risk using workplace and employee-related factors.

The goal of this project is to help HR teams identify employees who may be at risk of burnout and take preventive actions through data-driven insights.

---

## 🚀 Demo

🔗 Live Demo:
(Add your Streamlit deployment link here)

---

## 🎯 Objectives

- Predict employee burnout score using Machine Learning
- Identify high-risk employees
- Analyze important factors contributing to burnout
- Provide HR recommendations based on predicted risk

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib

### Tools
- Jupyter Notebook
- VS Code
- GitHub

---

## 📊 Dataset

Dataset:
Employee Burnout Analysis Dataset (Kaggle)

Features used:

- Gender
- Company Type
- WFH Setup Available
- Designation
- Resource Allocation
- Mental Fatigue Score
- Joining Month
- Quarter

Target:

- Burn Rate (Burnout Score)

---

## 🔄 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Encoding
6. Model Training
7. Model Evaluation
8. Streamlit Deployment

---

## 🤖 Models Implemented

The following regression models were tested:

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | 0.895 | 0.0496 | 0.0632 |
| Decision Tree | 0.830 | 0.0611 | 0.0804 |
| Random Forest | 0.888 | 0.0502 | 0.0652 |
| Gradient Boosting | 0.905 | 0.0474 | 0.0602 |

---

## 🏆 Best Model

### Gradient Boosting Regressor

Performance:

- R² Score: 0.9048
- MAE: 0.0474
- RMSE: 0.0602

Gradient Boosting was selected because it achieved the highest prediction accuracy among tested models.

---

## 📈 Feature Importance

The most important factors affecting burnout:

1. Mental Fatigue Score (~90%)
2. Resource Allocation (~9%)
3. WFH Setup Availability
4. Designation

---

## 💻 Project Structure
Employee-Burnout-Analysis/
│
├── app.py                                  # Streamlit deployment application
│
├── employee_burnout_model.pkl              # Trained Gradient Boosting model
│
├── requirements.txt                        # Python dependencies
│
├── README.md                               # Project documentation
│
├── datasets/
│   └── employee_burnout.csv                # Dataset (optional, if uploading)
│
├── notebooks/
│   └── Employee_Burnout_Analysis.ipynb     # Data analysis + model training notebook
│
├── images/
│   ├── prediction_page.png                 # Streamlit prediction screenshot
│   ├── model_performance.png               # Model comparison screenshot
│   └── feature_importance.png              # Feature importance screenshot
│
└── .gitignore                              # Files ignored by GitHub
