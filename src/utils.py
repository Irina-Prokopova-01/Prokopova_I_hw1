import json
import os.path


def get_transactions_json_file(path: str) -> list[dict]:
    """Функция которая принимает на вход путь до JSON-файла, возврящает список словарей с данными о фин. транзакциях"""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                json_file_transactions = json.load(f)
                if isinstance(json_file_transactions, list):
                    return json_file_transactions
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
