import streamlit as st
import os
import io
from PIL import Image

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
image_model = genai.GenerativeModel("gemini-1.5-flash")

def get_caption(platform,max_length,image):
    min_length = 20
    if platform is None:
        text = f"Generate a caption for this image: {image} with max length of {max_length} and min length of {min_length}"
    else:
        text = f"Generate me a caption for this image for {platform}: {image} which i can use on my {platform} and the caption should be maximum length of {max_length}"
    response = image_model.generate_content([text,image])
    return response.text

def get_userinput():
    user_input= st.text_input("")
    return user_input


st.header("Image :green[Caption] Generator :books:", divider=True)
st.write("This app generates captions for :blue[images]")

uploaded_file = st.file_uploader(":red[choose] :green[an] :blue[image]....", type=["jpg","png","jpeg"])
max_length = st.slider("Select the length of the caption", 50,100,70)

platform = ""

if st.button("Identify Image"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption="uploaded Image.", use_column_width= True)
        st.write("")
        st.write("Generating Caption")
        caption = get_caption(platform,max_length,image)
        st.write(f"Caption: {caption}")
    else:
        st.write("Please Uplaod an image first")

if st.button("Insta Caption"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image,caption="uploaded Image.", use_column_width= True)
        st.write("")
        st.write("Generating Caption for Instagram")
        caption = get_caption("Instagram",max_length,image)
        st.write(f"Caption: {caption}")
    else:
        st.write("Please Uplaod an image first")