# 🩺 Diabetes Prediction System using SVM

This project is a **web-based Diabetes Prediction System** developed using a **Support Vector Machine (SVM)** model. It takes user inputs such as health metrics and predicts whether the person is likely to have diabetes. The model is trained using the **Pima Indians Diabetes Dataset** and deployed with a simple and interactive frontend.

---

## Features

- Machine Learning model built using **SVM**.
- Clean and user-friendly **web interface**.
- Input fields for:
  - Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- Real-time prediction result (Diabetic / Non-Diabetic).

---

## Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn, Joblib)
- **Machine Learning**: Support Vector Machine (SVM)
- **Web Framework**: Flask / Streamlit *(mention whichever you used)*
- **HTML/CSS/Bootstrap** *(if applicable)*

---

## Project Structure

```bash
diabetes-prediction-svm/
│
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates (for Flask)
├── model/
│   └── svm_model.pkl    # Trained SVM model
├── app.py               # Main Flask/Streamlit application
├── model_training.ipynb # Jupyter notebook for model training
├── requirements.txt     # Python dependencies
└── README.md
