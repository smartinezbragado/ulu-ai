import runpod
from runpod.serverless.modules.rp_logger import RunPodLogger
from common.utils import load_model

logger = RunPodLogger()

## load your model(s) into vram here
tokenizer, model = load_model()


def handler(event):
    try:
        # Load inputs
        input = event['input']
        text = input['text']
        input_language = input['input_language']
        output_language = input['output_language']
        
        # Make prediction
        logger.info("Making inference")
        
        input_text = f"Translate {input_language} to {output_language}"
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")
        translation = model.generate(input_ids)
        
        return translation

    except Exception as e:
        logger.error(str(e))
        return {
            'status': 'error',
            'message': str(e)
        }


runpod.serverless.start({
    "handler": handler
})