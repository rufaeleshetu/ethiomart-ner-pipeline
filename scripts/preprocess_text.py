# scripts/preprocess_text.py

import json
import os
import re
import pandas as pd

def clean_text(text):
    # Remove unwanted symbols and extra spaces
    text = re.sub(r'[^\w\s፡።፣]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    return text.split()

def preprocess_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)

    processed = []
    for msg in messages:
        cleaned = clean_text(msg['message'])
        tokens = tokenize(cleaned)
        processed.append({
            "channel": msg['channel'],
            "timestamp": msg['timestamp'],
            "cleaned_text": cleaned,
            "tokens": " ".join(tokens)
        })

    df = pd.DataFrame(processed)
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"✅ Saved cleaned data to {output_file}")

# ✅ Channels you scraped from
channels = [
    'ZemenExpress',
    'nevacomputer',
    'meneshayeofficial',
    'ethio_brand_collection',
    'Leyueqa',
    'MerttEka',
    'AwasMart'
]

# ✅ Preprocess each raw file into cleaned CSV
for ch in channels:
    input_path = f"data/raw/{ch}.json"
    output_path = f"data/cleaned/{ch}_cleaned.csv"
    if os.path.exists(input_path):
        preprocess_file(input_path, output_path)
    else:
        print(f"⚠️ Skipped {ch} — raw data file missing.")