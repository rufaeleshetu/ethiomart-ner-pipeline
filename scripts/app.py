import gradio as gr
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model = AutoModelForTokenClassification.from_pretrained("rufeshe/ethio-ner-model")
tokenizer = AutoTokenizer.from_pretrained("rufeshe/ethio-ner-model")

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def predict_entities(text):
    return ner_pipeline(text)

gr.Interface(fn=predict_entities, 
             inputs=gr.Textbox(lines=5, placeholder="Enter Amharic e-commerce message..."), 
             outputs="json",
             title="Ethio NER Inference").launch()
