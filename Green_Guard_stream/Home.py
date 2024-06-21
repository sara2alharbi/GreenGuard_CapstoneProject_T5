import streamlit as st
from PIL import Image
import base64

st.set_page_config(initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    return base64_image


custom_css = f"""
<style>
body {{
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed; /* Optional - keeps the background fixed while scrolling */
}}

.title-wrapper {{
    display: flex;
    justify-content: center;
    margin-top: 50px;  /* Adjust the top margin for the title */
}}

.title {{
    text-align: center;
    color: #333333;  /* Set the text color for the title */
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


logo = Image.open('GG_logo.png')
st.sidebar.image(logo, use_column_width=True)

st.markdown('<div class="title-wrapper"><h1 class="title">Green Guard 🌿🤖</h1></div>', unsafe_allow_html=True)

st.write(
    """
    Green Guard is a plant monitoring system is a full hardware & software system. Which consist of its physical part
    Green guard Robot and its software part. It provides Database for images get from Raspberry pi and allows users 
    to upload images for plant disease classification.
    """
)
