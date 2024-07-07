import json
import os.path


def get_transactions_json_file(path: str) -> list[dict]:
    """Функция которая принимает на вход путь до JSON-файла, возврящает список словарей с данными о фин. транзакциях"""
    if not os.path.exists(path):
        # print("Путь до файла не найден")
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                json_file_transactions = json.load(f)
                if isinstance(json_file_transactions, list):
                    return json_file_transactions
                else:
                    # print("Ошибка: Файл не содержит список транзакций")
                    return []
            except json.JSONDecodeError:
                # print("Ошибка декодирования JSON")
                return []
    except FileNotFoundError:
        # print("Файл не найден")
        return []
