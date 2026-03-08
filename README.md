[README_customer_churn_project.md](https://github.com/user-attachments/files/25821700/README_customer_churn_project.md)

# Customer Churn Prediction System

## Overview
Customer churn is a major challenge for subscription-based businesses such as telecom companies, SaaS platforms, and banks. Losing customers directly impacts revenue and long-term growth.

This project builds a **machine learning system to predict whether a customer is likely to churn** based on demographic information, account details, and billing data.

The project demonstrates a **complete end-to-end data science workflow**, including data exploration, preprocessing, model training, evaluation, and deployment through an interactive web application.

---

## Dataset

The dataset contains **100,000 customer records** with the following features:

- Age
- Gender
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Customer ID
- Churn (Target Variable)

Target variable:

- **Churn = Yes / No**

---

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

Initial exploration of the dataset to understand patterns and distributions.

Analysis includes:

- Customer churn distribution
- Age and tenure distributions
- Monthly and total charge patterns
- Relationship between customer features and churn behavior

Tools used:
- Python
- Pandas
- Seaborn
- Matplotlib

---

### 2. Data Preprocessing

Data preparation steps include:

- Handling categorical variables
- One-hot encoding using `pd.get_dummies()`
- Train/Test split for model evaluation

Libraries used:

- Pandas
- Scikit-learn

---

### 3. Machine Learning Model

A **Random Forest Classifier** was used to predict customer churn.

Model workflow:

1. Train the model using training data
2. Evaluate performance on test data
3. Analyze feature importance

Libraries used:

- Scikit-learn
- Joblib

---

## Model Evaluation

Evaluation metrics used:

- Classification Report
- Confusion Matrix
- ROC-AUC Score

These metrics provide insight into how well the model distinguishes between customers who churn and those who remain.

---

## Feature Importance

Feature importance analysis identifies which variables contribute most to churn prediction.

Important drivers typically include:

- Contract type
- Tenure
- Monthly charges
- Payment method

Understanding these drivers can help businesses design **customer retention strategies**.

---

## Streamlit Prediction App

The trained model is deployed through a **Streamlit web application**.

The application allows users to input customer information and receive a churn prediction instantly.

Example inputs:

- Age
- Tenure
- Monthly charges
- Contract type
- Payment method

Output:

- Churn prediction (Stay / Churn)
- Model decision based on learned patterns

Run the application locally:

```
streamlit run app/app.py
```

---

## Power BI Dashboard (In Progress)

A **business intelligence dashboard** is being developed using Power BI to visualize churn insights.

The dashboard will include:

- Customer churn rate
- Churn by contract type
- Churn by payment method
- Customer tenure distribution
- Revenue impact analysis

This will help transform the machine learning results into **actionable business insights**.

---

## Project Structure

```
customer_churn_project

data/
notebooks/
    01_EDA.ipynb
    02_preprocessing.ipynb
    03_models.ipynb
    04_model_evaluation.ipynb

models/
    churn_model.pkl

app/
    app.py

dashboard/

README.md
requirements.txt
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Power BI (for dashboard visualization)

---

## Future Improvements

Possible future enhancements include:

- Adding advanced models such as XGBoost
- Implementing SHAP for model explainability
- Building an automated ML pipeline
- Deploying the application to the cloud

---

## Author

Youssef Tamer  
Data Science Student

This project was built as part of a **machine learning portfolio to demonstrate end-to-end data science skills** including modeling, analysis, and deployment.
