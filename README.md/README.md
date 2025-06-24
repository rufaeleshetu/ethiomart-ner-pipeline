# 📦 Ethio NER Pipeline

Named Entity Recognition (NER) pipeline tailored for **Amharic Telegram-based E-commerce vendors**, leveraging **XLM-RoBERTa** and Hugging Face libraries. The pipeline covers full end-to-end functionality including scraping, preprocessing, fine-tuning, and deployment.

---

## 📌 Objectives

- Extract Amharic messages from Telegram business channels
- Annotate and preprocess NER training data
- Fine-tune multilingual models (XLM-RoBERTa) on custom entities
- Evaluate and visualize model performance
- Deploy with Gradio and publish on Hugging Face Hub

---

## 🧱 Project Structure

ethiomart-ner-pipeline/
│
├── notebooks/                   # Jupyter notebooks (EDA, tokenization, training)
├── scripts/                     # Python scripts (scraper, preprocessor, app)
├── data/                        # Raw and labeled data (e.g., .conll format)
├── gradio_app/                  # Gradio UI for inference (deployed on Spaces)
├── final_ner_model/            # Saved fine-tuned model (pushed to HF Hub)
│
├── README.md
├── requirements.txt
└── .gitignore
🔍 Named Entity Labels
We used domain-specific labels:

B-Product, I-Product

B-PRICE, I-PRICE

B-LOC, I-LOC

O for outside tokens

🔬 Model Training & Evaluation
Metric	Score
Precision	86.27%
Recall	92.87%
F1 Score	89.45%
Eval Loss	1.65

Model: xlm-roberta-base (fine-tuned)

Trainer Args:

Epochs: 4

Batch Size: 8

Learning Rate: 2e-5

🚀 Deployment
✅ Model Hub: rufeshe/ethio-ner-model

✅ Gradio Space: rufeshe/ethio-ner-space

📥 Usage

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("rufeshe/ethio-ner-model")
model = AutoModelForTokenClassification.from_pretrained("rufeshe/ethio-ner-model")

ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
ner("ይህ አዲስ መሳሪያ በ500 ብር ነው።")
🧠 Model Comparison & Interpretability
Compared baseline bert-base-multilingual-cased with xlm-roberta-base

Chose XLM-RoBERTa due to better F1 and recall on underrepresented tags

Used manual token-level inspection to verify prediction behavior

⚖️ License
MIT License

👤 Author
Rufeshe
🔗 Hugging Face Profile
📬 For inquiries, reach out via your Hugging Face profile or GitHub