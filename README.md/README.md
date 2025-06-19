# Ethiomart NER Pipeline

## 📌 Project: Ethiomart Amharic NER Pipeline

This repo implements a data ingestion and NER annotation pipeline for Amharic-language Telegram e-commerce messages.

### ✅ Features

- Multi-channel Telegram scraper using Telethon
- Cleaned and normalized Amharic message texts
- CoNLL-formatted manual labeling for NER
- Ready for model fine-tuning

### 🛠️ Setup Instructions

1. Clone the repo and install dependencies:

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
