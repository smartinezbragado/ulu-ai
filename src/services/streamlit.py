import streamlit as st
from src.config import MODELS
from examples import (
    text_to_image_examples, 
    transcription_examples, 
    image_captioning_examples,
    translation_examples,
    sentiment_analysis_examples,
    lipsyncing_examples
)
from components.lipsyncing import add_lipsyncing_component
from components.text_to_text import add_text_to_text_component
from components.image_to_text import add_image_to_text_component
from components.text_to_image import add_text_to_image_component
from components.audio_to_text import add_audio_to_text_component
from components.image_to_image import add_image_to_image_component
from components.text_classification import add_text_classification_components


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
    tab1, tab2, tab3 = st.tabs(['Example', 'AI Model Playground', 'Model Details'])
    
    with tab1:
        
        if selected_model == "high_resolution_style":
            text_to_image_examples(
                input_prompt="Astronaut on Mars During sunset", 
                output_image_path="./docs/examples/outputs/images/high_resolution_style.png"
            )
        
        elif selected_model == "transcription":
            transcription_examples(
                input_audio_path="./docs/examples/inputs/audio/transcription.mp3", 
                output_text_path="./docs/examples/outputs/text/transcription.txt"
            )
            
        elif selected_model == "image_captioning":
            image_captioning_examples(
                input_image_path="./docs/examples/inputs/images/image_captioning.jpeg", 
                input_question_path="./docs/examples/inputs/text/image_captioning.txt", 
                output_text_path="./docs/examples/outputs/text/image_captioning.txt"
            )
            
        elif selected_model == "translation":
            translation_examples(
                input_text_path="./docs/examples/inputs/text/translation.txt",
                output_text_path="./docs/examples/outputs/text/translation.txt",
            )
            
        elif selected_model == "sentiment_analysis":
            sentiment_analysis_examples(
                input_text_path="./docs/examples/inputs/text/sentiment_analysis.txt",
                output_text_path="./docs/examples/outputs/text/sentiment_analysis.txt",
            )
            
        elif selected_model == "sadtalker":
            lipsyncing_examples(
                input_audio_path="./docs/examples/inputs/audio/lipsyncing.mp3",
                input_image_path="./docs/examples/inputs/images/lipsyncing.png",
                output_video_path="./docs/examples/outputs/video/lipsyncing.mp4"
            )
    
    with tab2:
        
        # Text to image
        if model_category == "text_to_image":
            add_text_to_image_component(selected_model)
            
        # Audio to text
        if model_category == "audio_to_text":
            add_audio_to_text_component(selected_model)
                
        # Image to text
        if model_category == "image_to_text":
            add_image_to_text_component(selected_model)
  
        # Lip Syncing
        if model_category == "lip_syncing":
            add_lipsyncing_component(selected_model)
                
        # Image to Image
        if model_category == "image_to_image":      
            add_image_to_image_component(selected_model)
            
        # Text to Text
        if model_category == "text_to_text":
            add_text_to_text_component(selected_model)

        # Text Classification
        if model_category == "text_classification":
            add_text_classification_components(selected_model)
        
        
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
            
                
        with tab3:
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

    
if __name__ == "__main__":
    main()
