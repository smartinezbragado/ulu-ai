import streamlit as st
from common.predict import send_api_request
from common.utils import download_text, launch_buttom  


def add_text_to_text_component(selected_model: str) -> None:
    if selected_model == "translation":
        
        if (input_text and input_language) and output_language:
            translation = launch_buttom(
                request_fn=send_api_request,
                input={
                    "inputs": {
                        "prompt": f"""
                            Translate to {output_language} the following text: '{input_text}'. Only return the translation. No additional text must be return." 
                        """,
                        "sampling_params": {
                            "max_tokens": 700,
                            "temperature": 0
                        }
                    }
                },
            )

            if translation:
                translation = translation['output']['text'][0]
                st.markdown("**Translation**")
                st.markdown(translation)
                download_text(translation, "Downloaded translation", "translation.txt")