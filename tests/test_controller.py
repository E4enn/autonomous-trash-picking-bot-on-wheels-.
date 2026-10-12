from src.robot.controller import choose_command


def test_close_obstacle_stops_robot():
    assert choose_command([], obstacle_distance_cm=10) == "S"


def test_no_detection_stops_robot():
    assert choose_command([]) == "S"


def test_low_confidence_detection_does_not_move():
    detections = [{"label": "bottle", "confidence": 0.2, "bbox": [0, 0, 10, 10]}]
    assert choose_command(detections) == "S"
