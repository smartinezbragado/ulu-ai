import runpod
from runpod.serverless.modules.rp_logger import RunPodLogger
from utils import decode_base64_to_image, load_model, encode_image_to_base64

logger = RunPodLogger()

## load your model(s) into vram here
pipeline = load_model()


def handler(event):
    try:
        # Load inputs
        input = event['input']
        encoded_image = input['image']
                
        # Decode input image
        image = decode_base64_to_image(encoded_image).resize((256, 256))

        # Upscale image
        upscaled_image = pipeline(prompt="", image=image).images[0]
        
        # Encode image
        upscaled_image_str = encode_image_to_base64(upscaled_image)
        
        return upscaled_image_str

    except Exception as e:
        logger.error(str(e))
        return {
            'status': 'error',
            'message': str(e)
        }


runpod.serverless.start({
    "handler": handler
})