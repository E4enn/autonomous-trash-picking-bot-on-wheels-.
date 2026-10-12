# Safety checklist

- Test code without motors before hardware integration.
- Lift wheels off the ground for initial motor tests.
- Use a correctly rated motor driver; GPIO pins cannot supply motor current.
- Verify power rails, polarity, current rating and common-ground requirements.
- Check Raspberry Pi GPIO voltage limits before connecting sensors.
- Use a physical power disconnect / emergency stop.
- Make stop-on-timeout the default if serial communication fails.
- Stop movement when sensor readings are invalid or an obstacle is too close.
- Keep hands, hair, clothing and loose objects away from rotating intake parts.
- Test with clean, dry, non-hazardous litter only; do not collect sharp, medical, chemical or unknown waste.
- Supervise tests and avoid roads, stairs, people and animals.
