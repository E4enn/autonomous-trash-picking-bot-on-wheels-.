"""Central configuration. Confirm hardware-specific values before use."""

SERIAL_BAUD_RATE = 9600
SERIAL_TIMEOUT_SECONDS = 1.0

# Example only: set the real serial device after checking your system.
# Windows examples: "COM3"; Linux examples: "/dev/ttyACM0".
SERIAL_PORT = None

# Do not enable the collection mechanism until its hardware is tested safely.
COLLECTION_ENABLED = False
