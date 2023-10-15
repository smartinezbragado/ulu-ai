import torch
import base64
from PIL import Image
from io import BytesIO
from transformers import (
    TrOCRProcessor,
    VisionEncoderDecoderModel
)


def load_model(path: str):
    """Loads model and processor"""
    device = torch.device('cuda:0' if torch.cuda.is_available else 'cpu')
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
    model = VisionEncoderDecoderModel.from_pretrained(path).to(device)
    return processor, model


def decode_image(image_string: str) -> PIL.Image:
    """Decodes base64 encoded image into PIL.Image"""
    image_bytes = base64.b64decode(image_string)
    image = Image.open(BytesIO(image_bytes))
    return image


def predict(image, processor, model) -> str:
    """
    :param image: PIL Image.
    :param processor: Huggingface OCR processor.
    :param model: Huggingface OCR model.

    Returns:
        generated_text: the OCR'd text string.
    """
    pixel_values = processor(image, return_tensors='pt').pixel_values.to(device)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text