from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import os
import json

app = Flask(__name__)
CORS(app)

# ==============================
# Load Model
# ==============================

MODEL_PATH = "rice_disease_model.keras"

model = load_model(MODEL_PATH)

print("Rice Disease Model Loaded Successfully")

# ==============================
# Class Names
# ==============================

CLASS_NAMES = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Healthy Rice Leaf",
    "Leaf Blast",
    "Leaf Scald",
    "Narrow Brown Leaf Spot",
    "Rice Hispa",
    "Sheath Blight"
]

# ==============================
# Disease Information
# ==============================

INFO_FILE = "disease_info.json"

if os.path.exists(INFO_FILE):
    with open(INFO_FILE, "r") as f:
        disease_info = json.load(f)
else:
    disease_info = {}


@app.route("/")
def home():

    return jsonify({
        "status": "Running",
        "model": "Rice Disease Detection",
        "classes": len(CLASS_NAMES)
    })




# ==============================
# Predict Route
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No file selected"
        }), 400

    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)

    file.save(filepath)

    try:

        # Load image
        img = image.load_img(filepath, target_size=(224, 224))
        img = image.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict
        prediction = model.predict(img, verbose=0)

        probs = prediction[0]

        best_index = np.argmax(probs)

        confidence = float(probs[best_index] * 100)

        predicted_class = CLASS_NAMES[best_index]

        # Unknown detection
        THRESHOLD = 40

        if confidence < THRESHOLD:

            return jsonify({
                "success": True,
                "disease": "Unknown",
                "confidence": round(confidence, 2),
                "description": "The uploaded image is not recognized as a rice leaf or the confidence is too low."
            })

        # Get disease information
        info = disease_info.get(predicted_class, {})

        return jsonify({
            "success": True,
            "disease": predicted_class,
            "confidence": round(confidence, 2),
            "description": info.get("description", ""),
            "scientific_name": info.get("scientific_name", ""),
            "cause": info.get("cause", ""),
            "risk_level": info.get("risk_level", ""),
            "symptoms": info.get("symptoms", []),
            "best_medicines": info.get("best_medicines", []),
            "medicine_usage": info.get("medicine_usage", []),
            "treatment": info.get("treatment", []),
            "prevention": info.get("prevention", []),
            "expert_tips": info.get("expert_tips", [])
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

# ==============================
# Display Uploaded Images
# ==============================

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)
# ==============================
# Run Application
# ==============================

if __name__ == "__main__":

    os.makedirs("uploads", exist_ok=True)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )