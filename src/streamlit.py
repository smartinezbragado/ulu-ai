import streamlit as st
from PIL import Image
from src.config import MODELS
from src.utils import upload_image, launch_buttom, upload_audio, download_images
from src.predict import (
    get_transcription, 
    get_image_captioning, 
    get_car_plate_recognition,
    get_text_to_image,
    get_image_tuning,
    get_image_resolution_increase
)


def main():
    # Select model category
    title_text = "<h1 style='text-align: center;'>🚀 **Ulu.ai** 🚀</h1>"
    st.markdown(title_text, unsafe_allow_html=True)
    subtitle_text =  "<h3 style='text-align: center; color: #0C6EFD; font-family: Arial, sans-serif;'>Unleashing the Power of Open Source</h3>"
    st.markdown(subtitle_text, unsafe_allow_html=True)

    # Select a category name
    st.markdown("<br>", unsafe_allow_html=True)
    category_names = [MODELS[category]['name'] for category in list(MODELS.keys())]
    st.markdown("<h5 style='text-align: left; color: black;'>Select model category</h5>", unsafe_allow_html=True)
    model_category = st.selectbox('', category_names)
    model_category = model_category.lower().strip().replace(" ", "_") if model_category else None
    
    # Select specific model
    st.markdown("<br>", unsafe_allow_html=True)
    model_names = [MODELS[model_category]['models'][model]['name'] for model in list(MODELS[model_category]['models'].keys())]
    st.markdown("<h5 style='text-align: left; color: black;'>Select model category</h5>", unsafe_allow_html=True)
    model_name = st.radio('', model_names, format_func=lambda x: f"**{x}**")
    selected_model = model_name.strip().lower().replace(" ", "_")
    print(selected_model)

    description = MODELS[model_category]['models'][selected_model]['description']
    st.write(description)
    
    
    # Text to image
    if model_category == "text_to_image":
        
        prompt = st.text_input('Describe your image in detail:')
        negative_prompt = st.text_input('Describe what you do not want in your image:')
        guidance_scale = st.text_input('Guidance Scale:', 7.5)
        number_of_images = st.text_input('Number of images:', 1)
        
        images = launch_buttom(
            fn=get_text_to_image,
            waiting_str="Grab a ☕... Your images are brewing:",
            input={
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": float(guidance_scale),
                "number_of_images": int(number_of_images),
                "model": selected_model
            },
            output_str="There it goes!"
        )
        if images:
            for i, image in enumerate(images):
                st.image(image, caption=f"Image {i+1}")
                
        download_images(images)
    
    # Audio to text
    if model_category == "audio_to_text":

        audio_file = upload_audio("Upload the audio you want to transcript")

        transcription = launch_buttom(
            fn=get_transcription,
            waiting_str="Grab a coffee... and your transcription will be ready soon:",
            input={"audio_file": audio_file,},
            output_str="There it goes!"
        )
        st.markdown(transcription)
        

    # Audio to text
    if model_category == "audio_to_text":
        uploaded_file = st.file_uploader("Upload what you want to transcript to text:", type=["mp3", "mp4"])
        
        if uploaded_file is not None:
            audio_file = uploaded_file.read()
            if uploaded_file.type == "audio/mp3":
                st.audio(audio_file, format='audio/mp3')
            elif uploaded_file.type == "audio/mp4":
                st.audio(audio_file, format='audio/mp4')

        if st.button('Launch'):
            st.write("Starting transcription...")
            text = get_transcription(audio_file)
            st.markdown(f"**Text translation:** {text}")
            
            
    # Image to text
    if model_category == "image_to_text":
        
        if selected_model == "car_plate_recognition":
            
            image = upload_image("Upload a picture of a vehicle:")
            
            
        if selected_model == "image_captioning":
            image = upload_image("Upload any picture you have in mind:")
            if image is not None:
                question = st.text_input("Ask something:")
                caption = launch_buttom(
                    fn=get_image_captioning,
                    input={"question": question},
                    waiting_str="Grab a coffee... and your caption will be ready soon:",
                    output_str="There it goes!"
                )
                st.write(caption)
            
    # Lip Syncing
    if model_category == "lip_syncing":
        
        uploaded_image = st.file_uploader("Upload your selfie:", type=["jpg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image.', use_column_width=True) 
            
        uploaded_message = st.file_uploader("Upload a random message:", type=["mp3", "mp4"])
        if uploaded_message is not None:
            audio_file = uploaded_message.read()
            if uploaded_message.type == "audio/mp3":
                st.audio(audio_file, format='audio/mp3')
            elif uploaded_message.type == "audio/mp4":
                st.audio(audio_file, format='audio/mp4')
            
            
    # Image to Image
    if model_category == "image_to_image":
        
        if selected_model == "increase_resolution":
            uploaded_image = upload_image("Upload a low quality image:")
            upscaled_image = launch_buttom(
                fn=get_image_resolution_increase,
                input=uploaded_image,
                waiting_str="Grab a coffee... and your new image will be ready soon:",
                output_str="There it goes!"
            )
                
        if selected_model == "image_tuning":
            uploaded_image = upload_image("Upload the image you want to modify:")
            prompt = st.text_input('Tell me what do you want to add / remove:')        
            tuned_image = launch_buttom(
                fn=get_image_tuning,
                input=uploaded_image,
                waiting_str="Grab a coffee... and your new image will be ready soon:",
                output_str="There it goes!"
            )
            
      
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
