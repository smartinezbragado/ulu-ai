import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, AutoTokenizer, BertForSequenceClassification


def load_tokenizer(model_name: str):
    if model_name in ["distilbert-base-uncased"]: 
        tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    elif model_name in ["ProsusAI/finbert"]:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer    

def load_model(model_name: str):
    if model_name in ["distilbert-base-uncased"]: 
        model = DistilBertForSequenceClassification.from_pretrained(model_name)
    elif model_name in ["ProsusAI/finbert"]:
        model = BertForSequenceClassification.from_pretrained(model_name)
    return model

def predict(input_text: str, tokenizer, model):
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    model.config.id2label[predicted_class_id]
    return model