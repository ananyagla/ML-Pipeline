# v3
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle, numpy as np

MODEL_NAME = "house-price"

app = Flask(__name__)
CORS(app)

try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except:
    model = None

@app.route("/")
def home():
    return jsonify({"message": "House Price Prediction API is running!", "endpoints": ["/health", "/predict"]})

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": MODEL_NAME})

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Missing features"}), 400
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"model": MODEL_NAME, "prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
