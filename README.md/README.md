# 🇪🇹 EthioMart NER Pipeline

This repository contains an end-to-end Named Entity Recognition (NER) pipeline tailored for Amharic e-commerce vendors on Telegram. It automates the entire process — from data scraping and preprocessing, to fine-tuning and deploying an NER model.


## 📌 Project Overview

Telegram-based e-commerce is rapidly growing in Ethiopia. However, business data is scattered and unstructured. This project extracts, cleans, and annotates messages from various Telegram vendors, enabling Named Entity Recognition (NER) for better vendor profiling, customer analytics, and loan eligibility modeling.


## 📂 Folder Structure

.
├── data
│   ├── raw/                   # Unprocessed scraped JSON files
│   └── cleaned/               # Cleaned CSVs used for analysis
├── notebooks
│   ├── task1_data_exploration.ipynb      # Exploratory Data Analysis
│   ├── ner_train_preparation.ipynb       # CoNLL formatting and prep
│   └── final_ner_model/                  # Hugging Face link below
├── scripts
│   ├── scrape_telegram.py    # Telegram scraping bot
│   └── preprocess_text.py    # Normalization, cleaning, tokenizing
├── requirements.txt
└── README.md
🧠 Model
I fine-tuned a xlm-roberta-base model for token classification using a CoNLL-formatted Amharic dataset derived from Telegram messages.

📎 Hugging Face Model
🔗 Access the model here:
👉 rufeshe/ethio-ner-model

📥 Load the Model

from transformers import AutoTokenizer, AutoModelForTokenClassification

model = AutoModelForTokenClassification.from_pretrained("rufeshe/ethio-ner-model")
tokenizer = AutoTokenizer.from_pretrained("rufeshe/ethio-ner-model")