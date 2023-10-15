import runpod
import os
import time
from .utils import decode_image, load_model, predict

## load your model(s) into vram here
processor, model = load_model(path='')

def handler(event):
    # Load inputs
    input = event['input']
    encoded_image = event['encoded_image']
    # Decode input image
    image = decode_image(encoded_image)
    # Get plate text
    text = predict(image, processor, model)
    return {
        "text": text
    }


runpod.serverless.start({
    "handler": handler
})