# 📊 Customer Churn Prediction & Retention Intelligence System

An end-to-end Machine Learning application that predicts customer churn and generates personalized retention strategies based on customer behavior.

The project combines data preprocessing, exploratory data analysis, machine learning, and an interactive Streamlit dashboard to help businesses identify customers who are likely to leave and recommend actions to improve retention.

---

## Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses.

This project predicts whether a customer is likely to churn using historical customer data and provides business-oriented retention recommendations instead of only displaying prediction results.

The project includes:

- Complete data preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Streamlit Web Application
- Customer Risk Analysis
- Personalized Retention Intelligence

---

## Features

### Machine Learning

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Feature Encoding
- Feature Scaling
- Multiple Machine Learning Models
- Model Comparison
- Probability Prediction

Models Used

- Logistic Regression
- Random Forest
- Gradient Boosting

Best Performing Model

- Random Forest Classifier

---

### Data Analysis

Exploratory Data Analysis includes

- Customer distribution
- Gender analysis
- Senior citizen analysis
- Partner analysis
- Dependents analysis
- Internet service analysis
- Payment method analysis
- Contract analysis
- Monthly charges
- Total charges
- Customer tenure
- Correlation Heatmap
- Feature Importance
- ROC Curve Comparison
- Confusion Matrix

---

### Streamlit Dashboard

Interactive dashboard includes

- Customer profile input
- Churn probability prediction
- Risk level classification
- Progress indicator
- Business explanation of churn
- Personalized retention strategies

---

### Business Intelligence

Instead of simply predicting churn, the application explains

- Why the customer is at risk
- Risk factors
- Customer behavior
- Suggested retention plans
- Discount recommendations
- Upselling opportunities
- Loyalty programs

---

## Dataset

Dataset used

Telco Customer Churn Dataset

Features include

- Demographics
- Account Information
- Internet Services
- Billing Information
- Contract Type
- Payment Method
- Customer Charges
- Customer Tenure

Target Variable

- Churn

---

## Project Structure

```
Customer-Churn-Prediction/

│
├── app.py
├── Customer_Churn_Project.ipynb
├── Customer-Churn.csv
├── rf_model.pkl
├── lr_model.pkl
├── scaler.pkl
├── columns.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Machine Learning Workflow

1. Load Dataset

2. Data Cleaning

- Handle missing values
- Convert TotalCharges to numeric
- Remove unnecessary columns

3. Exploratory Data Analysis

- Distribution plots
- Count plots
- Histograms
- Box plots
- Heatmap
- Scatter plots

4. Feature Engineering

- Label Encoding
- One-Hot Encoding
- Feature Scaling

5. Train-Test Split

80% Training

20% Testing

6. Model Training

- Logistic Regression
- Random Forest
- Gradient Boosting

7. Model Evaluation

- Accuracy
- ROC-AUC Score
- Confusion Matrix
- ROC Curve
- Feature Importance

8. Save Model

- scaler.pkl
- rf_model.pkl
- columns.json

9. Deploy using Streamlit

---

## Application Workflow

User Inputs Customer Details

↓

Data Preprocessing

↓

Feature Scaling

↓

Random Forest Prediction

↓

Churn Probability

↓

Risk Classification

↓

Business Explanation

↓

Personalized Retention Strategy

---

## Risk Categories

| Risk Level | Probability |
|------------|-------------|
| Low Risk | 0–30% |
| Medium Risk | 30–60% |
| High Risk | 60–100% |

---

## Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Joblib

JSON

Streamlit

---

## Installation

Clone Repository

```bash
git clone https://github.com/saicharan-r02/Customer-Churn-Prediction-Retention-Intelligence-System.git
```

### Navigate to the Project Directory

```bash
cd Customer-Churn-Prediction-Retention-Intelligence-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Screenshots

Add screenshots here after deployment.

Example

- Dashboard
- Prediction Result
- Retention Recommendation
- Feature Importance

---

## Future Improvements

- SHAP Explainable AI
- XGBoost / LightGBM
- Hyperparameter Tuning
- Docker Support
- CI/CD Pipeline
- Cloud Deployment
- Customer Segmentation
- Real-time API
- Authentication
- Database Integration
- LLM-powered Recommendation Engine

---

## Author

Sai Charan

Machine Learning | Data Science | AI
