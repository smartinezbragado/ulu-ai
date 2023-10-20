import streamlit as st
from utils import launch_buttom
from predict import send_runpod_api_request

def add_text_classification_components(selected_model: str) -> None:
    model_name = st.selectbox(
        'Select the type of text you want to analyse:',
        ('Twitter', 'Financial', 'Generic')
    )
    input_text = st.text_input("Enter the text:")

    if input_text and model_name:
        sentiment_analysis = launch_buttom(
            request_fn=send_runpod_api_request,
            input={
                "model": selected_model,
                "category": "text_classification",
                "inputs": {
                    "model_name": model_name.lower(),
                    "text": input_text
                }
            },
            waiting_str="🤖 Our AI is diving deep into the text...",
            output_str="🎉 Voila! Sentiment analysis is ready for your review."
        )
        
        if sentiment_analysis:
            st.markdown(f"Your text is {sentiment_analysis['sentiment']} with a score of {sentiment_analysis['score']}")
            