import json
import logging
import os

import pandas as pd

from src.external_api import convert_to_rubles

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def remove_empty_dicts(func):
    """
    Декоратор, который удаляет из списка, возвращаемого декорируемой функцией, все пустые словари.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [item for item in result if item]

    return wrapper


@remove_empty_dicts
def get_transactions_json_csv_xlsx_file(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до файла с расширением JSON, csv или xlsx и
    возвращает список словарей с данными о фин. транзакциях."""
    if not os.path.exists(path):
        logger.warning(f"Проверте корректность указанного пути {path}.")
        return []
    if ".json" in path:
        with open(path, encoding="utf-8") as f:
            try:
                json_file_transactions = json.load(f)
                logger.info(f"Файл {json_file_transactions} прочитан.")
            except json.JSONDecodeError:
                logger.error(f"Данные в файле {json_file_transactions} не соответствуют формату JSON.")
                return []

        if isinstance(json_file_transactions, list):
            logger.info(f"Данные файла {json_file_transactions} это список.")
            return json_file_transactions
        else:
            logger.warning(f"Данные {json_file_transactions} не является списоком.")
            return []
    elif ".csv" in path:
        csv_file_transactions = pd.read_csv("../data/transactions.csv")
        logger.info(f"Файл {csv_file_transactions} прочитан.")
        return csv_file_transactions.to_dict(orient="records")
    elif ".xlsx" in path:
        xlsx_file_transactions = pd.read_excel("../data/transactions_excel.xlsx")
        logger.info(f"Файл {xlsx_file_transactions} прочитан.")
        return xlsx_file_transactions.to_dict(orient="records")


def amount_transaction(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции в рублях.
    """
    logger.info(f"Список транзакций {transaction} успешно передан.")
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency.upper() != "RUB":
        logger.debug(f"Валюту переданной транзакции {currency}, конвертируем в RUB.")
        amount = convert_to_rubles(currency, amount)
        logger.info(f"Конвертация {currency} в RUB прошла успешно.")
    return amount


if __name__ == "__main__":

    transactions = get_transactions_json_csv_xlsx_file("../data/operations.json")
    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный формат.")

    transactions_csv = get_transactions_json_csv_xlsx_file("../data/transactions.csv")
    if transactions_csv:
        print("Список транзакций из CSV-файла:")
        for transaction in transactions_csv:
            print(transactions_csv)
    else:
        print("Ошибка при чтении CSV-файла.")

    transactions_excel = get_transactions_json_csv_xlsx_file("../data/transactions_excel.xlsx")
    if transactions_excel:
        print("\nСписок транзакций из XLSX-файла:")
        for transaction in transactions_excel:
            print(transaction)
    else:
        print("Ошибка при чтении XLSX-файла.")

    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }

    # transaction = {
    #     "id": 41428829,
    #     "state": "EXECUTED",
    #     "date": "2019-07-03T18:35:29.512364",
    #     "operationAmount": {"amount": "8221", "currency": {"name": "USD", "code": "USD"}},
    #     }

    print(amount_transaction(transaction))
