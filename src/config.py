MODELS = {
    # "text_classification":{
    #     "sentiment-analysis": {
    #         "options": ["distilbert-base-uncased"],
            # "input_column": "text",
            # "input_format": ["xlsx", "csv"],
            # "output_format": ["xlsx", "csv"],
            # "output_path": ["path"]
    #     },
    # },
    "image_classification": {
        "plate_recognition": {
            "name": "Car Plate Recognition",
            "input_type": "image",
            "output_type": "text",
        }
    },
    "lipsyncing": {
        "sadtalker": {
            "name": "LipSyncing",
            "input": ["image", "audio"],
            "output": "video",
            "endpoint_name": ""
        }
    }

    ""
    
}