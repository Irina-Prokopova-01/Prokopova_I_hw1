import pytest
from unittest.mock import Mock
from unittest.mock import patch
from src.external_api import amount_transaction

@pytest.fixture
def data() -> list[dict]:
    return {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
    }
}



@pytest.mark.parametrize("expected", [(31957.58)])
def test_amount_transaction_RUB(data, expected):
    assert amount_transaction(data) == expected


@patch(path)
def test_amount_transaction_path(mock_amount):
    mock_amount.return_value =