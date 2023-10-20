import streamlit as st
from PIL import Image


def text_to_image_examples(input_prompt: str, output_image_path: str) -> None:
    st.markdown(f"**Prompt:**")
    st.markdown(input_prompt)

    st.markdown("**Generated Image:**")
    img = Image.open(output_image_path)
    st.image(img, caption="Generated Image", use_column_width=True)
        

def transcription_examples(input_audio_path: str, output_text_path: str) -> None:
    st.markdown("**Audio:**")
    audio = open(input_audio_path, 'rb').read()
    st.audio(audio, format='audio/mp3')
    
    with open(output_text_path, 'r') as file:
        output_text = file.read()
        
    st.markdown("**Transcription:**")
    st.markdown(output_text)


def image_to_image_examples(input_image_path: str, output_image_path: str) -> None:
    st.markdown("**256 x 256  Image:**")
    input_img = Image.open(input_image_path)
    st.image(input_img, caption="Input Image", use_column_width=True)
    
    st.markdown("**1024 x 1024 Image:**")
    output_img = Image.open(output_image_path)
    st.image(output_img, caption="Output Image", use_column_width=True)
    
    
def image_captioning_examples(input_image_path: str, input_question_path: str, output_text_path: str) -> None:
    st.markdown("**Input Image:**")
    input_img = Image.open(input_image_path)
    st.image(input_img, caption='Input Image.', width=input_img.width)
    
    with open(input_question_path, 'r') as file:
        question_text = file.read()
        
    st.markdown("**Question:**")
    st.markdown(question_text)
    
    with open(output_text_path, 'r') as file:
        output_text = file.read()
        
    st.markdown("**Answer:**")
    st.markdown(output_text)


def translation_examples(input_text_path: str, output_text_path: str) -> None:
    st.markdown("**Text to translate:**")
    with open(input_text_path, 'r') as file:
        input_text = file.read()
    st.markdown(input_text)
    
    st.markdown("**Output Language:**")
    st.markdown("English")
    
    st.markdown("**Translation:**")
    with open(output_text_path, 'r') as file:
        translation = file.read()
    st.markdown(translation)


def sentiment_analysis_examples(input_text_path: str, output_text_path: str) -> None:
    st.markdown("**Text to analyse:**")
    with open(input_text_path, 'r') as file:
        input_text = file.read()
    st.markdown(input_text)
    
    st.markdown("**Type of model:**")
    st.markdown("Twitter")
    
    st.markdown("**Output:**")
    with open(output_text_path, 'r') as file:
        sentiment_analysis = file.read()
    st.markdown(sentiment_analysis)
    
    
def lipsyncing_examples(input_image_path: str, input_audio_path: str, output_video_path: str) -> None:
    st.markdown("**Input Image:**")
    input_img = Image.open(input_image_path)
    st.image(input_img, caption='Input Image.', width=input_img.width)
    
    st.markdown("**Input Audio:**")
    with open(input_audio_path, 'rb') as audio_file:
        audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    
    st.markdown("**Output Video:**")
    with open(output_video_path, 'rb') as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4')
