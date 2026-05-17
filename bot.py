import os

import requests

from datetime import date

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

COUNTRY = "DE"

REMIND_DAYS = list(range(0, 365))

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

today = date.today()

year = today.year

url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{COUNTRY}"

holidays = requests.get(url).json()

for holiday in holidays:

    holiday_date = date.fromisoformat(holiday["date"])

    days_left = (holiday_date - today).days

    if days_left in REMIND_DAYS:

        text = (

            f"ACHTUNG: in {days_left} days is Feiertag - "

            f"{holiday['localName']}.\n"

            f"ALLES GESCHLOSSEN"

        )

        requests.post(send_url, json={

            "chat_id": CHAT_ID,

            "text": text

        })