"""High-level decision logic, independent of physical hardware."""

from .commands import validate_command


def choose_command(detections, obstacle_distance_cm=None, min_confidence=0.70):
    """Choose a conservative movement command from detections and sensor distance.

    This is a simple placeholder, not a complete navigation algorithm.
    Obstacle stop takes priority. Tune thresholds using measured tests.
    """
    if obstacle_distance_cm is not None and obstacle_distance_cm < 25:
        return "S"

    usable = [
        item for item in detections
        if item.get("confidence", 0.0) >= min_confidence
    ]
    if not usable:
        return "S"

    # Placeholder policy: collection is NOT triggered automatically yet.
    # Replace with camera geometry and a tested approach/collection state machine.
    return validate_command("S")
