import streamlit as st
from google.cloud import storage
from firebase_admin import credentials, initialize_app
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
import firebase_admin


service_account_key = "C:/Users/Lena0/Desktop/Green_Guard_stream/capstone-1ccd7-firebase-adminsdk-1dq74-cf7b41c4fe.json"


if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_key)
    initialize_app(cred)


client = storage.Client.from_service_account_json(service_account_key)


bucket_name = 'capstone-1ccd7.appspot.com'
bucket = client.bucket(bucket_name)


def list_image_urls_and_names():
    images = []
    try:
        blobs = bucket.list_blobs()
        for blob in blobs:
            
            url = blob.generate_signed_url(version='v4', expiration=3600)
            
            name = blob.name
            images.append((name, url))
    except Exception as e:
        st.write(f"An error occurred while listing image URLs and names: {e}")
    return images

def extract_relevant_name(name):

    name = name.rsplit('.', 1)[0]

    parts = name.split('_')

    relevant_name = '_'.join(parts[:5]) 
    return relevant_name

st.title("Images from Green Guard Database")
st.markdown("<br>", unsafe_allow_html=True)

images = list_image_urls_and_names()


image_size = (200, 200)


for i in range(0, len(images), 3):
    cols = st.columns(3)
    for col, (name, url) in zip(cols, images[i:i+3]):
        with col:
            relevant_name = extract_relevant_name(name)
          
        
            response = requests.get(url)
            
            
            if response.status_code == 200:
                try:
                    
                    content_type = response.headers['Content-Type']
                    if 'image' in content_type:
                        
                        image = Image.open(BytesIO(response.content))
                        
                        image = image.resize(image_size)
                        
                        st.image(image, caption=relevant_name, use_column_width=True)
                    else:
                        st.write(f"Content type is not an image: {content_type}")
                except UnidentifiedImageError:
                    st.write("Error: Cannot identify the image file")
                except Exception as e:
                    st.write(f"An error occurred: {e}")
            else:
                st.write(f"Failed to retrieve image from {url}, status code: {response.status_code}")
