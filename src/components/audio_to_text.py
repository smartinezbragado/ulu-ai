import streamlit as st
from services.utils import upload_audio, launch_buttom, encode_audio_to_base64, download_text
from services.predict import send_api_request   
    
def add_audio_to_text_component(selected_model: str) -> None:
    uploaded_audio = upload_audio("Ready to transform your audio into text? Upload your audio file here:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if selected_model == "transcription" and uploaded_audio is not None:
        transcription = launch_buttom(
            request_fn=send_api_request,
            input={
                "model": selected_model,
                "category": "audio_to_text",
                "inputs": {
                    "audio_base64": encode_audio_to_base64(uploaded_audio),
                    "model": "large-v2",
                    "transcription": "plain text",
                    "translate": False,
                    "language": "en",
                }
            },
            waiting_str="🎧 Hang tight... We're spinning your audio into text! 🌀",
            output_str="🎬 Voila! Your audio has been magically transcribed. 🎉"
        )
        
        if transcription:
            transcipted_text = ' '.join([segment['text'] for segment in transcription['output']['segments']])
            st.markdown(transcipted_text, unsafe_allow_html=True)
            download_text(
                text=transcipted_text, label="Download transcription", filename="transcription.txt"
            )