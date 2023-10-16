import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration


def decode_image(image_string: str) -> PIL.Image:
    """Decodes base64 encoded image into PIL.Image"""
    image_bytes = base64.b64decode(image_string)
    image = Image.open(BytesIO(image_bytes))
    return image


def load_model():
    """Loads the model and preprocessor"""
    processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
    model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16, device_map="auto")
    return processor, model


def predict(image: PIL.Image, question: str): -> str
    input_ids = processor(raw_image, question, return_tensors="pt").to("cuda", torch.float16)
    output_ids = model.generate(**input_ids)
    text = processor.decode(out[0], skip_special_tokens=True).strip()
    return text
