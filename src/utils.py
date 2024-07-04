import json
import os.path

import requests

def get_transactions_json_file(path: str = []) -> list:
      """Функция которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
      if not os.path.exists(path):
          print('Путь до файла не найдет')
          return []
      try:
          with open(path, 'r', encoding='utf-8') as f:
              try:
                  json_file_transactions = json.load(f)
              except json.JSONDecodeError:
                  print('Ошибка декодирования')
                  return []
              if isinstance(json_file_transactions, list):
                  return json_file_transactions
              else:
                  print('Обьект не принадлежит к классу list')
                  return []
      except FileNotFoundError:
          print('Файл не найден')
          return []

# if __name__ == '__main':
path = '../data/operations.json'
a = get_transactions_json_file(path)
print(a)
