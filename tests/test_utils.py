import json
from unittest.mock import patch

from src.utils import get_transactions_json_file

@patch("os.path.exists")
@patch("builtins.open")
def test_get_transactions_json_file(mock_open, mock_path_exists):
    mock_file = mock_open.return_value.__enter__.return_value

    # Проверка на удачный результат.
    mock_path_exists.return_value = True
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_json_file("test.json") == [{"test": "test"}]

    # Проверка на ошибку типа файла.
    mock_file.read.return_value = json.dumps({})
    assert get_transactions_json_file("test.json") == []

    # Проверка на некорректный файл.
    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_json_file("test.json") == []

    # Проверка на пустой файл.
    mock_file.read.return_value = ""
    assert get_transactions_json_file("test.json") == []

    # Проверка на путь, который не существует.
    mock_path_exists.return_value = False
    assert get_transactions_json_file("test.json") == []
