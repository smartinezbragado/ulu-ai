import pandas as pd
import streamlit as st
from services.predict import send_api_request   
from services.utils import (
    upload_dataframe, 
    launch_buttom, 
    encode_audio_to_base64, 
    download_text, 
    handle_exceptions,
    upload_text
)
    
    
@handle_exceptions
def ai_on_documents_component(selected_model: str) -> None:
    uploaded_dataframe = upload_dataframe("Ready to transform your data? Upload a csv or excel file here:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if isinstance(uploaded_dataframe, pd.DataFrame):
        column_to_modify = st.selectbox('Select the column you want to modify:', uploaded_dataframe.columns)
        
        if column_to_modify is not None:
            prompt = st.text_input(f'Explain the modification with natural text in the column {column_to_modify}:')
    
            if selected_model == "Apply modifications with natural language" and prompt is not None :
                modified_df = launch_buttom(
                    request_fn=send_api_request,
                    input={
                        "model": selected_model,
                        "category": "llm_on_documents",
                        "inputs": {
                            "prompt": encode_audio_to_base64(uploaded_audio),
                            "model": "large-v2",
                            "transcription": "plain text",
                            "translate": False,
                            "language": "en",
                        }
                    },
                    waiting_str="🎧 Hang tight... We're spinning your audio into text! 🌀",
                    output_str="🎬 Voila! Your audio has been magically transcribed. 🎉"
                )
        
            if modified_df:
                transcipted_text = ' '.join([segment['text'] for segment in transcription['output']['segments']])
                st.markdown(transcipted_text, unsafe_allow_html=True)
                download_text(
                    text=transcipted_text, label="Download transcription", filename="transcription.txt"
                )