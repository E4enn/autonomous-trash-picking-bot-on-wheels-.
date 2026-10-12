"""Validation for the proposed Raspberry Pi -> Arduino command protocol."""

VALID_COMMANDS = {"F", "L", "R", "S", "C"}


def validate_command(command: str) -> str:
    """Return a normalized valid one-character command or raise ValueError."""
    if not isinstance(command, str):
        raise ValueError("Command must be a string")
    normalized = command.strip().upper()
    if normalized not in VALID_COMMANDS:
        raise ValueError(f"Unsupported command: {command!r}")
    return normalized


def encode_command(command: str) -> bytes:
    """Encode one command as an ASCII byte followed by a newline."""
    return (validate_command(command) + "\n").encode("ascii")
