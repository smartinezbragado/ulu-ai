import yaml
import streamlit as st
from src.examples import (
    text_to_image_examples, 
    transcription_examples, 
    image_captioning_examples,
    translation_examples,
    sentiment_analysis_examples,
    lipsyncing_examples
)
from src.services.display import (
    display_launch_buttom, 
    display_model_inputs, 
    display_model_outputs,
    parse_api_output,
    parse_runpod_output
)


with open('src/config.yaml', 'r') as file:
    config = yaml.safe_load(file)



def main():
    # Select model category
    title_text = "<h1 style='text-align: center;'>🌊 Ulu.ai 🌊</h1>"
    st.markdown(title_text, unsafe_allow_html=True)
    subtitle_text =  "<h3 style='text-align: center; color: #0C6EFD; font-family: Arial, sans-serif;'>Unleashing the Power of Open Source</h3>"
    st.markdown(subtitle_text, unsafe_allow_html=True)

    # Select a category name
    with st.sidebar:
        category_names = [config[category]['display_name'] for category in list(config.keys())]
        st.markdown("<h4 style='text-align: left; color: black;'>Select the AI category:</h4>", unsafe_allow_html=True)
        model_category = st.selectbox('', category_names)
        model_category = model_category.lower().strip().replace(" ", "_") if model_category else None
    
        # Select specific model
        st.markdown("<br>", unsafe_allow_html=True)
        model_names = [config[model_category]['models'][model]['display_name'] for model in list(config[model_category]['models'].keys())]
        st.markdown("<h4 style='text-align: left; color: black;'>Choose your model:</h4>", unsafe_allow_html=True)
        model_name = st.radio('', model_names, format_func=lambda x: f"**{x}**")
        model_name = model_name.strip().lower().replace(" ", "_")

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(['Example', 'AI Model Playground', 'Model Details'])
    
    with tab1:
        
        if model_name == "high_resolution_style":
            text_to_image_examples(
                input_prompt="Astronaut on Mars During sunset", 
                output_image_path="./docs/examples/outputs/images/high_resolution_style.png"
            )
        
        elif model_name == "transcription":
            transcription_examples(
                input_audio_path="./docs/examples/inputs/audio/transcription.mp3", 
                output_text_path="./docs/examples/outputs/text/transcription.txt"
            )
            
        elif model_name == "image_captioning":
            image_captioning_examples(
                input_image_path="./docs/examples/inputs/images/image_captioning.jpeg", 
                input_question_path="./docs/examples/inputs/text/image_captioning.txt", 
                output_text_path="./docs/examples/outputs/text/image_captioning.txt"
            )
            
        elif model_name == "translation":
            translation_examples(
                input_text_path="./docs/examples/inputs/text/translation.txt",
                output_text_path="./docs/examples/outputs/text/translation.txt",
            )
            
        elif model_name == "sentiment_analysis":
            sentiment_analysis_examples(
                input_text_path="./docs/examples/inputs/text/sentiment_analysis.txt",
                output_text_path="./docs/examples/outputs/text/sentiment_analysis.txt",
            )
            
        elif model_name == "sadtalker":
            lipsyncing_examples(
                input_audio_path="./docs/examples/inputs/audio/lipsyncing.mp3",
                input_image_path="./docs/examples/inputs/images/lipsyncing.png",
                output_video_path="./docs/examples/outputs/video/lipsyncing.mp4"
            )
    
    with tab2:
        
        # Get model inputs and inference config
        input_config = config[model_category]['models'][model_name]['inputs']
        output_config = config[model_category]['models'][model_name]['output']
        inference_config = config[model_category]['models'][model_name]['inference']
        
        # Display inputs
        user_inputs = display_model_inputs(input_config=input_config)
        print(user_inputs)
        
        # Display launch buttom
        model_output = display_launch_buttom(
            user_inputs=user_inputs, inference_config=inference_config
        )
        
        # Display model outputs 
        if model_output:
            # Parse output depending on the inference type
            if inference_config['endpoint_type'] == 'api':
                model_output = parse_api_output(model_output=model_output, model_name=model_name)
            
            elif inference_config['endpoint_type'] == 'runpod':
                model_output = parse_runpod_output(model_output=model_output, output_config=output_config)
            
            display_model_outputs(model_output=model_output)
            
                
        with tab3:
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown("<h5 style='text-align: left; color: black;'>Open Source Model:</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{model_name}</p>", unsafe_allow_html=True)
            
            st.markdown("<h5 style='text-align: left; color: black;'>Technical Description:</h5>", unsafe_allow_html=True)
            tech_description = config[model_category]['models'][model_name]['description']
            st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{tech_description}</p>", unsafe_allow_html=True)
            
            st.markdown("<h5 style='text-align: left; color: black;'>Usage:</h5>", unsafe_allow_html=True)
            usage = None #MODELS[model_category]['models'][selected_model]['usage']
            st.markdown(f"<p style='text-align: left; color: #696969; font-family: Arial, sans-serif;'>{usage}</p>", unsafe_allow_html=True)
            
            st.markdown("<hr>", unsafe_allow_html=True)

    
if __name__ == "__main__":
    main()
