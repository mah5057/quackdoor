import pytest
from unittest.mock import mock_open, patch
from quackdoor.payload import read_payload


def test_read_payload_success():
    mock_data = "  test_data  \n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_payload("fake_file.txt")
        assert result == "test_data"


def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("Original error")):
        with pytest.raises(FileNotFoundError) as excinfo:
            read_payload("no_such_file.txt")

    assert "File not found" in str(excinfo.value)
    assert isinstance(excinfo.value.__cause__, FileNotFoundError)


def test_permission_error():
    with patch("builtins.open", side_effect=PermissionError("Original error")):
        with pytest.raises(PermissionError) as excinfo:
            read_payload("unauthorized.txt")

    assert "Permission denied" in str(excinfo.value)
    assert isinstance(excinfo.value.__cause__, PermissionError)


def test_unicode_decode_error():
    # Simulate reading non-UTF-8 content triggering UnicodeDecodeError
    def mock_open_with_unicode_error(*args, **kwargs):
        raise UnicodeDecodeError("utf-8", b"", 0, 1, "Original decode error")

    with patch("builtins.open", mock_open_with_unicode_error):
        with pytest.raises(UnicodeDecodeError) as excinfo:
            read_payload("non_utf8.txt")

    assert "File is not UTF-8 encoded" in str(excinfo.value)
    assert isinstance(excinfo.value.__cause__, UnicodeDecodeError)


def test_os_error():
    with patch("builtins.open", side_effect=OSError("General I/O error")):
        with pytest.raises(OSError) as excinfo:
            read_payload("some_file.txt")

    assert "Failed to read file" in str(excinfo.value)
    assert isinstance(excinfo.value.__cause__, OSError)
