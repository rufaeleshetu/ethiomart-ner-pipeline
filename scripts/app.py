import gradio as gr
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load your model
model_name = "rufeshe/ethio-ner-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Use HuggingFace pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def extract_entities(text):
    ner_results = ner_pipeline(text)
    return {entity['entity_group']: entity['word'] for entity in ner_results}

# Create Gradio interface
demo = gr.Interface(fn=extract_entities,
                    inputs=gr.Textbox(lines=4, placeholder="Enter Amharic text..."),
                    outputs="json",
                    title="Amharic NER Extractor")

if __name__ == "__main__":
    demo.launch()
