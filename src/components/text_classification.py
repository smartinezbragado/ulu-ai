import streamlit as st
from common.utils import launch_buttom
from common.predict import send_runpod_api_request


def add_text_classification_components(selected_model: str) -> None
        
        if sentiment_analysis:
            st.markdown(f"Your text is {sentiment_analysis['sentiment']} with a score of {sentiment_analysis['score']}")
            