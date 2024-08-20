import streamlit as st
from PIL import Image

with st.expander('Start Camera!'):
    camera_image = st.camera_input('Camera')

with st.expander('Select a image!'):
    uploaded_image = st.file_uploader("Upload Image")


if camera_image:
    img_saved = Image.open(camera_image)
    camera_gray = img_saved.convert('L')
    st.image(camera_gray)

if uploaded_image:
    img_saved = Image.open(uploaded_image)
    uploaded_gray = img_saved.convert('L')
    st.image(uploaded_gray)
