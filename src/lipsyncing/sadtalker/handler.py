#!/usr/bin/env python
''' Contains the handler function that will be called by the serverless. '''

import os
import io
import base64
import runpod
import logging
from PIL import Image
from inference import main


logger = logging.getLogger(__name__)


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


OUTPUT_VIDEO_PATH = os.path.join("results", "sadtalker.mp4")

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    # Get input rquest
    input = event["input"]
    logger.info(input)
    os.makedirs("./inputs/", exist_ok=True)
    os.makedirs("./results/", exist_ok=True)

    image = decode_base64_to_image(input['image'])
    image_path = "./inputs/input_image.jpg"
    image.save(image_path, quality=95)

    audio = decode_base64_to_audio(input['audio'])
    audio_path = "./inputs/input_audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(audio)
    
    args = {
        "driven_audio": audio_path,
        "source_image": image_path,
        "checkpoint_dir": "./checkpoints",
        "result_dir": "./results",
        "enhancer": input.get("enhancer", "gfpgan"),
        "preprocess": input.get("preprocess", "full"),
        "still": input.get("still", False),
        "size": input.get("size", 256)
    }
    main(args)

    # Clean the folders
    os.system("rm -r ./inputs/")
    os.system("rm -r ./results/")

    return {
        "video": encode_video_to_base64(OUTPUT_VIDEO_PATH)
    }


runpod.serverless.start({"handler": handler})
