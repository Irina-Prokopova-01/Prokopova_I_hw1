import os

import requests


def amount_transaction(transaction: dict) -> float | None:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    if currency != "RUB":
        API_KEY = "nVPFAFLowSNmYQlCt04CS365AOFrjLWT"
        url = f"https://api.apilayer.com/exchangerates_data/convert"
        headers = {"apikey": API_KEY}
        params = {"to": "RUB", "from": currency, "amount": amount}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            if "result" in data:
                amount = data["result"]
                return amount
    # print(response)
    # raise ValueError(f"Exchange rate for {currency} not found in API response")


# transaction = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
# }

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221", "currency": {"name": "USD", "code": "USD"}},
}

print(amount_transaction(transaction))


# import os
#
# import requests
# from dotenv import load_dotenv
#
# load_dotenv(".env")
#
#
# def amount_transaction(transaction: dict) -> float | None:
#     """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float"""
#     amount = float(transaction["operationAmount"]["amount"])
#     currency = transaction["operationAmount"]["currency"]["code"]
#     if currency == "RUB":
#         return amount
#     if currency != "RUB":
#         API_KEY = os.getenv("API_KEY")
#         url = f"https://api.apilayer.com/exchangerates_data/convert"
#         response = requests.get(
#             url, headers={"apikey": API_KEY}, params={"from": currency, "to": "RUB", "amount": amount}
#         )
#         if response.status_code == 200:
#             data = response.json()
#             if "result" in data:
#                 amount = data["result"]
#                 return amount
#     print(response.status_code)
#     raise ValueError(f"Exchange rate for {currency} not found in API response")
#
#
# # transaction = {
# #     "id": 441945886,
# #     "state": "EXECUTED",
# #     "date": "2019-08-26T10:50:58.294041",
# #     "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
# # }
#
# transaction = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {"amount": "8221", "currency": {"name": "USD", "code": "USD"}},
# }
#
# print(amount_transaction(transaction))
