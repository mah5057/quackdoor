from quackdoor.encoder import encode_payload, build_python_exec_command
import base64


def test_build_python_exec_command():
    original = "print('hi')"
    encoded = encode_payload(original)
    decoded = base64.b64decode(encoded).decode()
    assert decoded == original
    assert "exec(" in build_python_exec_command(encoded)
