import streamlit as st
from src.config import MODELS


def main():
    # Select model type
    model_type = st.selectbox('Select model type:', list(MODELS.keys()))

    # Select specific model
    model_name = st.selectbox('Select specific model:', [model['name'] for model in MODELS[model_type]])

    # Get selected model
    selected_model = next(model for model in MODELS[model_type] if model['name'] == model_name)

    # Input format
    input_format = st.text_input('Input format:', value=)
    if selected_model['input_format'] == 'image':
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
    elif selected_model['input_format'] == 'audio':
        uploaded_file = st.file_uploader("Choose an audio file...", type="mp3")
        if uploaded_file is not None:
            audio_file = uploaded_file.read()
            st.audio(audio_file, format='audio/mp3')
    elif selected_model['input_format'] == 'video':
        uploaded_file = st.file_uploader("Choose a video file...", type="mp4")
        if uploaded_file is not None:
            st.video(uploaded_file)
    elif selected_model['input_format'] == 'text':
        text_input = st.text_input('Enter your text here:')
    else:
        st.write("Unsupported input format.")
    
if __name__ == "__main__":
    main()

    

