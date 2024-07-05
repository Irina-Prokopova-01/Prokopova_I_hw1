import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')


def amount_transaction(transaction: dict) -> float | None:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["amount"]["currency"]["code"]
    if currency == "RUB":
        return (float(amount))
    if currency != "RUB":
        API_KEY = os.getenv("API_KEY")
        url = f'https://api.apilayer.com/exchangerates_data/convert'
        response = requests.get(url, headers={'apikey': API_KEY}, params={'from': currency, 'to': 'RUB', 'amount': amount})
        if response.status_code == 200:
            data = response.json()
            if 'result' in data:
                amount = data['result']
                return float(amount)
            else:
                raise ValueError(f'Exchange rate for {currency} not found in API response')

    return float(amount)

transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
}

print(amount_transaction(transaction))

