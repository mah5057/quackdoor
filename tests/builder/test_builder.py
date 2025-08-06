from quackdoor.builder import build_ducky_script
import base64


def test_build_ducky_script():
    exec_command = "Test exec command"
    ducky_script = build_ducky_script(exec_command)
    assert exec_command in ducky_script
