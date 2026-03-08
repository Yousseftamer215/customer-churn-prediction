import streamlit as st
import pandas as pd
import joblib

model = joblib.load("../models/churn_model.pkl")

st.title("Customer Churn Prediction")

age = st.slider("Age",18,90)
tenure = st.slider("Tenure",0,72)
monthly = st.number_input("Monthly Charges",0.0,500.0)
total = st.number_input("Total Charges",0.0,20000.0)

gender = st.selectbox("Gender",["Male","Female","Other"])
contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
payment = st.selectbox("Payment Method",
["Credit card","Electronic check","Mailed check","Bank transfer"])

if st.button("Predict"):

    data = pd.DataFrame({
        "Age":[age],
        "Tenure":[tenure],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total],
        "Gender":[gender],
        "Contract":[contract],
        "PaymentMethod":[payment]
    })

    data = pd.get_dummies(data)

    model_features = model.feature_names_in_

    for col in model_features:
        if col not in data.columns:
            data[col] = 0

    data = data[model_features]

    prediction = model.predict(data)
    prob = model.predict_proba(data)[0][1]
    st.write("Churn Probability:", round(prob*100,2), "%")
    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")
