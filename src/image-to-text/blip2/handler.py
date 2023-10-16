import runpod
import os
import time
from .utils import decode_image, load_model, predict

## load your model(s) into vram here
processor, model = load_model()

def handler(event):
    # Load inputs
    input = event['input']
    question = input['question']
    encoded_image = input['encoded_image']
    
    # Decode input image
    image = decode_image(encoded_image)
    
    # Get plate text
    text = predict(image, question)
    
    return {"text": text}


runpod.serverless.start({
    "handler": handler
})