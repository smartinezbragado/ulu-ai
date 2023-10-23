import streamlit as st
from common.predict import send_runpod_api_request
from common.utils import (
    encode_image_to_base64, 
    decode_base64_to_image, 
    upload_image,
    download_images,
    launch_buttom  
)

def add_image_to_image_component(selected_model: str) -> None:
    if selected_model == "image_upscaling":
        uploaded_image = upload_image("Upload your squared image and convert it to 1024x1024 resolution:")
        
        if uploaded_image:
            upscaled_image_str = launch_buttom(
                request_fn=send_runpod_api_request,
                input={
                    "model": selected_model,
                    "category": "image_to_image",
                    "inputs": {
                        "image": encode_image_to_base64(uploaded_image)
                    }
                },
                output_str="🎉 Your upscaled image is ready! 🚀",
                waiting_str="🕒 Your image is being processed... 🖼️"
            )

            if upscaled_image_str:
                upscaled_image = decode_base64_to_image(upscaled_image_str)
                st.image(upscaled_image, caption=f"High resolution image")
                
                download_images([upscaled_image])

            
    if selected_model == "image_tuning":
        uploaded_image = upload_image("Upload the image you want to modify:")
        prompt = st.text_input('Tell me what do you want to add / remove:')  