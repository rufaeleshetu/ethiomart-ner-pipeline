import pandas as pd
import os
import re

def normalize_amharic(text):
    # Basic Amharic normalization
    replacements = {
        "ኣ": "አ", "ሃ": "ሀ", "ሐ": "ሀ", "ኅ": "ሀ", "እ": "", "ሕ": "ሀ"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def clean_text(text):
    text = re.sub(r'[^\w\s፡።፣]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return normalize_amharic(text)

def tokenize(text):
    return text.split()

def preprocess_file(input_file, output_file):
    df = pd.read_json(input_file)
    rows = []
    for msg in df["message"].dropna():
        if len(msg) < 10: continue  # Filter short messages
        cleaned = clean_text(msg)
        tokens = tokenize(cleaned)
        rows.append({
            "cleaned_text": cleaned,
            "tokens": " ".join(tokens)
        })
    os.makedirs("data/cleaned", exist_ok=True)
    pd.DataFrame(rows).to_csv(output_file, index=False, encoding='utf-8-sig')

# Run for each channel
channels = [
    'ZemenExpress',
    'nevacomputer',
    'meneshayeofficial',
    'ethio_brand_collection',
    'Leyueqa',
    'MerttEka',
    'AwasMart'
]

for ch in channels:
    input_file = f"data/raw/{ch}.json"
    output_file = f"data/cleaned/{ch}_cleaned.csv"
    if os.path.exists(input_file):
        preprocess_file(input_file, output_file)