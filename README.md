# 🌾 Rice Disease Detection API

A Deep Learning-based Rice Disease Detection System developed using TensorFlow, Keras, and Flask.

This API classifies rice leaf images into rice diseases, healthy rice, or unknown images and returns detailed disease information.

---

# 📌 Features

- Rice Disease Detection using Deep Learning
- MobileNetV2 Transfer Learning
- Detects Rice Diseases and Healthy Rice
- Unknown Class Detection (Non-rice images)
- REST API using Flask
- JSON Response
- AWS EC2 Deployment Ready
- GitHub Ready
- React Native Compatible

---

# 📂 Project Structure

```
RiceDiseaseAPI/
│
├── app.py
├── Crop_Disease_Model.keras
├── disease_info.json
├── requirements.txt
├── README.md
├── .gitignore
├── uploads/
└── static/
```

---

# 🌾 Supported Classes

- Rice Bacterial Leaf Blight
- Rice Blast
- Rice Brown Spot
- Rice Healthy
- Rice Hispa
- Rice Leaf Blast
- Rice Leaf Blight
- Rice Leaf Scald
- Rice Narrow Brown Leaf Spot
- Rice Sheath Blight
- Unknown

> **Unknown** is returned when the uploaded image is not a rice leaf or belongs to an unsupported crop or disease.

---

# 🧠 Model Information

| Property | Value |
|----------|-------|
| Framework | TensorFlow / Keras |
| Architecture | MobileNetV2 |
| Input Size | 224 × 224 × 3 |
| Output | Rice Diseases + Healthy + Unknown |
| Loss Function | Categorical Crossentropy |
| Optimizer | Adam |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RiceDiseaseAPI.git
```

Move into the project

```bash
cd RiceDiseaseAPI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Server

```bash
python app.py
```

The server will start at

```
http://127.0.0.1:5000
```

---

# 🚀 API Endpoint

### POST

```
/predict
```

### Form Data

```
image : rice_leaf.jpg
```

---

# 📦 Example Response

```json
{
    "prediction": "Rice Blast",
    "confidence": 98.74,
    "scientific_name": "Magnaporthe oryzae",
    "description": "Rice Blast is one of the most destructive fungal diseases affecting rice...",
    "symptoms": [
        "Diamond-shaped lesions",
        "Gray center with brown edges"
    ],
    "causes": [
        "Magnaporthe oryzae fungus"
    ],
    "treatment": [
        "Apply Tricyclazole fungicide"
    ],
    "prevention": [
        "Use resistant rice varieties"
    ]
}
```

---

# ☁️ Deployment

This API can be deployed on:

- AWS EC2
- Docker
- Render
- Railway
- Azure
- Google Cloud Platform

---

# 📱 Mobile Application

This backend is designed to work with:

- React Native
- Android
- Flutter

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- Pillow
- Gunicorn

---

# 👨‍🎓 Final Year Project

**Rice Disease Detection Using Deep Learning**

This project uses transfer learning with MobileNetV2 to identify common rice diseases from leaf images. If the uploaded image is not a rice leaf or does not belong to the trained classes, the model returns **Unknown**.

---

# 📄 License

This project is developed for educational and research purposes.