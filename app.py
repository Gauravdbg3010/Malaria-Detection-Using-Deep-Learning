from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from datetime import datetime

app = Flask(__name__, static_folder="Static")

# model load
model = tf.keras.models.load_model("Model/malaria_model.h5")

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
    return render_template("index.html",
                           prediction=None,
                           confidence=None,
                           p_parasitized=None,
                           p_uninfected=None,
                           image_path=None,
                           timestamp=None)

@app.route('/predict', methods=["POST"])
def predict():
    # validations
    if "file" not in request.files:
        return render_template("index.html", prediction="No file selected!", image_path=None)

    file = request.files["file"]
    if file.filename == "":
        return render_template("index.html", prediction="No file selected!", image_path=None)

    # save upload
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # preprocess + predict
    img = prepare_image(filepath)
    pred = model.predict(img, verbose=0)
    p = float(pred[0][0])  # sigmoid output

    # Assumption: Parasitized=0, Uninfected=1 (alphabetical mapping)
    p_uninfected = p
    p_parasitized = 1 - p

    if p >= 0.5:
        result = "Uninfected"
        confidence = p_uninfected * 100
    else:
        result = "Parasitized"
        confidence = p_parasitized * 100

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # pass data to UI
    return render_template(
        "index.html",
        prediction=result,
        confidence=f"{confidence:.2f}",
        p_parasitized=f"{p_parasitized*100:.2f}",
        p_uninfected=f"{p_uninfected*100:.2f}",
        image_path=filepath.replace("\\", "/"),
        timestamp=ts
    )

@app.route("/health")
def health():
    return jsonify({"server": "running", "model_loaded": model is not None})

if   __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
