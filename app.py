from flask import Flask, request, render_template, jsonify
import numpy as np
from PIL import Image
import os
from datetime import datetime

app = Flask(__name__, static_folder="Static")

UPLOAD_FOLDER = os.path.join("Static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

IMG_SIZE = 64

def prepare_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def home():
    return render_template(
        "index.html",
        prediction=None,
        confidence=None,
        p_parasitized=None,
        p_uninfected=None,
        image_path=None,
        timestamp=None
    )

@app.route('/predict', methods=["POST"])
def predict():
    if "file" not in request.files:
        return render_template(
            "index.html",
            prediction="No file selected!",
            confidence=None,
            p_parasitized=None,
            p_uninfected=None,
            image_path=None,
            timestamp=None
        )

    file = request.files["file"]

    if file.filename == "":
        return render_template(
            "index.html",
            prediction="No file selected!",
            confidence=None,
            p_parasitized=None,
            p_uninfected=None,
            image_path=None,
            timestamp=None
        )

    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.filename}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Temporary output for deployment testing
    result = "Prediction temporarily disabled"
    confidence = "0"
    p_parasitized = "0"
    p_uninfected = "0"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        p_parasitized=p_parasitized,
        p_uninfected=p_uninfected,
        image_path=filepath.replace("\\", "/"),
        timestamp=ts
    )

@app.route("/health")
def health():
    return jsonify({
        "server": "running",
        "model_loaded": False
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


   
        
