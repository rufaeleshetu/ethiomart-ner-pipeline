# Ethiomart NER Pipeline

This project is part of the KAIM Week 4 challenge from 10 Academy. The goal is to build an Amharic Named Entity Recognition (NER) system that extracts key entities — such as product names, prices, and locations — from messages posted in Ethiopian Telegram-based e-commerce channels.

## 🔍 Project Objective

To transform messy, unstructured Amharic text and images from Telegram posts into structured data to support micro-lending decisions for vendors using EthioMart.

## 📁 Folder Structure

ethiomart-ner-pipeline/
├── data/
│ ├── raw/ # Raw scraped Telegram messages (.json)
│ └── cleaned/ # Preprocessed and tokenized text (.csv)
├── images/ # Product or post images (to be implemented)
├── notebooks/ # Jupyter notebooks for exploration
├── scripts/ # Python scripts for scraping and preprocessing
├── README.md # Project overview and documentation
├── requirements.txt # Python dependencies

markdown
Copy
Edit

## ⚙️ Scripts

- `scripts/scrape_telegram.py`: Scrapes messages from Telegram channels using Telethon.
- `scripts/preprocess_text.py`: Cleans and tokenizes Amharic text messages.

## 📦 Requirements

See [requirements.txt](./requirements.txt)

## 📌 Status

- ✅ Task 1: Data Ingestion and Preprocessing — complete
- 🚧 Task 2: Entity labeling (CoNLL) — in progress
- ⏳ Task 3-6: Model fine-tuning, evaluation, interpretability — upcoming

## 📚 References

- [Telethon Docs](https://docs.telethon.dev/)
- [XLM-Roberta on Hugging Face](https://huggingface.co/FacebookAI/xlm-roberta-base)
