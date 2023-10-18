import streamlit as st
from PIL import Image
from src.config import MODELS
import requests
from io import BytesIO
from src.utils import (
    upload_image, 
    launch_buttom, 
    upload_audio, 
    download_text,
    download_images,
    encode_audio_to_base64, 
    encode_image_to_base64, 
    decode_base64_to_image,
    decode_base64_to_video,
    
)
from predict import send_api_request, send_runpod_api_request


def main():
    # Select model category
    title_text = "<h1 style='text-align: center;'>🌊 Ulu.ai 🌊</h1>"
    st.markdown(title_text, unsafe_allow_html=True)
    subtitle_text =  "<h3 style='text-align: center; color: #0C6EFD; font-family: Arial, sans-serif;'>Unleashing the Power of Open Source</h3>"
    st.markdown(subtitle_text, unsafe_allow_html=True)

    # Select a category name
    with st.sidebar:
        category_names = [MODELS[category]['name'] for category in list(MODELS.keys())]
        st.markdown("<h4 style='text-align: left; color: black;'>Select the AI category:</h4>", unsafe_allow_html=True)
        model_category = st.selectbox('', category_names)
        model_category = model_category.lower().strip().replace(" ", "_") if model_category else None
    
        # Select specific model
        st.markdown("<br>", unsafe_allow_html=True)
        model_names = [MODELS[model_category]['models'][model]['name'] for model in list(MODELS[model_category]['models'].keys())]
        st.markdown("<h4 style='text-align: left; color: black;'>Choose your model:</h4>", unsafe_allow_html=True)
        model_name = st.radio('', model_names, format_func=lambda x: f"**{x}**")
        selected_model = model_name.strip().lower().replace(" ", "_")

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(['AI Model Playground', 'Model Details'])
    
    with tab2:
        st.markdown("<hr>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='text-align: left; color: black;'>Open Source Model:</h5>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{selected_model}</p>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='text-align: left; color: black;'>Technical Description:</h5>", unsafe_allow_html=True)
        tech_description = MODELS[model_category]['models'][selected_model]['description']
        st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{tech_description}</p>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='text-align: left; color: black;'>Usage:</h5>", unsafe_allow_html=True)
        usage = None #MODELS[model_category]['models'][selected_model]['usage']
        st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{usage}</p>", unsafe_allow_html=True)
        
        st.markdown("<hr>", unsafe_allow_html=True)
    
    with tab1:
        
        # Text to image
        if model_category == "text_to_image":
            
            prompt = st.text_input('Describe your image in detail:')
            negative_prompt = st.text_input('Describe what you do not want in your image:')
            guidance_scale = st.text_input('Guidance Scale:', 7.5)
            number_of_images = st.text_input('Number of images:', 1)
            
            if selected_model == "high_resolution_style":
                input = {
                    "model": selected_model,
                    "category": model_category,
                    "inputs": {
                        "prompt": prompt,
                        "negative_prompt": negative_prompt,
                        "guidance_scale": float(guidance_scale),
                        "num_images": int(number_of_images),
                    }
                }
            else:
                input = {
                    "model": selected_model,
                    "category": model_category,
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

            
        # Audio to text
        if model_category == "audio_to_text":
            uploaded_audio = upload_audio("Ready to transform your audio into text? Upload your audio file here:")
            st.markdown("<br>", unsafe_allow_html=True)
            
            if selected_model == "transcription" and uploaded_audio is not None:
                transcription = launch_buttom(
                    request_fn=send_api_request,
                    input={
                        "model": selected_model,
                        "category": model_category,
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
                
        # Image to text
        if model_category == "image_to_text":
            
            if selected_model == "car_plate_recognition":
                image = upload_image("Upload a picture of a vehicle:")
                
            if selected_model == "handwritten_transcription":
                st.markdown("<br>", unsafe_allow_html=True)
                image = upload_image("Upload a picture of a handwritten text:")
                if image is not None:
                    transcription = launch_buttom(
                        input={
                            "model": selected_model,
                            "category": model_category,
                            "inputs": {
                                "image": encode_image_to_base64(image),
                            }
                        },
                        waiting_str="✍️ Grab a cup of coffee... we're transcribing your handwritten text! ☕",
                        output_str="🚀 Hurray! Your handwritten text has been transcribed! 🎉"
                    )
                                        
                    st.write(transcription)
                
            if selected_model == "image_captioning":
                st.markdown("<br>", unsafe_allow_html=True)
                image = upload_image("Got a cool picture? Upload it here:")
                if image is not None:
                    # st.image(image, caption='Uploaded Image.', use_column_width=True)
                    question = st.text_input("Ask something:")
                    caption = launch_buttom(
                        request_fn=send_runpod_api_request,
                        input={
                            "model": selected_model,
                            "category": model_category,
                            "inputs": {
                                "image": encode_image_to_base64(image),
                                "question": question,
                            }
                        },
                        waiting_str="🕒 Time for a quick coffee break... your caption will be ready in a jiffy! ☕",
                        output_str="🎉 Voila! Your caption is ready! 🚀"
                    )
                    print(f"Caption: {caption}")
                    if caption:      
                        st.write(caption)
                
        # Lip Syncing
        if model_category == "lip_syncing":
            
            uploaded_image = upload_image("Upload your stunning selfie:")                
            uploaded_audio = upload_audio("Upload a funny audio:")
                    
            if uploaded_image is not None and uploaded_audio is not None:
                encoded_video = launch_buttom(
                    request_fn=send_runpod_api_request,
                    input={
                        "model": selected_model,
                        "category": model_category,
                        "inputs": {
                            "image": encode_image_to_base64(uploaded_image),
                            "audio": encode_audio_to_base64(uploaded_audio),
                        }
                    },
                    waiting_str="🎬 Lights, camera, action! Your lip sync video is in the making... 🍿",
                    output_str="🌟 And cut! Your blockbuster lip sync video is ready for the premiere! 🎥"
                )
                if encoded_video is not None:
                    st.video(decode_base64_to_video(encoded_video))
                
                
        # Image to Image
        if model_category == "image_to_image":
            
            if selected_model == "increase_resolution":
                uploaded_image = upload_image("Upload a low quality image:")

                    
            if selected_model == "image_tuning":
                uploaded_image = upload_image("Upload the image you want to modify:")
                prompt = st.text_input('Tell me what do you want to add / remove:')        
                
        
        # chat_with_documents 
        if model_category == "chat_with_documents":
            
            if selected_model == "pdf":
                uploaded_file = st.file_uploader("Upload your PDF:", type=["pdf"])
                if uploaded_file is not None:
                    pass
            
            if selected_model == "csv":
                uploaded_file = st.file_uploader("Upload your CSV:", type=["csv"])
                if uploaded_file is not None:
                    pass
                
            if selected_model == "text_document":
                uploaded_file = st.file_uploader("Upload your text document:", type=["csv"])
                if uploaded_file is not None:
                    pass
                    
            question = st.text_input('Enter your question here:')


        # Video to Videpo
        if model_category == "video_to_video":
            
            uploaded_file = st.file_uploader("Upload your video:", type=["mp4"])
            if uploaded_file is not None:
                pass

            prompt = st.text_input('Tell me what do you want to add / remove:')   
            
        # LLM document modification
        if model_category == "llm_on_documents":
            
            uploaded_file = st.file_uploader("Upload your video:", type=["csv", "xlsx"])
            if uploaded_file is not None:
                pass
            
        # Text to Text
        if model_category == "text_to_text":
            
            if selected_model == "translation":
                st.text_input("Paste the text you want to translate")
                st.selectbox("Select the translation language", ["english", "spanish", "german", "french"])
            
            if selected_model == "email_generation":
                st.text_input("Paste the key points of your email")
                st.selectbox("Select your tonne", ["angry", "happy", "other"])
            
            elif selected_model == "social_media_content_generation":
                st.text_input("Paste the key points of your social media post")
                st.selectbox("Select the social media", ["instagram", "facebook", "linkedin", "medium"])

            elif selected_model == "summary_generation":
                st.text_input("Paste the text you want to summarise:")

    
if __name__ == "__main__":
    main()
