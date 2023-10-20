import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


def load_model():
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large", device_map="auto", torch_dtype=torch.float16)
    return tokenizer, model.to('cuda')