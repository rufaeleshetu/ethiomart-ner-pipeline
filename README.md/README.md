# 🌍 EthioMart NER Pipeline

This repository provides an end-to-end Named Entity Recognition (NER) pipeline for Amharic e-commerce Telegram data, covering:

- Task 1: Data exploration and visualization
- Task 2: Data formatting in CoNLL
- Task 3: Dataset preparation for training
- ✅ Task 4: Fine-tuning and uploading the NER model to Hugging Face

---

## 🔧 Project Structure

ethiomart-ner-pipeline/
│
├── data/
│ ├── raw/ # Raw Telegram vendor data (JSON)
│ ├── cleaned/ # Cleaned CSVs
│ ├── ethiomart_task2_labeled.conll # Final CoNLL file
│
├── notebooks/
│ ├── task1_data_exploration.ipynb
│ ├── ner_train_preparation.ipynb # Task 4 training notebook
│ ├── final_ner_model/ # Saved fine-tuned model
│
├── scripts/
│ ├── scrape_telegram.py
│ └── preprocess_text.py
│
├── README.md
└── requirements.txt

yaml
Copy
Edit

---

## ✅ Task 4: Fine-Tuning and Uploading the NER Model

We trained a token classification model using the `xlm-roberta-base` architecture. The model was trained for 3 epochs with ~0.20 evaluation loss and exported using the `Trainer` API.

### 🔗 Model on Hugging Face

The trained model has been uploaded to Hugging Face:

👉 **[rufeshe/ethio-ner-model](https://huggingface.co/rufeshe/ethio-ner-model)**

Use it in your Python code:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model = AutoModelForTokenClassification.from_pretrained("rufeshe/ethio-ner-model")
tokenizer = AutoTokenizer.from_pretrained("rufeshe/ethio-ner-model")
📦 Requirements
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🧠 Authors
👤 @rufeshe

