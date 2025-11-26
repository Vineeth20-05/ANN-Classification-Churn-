🌟 Customer Churn Prediction – Streamlit Web App

This project is a Customer Churn Prediction Web Application built using Machine Learning, TensorFlow, and Streamlit.
The app predicts whether a bank customer is likely to churn based on demographic, financial, and account-related inputs.

You can try the deployed demo here:

## 🚀 Live Demo
Try the deployed web app here:

👉 **https://a2x3qbasvenznwrm4go6fk.streamlit.app/**


🚀 Features

Interactive Streamlit UI

Predicts Customer Churn Probability

Uses a trained Keras .h5 model`

Handles:

One-Hot Encoding (Geography)

Label Encoding (Gender)

Feature Scaling

Real-time probability calculation

Clear interpretation (Churn / Not Churn)

📂 Project Structure
📦 Customer-Churn-Prediction
│
├── model.h5                  # Trained Keras model
├── onehot_geo.pkl            # OneHotEncoder for Geography
├── label_encoder_gender.pkl  # LabelEncoder for Gender
├── scaler.pkl                # StandardScaler for numerical features
├── app.py                    # Streamlit application code
├── requirements.txt          # Required dependencies
└── README.md                 # Project documentation

🧠 Machine Learning Model

Framework: TensorFlow / Keras

Type: Binary Classification

Output: Probability of churn (0 → No churn, 1 → Churn)

Preprocessing:

Categorical features:

Geography → OneHotEncoder

Gender → LabelEncoder

Numerical features:

Scaled using StandardScaler

The preprocessing objects are saved as .pkl using joblib and loaded during prediction.

🎛️ Streamlit Application

The UI collects user inputs:

Geography

Gender

Age

Balance

Credit Score

Tenure

Number of Products

Has Credit Card

Is Active Member

Estimated Salary

These inputs are transformed using saved encoders + scaler.
The final processed array is passed to the trained model.

🧾 How It Works (Prediction Flow)

User enters details in Streamlit UI

Geography → OneHotEncoded

Gender → LabelEncoded

Numerical features → Scaled

Features combined into a single row

Model predicts churn probability

UI displays:

Probability

Prediction (Churn / Not Churn)
