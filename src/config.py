MODELS = {
    "text_to_image": {
        "name": "Text to Image",
        "models": {
            "high_resolution_style": {
                "name": "High Resolution Style",
                "description": "Create stunning 2048 resolution images from your imagination",
                "endpoint_name": "SD_XL_ENDPOINT"
            },
            "realistic_style": {
                "name": "Realistic Style",
                "description": "Bring your imagination to life with a touch of realism",
                "endpoint_name": "SD_REALISTIC_VISION_ENDPOINT",
            },
            "anime_style":{
                "name": "Anime Style",
                "description": "Turn your ideas into vibrant anime-style images",
                "endpoint_name": "SD_ANIME_STYLE_ENDPOINT",
            },
            "openjourney":{
                "name": "OpenJourney",
                "description": "Open Source version of the famous Midjourney model",
                "endpoint_name": "SD_OPENJOURNEY_ENDPOINT",
            }
        },
        "input_format": ["text"],
        "output_format": "image",
    },
    "image_to_text": {
        "name": "Image to text",
        "models": {
            "image_captioning": {
                "name": "Image Captioning",
                "description": "Interact with images by asking any question",
                "endpoint_name": "IMAGE_CAPTIONING_ENDPOINT"
            },
            "car_plate_transcription": {
                "name": "Car Plate Transcription",
                "description": "Extract and read car plate numbers from vehicle images",
                "endpoint_name": "CAR_PLATE_REGONITION_ENDPOINT",
            },
            "handwritten_transcription": {
                "name": "Handwritten Transcription",
                "description": "Transcribe text from handwritten images with ease",
                "endpoint_name": "HANDWRITTEN_TRANSCRIPTION",
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
                "description": "Create a video of yourself speaking as someone else",
                "endpoint_name": "LIPSYNCING_ENDPOINT"
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
                "description": "Convert any audio into readable text",
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
                "description": "Enhance the resolution of any image for a clearer view",
                "endpoint_name": ""
            },
            "image_tuning": {
                "name": "Image Tuning",
                "description": "Customize your image to your liking",
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
                "description": "Interact with your PDF by asking questions",
                "endpoint_name": ""
            },
            "csv": {
                "name": "CSV",
                "description": "Query your CSV files like a pro",
                "endpoint_name": ""
            },
            "text_document": {
                "name": "Text Document",
                "description": "Ask questions and get answers from your text documents",
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
                "description": "Speak in your language, let us generate the video in another",
                "endpoint_name": ""
            },
            "video_subtitles": {
                "name": "Video Subtitles",
                "description": "Add subtitles to your videos for better understanding",
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
                "description": "Understand the sentiment behind your tweets",
                "endpoint_name": ""
            },
            "product_review_sentiment": {
                "name": "Product review sentiment",
                "description": "Analyze the sentiment behind product reviews",
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
                "description": "Manipulate your CSV columns using natural language",
                "endpoint_name": ""
        },
            "excel": {
                "name": "EXCEL",
                "description": "Transform your EXCEL columns using simple language",
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
                "description": "Translate your text into different languages",
                "endpoint_name": ""
        },
            "email_generation": {
                "name": "Email Generation",
                "description": "Turn your thoughts into a professionally written email",
                "endpoint_name": ""
        },
            "social_media_content_generation": {
                "name": "Social Media Content Generation",
                "description": "Generate engaging content for your social media platforms",
                "endpoint_name": ""
        },
            "summary_generation": {
                "name": "Summary Generation",
                "description": "Get a concise summary of your lengthy text",
                "endpoint_name": ""
            }
        },
        "input_format": ["csv", "xslx", "text"],
        "output_format": ["csv", "xslx", "text"],
    }
}