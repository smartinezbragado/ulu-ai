#!/usr/bin/env python
''' Contains the handler function that will be called by the serverless. '''

import os
import runpod
import logging
from utils import load_model, predict, decode_base64_to_image


logger = logging.getLogger(__name__)


processor, model = load_model()


def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    # Get input rquest
    input = event["input"]
    logger.info(input)
    
    # Load image
    image = decode_base64_to_image(input['image'])
    
    # Make the prediction
    text = predict(image)

    return text


runpod.serverless.start({"handler": handler})
