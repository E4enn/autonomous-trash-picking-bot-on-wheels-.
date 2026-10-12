# Autonomous Trash-Picking Robot with AI

> **Project status:** Early-stage starter repository. Replace this status with your actual progress. Do not describe hardware or AI features as completed until you have built and tested them.

An educational robotics project exploring how a small mobile robot could detect selected litter, navigate toward it, and collect it. The proposed system uses a Raspberry Pi for vision and high-level decisions, an Arduino for low-level motor control, and sensors for obstacle awareness.

## Problem

Litter in school and community environments can be difficult to collect consistently. This project investigates whether a low-cost robot can assist with identifying and collecting selected types of litter in a controlled environment.

## Goals

- Detect a defined set of litter categories using a camera.
- Send safe, simple movement commands from Raspberry Pi to Arduino.
- Avoid nearby obstacles using an ultrasonic sensor.
- Operate a collection mechanism only when appropriate.
- Record test results, limitations, and improvements.

## Proposed hardware

| Component | Role | Status |
|---|---|---|
| Raspberry Pi 4 Model B (4 GB) | Runs Python vision and decision logic | Planned / verify |
| Camera compatible with the Pi | Captures images for detection | Planned / verify |
| Arduino-compatible board | Reads commands and controls motors | Planned / verify |
| Four TT geared motors + motor driver | Drives the robot | Planned / verify |
| Ultrasonic distance sensor | Detects nearby obstacles | Planned / verify |
| Collection mechanism / rotating intake | Moves selected litter into a container | Planned / verify |
| Battery and regulated power | Supplies appropriate power to electronics and motors | Planned / verify |
| Chassis, wheels, wiring, emergency stop | Mechanical platform and safety | Planned / verify |

Update the Status column honestly as components are acquired and tested.

## System architecture

```text
Camera
  |
  v
Raspberry Pi: image capture -> litter detection -> decision logic
  |                                  ^
  | serial command                   | optional status / sensor data
  v                                  |
Arduino: command validation -> obstacle check -> motor driver
  |                                  |
  v                                  v
Drive motors + collection motor   Ultrasonic sensor
```

**Safety principle:** the Arduino should stop the motors if commands become invalid or communication is lost. Test motor control with the wheels lifted before running on the floor. Use a suitable motor driver and separate regulated motor power; never power motors directly from GPIO pins.

## Software stack (planned)

- Python 3
- OpenCV for camera/image processing
- A model runtime selected to match the trained model and Raspberry Pi hardware
- pySerial for Raspberry Pi ↔ Arduino communication
- Arduino C/C++ firmware
- pytest for software tests

Do not claim a model, accelerator, or performance result until you have tested it on your actual hardware.

## Repository map

```text
autonomous-trash-picking-robot/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── docs/
│   ├── architecture.md
│   ├── hardware.md
│   ├── testing.md
│   ├── safety.md
│   └── development-log.md
├── src/
│   └── robot/
│       ├── __init__.py
│       ├── config.py
│       ├── commands.py
│       ├── serial_link.py
│       ├── vision.py
│       └── controller.py
├── arduino/
│   └── robot_controller/
│       └── robot_controller.ino
├── tests/
│   ├── test_commands.py
│   └── test_controller.py
├── assets/
│   ├── diagrams/
│   └── photos/
└── models/
    └── README.md
```

## Getting started

1. Create and activate a Python virtual environment.
2. Install the packages listed in `requirements.txt`.
3. Run unit tests with `python -m pytest`.
4. Develop and test command logic before connecting motors.
5. Add your actual wiring diagram, original photos, model details, and test evidence as the project progresses.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Raspberry Pi OS / Linux:
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

## Command protocol (initial proposal)

The Pi sends one newline-terminated command at a time:

- `F` — move forward
- `L` — turn left
- `R` — turn right
- `S` — stop
- `C` — collection mechanism request

This is only a proposed protocol. The Arduino must validate commands, apply a timeout, and make obstacle avoidance / emergency stop take priority over movement. Collection commands should be disabled until the mechanism is mechanically safe.

## Testing plan

- Unit-test command validation without hardware.
- Test serial connection with motors disconnected.
- Test motor direction with the chassis raised.
- Test obstacle-stop behaviour using safe, controlled distances.
- Measure detection precision/recall on a documented test set.
- Run repeated collection trials with known objects in a controlled area.
- Record failures as well as successes.

See [`docs/testing.md`](docs/testing.md).

## Current limitations

- This starter does not include a trained litter-detection model.
- Pin assignments and motor-driver wiring are not specified until the exact components are confirmed.
- No robot performance, detection accuracy, or collection success rate is claimed.
- Outdoor operation, weather resistance, and real-world safety have not been validated.

## Roadmap

- [ ] Confirm components and power design
- [ ] Draw wiring and system diagrams
- [ ] Implement and unit-test command protocol
- [ ] Test Arduino motor control with wheels raised
- [ ] Add camera capture
- [ ] Choose or train a litter-detection model
- [ ] Integrate obstacle avoidance
- [ ] Test collection mechanism
- [ ] Publish measured results and demo video

## Author

**Your Name** — Zimbabwean A-Level student studying Mathematics, Physics and Computer Science.

Add your GitHub profile link and a short note about your personal contribution. Only include work you personally completed.

## License

See [`LICENSE`](LICENSE). Review the license before reusing third-party models, datasets, or code.
