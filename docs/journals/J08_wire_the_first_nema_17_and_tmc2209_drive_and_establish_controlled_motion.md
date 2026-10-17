# J08 Getting commanded motion out of the feeder

*Milestone 2 | Retrospective build notes*

I put together the first drive setup with the NEMA 17, TMC2209, and a breadboard, using the Pi 4 as the initial control connection. This was where the printed mechanism started becoming something I could command instead of only inspect or move by hand.

I needed to keep the task small enough to debug. Direction, STEP pulses, and enable first. A spinning auger would be progress, but it wouldn't tell me how many grams had reached the cup. That was a separate job for the scale.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

The saved test files make one source of confusion obvious: the pin assignments changed. The small AccelStepper test uses STEP 3 and DIR 2, while the July controller uses STEP 2 and DIR 3. Both are real versions. Mixing them would give me a wiring problem that had nothing to do with powder.

The exact original Pi GPIO map and TMC2209 current setting aren't in the record I'm reconstructing from. I've kept the concrete later pin maps below rather than filling that gap with whichever version happens to be easiest to find.

## Pin maps to keep straight

STEP, DIR, and EN control different aspects of the drive. STEP requests incremental motion, DIR selects its direction, and EN activates or disables the driver according to its polarity. The motor winding connections and shared signal reference are separate from those logic functions. A breadboard layout records packaging, while the corresponding pin assignments identify a particular controller revision.

The later July Arduino source makes the eventual command interface concrete: auger STEP is pin 2, DIR is pin 3, and ENABLE is pin 4. In that file, LOW enables the driver and HIGH disables it, while HIGH is the dispensing direction. That's the archived Arduino configuration. It isn't the original Pi GPIO map. The timer-based firmware later uses different pins and the opposite enable level, so those diagrams must be kept version-specific.

The standalone repository test uses AccelStepper::DRIVER with stepPin 3 and directionPin 2, sets a 1000-step/s maximum, and calls runSpeed() at 600 steps/s. That is a motor-only test with a different pin order from the July controller. It doesn't contain the mass-feedback loop or establish the final integrated wiring.

## More views

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 20–37

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint8_t AUGER_STEP_PIN = 2;
const uint8_t AUGER_DIR_PIN = 3;
const uint8_t AUGER_ENABLE_PIN = 4;

// Most stepper drivers use LOW = enabled and HIGH = disabled.
const uint8_t DRIVER_ENABLE_LEVEL = LOW;
const uint8_t DRIVER_DISABLE_LEVEL = HIGH;

// Change HIGH to LOW if the auger turns in the wrong direction.
const uint8_t DISPENSE_DIRECTION = HIGH;

// ============================================================
// SPEED TUNING
// ============================================================
// Values are STEP pulses per second, not motor RPM.
// At 1/16 microstepping on a 200-step motor:
//   3200 steps/s = 60 RPM
//   4000 steps/s = 75 RPM
```

### timer_controller_later.ino · lines 39–55

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t AUGER_STEP_PIN   = 9;   // OC1A
const uint8_t AUGER_DIR_PIN    = 8;
const uint8_t AUGER_ENABLE_PIN = 10;
const uint8_t AUGER_ALM_PIN    = 7;

const uint8_t DISK_STEP_PIN    = 11;  // OC2A
const uint8_t DISK_DIR_PIN     = 12;
const uint8_t DISK_ENABLE_PIN  = 4;
const uint8_t DISK_ALM_PIN     = 6;

const uint8_t DRIVER_ENABLE_LEVEL  = HIGH;
const uint8_t DRIVER_DISABLE_LEVEL = LOW;
const uint8_t DISPENSE_DIR_LEVEL   = LOW;
const uint8_t DISK_FORWARD_DIR_LEVEL = HIGH;
const uint8_t DISK_REVERSE_DIR_LEVEL = LOW;

// ============================================================
```

There was now an electrical route to drive the feeder. The next missing piece was a quantity the program could trust. Without scale input, I was still controlling motion and hoping the powder did something useful in response.

<details>
<summary>Notes added while reconstructing this entry</summary>

M2 began with one active hopper, so the electrical prototype used one NEMA 17 and a TMC2209 on a breadboard. The Raspberry Pi 4 provided the initial control connection, and the touchscreen added the user interface. At this point I needed to prove direction, enable control, and repeatable commanded motion separately from target-mass accuracy.

The saved record establishes the breadboard components and the motion-test configurations. It doesn't preserve a complete electrical test sequence, supply measurements, or the TMC2209 current setting for the initial setup. I've retained that boundary while documenting the actual code values, rather than describing unrecorded checks as successful trials.

This was the motor setup for the first scale-controlled doser. The next step was to read meaningful mass data, because a rotating motor alone can't tell the machine how much powder reached the cup.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
