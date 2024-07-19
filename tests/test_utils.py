import json
from unittest.mock import Mock, mock_open, patch

import pandas as pd
import pytest

from src.utils import amount_transaction, get_transactions_json_csv_xlsx_file


@patch("tests.test_utils.pd.read_csv")
def test_get_transactions_json_csv_xlsx_file_csv(path):
    path.return_value = pd.DataFrame()
    assert get_transactions_json_csv_xlsx_file("foo") == []


@patch("tests.test_utils.pd.read_excel")
def test_get_transactions_json_csv_xlsx_file_xlsx(path):
    path.return_value = pd.DataFrame()
    assert get_transactions_json_csv_xlsx_file("foo") == []


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


@pytest.fixture()
def mocked_path_exists():
    with patch("os.path.exists", return_value=True) as mocked_path_exists:
        yield mocked_path_exists


@pytest.mark.usefixtures("mocked_path_exists")
class TestGetTransactionsJsonFile:

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"name": "John", "age": 12}]))
    def test_returns_values_if_file_contains_list_of_dict(self, mock_file):
        expected = [{"name": "John", "age": 12}]
        assert get_transactions_json_csv_xlsx_file("test.json") == expected

    def test_returns_empty_list_if_file_not_exists_(self, mocked_path_exists):
        mocked_path_exists.return_value = False
        assert get_transactions_json_csv_xlsx_file("test.json") == []

    # @patch("builtins.open", new_callable=mock_open, read_data="")
    # def test_returns_empty_list_if_file_is_empty(self, mock_file):
    #     assert get_transactions_json_csv_xlsx_file("test.json") == []
    #
    # @patch("builtins.open", new_callable=mock_open, read_data="not_json")
    # def test_returns_empty_list_if_file_has_not_json_data(self, mock_file):
    #     assert get_transactions_json_csv_xlsx_file("test.json") == []

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"name": "John", "age": 12}))
    def test_returns_empty_list_if_file_contains_not_list(self, mock_file):
        assert get_transactions_json_csv_xlsx_file("test.json") == []


# @patch("src.utils.pd.read_csv")
# def test_get_transactions_json_csv_xlsx_file_csv(mock_read_csv):
#     mock_read_csv.return_value = pd.DataFrame()
#     assert get_transactions_json_csv_xlsx_file("foo") == []
#
#
# @patch("src.utils.pd.read_excel")
# def test_get_transactions_json_csv_xlsx_file_xlsx(mock_read_excel):
#     mock_read_excel.return_value = pd.DataFrame()
#     assert get_transactions_json_csv_xlsx_file("foo") == []
