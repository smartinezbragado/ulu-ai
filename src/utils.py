import io
import base64
import time
import pandas as pd
import dotenv
import zipfile
from PIL import Image
import streamlit as st
from typing import Callable, Union, List
from predict import send_runpod_api_request, send_api_request


dotenv.load_dotenv()


class InvalidFormatError(Exception):
    pass


def read_file_as_dataframe(path: str) -> pd.DataFrame:
    """Given a file path to an excel or csv file returns a pandas dataframe"""
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)
    else:
        raise InvalidFormatError("Invalid file format")

    
 
def encode_image_to_base64(image: Image) -> str:
    """Given a PIL.Image object, returns the base64 encoded string of the image"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')
    

def encode_audio_to_base64(audio_file: str) -> str:
    """Given an audio file path, returns the base64 encoded string of the audio"""
    return base64.b64encode(audio_file).decode('utf-8')


def decode_base64_to_image(base64_string: str) -> Image:
    """Given a base64 string, returns the decoded image"""
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(decoded_image))
    return image


def decode_base64_to_audio(base64_string: str) -> bytes:
    """Given a base64 string, returns the decoded audio"""
    decoded_audio = base64.b64decode(base64_string)
    return decoded_audio


def decode_base64_to_video(base64_string: str) -> io.BytesIO:
    """Given a base64 string, returns the decoded video as a BytesIO object"""
    decoded_video = base64.b64decode(base64_string)
    video = io.BytesIO(decoded_video)
    return video


def upload_image(text: str) -> Image:
    """Upload image"""
    uploaded_file = st.file_uploader(text, type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        return image
    
def download_images(images):
    """Download images in streamlit, given a list of PIL.Image objects"""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
        for i, image in enumerate(images):
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='PNG')
            image_bytes = image_bytes.getvalue()
            zip_file.writestr(f"image_{i+1}.png", image_bytes)
    zip_buffer.seek(0)
    st.download_button(
        label="Download All Images",
        data=zip_buffer,
        file_name="images.zip",
        mime="application/zip",
    )


def upload_audio(text: str):
    uploaded_file = st.file_uploader(text, type=["mp3", "mp4"])
    
    if uploaded_file is not None:
        audio_file = uploaded_file.read()
        if uploaded_file.type == "audio/mp3":
            st.audio(audio_file, format='audio/mp3')
        elif uploaded_file.type == "video/mp4":
            st.audio(audio_file, format='audio/mp4')
        else:
            raise ValueError("The audio must be mp3 or mp4 format")
        
        return audio_file


def launch_buttom(input: dict, waiting_str: str, output_str: str, request_fn: Callable):
    if st.button('Launch'):
        st.write(waiting_str)
        output = request_fn(**input)
        st.markdown(output_str)
        return output