import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, UnidentifiedImageError

st.markdown('<div class="title-wrapper"><h1 class="title">Image prediction</h1></div>', unsafe_allow_html=True)

custom_css = """
<style>
.title-wrapper {
    display: flex;
    justify-content: center;
}
.title {
    text-align: center;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

model = tf.keras.models.load_model("plant_disease_model_tuned_mobileNetV2.h5")

def predict_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class_index]
    disease_detected = predicted_class_name != "healthy"
    return disease_detected, predicted_class_name

class_names = ["Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
               "Blueberry___healthy", "Cherry_(including_sour)__Powedery_mildew", "Cherry_(including_sour)__healthy",
               "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", "Corn_(maize)___Common_rust_", "Corn_(maize)___Northern_Leaf_Blight",
               "Corn_(maize)___healthy", "Grape___Black_rot", "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
               "Grape___healthy", "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot", "Peach___healthy",
               "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy", "Potato___Early_blight", "Potato___Late_blight",
               "Potato___healthy", "Raspberry___healthy", "Soybean___healthy", "Squash___Powdery_mildew",
               "Strawberry___Leaf_scorch", "Strawberry___Healthy", "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight",
               "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite",
               "Tomato___Target_Spot", "Tomato_Yellow_Leaf_Curl_Virus", "Tomato_mosaic_virus", "Tomato___healthy"]

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    disease_detected, predicted_class_name = predict_image(image)
    status = f": {predicted_class_name}" if disease_detected else "No disease detected"
    st.write(f'Prediction: {status}')
    st.session_state.status = status
