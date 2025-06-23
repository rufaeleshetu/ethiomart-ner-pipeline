import asyncio
import json
import os
import time
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, ChannelPrivateError

# Credentials
api_id = 24663797
api_hash = '680b7a86c5990f6a63317d4277b12854'
phone = input("Enter your phone number (+251...): ")

client = TelegramClient('ethiomart_session', api_id, api_hash)

channels = [
    'ZemenExpress',
    'nevacomputer',
    'meneshayeofficial',
    'ethio_brand_collection',
    'Leyueqa',
    'MerttEka',
    'AwasMart'
]

os.makedirs("data/raw", exist_ok=True)

async def fetch_channel_messages(channel, limit=100, retries=3):
    file_path = f"data/raw/{channel}.json"
    if os.path.exists(file_path):
        print(f"✅ Skipped {channel} — already fetched.")
        return

    for attempt in range(retries):
        try:
            messages = []
            async for msg in client.iter_messages(channel, limit=limit):
                if msg.text:
                    messages.append({
                        "channel": channel,
                        "sender_id": str(msg.sender_id),
                        "timestamp": str(msg.date),
                        "message": msg.text,
                        "has_media": bool(msg.media)
                    })
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(messages, f, ensure_ascii=False, indent=2)
            print(f"✅ Saved {len(messages)} messages from @{channel}")
            return

        except FloodWaitError as e:
            print(f"⏳ Rate limited. Sleeping for {e.seconds} seconds...")
            time.sleep(e.seconds)

        except ChannelPrivateError:
            print(f"🚫 Cannot access @{channel} — channel is private or blocked.")
            return

        except Exception as e:
            print(f"❌ Error on @{channel}: {e}. Retrying ({attempt + 1}/{retries})...")
            time.sleep(3)

    print(f"❗ Failed to fetch @{channel} after {retries} attempts.")

async def run_all():
    await client.start(phone=phone)
    for ch in channels:
        await fetch_channel_messages(ch)

with client:
    client.loop.run_until_complete(run_all())