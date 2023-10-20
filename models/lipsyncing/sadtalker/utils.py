import io
import base64
from PIL import Image


def decode_base64_to_image(base64_string: str) -> Image:
    """Given a base64 string, returns the decoded image"""
    decoded_image = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(decoded_image))
    return image


def decode_base64_to_audio(base64_string: str) -> bytes:
    """Given a base64 string, returns the decoded audio"""
    decoded_audio = base64.b64decode(base64_string)
    return decoded_audio


def encode_video_to_base64(video_path: str) -> str:
    """Given a video path, returns the encoded base64 string"""
    with open(video_path, "rb") as video_file:
        return base64.b64encode(video_file.read()).decode()