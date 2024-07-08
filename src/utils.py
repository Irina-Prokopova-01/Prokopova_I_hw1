import json
import os

from src.external_api import convert_to_rubles


def get_transactions_json_file(path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла,
    возвращает список словарей с данными о фин. транзакциях.
    """
    if not os.path.exists(path):
        return []

    with open(path, encoding="utf-8") as f:
        try:
            json_file_transactions = json.load(f)
        except json.JSONDecodeError:
            return []

    if isinstance(json_file_transactions, list):
        return json_file_transactions
    else:
        return []


def amount_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency.upper() != "RUB":
        amount = convert_to_rubles(currency, amount)
    return amount


