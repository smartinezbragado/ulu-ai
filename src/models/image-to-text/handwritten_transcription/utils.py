import io
import torch
import base64
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel


device = torch.device('cuda:0' if torch.cuda.is_available else 'cpu')


def predict(image: Image) -> str: 
    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text


def load_model():
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten').to(device)
    return processor, model


def decode_base64_to_image(base64_string: str) -> Image:
    """Given a base64 string, returns the decoded image"""
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(decoded_image)).convert("RGB")
    return image