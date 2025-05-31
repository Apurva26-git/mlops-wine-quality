from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load trained model
model = joblib.load('iris_model.pkl')

# Class label mapping
class_map = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read features from form input
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        prediction_input = np.array(features).reshape(1, -1)
        prediction = model.predict(prediction_input)
        predicted_class = class_map[int(prediction[0])]

        return render_template('index.html', prediction=predicted_class)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)