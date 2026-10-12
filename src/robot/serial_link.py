"""Serial link wrapper. Keep hardware communication separate from AI logic."""

from .commands import encode_command


class RobotSerialLink:
    def __init__(self, port: str, baudrate: int = 9600, timeout: float = 1.0):
        try:
            import serial
        except ImportError as exc:
            raise RuntimeError("Install dependencies with: pip install -r requirements.txt") from exc
        self._serial_module = serial
        self.connection = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    def send(self, command: str) -> None:
        self.connection.write(encode_command(command))

    def close(self) -> None:
        if self.connection and self.connection.is_open:
            self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
