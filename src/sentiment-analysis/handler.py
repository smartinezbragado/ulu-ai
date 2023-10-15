import runpod
from utils import read_file_as_dataframe
from inference import load_model, load_tokenizer, predict


def handler(event):
    path = event['path']
    model_name = event['model_name']
    
    # Model loading
    model = load_model(model_name)
    tokenizer = load_tokenizer(model_name)
    
    # Data loading
    df = read_file_as_dataframe(path)
    
    # Inference
    df['classification'] = df.text.apply(
        lambda row: predict(input_text=row, tokenizer=tokenizer, model=model)
    )

    return df.to_excel("uluai.xlsx")


runpod.serverless.start({
    "handler": handler
})