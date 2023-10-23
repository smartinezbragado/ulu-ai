import runpod
from common.utils import load_model, predict

financial_model = load_model("ProsusAI/finbert")
twitter_model = load_model("cardiffnlp/twitter-roberta-base-sentiment-latest")
generic_model = load_model("distilbert-base-uncased-finetuned-sst-2-english")


def handler(event):
    input = event['input']
    model_name = input['model_name']
    text = input['text']
    
    # Inference
    if model_name == "financial":
        sentiment, score = predict(financial_model, text)
        return {"sentiment": sentiment, "score": score}
    
    if model_name == "twitter":
        sentiment, score = predict(twitter_model, text)
        return {"sentiment": sentiment, "score": score}
    
    if model_name == "generic":
        sentiment, score = predict(generic_model, text)
        return {"sentiment": sentiment, "score": score}
    
    else:
        raise ValueError("model_name must be within: [generic, twitter, financial]")


runpod.serverless.start({
    "handler": handler
})