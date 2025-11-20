import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
import tensorflow as tf
import joblib

model = tf.keras.models.load_model("model.h5")
onehot_geo = joblib.load("onehot_geo.pkl")
label_encoder_gender=joblib.load("label_encoder_gender.pkl")
scaler=joblib.load("scaler.pkl")

st.title('Customer Churn Prediction')

geography = st.selectbox('Geography', onehot_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])


input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

encoded_geo = onehot_geo.transform([[geography]])
encoded_geo_df= pd.DataFrame(encoded_geo,columns=onehot_geo.get_feature_names_out(["Geography"]))

input_data = pd.concat([input_data.reset_index(drop=True),encoded_geo_df],axis=1)
input_data_scaled = scaler.transform(input_data)

predicted = model.predict(input_data_scaled)

predicted_probo= predicted[0][0]
st.write(f"Churn Probabilty:{predicted_probo:.2f}")

if predicted_probo > 0.5:
    st.write("Customer like to Chrun")
else:
    st.write("Customer not likely to Churn")