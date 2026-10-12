/*
 * Arduino-side command receiver skeleton.
 * IMPORTANT: This example only validates commands and reports them.
 * It does NOT drive motors. Add motor-driver pins only after verifying your
 * exact driver, wiring, power supply, and emergency-stop design.
 */
const unsigned long COMMAND_TIMEOUT_MS = 1000;
unsigned long lastCommandMs = 0;
char lastCommand = 'S';

bool isValidCommand(char command) {
  return command == 'F' || command == 'L' || command == 'R' ||
         command == 'S' || command == 'C';
}

void stopRobot() {
  // TODO: Set all motor-driver outputs to the safe stop state.
  // Keep the robot stopped until motor-control wiring has been tested.
  lastCommand = 'S';
}

void setup() {
  Serial.begin(9600);
  lastCommandMs = millis();
  stopRobot();
  Serial.println("Robot controller ready; motors are not implemented.");
}

void loop() {
  while (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '\r' || command == '\n' || command == ' ') {
      continue;
    }

    if (!isValidCommand(command)) {
      stopRobot();
      Serial.println("ERR: invalid command");
      continue;
    }

    lastCommandMs = millis();
    lastCommand = command;

    if (command == 'S') {
      stopRobot();
      Serial.println("OK: stop");
    } else if (command == 'C') {
      // Collection is intentionally disabled in this starter.
      stopRobot();
      Serial.println("INFO: collection disabled");
    } else {
      // Movement commands are intentionally disabled until motor pins
      // and a verified motor driver are configured.
      stopRobot();
      Serial.println("INFO: movement disabled; configure hardware first");
    }
  }

  if (millis() - lastCommandMs > COMMAND_TIMEOUT_MS) {
    stopRobot();
  }
}
