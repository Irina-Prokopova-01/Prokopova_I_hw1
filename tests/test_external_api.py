import json
from unittest.mock import patch

from src.external_api import amount_transaction

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221", "currency": {"name": "USD", "code": "USD"}},
}


@patch("requests.get")
def test_amount_transaction_status_code(mock_get):
    mock_get.return_value.status_code = 200


@patch("requests.get")
def test_amount_transaction_test_json(mock_get):
    mock_get.assert_called_once()


@patch("requests.get")
def test_amount_transaction_convertation(mock_get):
    mock_get.assert_called_with(url, headers=headers, params=params)


@patch("requests.get")
def test_amount_transaction_convertation(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221},
        "info": {"timestamp": 1720422065, "rate": 88.644718},
        "date": "2024-07-08",
        "result": 728748.226678,
    }
    assert amount_transaction(transaction) == 822100.0
    # mock_get.assert_called_once()
    # mock_get.assert_called_with(url, headers=headers, params=params)


# import json
# from unittest.mock import patch
#
# from src.utils import get_transactions_json_file
#
#
# @patch("os.path.exists")
# @patch("builtins.open")
# def test_get_transactions_json_file(mock_open, mock_path_exists):
#     mock_file = mock_open.return_value.__enter__.return_value
#
#     # Проверка на удачный результат.
#     mock_path_exists.return_value = True
#     mock_file.read.return_value = json.dumps([{"test": "test"}])
#     assert get_transactions_json_file("test.json") == [{"test": "test"}]
#
#     # Проверка на ошибку типа файла.
#     mock_file.read.return_value = json.dumps({})
#     assert get_transactions_json_file("test.json") == []
#
#     # Проверка на некорректный файл.
#     mock_file.read.return_value = json.dumps("testtest")
#     assert get_transactions_json_file("test.json") == []
#
#     # Проверка на пустой файл.
#     mock_file.read.return_value = ""
#     assert get_transactions_json_file("test.json") == []
#
#     # Проверка на путь, который не существует.
#     mock_path_exists.return_value = False
#     assert get_transactions_json_file("test.json") == []
