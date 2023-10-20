#!/usr/bin/env python
''' Contains the handler function that will be called by the serverless. '''

import os
import runpod
from inference import main
from runpod.serverless.modules.rp_logger import RunPodLogger
from utils import encode_video_to_base64, decode_base64_to_image, decode_base64_to_audio


logger = RunPodLogger()


OUTPUT_VIDEO_PATH = os.path.join("results", "sadtalker.mp4")

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    # Get input rquest
    input = event["input"]
        
    os.makedirs("./inputs/", exist_ok=True)
    os.makedirs("./results/", exist_ok=True)

    image = decode_base64_to_image(input['image'])
    image_path = "./inputs/input_image.jpg"
    image.save(image_path, quality=95)

    audio = decode_base64_to_audio(input['audio'])
    audio_path = "./inputs/input_audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(audio)
    
    logger.info(os.system("ls checkpoints"))
    logger.info("Starting inference:")
    
    args = {
        "driven_audio": audio_path,
        "source_image": image_path,
        "checkpoint_dir": "./checkpoints",
        "result_dir": "./results",
        "enhancer": input.get("enhancer", "gfpgan"),
        "preprocess": input.get("preprocess", "full"),
        "still": input.get("still", True),
        "size": input.get("size", 256)
    }
    main(args)

    # Clean the folders
    os.system("rm -r ./inputs/")

    return encode_video_to_base64(OUTPUT_VIDEO_PATH)


runpod.serverless.start({"handler": handler})
