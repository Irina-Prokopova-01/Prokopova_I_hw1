import json
from unittest.mock import patch, Mock

import pandas as pd

from src.utils import amount_transaction, get_transactions_json_csv_xlsx_file

@patch('tests.test_utils.pd.read_csv')
def test_get_transactions_json_csv_xlsx_file_csv(path):
    Mock.return_value = pd.DataFrame()
    assert get_transactions_json_csv_xlsx_file('foo') == []


@patch('tests.test_utils.pd.read_excel')
def test_get_transactions_json_csv_xlsx_file_xlsx(path):
    Mock.return_value = pd.DataFrame()
    assert get_transactions_json_csv_xlsx_file('foo') == []


@patch("os.path.exists")
@patch("builtins.open")
def test_get_transactions_json_csv_xlsx_file(mock_open, mock_path_exists):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_path_exists.return_value = True
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_json_csv_xlsx_file("test.json") == [{"test": "test"}]

    mock_file.read.return_value = json.dumps({})
    assert get_transactions_json_csv_xlsx_file("test.json") == []

    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_json_csv_xlsx_file("test.json") == []

    mock_file.read.return_value = ""
    assert get_transactions_json_csv_xlsx_file("test.json") == []

    mock_path_exists.return_value = False
    assert get_transactions_json_csv_xlsx_file("test.json") == []


def test_get_transactions_json_file_uncorrect_path():
    assert get_transactions_json_csv_xlsx_file("fgh") == []


def test_get_transactions_json_file_str():
    assert get_transactions_json_csv_xlsx_file("") == []


@patch("src.utils.convert_to_rubles")
def test_rubles(mock_convert):
    transaction = {
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }

    res = amount_transaction(transaction)

    assert res == 31957.58
    mock_convert.assert_not_called()


@patch("src.utils.convert_to_rubles")
def test_bar(mock_convert):
    mock_convert.return_value = 123.45
    transaction = {
        "operationAmount": {"amount": "31957.58", "currency": {"name": "$", "code": "USD"}},
    }

    res = amount_transaction(transaction)

    assert res == 123.45
    mock_convert.assert_called_once_with("USD", 31957.58)
