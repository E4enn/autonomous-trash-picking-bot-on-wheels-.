# Hardware and wiring notes

Fill this document only after confirming the exact components.

| Item | Exact model | Voltage/current | Connection notes | Tested? |
|---|---|---|---|---|
| Raspberry Pi | Raspberry Pi 4 Model B 4 GB (planned) | Confirm official supply | Camera + USB/serial | No |
| Camera | To be confirmed | To be confirmed | CSI or USB, depending on model | No |
| Arduino | To be confirmed | To be confirmed | USB serial to Pi | No |
| Motor driver | To be confirmed | Must support motor stall current | Separate motor supply as required | No |
| TT motors | To be confirmed | Check motor specifications | Through motor driver only | No |
| Ultrasonic sensor | To be confirmed | Verify voltage compatibility | Level shifting may be needed for 5 V echo to Pi | No |
| Battery/regulator | To be confirmed | Calculate current budget | Common ground where required by design | No |

Safety: never connect a motor directly to Raspberry Pi or Arduino GPIO. Verify logic voltage levels. Many ultrasonic modules use a 5 V echo signal that can damage a Raspberry Pi GPIO; use a suitable divider or level shifter. Secure the battery, insulate exposed conductors, and add a physical power disconnect.
