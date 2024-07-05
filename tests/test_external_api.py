import pytest
from unittest.mock import Mock
from unittest.mock import patch
from src.external_api import amount_transaction


@pytest.mark.parametrize(
    "state, expected", ["RUB", "31957.58"])
data = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }}]
def test_amount_transaction_RUB(data, state, expected):
    assert amount_transaction(data, state) == expected

@patch(float(amount))
def test_amount_transaction(mock_amount):
    mock_amount.return_value =