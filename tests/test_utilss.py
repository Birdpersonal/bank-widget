from typing import Any
from unittest.mock import patch

from utils.utilss import road_to_json


@patch("builtins.open", create=True)
def test_open_file_get_transactions(mock_open: Any) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = []
    assert road_to_json("test.txt") == []
