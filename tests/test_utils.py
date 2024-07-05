import pytest
from unittest.mock import Mock
from src.utils import get_transactions_json_file

def test_get_transactions_json_file_path():
    assert get_transactions_json_file('../data/operations.json') ==
    assert get_transactions_json_file()

def test_get_transactions_json_file_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        get_transactions_json_file([])