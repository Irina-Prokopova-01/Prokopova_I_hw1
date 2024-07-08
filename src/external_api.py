import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(currency: str, amount: float) -> float:
    """Обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": os.getenv("API_KEY")}
    params = {"to": "RUB", "from": currency, "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    return round(data["result"], 2)


