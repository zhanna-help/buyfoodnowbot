import requests

from datetime import date, timedelta

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

COUNTRY = "DE"

REMIND_DAYS = [1, 3, 7]

today = date.today()

year = today.year

url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{COUNTRY}"

holidays = requests.get(url).json()

for holiday in holidays:

    holiday_date = date.fromisoformat(holiday["date"])

    days_left = (holiday_date - today).days

    if days_left in REMIND_DAYS:

        text = (

            f"ACHTUNG: in {days_left} days Feiertag — "

            f"{holiday['localName']}.\n"

            f"ALLES GESCHLOSSEN"

        )

        send_url = f"https://api.telegram.org/bot{8829249920:AAHeSCWXDJXdKgqfVO0zuh5iMtNxKHmpQRo}/sendMessage"

        requests.post(send_url, json={

            "chat_id": CHAT_ID,

            "text": text

        })