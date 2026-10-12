import pytest
from src.robot.commands import validate_command, encode_command


@pytest.mark.parametrize("command", ["F", "L", "R", "S", "C", " f "])
def test_valid_commands(command):
    assert validate_command(command) in {"F", "L", "R", "S", "C"}


@pytest.mark.parametrize("command", ["", "FORWARD", "X", "STOP", None, 12])
def test_invalid_commands(command):
    with pytest.raises(ValueError):
        validate_command(command)


def test_encoding_adds_newline():
    assert encode_command("F") == b"F\n"
