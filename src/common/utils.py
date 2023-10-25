import io
import base64
import pandas as pd
import dotenv
import zipfile
from PIL import Image
import streamlit as st
from typing import Callable


dotenv.load_dotenv()


class InvalidFormatError(Exception):
    pass


def handle_exceptions(func: Callable):
    """Decorator to handle exceptions and display appropriate Streamlit messages"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    return wrapper


# Image
def encode_image_to_base64(image: Image) -> str:
    """Given a PIL.Image object, returns the base64 encoded string of the image"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')


def decode_base64_to_image(base64_string: str) -> Image:
    """Given a base64 string, returns the decoded image"""
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(decoded_image))
    return image


def upload_image(text: str) -> Image:
    """Upload image"""
    uploaded_file = st.file_uploader(text, type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
    return image


def download_images(images: list):
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
        file_name="uluai.zip",
        mime="application/zip",
    )


# Audio
def encode_audio_to_base64(audio_file: str) -> str:
    """Given an audio file path, returns the base64 encoded string of the audio"""
    return base64.b64encode(audio_file).decode('utf-8')


def decode_base64_to_audio(base64_string: str) -> bytes:
    """Given a base64 string, returns the decoded audio"""
    decoded_audio = base64.b64decode(base64_string)
    return decoded_audio


def upload_audio(label: str):
    uploaded_file = st.file_uploader(label, type=["mp3", "mp4", "wav"])
    st.markdown("<br>", unsafe_allow_html=True)
    
    if uploaded_file is not None:
        audio_file = uploaded_file.read()
        st.audio(audio_file)
            
    return audio_file


def download_audio(audio: bytes):
    st.download_button(
        label="Download generated audio",
        data=audio,
        file_name="ulu.mp3",
        mime='audio/mpeg',
    )


# Text
def download_text(text: str):
    st.download_button(
        label="Download generated text",
        data=text,
        file_name="ulu.txt",
        mime='text/plain',
    )


# Video
def encode_video_to_base64(video_file: str) -> str:
    """Given a video file path, returns the base64 encoded string of the video"""
    with open(video_file, "rb") as video:
        return base64.b64encode(video.read()).decode('utf-8')
    

def decode_base64_to_video(base64_string: str) -> io.BytesIO:
    """Given a base64 string, returns the decoded video as a BytesIO object"""
    decoded_video = base64.b64decode(base64_string)
    video = io.BytesIO(decoded_video)
    return video


def upload_video(label: str) -> io.BytesIO:
    """Upload video"""
    uploaded_file = st.file_uploader(label, type=["mp4", "avi"])
    if uploaded_file is not None:
        video = io.BytesIO(uploaded_file.read())
        st.video(video, caption='Uploaded Video.')
        return video


def download_video(video: bytes):
    st.download_button(
        label="Download generated video",
        data=video,
        file_name="ulu.mp4",
        mime='video/mp4',
    )


# Excel and csv files
def upload_file(label: str) -> io.BytesIO:
    """Upload excel or csv file"""
    uploaded_file = st.file_uploader(label, type=["csv", "xlsx"])
    if uploaded_file is not None:
        file = io.BytesIO(uploaded_file.read())
        return file


def download_file(df: pd.DataFrame, label: str, type: str):
    if type == 'csv':
        data = df.to_csv(index=False)
        mime_type = 'text/csv'
    elif type == 'xlsx':
        data = df.to_excel(index=False)
        mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    else:
        raise ValueError("Invalid type. Expected 'csv' or 'excel'")
    
    st.download_button(
        label=label,
        data=data,
        file_name=f"ulu.{type}",
        mime=mime_type,
    )
    

def read_file_as_dataframe(path: str) -> pd.DataFrame:
    """Given a file path to an excel or csv file returns a pandas dataframe"""
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)
    else:
        raise InvalidFormatError("Invalid file format")

 


    


















def download_dataframe(df: pd.DataFrame, label: str, filename: str, type: str):
    if type == 'csv':
        data = df.to_csv(index=False)
        mime_type = 'text/csv'
    elif type == 'excel':
        data = df.to_excel(index=False)
        mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    else:
        raise ValueError("Invalid type. Expected 'csv' or 'excel'")
    
    st.download_button(
        label=label,
        data=data,
        file_name=filename,
        mime=mime_type,
    )




        


def upload_dataframe(text: str):
    """Upload csv or excel file and return a pandas dataframe"""
    uploaded_file = st.file_uploader(text, type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.type == "application/vnd.ms-excel":
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
            else:
                raise ValueError("Uploaded file is not a csv or excel file")
            st.dataframe(df)
            return df
        except Exception as e:
            st.error(f"Error: {e}")

