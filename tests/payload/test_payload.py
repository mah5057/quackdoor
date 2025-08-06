from unittest.mock import mock_open, patch
from quackdoor.payload import read_payload


def test_read_payload():
    mock_data = "test_data"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_payload("test.txt")
        assert result == "test_data"
