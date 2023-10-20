from PIL import Image
import io
from diffusers import StableDiffusionUpscalePipeline
import torch
import base64


def load_model():
    # load model and scheduler
    pipeline = StableDiffusionUpscalePipeline.from_pretrained("stabilityai/stable-diffusion-x4-upscaler", torch_dtype=torch.float16)
    pipeline = pipeline.to("cuda")
    return pipeline


def decode_base64_to_image(encoded_image):
    image = Image.open(io.BytesIO(base64.b64decode(encoded_image)))
    return image


def encode_image_to_base64(image: Image) -> str:
    """Given a PIL.Image object, returns the base64 encoded string of the image"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str.decode('utf-8')
