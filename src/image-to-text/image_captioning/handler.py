import runpod
from utils import decode_base64_to_image, load_model, predict

## load your model(s) into vram here
processor, model = load_model()


def handler(event):
    # Load inputs
    input = event['input']
    question = input['question']
    encoded_image = input['image']
    
    # Decode input image
    image = decode_base64_to_image(encoded_image)
    
    # Get plate text
    text = predict(image=image, question=question)
    
    return text


runpod.serverless.start({
    "handler": handler
})