# Malaria Detection Using Deep Learning
A deep learning-based web application for detecting malaria parasites from microscopic blood cell images. This project uses a Convolutional Neural Network (CNN) model to classify cell images as **Parasitized** or **Uninfected** and provides predictions through a simple Flask web interface.

## Project Overview
Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected mosquitoes. Traditional malaria diagnosis is usually performed manually by examining blood smear images under a microscope, which is time-consuming and requires trained medical experts.
This project aims to automate the malaria screening process using **Deep Learning**. A CNN model is trained on blood cell images and integrated into a Flask-based web application where users can upload an image and get a prediction result instantly.

## Features
- Malaria detection from microscopic blood cell images
- Deep learning model built using CNN
- Binary classification:
  - **Parasitized**
  - **Uninfected**
- Flask web application for prediction
- Image upload support
- Prediction confidence display
- Clean and user-friendly interface

## Technologies Used
- **Python**
- **TensorFlow / Keras**
- **Flask**
- **NumPy**
- **Pillow**
- **HTML**
- **CSS**

## Dataset
This project uses the **Malaria Cell Images Dataset**, which contains microscopic images of blood smear cells divided into two categories:
- **Parasitized** – infected blood cells containing malaria parasites
- **Uninfected** – healthy blood cells without infection

Dataset source: Kaggle Malaria Cell Images Dataset


# How It Works
The user uploads a blood cell image through the web interface.
The image is resized and normalized.
The trained CNN model processes the image.
The model predicts whether the cell is:
Parasitized
Uninfected
The result and confidence score are displayed on the screen.

# Model Workflow
Input Image

   ↓
   
Image Preprocessing

   ↓
   
CNN Model Prediction

   ↓
   
Classification Output

   ↓
   
Parasitized / Uninfected

# Installation and Setup
1. Clone the repository
git clone https://github.com/Gauravdbg3010/Malaria-Detection-Using-Deep-Learning.git
cd Malaria-Detection-Using-Deep-Learning
2. Install required libraries
pip install tensorflow flask numpy pillow
You can also install other commonly used libraries if needed:
pip install pandas matplotlib seaborn scikit-learn
3. Run the Flask application
python app.py
4. Open in browser
http://127.0.0.1:5000
Training the Model
To train the CNN model again, run:
python train_model.py
After training, the model file will be saved in the Model/ folder as:
malaria_model.h5

# Output
The application predicts one of the following classes:
Parasitized
Uninfected
It also displays:
Prediction confidence
Uploaded image preview
Timestamp of prediction

# Example Use Case
This system can be used as a supportive diagnostic tool to help identify malaria infection from blood smear images quickly and efficiently. It is especially useful for educational, research, and prototype healthcare applications.

# Future Improvements
Improve model accuracy using transfer learning
Add login and registration system
Store prediction history in database
Deploy on cloud platforms
Add support for mobile devices
Use explainable AI for better medical interpretation





