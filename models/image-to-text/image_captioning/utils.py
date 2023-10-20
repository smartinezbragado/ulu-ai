import base64
import io
import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

device = torch.device('cuda:0' if torch.cuda.is_available else 'cpu')


def decode_base64_to_image(base64_string: str) -> Image:
    """Given a base64 string, returns the decoded image"""
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(decoded_image))
    return image


def load_model():
    """Loads the model and preprocessor"""
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16 , device_map="auto")
    return processor, model.to(device)
