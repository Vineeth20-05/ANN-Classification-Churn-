# 🌟 Customer Churn Prediction – Streamlit Web App

This project is a **Customer Churn Prediction Web Application** built using **Machine Learning, TensorFlow, and Streamlit**.  
The app predicts whether a bank customer is likely to churn based on demographic, financial, and account-related features.

---

## 🚀 Live Demo

👉 **https://a2x3qbasvenznwrm4go6fk.streamlit.app/**

Try the deployed web app and explore real-time churn predictions!

---

## 🚀 Features

### 🎨 Interactive Streamlit UI  
A clean and responsive interface to collect customer details.

### 🔮 Real-time Churn Prediction  
Displays both:  
- **Churn / Not Churn** classification  
- **Prediction probability**

### 🧠 Trained Deep Learning Model  
Uses a saved **Keras `.h5` model** for inference.

### 🔧 Handles All Preprocessing Automatically  
- **One-Hot Encoding** for *Geography*  
- **Label Encoding** for *Gender*  
- **Standard Scaling** for numerical features  

Encoders and scaler are loaded from pre-saved `.pkl` files.

### ⚡ Instant Results  
Once the user enters values → Streamlit processes → Model predicts immediately.

---

## 🧠 Machine Learning Model

- **Framework:** TensorFlow / Keras  
- **Type:** Binary Classification  
- **Target:** Predict if a customer will churn  
- **Output:** Probability (between 0 and 1)

### 🔍 Preprocessing Steps Used During Training

#### 📌 Categorical Features  
- **Geography → OneHotEncoder**  
  (France, Germany, Spain converted to binary vectors)  
- **Gender → LabelEncoder**  
  (Male = 1, Female = 0)

#### 📌 Numerical Features  
Scaled using **StandardScaler** to normalize ranges.

All preprocessing objects were saved using **joblib** as:
- `onehot_geo.pkl`
- `label_encoder_gender.pkl`
- `scaler.pkl`

These are loaded inside the Streamlit app during prediction.

---

## 🎛️ Streamlit Application Workflow

The UI collects user inputs for:

- Geography  
- Gender  
- Age  
- Balance  
- Credit Score  
- Tenure  
- Number of Products  
- Has Credit Card  
- Is Active Member  
- Estimated Salary  

### 🔁 Prediction Flow

1. User enters information  
2. Input is passed to preprocessing pipeline  
3. Features transformed:  
   - Geography → one-hot encoded  
   - Gender → label encoded  
   - Numerical features → scaled  
4. All features combined into a single row  
5. Model predicts probability of churn  
6. Streamlit displays:  
   - ✔ **Churn / Not Churn** decision  
   - ✔ **Probability score**

---

## 🏁 Summary

This project demonstrates a complete end-to-end **Machine Learning deployment pipeline** using:

- TensorFlow  
- Encoders + Scalers  
- Streamlit UI  
- Real-time predictions  

Perfect for showcasing ML deployment skills!

---

## 📄 License  
MIT License © 2025
