import os
import time
import json
import runpod
import requests
import streamlit as st
from src.config import MODELS


runpod.api_key = os.environ['RUNPOD_API_KEY']

def check_api_status(request) -> str:
    time.sleep(1)
    if request.status() == "IN_PROGRESS":
        st.write("The model is currently processing your request. Thank you for your patience.")
    if request.status() == "IN_QUEUE":
        st.write("Your request is in the queue. Hang tight!")
    while request.status() == "IN_QUEUE":
        time.sleep(2)
    if request.status() == "FAILED":
        st.write("Your request failed")
        
        
def send_runpod_api_request(model: str, category: str, inputs: dict):
    endpoint_name = MODELS[category]['models'][model]['endpoint_name']
    endpoint = runpod.Endpoint(os.environ[endpoint_name])
    run_request = endpoint.run(inputs)
    check_api_status(run_request)
    output = run_request.output()
    return output


def send_api_request(model: str, category: str, inputs: dict):
    endpoint_name = MODELS[category]['models'][model]['endpoint_name']
    endpoint = os.environ[endpoint_name]
    payload = payload = {"input": inputs}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": os.environ['RUNPOD_API_KEY']

    }
    response = requests.post(endpoint, json=payload, headers=headers)
    return json.loads(response.text)
