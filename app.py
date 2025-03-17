from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)   #enable CORS for all routes

# Load the trained model
model = joblib.load("nids_logistic_regression.pkl")

@app.route('/', methods=["GET"])
def home():
    return "NIDS API is running! Use /predict for predictions."


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)  # Reshape for single input
    print("Received features:", features)
    prediction_prob = model.predict_proba(features)
    print("Prediction Probability:", prediction_prob)
    prediction = model.predict(features)
    return jsonify({"prediction": int(prediction[0]), "probability": prediction_prob.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
