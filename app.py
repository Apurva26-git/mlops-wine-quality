from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load('iris_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "Iris Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction_input = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(prediction_input)
    return jsonify({
        'prediction': int(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=True)
