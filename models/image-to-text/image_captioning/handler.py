import runpod
import logging
from runpod.serverless.modules.rp_logger import RunPodLogger
from services.utils import decode_base64_to_image, load_model, device

logger = RunPodLogger()

## load your model(s) into vram here
processor, model = load_model()


def handler(event):
    try:
        # Load inputs
        input = event['input']
        question = input['question']
        encoded_image = input['image']
                
        # Decode input image
        image = decode_base64_to_image(encoded_image)
        
        # Encode inputs
        qtext = f"Question: {question} Answer:"
        inputs = processor(image, qtext, return_tensors="pt").to(device)
        
        # Make prediction
        logger.info("Making inference")
        encoded_output = model.generate(**inputs)
        
        # Decode output
        generated_text = processor.decode(encoded_output[0], skip_special_tokens=True).strip()
        
        return generated_text

    except Exception as e:
        logger.error(str(e))
        return {
            'status': 'error',
            'message': str(e)
        }


runpod.serverless.start({
    "handler": handler
})