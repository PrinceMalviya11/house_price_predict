# Machine Learning Prediction System (Django)

A web-based application built with Django that leverages pre-trained Machine Learning models to provide predictions for two distinct use cases: House Price Estimation and Student Performance (Pass/Fail) Prediction.

## 🚀 Features

### 1. 🏠 House Price Predictor
Predicts the estimated price of a house in Ahmedabad based on:
* **BHK**: Number of bedrooms.
* **Square Feet**: Total area of the property.
* **Area Type**: Classification of the area (e.g., Normal, VIP).
* **Location**: Supports multiple localities including Navrangpura, Bopal, Vastrapur, Nikol, SG Highway, and more.

### 2. 🎓 Student Pass/Fail Predictor
Predicts whether a student will pass or fail based on their academic habits:
* **Hours of Study**: Average study time per day.
* **Attendance**: Percentage of classes attended.
* **Past Exam Score**: Performance in previous examinations.

---

## 🛠️ Tech Stack

* **Backend**: Django (Python Framework)
* **Machine Learning**: 
    * **Scikit-learn**: Used for Linear Regression (House Price) and Logistic Regression (Student Result) models.
    * **Pandas & NumPy**: For data manipulation and processing.
    * **Joblib**: For loading serialized `.pkl` model files.
* **Frontend**: HTML5, CSS3 (with CSS Linear Gradients).
* **Database**: SQLite3 (Default Django DB).

---

## 💡 How it Works

1.  **Input**: Users provide data through web forms (e.g., BHK, study hours).
2.  **Processing**: The backend converts input into a Pandas DataFrame.
3.  **Scaling**: For student data, the input is normalized using a pre-trained `StandardScaler`.
4.  **Prediction**: The loaded model processes the data and returns a result.
5.  **Output**: The result is displayed dynamically on the result page.

---

## 📝 License
This project is developed for educational and predictive analysis purposes.
