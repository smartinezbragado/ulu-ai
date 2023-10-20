from transformers import pipeline


def load_model(hf_repository: str):
    sentiment_pipeline = pipeline('sentiment-analysis', model=hf_repository)
    return sentiment_pipeline


def predict(sentiment_pipeline, text: str):
    result = sentiment_pipeline(text)
    sentiment = result[0]["label"]
    confidence = result[0]["score"]
    return sentiment, confidence
