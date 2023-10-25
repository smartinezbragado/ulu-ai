import torch
import scipy
import base64
from transformers import BarkModel, AutoProcessor


DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"


def load_model(hf_repository: str = "suno/bark"):
    processor = AutoProcessor.from_pretrained(hf_repository)
    model = BarkModel.from_pretrained(hf_repository)
    return processor, model.to(DEVICE)


def save_speech(path: str, speech, model) -> None:
    sampling_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(path, rate=sampling_rate, data=speech[0].cpu().numpy())
    
    
def encode_audio_to_base64(path: str) -> str:
    with open(path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode('utf-8')

    
    
MALE_LANGUAGE_TO_VOICE = {
    "english": "v2/en_speaker_6",
    "french": "v2/fr_speaker_3",
    "spanish": "v2/es_speaker_5",
    "italian": "v2/it_speaker_4",
    "german": "v2/de_speaker_1" 
}

FEMALE_LANGUAGE_TO_VOICE = {
    "english": "v2/en_speaker_9",
    "french": "v2/fr_speaker_5",
    "spanish": "v2/es_speaker_9",
    "italian": "v2/it_speaker_7",
    "german": "v2/de_speaker_8" 
}