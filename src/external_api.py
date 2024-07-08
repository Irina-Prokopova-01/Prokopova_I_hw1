import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(currency: str, amount: float) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": os.getenv("API_KEY")}
    params = {"to": "RUB", "from": currency, "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    return round(data["result"], 2)


if __name__ == "__main__":

    # transaction = {
    #     "id": 41428829,
    #     "state": "EXECUTED",
    #     "date": "2019-07-03T18:35:29.512364",
    #     "operationAmount": {"amount": "8221", "currency": {"name": "USD", "code": "USD"}},
    # }
    #
    # print(convert_to_rubles("USD", "8221"))
