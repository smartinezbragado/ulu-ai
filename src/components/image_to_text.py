import streamlit as st
from services.utils import upload_image, encode_image_to_base64, launch_buttom
from services.predict import send_runpod_api_request
    
    
def add_image_to_text_component(selected_model: str) -> None:
    
    if selected_model == "car_plate_recognition":
        image = upload_image("Upload a picture of a vehicle:")
        
    if selected_model == "handwritten_transcription":
        st.markdown("<br>", unsafe_allow_html=True)
        image = upload_image("Upload a picture of a handwritten text:")
        if image is not None:
            transcription = launch_buttom(
                input={
                    "model": selected_model,
                    "category": "image_to_text",
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
                    "category": "image_to_text",
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
                st.markdown(f"**Answer:** {caption}", unsafe_allow_html=True)