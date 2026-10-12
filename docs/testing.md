# Testing plan

Record each run with a date, hardware revision, software commit, environment, procedure, expected result, actual result and notes.

| Test ID | Test | Metric | Result |
|---|---|---|---|
| SW-01 | Command validation unit tests | Pass/fail | Not run |
| HW-01 | Serial communication with motors disconnected | Valid messages received | Not run |
| HW-02 | Motor direction with wheels raised | Correct direction / stop | Not run |
| SEN-01 | Obstacle stop at controlled distances | Stop response and repeatability | Not run |
| AI-01 | Detection on labelled test images | Precision, recall, confusion matrix | Not run |
| SYS-01 | End-to-end collection trial | Successes / attempts, failures | Not run |

Do not invent results. Include failed trials and describe what changed afterward.

For classification/detection, keep training and test images separate. Avoid testing only on images used during training.
