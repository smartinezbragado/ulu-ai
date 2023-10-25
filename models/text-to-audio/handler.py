import runpod
from utils import (
    load_model, 
    MALE_LANGUAGE_TO_VOICE, 
    FEMALE_LANGUAGE_TO_VOICE,
    DEVICE,
    save_speech,
    encode_audio_to_base64
)


processor, model = load_model()


def handler(event):
    input = event['input']
    text = input['text']
    gender = input['gender'].lower()
    language = input['language'].lower()
    
    # Select voice type
    if gender == "male":
        voice = MALE_LANGUAGE_TO_VOICE[language]
    
    elif gender == "female":
        voice = FEMALE_LANGUAGE_TO_VOICE[language]
    
    else:
        raise ValueError("Gender must be male or female")
    
    # Make Inference
    inputs = processor(text, voice_preset=voice).to(DEVICE)
    speech = model.generate(**inputs)
    
    # Encode Speech
    save_speech(path="ulu.wav", speech=speech, model=model)
    encoded_speech = encode_audio_to_base64("ulu.wav")
    
    return {'audio': encoded_speech}


runpod.serverless.start({
    "handler": handler
})