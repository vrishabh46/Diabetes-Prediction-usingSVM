from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load('svm_diabetes_model.pkl')
scaler = joblib.load('diabetes_scaler.pkl')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        input_data = np.array(data).reshape(1, -1)
        std_data = scaler.transform(input_data)
        prediction = model.predict(std_data)

        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template('index.html', prediction_text=f'The person is likely: {result}')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
