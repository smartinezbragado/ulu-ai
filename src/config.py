MODELS = {
    "text_to_image": {
        "name": "Text to Image",
        "models": {
            "high_resolution_style": {
                "name": "High Resolution Style",
                "description": "Generate anything you can imagine in 2048 resolution",
                "endpoint_name": "SD_XL_ENDPOINT"
            },
            "realistic_style": {
                "name": "Realistic Style",
                "description": "Generate anything you can imagine with a realistic style",
                "endpoint_name": "SD_REALISTIC_VISION_ENDPOINT",
            },
            "anime_style":{
                "name": "Anime Style",
                "description": "Generate anything you can imagine with a anime style",
                "endpoint_name": "SD_ANIME_STYLE_ENDPOINT",
            }
        },
        "input_format": ["text"],
        "output_format": "image",
    },
    "image_to_text": {
        "name": "Image to text",
        "models": {
            "car_plate_recognition": {
                "name": "Car Plate Recognition",
                "description": "Extract the car plate from a vehicle image",
                "endpoint_name": "CAR_PLATE_REGONITION_ENDPOINT",
            },
            "image_captioning": {
                "name": "Image Captioning",
                "description": "Ask any question you have to an image",
                "endpoint_name": "IMAGE_CAPTIONING_ENDPOINT"
            },
        },
        "input_format": ["image"],
        "output_format": "text"
    },
    "lip_syncing": {
        "name": "Lip Syncing",
        "models": {
            "sadtalker": {
                "name": "SadTalker",
                "description": "Get a video of yourself talking as someone else",
                "endpoint_name": "SADTALKER_ENDPOINT"
            }
        },
        "input_format": ["image", "audio"],
        "output_format": "video",
    },    
    "audio_to_text": {
        "name": "Audio to Text",
        "models": {
            "transcription": {
                "name": "Transcription",
                "description": "Transcript any audio into text",
                "endpoint_name": "TRANSCRIPTION_ENDPOINT"
            }
        },
        "input_format": ["audio"],
        "output_format": "text",
    },  
    "image_to_image": {
        "name": "Image to Image",
        "models": {
            "increase_resolution": {
                "name": "Increase Resolution",
                "description": "Increase the resolution of any image",
                "endpoint_name": ""
            },
            "image_tuning": {
                "name": "Image Tuning",
                "description": "Modify your image as you wish",
                "endpoint_name": ""
            }
        },
        "input_format": ["image", "text"],
        "output_format": "image",
    },
    "chat_with_documents": {
        "name": "Chat with documents",
        "models": {
            "pdf": {
                "name": "PDF",
                "description": "Ask questions to your pdf",
                "endpoint_name": ""
            },
            "csv": {
                "name": "CSV",
                "description": "Ask questions to your csv",
                "endpoint_name": ""
            },
            "text_document": {
                "name": "Text Document",
                "description": "Ask questions to your text document",
                "endpoint_name": ""
            }
        },
        "input_format": ["document", "text"],
        "output_format": "text",
    },
    "video_to_video": {
        "name": "Video to Video",
        "models": {
            "video_translation": {
                "name": "Video Translation",
                "description": "Generate vides as you talk in a new language",
                "endpoint_name": ""
            },
            "video_subtitles": {
                "name": "Video Subtitles",
                "description": "Add subtitles to your video",
                "endpoint_name": ""
            }
        },
        "input_format": ["video", "text"],
        "output_format": "video"
    },
    "sentiment_analysis": {
        "name": "Sentiment Analysis",
        "models": {
            "tweets_sentiment": {
                "name": "Tweets sentiment",
                "description": "Get the sentiment of your tweets",
                "endpoint_name": ""
            },
            "product_review_sentiment": {
                "name": "Product review sentiment",
                "description": "Product review sentiment",
                "endpoint_name": ""
            }
        },
        "input_format": ["text"],
        "output_format": ["float", "text"]
    },
    "llm_on_documents": {
        "name": "LLM on documents",
        "models": {
            "csv": {
                "name": "CSV",
                "description": "Transform the columns of your CSV using natural language",
                "endpoint_name": ""
        },
            "excel": {
                "name": "EXCEL",
                "description": "Transform the columns of your EXCEL using natural language",
                "endpoint_name": ""
        },
        
        },
        "input_format": ["csv", "xslx", "text"],
        "output_format": ["csv", "xslx", "text"],
    },
    "text_to_text": {
        "name": "Text to Text",
        "models": {
            "translation": {
                "name": "Translation",
                "description": "Transform the columns of your CSV using natural language",
                "endpoint_name": ""
        },
            "email_generation": {
                "name": "Email Generation",
                "description": "Convert your inputs into a well-written email",
                "endpoint_name": ""
        },
            "social_media_content_generation": {
                "name": "Social Media Content Generation",
                "description": "Generate social media content",
                "endpoint_name": ""
        },
            "summary_generation": {
                "name": "Summary Generation",
                "description": "Generate a summary of your text",
                "endpoint_name": ""
            }
        },
        "input_format": ["csv", "xslx", "text"],
        "output_format": ["csv", "xslx", "text"],
    }
}