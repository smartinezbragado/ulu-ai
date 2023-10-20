import streamlit as st
from predict import send_runpod_api_request
from utils import (
    encode_audio_to_base64, 
    encode_image_to_base64, 
    launch_buttom, 
    decode_base64_to_video,
    upload_audio,
    upload_image,
    download_video
)
    
def add_lipsyncing_component(selected_model: str) -> None:
    uploaded_image = upload_image("Upload your stunning selfie:")                
    uploaded_audio = upload_audio("Upload a funny audio:")
            
    if uploaded_image and uploaded_audio:
        encoded_video = launch_buttom(
            request_fn=send_runpod_api_request,
            input={
                "model": selected_model,
                "category": "lip_syncing",
                "inputs": {
                    "image": encode_image_to_base64(uploaded_image),
                    "audio": encode_audio_to_base64(uploaded_audio),
                }
            },
            waiting_str="🎬 Lights, camera, action! Your lip sync video is in the making... 🍿",
            output_str="🌟 And cut! Your blockbuster lip sync video is ready for the premiere! 🎥"
        )
        print(encoded_video)
        if encoded_video is not None:
            decoded_video = decode_base64_to_video(encoded_video)
            st.video(decoded_video)
            
            download_video(decoded_video, "Download video", "lipsyncing.mp4")