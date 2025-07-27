from typing import Any
from unittest.mock import patch

from external_api.conversion import conversion_currency


@patch("requests.get")
def test_conversion_currency(mock_currency: Any) -> None:
    mock_respons_amount = 991.49
    mock_currency.return_value.json.return_value = {"result", mock_respons_amount}
    result = conversion_currency(
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781",
        }
    )
    assert result == round(mock_respons_amount, 2)
