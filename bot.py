send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(send_url, json={

    "chat_id": CHAT_ID,

    "text": "Test: bot is working"

})

print("Telegram status:", response.status_code)

print("Telegram response:", response.text)

response.raise_for_status()