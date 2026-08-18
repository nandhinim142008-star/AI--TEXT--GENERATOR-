import streamlit as st
from transformers import pipeline
from PIL import Image

 #Page settings
st.set_page_config(
 page_title="AI Text Generator",
 page_icon="🤖"
)

st.title("🔍 AI Object Detection")
detector = pipeline("object-detection")
image = st.file_uploader(
  "Upload an image",
  type=["jpg", "png", "jpeg"]
)
if image:
  img = Image.open(image)
  st.image(img)
  if st.button("🔍 Detect Objects"):
    result = detector(img)
    st.write(result)

