# J08 Wire the first NEMA 17 and TMC2209 drive and establish controlled motion

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I assembled the initial electrical drive using a NEMA 17, a TMC2209 driver, and a breadboard. The Raspberry Pi 4 provided the first control connection, with a touchscreen for the user interface. This moved the project from mechanical powder trials toward commanded feeding.

I kept the basic motion task separate from target-mass accuracy. STEP pulses, direction, and driver enable determine what the motor is asked to do; none of them measure how much powder reaches the cup. Before a closed-loop controller could be useful, the feeder needed an electrical interface that could start, change behavior, and stop.

The saved code includes multiple wiring stages. A small AccelStepper test uses STEP on pin 3 and DIR on pin 2, while the July controller assigns those signals differently. I have kept those configurations separate below. The exact original Pi GPIO map and driver current setting are not recorded in the material used for this account.

## Technical detail

M2 began with one active hopper, so the electrical prototype used one NEMA 17 and a TMC2209 on a breadboard. The Raspberry Pi 4 provided the initial control connection, and the touchscreen added the user interface. At this point I needed to prove direction, enable control, and repeatable commanded motion separately from target-mass accuracy.

STEP, DIR, and EN control different aspects of the drive. STEP requests incremental motion, DIR selects its direction, and EN activates or disables the driver according to its polarity. The motor winding connections and shared signal reference are separate from those logic functions. A breadboard layout records packaging, while the corresponding pin assignments identify a particular controller revision.

The later July Arduino source makes the eventual command interface concrete: auger STEP is pin 2, DIR is pin 3, and ENABLE is pin 4. In that file, LOW enables the driver and HIGH disables it, while HIGH is the dispensing direction. This is an archived Arduino configuration, not the original Pi GPIO map. The timer-based firmware later uses different pins and the opposite enable level, so those diagrams must be kept version-specific.

The standalone repository test uses AccelStepper::DRIVER with stepPin 3 and directionPin 2, sets a 1000-step/s maximum, and calls runSpeed() at 600 steps/s. That is a motor-only test with a different pin order from the July controller. It does not contain the mass-feedback loop or establish the final integrated wiring.

The source record establishes the breadboard components and the motion-test configurations. It does not preserve a complete electrical test sequence, supply measurements, or the TMC2209 current setting for the initial setup. I have retained that boundary while documenting the actual code values, rather than describing unrecorded checks as successful trials.

The outcome was the motor system used for the first scale-controlled doser. The next step was to read meaningful mass data, because a rotating motor alone cannot tell the machine how much powder reached the cup.

## Archived implementation

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

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Outcome and reflection

The first motor setup gave the single doser an electrically commanded drive. It also established the need to track wiring together with firmware: a pin assignment from a standalone test cannot be carried into a different controller by assumption. I then added scale feedback so the machine could act on the mass actually collected.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
