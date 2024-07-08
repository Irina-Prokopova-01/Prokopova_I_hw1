import json
from unittest.mock import patch

from src.utils import get_transactions_json_file


@patch("os.path.exists")
@patch("builtins.open")
def test_get_transactions_json_file(mock_open, mock_path_exists):
    mock_file = mock_open.return_value.__enter__.return_value

    mock_path_exists.return_value = True
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_json_file("test.json") == [{"test": "test"}]

    mock_file.read.return_value = json.dumps({})
    assert get_transactions_json_file("test.json") == []

    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_json_file("test.json") == []

    mock_file.read.return_value = ""
    assert get_transactions_json_file("test.json") == []

    mock_path_exists.return_value = False
    assert get_transactions_json_file("test.json") == []


def test_get_transactions_json_file_uncorrect_path():
    assert get_transactions_json_file("fgh") == []


def test_get_transactions_json_file_str():
    assert get_transactions_json_file("") == []
