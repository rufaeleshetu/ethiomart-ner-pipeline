# scripts/scrape_telegram.py

from telethon.sync import TelegramClient
import json
import os
import asyncio

# ✅ Your Telegram API credentials
api_id = 24663797
api_hash = '680b7a86c5990f6a63317d4277b12854'
phone = input("Enter your phone number with +251: ")

client = TelegramClient('ethiomart_session', api_id, api_hash)

# ✅ Create data/raw folder if it doesn't exist
if not os.path.exists("data/raw"):
    os.makedirs("data/raw")

# ✅ 7 real verified public Telegram e-commerce channels
channels = [
    'ZemenExpress',
    'nevacomputer',
    'meneshayeofficial',
    'ethio_brand_collection',
    'Leyueqa',
    'MerttEka',
    'AwasMart'
]

async def fetch_channel_messages(channel_username, limit=100):
    output_file = f"data/raw/{channel_username}.json"

    # Skip if already fetched
    if os.path.exists(output_file):
        print(f"⚠️ Skipping @{channel_username} — file already exists.")
        return

    messages_data = []
    async for message in client.iter_messages(channel_username, limit=limit):
        if message.text:
            messages_data.append({
                'channel': channel_username,
                'sender_id': str(message.sender_id),
                'timestamp': str(message.date),
                'message': message.text,
                'has_media': bool(message.media)
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(messages_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(messages_data)} messages from @{channel_username} to {output_file}")

async def run_all():
    await client.start(phone=phone)
    for ch in channels:
        try:
            await fetch_channel_messages(ch)
        except Exception as e:
            print(f"❌ Error fetching @{ch}: {e}")

# 🚀 Run it
with client:
    client.loop.run_until_complete(run_all())