# System architecture

## Responsibilities

- **Camera:** captures the scene.
- **Raspberry Pi / Python:** image processing, model inference, decision state machine, command transmission, logging.
- **Arduino:** validates commands, reads local sensors, controls motor-driver outputs, enforces timeout and emergency stop.
- **Motor driver:** supplies motor current; GPIO pins must not drive motors directly.
- **Ultrasonic sensor:** provides a local obstacle-distance estimate.
- **Collection mechanism:** powered only when safe and when the collection state machine permits it.

## Proposed command sequence

1. Pi captures a frame.
2. Vision module returns zero or more labelled detections with confidence and bounding box.
3. Controller checks obstacle status and robot state.
4. Pi sends a validated single-character command with newline.
5. Arduino validates the command and applies safety rules.
6. Arduino reports status; Pi logs timestamp, command, sensor reading and outcome.

## Decisions still required

- Exact Arduino board and motor driver.
- Camera model and mounting position.
- Litter classes and training/evaluation dataset.
- Model architecture and runtime supported by the Pi.
- Motor direction mapping and calibrated turning behaviour.
- Collection mechanism design and safety interlock.
