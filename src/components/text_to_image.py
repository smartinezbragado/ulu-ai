import requests
import streamlit as st
from PIL import Image
from io import BytesIO
from services.utils import launch_buttom
from services.predict import send_api_request, send_runpod_api_request
from services.utils import download_images, decode_base64_to_image


def add_text_to_image_component(selected_model: str) -> None:
    prompt = st.text_input('Describe your image in detail:')
    negative_prompt = st.text_input('Describe what you do not want in your image:')
    guidance_scale = st.text_input('Guidance Scale:', 7.5)
    number_of_images = st.text_input('Number of images:', 1)

    if selected_model == "high_resolution_style":
        image_sizes = [512, 768, 1024]
        image_size = st.selectbox('Image size in pixels:', image_sizes)
        input = {
            "model": selected_model,
            "category": "text_to_image",
            "inputs": {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": float(guidance_scale),
                "num_images": int(number_of_images),
                "width": image_size,
                "height": image_size
            }
        }
    else:
        input = {
            "model": selected_model,
            "category": "text_to_image",
            "inputs": {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": float(guidance_scale),
                "num_outputs": int(number_of_images),
            }
        }       

    if selected_model in ["high_resolution_style", "openjourney"]:
        images = launch_buttom(
            request_fn=send_api_request,
            waiting_str="Grab a ☕... Your images are brewing:",
            input=input,
            output_str="There it goes!"
        )
        if images:
            if selected_model == "high_resolution_style":
                images = [Image.open(BytesIO(requests.get(img).content)) for img in images['output']['images']]
            else:
                images = [Image.open(BytesIO(requests.get(img['image']).content)) for img in images['output']]
            for i, image in enumerate(images):
                st.image(image, caption=f"Image {i+1}")
                
            download_images(images)                    
            
    else:
        images = launch_buttom(
            request_fn=send_runpod_api_request,
            waiting_str="Grab a ☕... Your images are brewing:",
            input=input,
            output_str="There it goes!"
        )
        if images:
            images = [decode_base64_to_image(img['image']) for img in images]
            for i, image in enumerate(images):
                st.image(image, caption=f"Image {i+1}")
                
            download_images(images)