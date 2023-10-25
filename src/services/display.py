import requests
import streamlit as st
from typing import Optional
from PIL import Image
from io import BytesIO
from src.common.predict import send_api_request, send_runpod_api_request
from src.common.utils import (
    upload_image, 
    upload_audio, 
    encode_audio_to_base64, 
    encode_image_to_base64, 
    handle_exceptions,
    download_images,
    download_text,
    download_video,
    download_audio,
    decode_base64_to_audio,
    decode_base64_to_image,
    decode_base64_to_video
)


@handle_exceptions
def display_model_inputs(input_config: dict) -> dict:
    user_inputs = {}
    for name, cfg in input_config.items():
        
        if cfg['type'] == 'text':
            user_inputs[name] = st.text_input(
                label=cfg['display_sentence'], value=cfg['place_holder']
            )
            
        elif cfg['type'] == 'slider':
            user_inputs[name] = st.slider(
                label=cfg['display_sentence'], min_value=cfg['min_value'], max_value=cfg['max_value'], value=cfg['default_value']
            )
        
        elif cfg['type'] == 'selectbox':
            user_inputs[name] = st.selectbox(
                label=cfg['display_sentence'], options=cfg['options']
            )
            
        elif cfg['type'] == 'image':
            img = upload_image(label=cfg['display_sentence'])
            user_inputs[name] = encode_image_to_base64(img) if img else None
            
        elif cfg['type'] == 'audio':
            audio = upload_audio(label=cfg['display_sentence'])
            user_inputs[name] = encode_audio_to_base64(audio) if audio else None
    
    return user_inputs


@handle_exceptions
def display_launch_buttom(
    user_inputs: dict, inference_config: dict
):
    if st.button('Launch'):
        st.write(inference_config['waiting_sentence'])
        
        if inference_config['endpoint_type'] == 'api':
            output = send_api_request(
                inputs=user_inputs, endpoint_name=inference_config['endpoint_name']
            )
        elif inference_config['endpoint_type'] == 'runpod':
            output = send_runpod_api_request(
                inputs=user_inputs, endpoint_name=inference_config['endpoint_name']
            )

        st.markdown(inference_config['output_sentence'])
        return output
    
    
def parse_api_output(model_output, model_name: Optional[str] = None) -> dict:
    if model_name == "high_resolution_style":
        parsed_output = [Image.open(BytesIO(requests.get(img).content)) for img in model_output['output']['images']]
        return {'image': parsed_output}
    
    elif model_name == "transcription":
        transcipted_text = ' '.join([segment['text'] for segment in model_output['output']['segments']])
        return {'text': transcipted_text}
    
    elif model_name == "translation":
        translated_text = model_output['output']['text'][0]
        return {'text': translated_text}
     

def parse_runpod_output(model_output, output_config: str):
    if output_config['type'] == "text":
        return {'text': model_output}
    
    elif output_config['type'] == "video":
        decoded_video = decode_base64_to_video(model_output)
        return {'video': decoded_video}
    
    elif output_config['type'] == "image":
        if isinstance(model_output, list):
            decoded_image = [decode_base64_to_image(img) for img in  model_output]
        else:
            decoded_image = [decode_base64_to_image(model_output)]
        return {'image': decoded_image}
    
    elif output_config['type'] == "audio":
        if isinstance(model_output, dict):
            decoded_audio = decode_base64_to_audio(model_output['audio'])
        else:
            decoded_audio = decode_base64_to_audio(model_output)
        return {'audio': decoded_audio}
    
    
@handle_exceptions
def display_model_outputs(model_output: dict) -> None:
    for type in model_output.keys():
        if type == 'text':
            st.markdown(f"**Answer:** {model_output[type]}", unsafe_allow_html=True)
            download_text(model_output[type])
            
        elif type == 'image':
            for i, image in enumerate(model_output[type]):
                st.image(image, caption=f"Image {i+1}")
            download_images(model_output[type])
            
        elif type == 'audio':
            st.audio(model_output[type])
            download_audio(model_output[type])
            
        elif type == 'video':
            st.video(model_output[type])
            download_video(model_output[type])