from unittest.mock import ANY, MagicMock, patch

import pytest
from requests.exceptions import HTTPError

from src.external_api import convert_to_rubles


@patch("requests.get")
def test_successfully_convert(mocked_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 212.7234}
    mocked_requests_get.return_value = mock_response

    res = convert_to_rubles("USD", 100)

    assert res == 212.72
    mocked_requests_get.assert_called_once_with(
        ANY, headers={"apikey": ANY}, params={"to": "RUB", "from": "USD", "amount": 100}
    )


@patch("requests.get")
def test_external_api_error(mocked_requests_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = HTTPError("Not authenticated")
    mocked_requests_get.return_value = mock_response

    with pytest.raises(HTTPError):
        convert_to_rubles("USD", 100)
