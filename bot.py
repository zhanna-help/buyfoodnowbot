import os

import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN exists:", BOT_TOKEN is not None)

print("BOT_TOKEN starts with:", BOT_TOKEN[:5] if BOT_TOKEN else "None")

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(send_url, json={

    "chat_id": CHAT_ID,

    "text": "Test: bot is working"

})

print("Telegram status:", response.status_code)

print("Telegram response:", response.text)