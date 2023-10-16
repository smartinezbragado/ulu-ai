import os
import runpod
from PIL import Image
from src.config import MODELS
from src.utils import decode_base64_to_image, encode_audio_to_base64, encode_image_to_base64, check_api_status


runpod.api_key = os.environ['RUNPOD_API_KEY']


def get_text_to_image(
        model: str, 
        prompt: str, 
        negative_prompt: str,
        guidance_scale: float,
        number_of_images: int
    ) -> Image:
    endpoint_name = MODELS["text_to_image"]['models'][model]['endpoint_name']
    endpoint = runpod.Endpoint(os.environ[endpoint_name])
    if model != "high_resolution_style":
        run_request = endpoint.run(
            {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": guidance_scale,
                "width": 768,
                "height": 768,
                "num_outputs": number_of_images
            }
        )
    else:
        run_request = endpoint.run(
            {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": guidance_scale,
                "width": 768,
                "height": 768,
                "num_images": number_of_images
            }
        )
    check_api_status(run_request)
    images = run_request.output()
    try:
        images = [decode_base64_to_image(img['image']) for img in images]
    except:
        images = [decode_base64_to_image(img.replace("data:image/png;base64", "")) for img in images['images']]
    return images


def get_image_captioning():
    pass


def get_car_plate_recognition():
    pass


def get_image_tuning():
    pass


def get_image_resolution_increase():
    pass


def get_transcription(audio_file) -> str:
    endpoint = runpod.Endpoint(os.environ['TRANSCRIPTION_ENDPOINT'])

    tmp_file_path = "src/tmp/audio_file.mp3"
    
    with open(tmp_file_path, 'wb') as f:
        f.write(audio_file)
        
    base_64_audio_str = encode_audio_to_base64(audio_file)
        
    with open('base_64_audio.txt', 'w') as f:
        f.write(base_64_audio_str)
        
    run_request = endpoint.run(
        {
            # "audio": "/Users/santiago.martinez/Documents/personal/ulu_ai/src/tmp/audio_file.mp3",
            "audio_base64": base_64_audio_str,
            "model": "medium",
            "transcription": "plain text",
            "language": None
        }
    )
    text = run_request.output()
    return text