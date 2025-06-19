# 📦 Ethiomart Amharic NER Pipeline

This project implements a full data ingestion and preprocessing pipeline for extracting messages from Ethiopian e-commerce Telegram channels and preparing them for Named Entity Recognition (NER) using CoNLL format. It supports Amharic-language data and prepares it for downstream model fine-tuning.

---

## 🧠 Project Objective

To build a dataset for Named Entity Recognition (NER) that identifies `Product`, `Price`, and `Location` entities from Amharic messages posted on Telegram e-commerce channels.

---

## 🛠️ Features

- ✅ Ingests messages from 7 real Telegram e-commerce channels
- ✅ Extracts metadata: timestamp, sender, text, media flag
- ✅ Cleans and normalizes Amharic text
- ✅ Tokenizes and structures data into clean CSVs
- ✅ Generates a CoNLL-formatted file (`B-PRICE`, `B-LOC`, `B-PRODUCT`) for manual or automated NER labeling
- ✅ Modular and reproducible pipeline

---

## 📂 Folder Structure

```bash
.
├── data/
│   ├── raw/                 # Raw messages (JSON)
│   └── cleaned/             # Preprocessed CSVs
├── notebooks/
│   ├── task1_data_exploration.ipynb
│   └── ethiomart_task2_labeled.conll
├── scripts/
│   ├── scrape_telegram.py   # Telegram data ingestion
│   └── preprocess_text.py   # Amharic message cleaning
├── requirements.txt
└── README.md
🚀 How to Run
1. 🧱 Setup Environment
bash
Copy
Edit
pip install -r requirements.txt
2. 🔑 Set Up Telegram Access
Go to https://my.telegram.org

Create an app to get api_id and api_hash

Replace placeholders in scrape_telegram.py with your credentials

3. 📥 Run Data Ingestion
bash
Copy
Edit
python scripts/scrape_telegram.py
This will save raw .json message files in data/raw/.

4. 🧹 Run Preprocessing
bash
Copy
Edit
python scripts/preprocess_text.py
This will generate cleaned .csv files with tokenized Amharic messages in data/cleaned/.

5. 🏷️ NER Labeling (Task 2)
Open notebooks/ethiomart_task2_labeled.conll

Follow CoNLL format to label ~30–50 messages

🏷️ Entity Labels Used
Entity	Format	Example
Product	B-Product / I-Product	"የሕፃናት ጫማ"
Price	B-PRICE / I-PRICE	"በ 1500 ብር"
Location	B-LOC / I-LOC	"አዲስ አበባ"
Other	O	Non-entity words

✅ Contributors
Rufael Eshetu

