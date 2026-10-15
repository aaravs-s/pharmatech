# R08 Wire the first NEMA 17 and TMC2209 drive and establish controlled motion

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J13

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Turn the printable feeder into an electrically driven prototype before adding mass feedback.

## Design process

I assembled the first motor-control setup using a NEMA 17, a TMC2209 driver, and a breadboard. This gave the single doser a controllable drive so I could move from manually testing powder flow to commanding the auger electrically.

The hardware had to provide the motor's power and a valid control interface. The milestone notes describe the Raspberry Pi connection, while the repository contains a small AccelStepper test sketch that uses STEP on pin 3 and DIR on pin 2, sets a maximum of 1000 steps per second, and commands 600 steps per second. That sketch is evidence of one standalone motor test; it should not be mistaken for the complete final controller or used to infer the final pin assignments.

I would record the wiring revision that actually powered this milestone, including supply voltage, current setting, microstepping, signal ground, and enable behavior. The breadboard photos are useful for showing the prototype layout, but a labeled wiring diagram is needed before another builder could reproduce it reliably.

## Construction and implementation detail

M2 began with one active hopper, so the electrical prototype used one NEMA 17 and a TMC2209 on a breadboard. The Raspberry Pi 4 provided the initial control connection, and the touchscreen added the user interface. At this point I needed to prove direction, enable control, and repeatable commanded motion separately from target-mass accuracy.

STEP, DIR, and EN serve different purposes. STEP commands incremental motion; DIR chooses the direction associated with those pulses; EN determines whether the driver is active. A journal needs a wiring view that labels each of these paths, the motor winding pairs, the power supply, and the shared signal reference. A generic photograph of a breadboard cannot establish the pin mapping or enable polarity by itself.

The later July Arduino source makes the eventual command interface concrete: auger STEP is pin 2, DIR is pin 3, and ENABLE is pin 4. In that file, LOW enables the driver and HIGH disables it, while HIGH is the dispensing direction. This is an archived Arduino configuration, not the original Pi GPIO map. The timer-based firmware later uses different pins and the opposite enable level, so those diagrams must be kept version-specific.

The available motor-only repository test uses AccelStepper::DRIVER with stepPin 3 and directionPin 2, a maximum speed of 1000, and a running speed of 600 through runSpeed(). Its pin order differs from the July controller. The test can document how basic motion was exercised; it should not be presented as the complete mass-feedback firmware or copied into the later wiring without reconciliation.

For this update, I would describe the actual checks in the order performed: identify the winding pairs, apply the chosen driver settings, confirm the screw rotates in the feeding direction, verify stopping, and then repeat with powder present. The notes confirm the components and breadboard arrangement but do not provide the electrical measurements, current-limit setting, or detailed results for every check. Those items remain prompts rather than invented successful trials.

The outcome was the motor system used for the first scale-controlled doser. The next step was to read meaningful mass data, because a rotating motor alone cannot tell the machine how much powder reached the cup.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Result and handoff

The initial single-doser breadboard drive used a NEMA 17 and TMC2209. Later archived pin maps are documented separately to avoid applying the final wiring to the early prototype.

## Complete from your records

Recover the Pi GPIO map, driver current and microstep settings, supply voltage, motor winding identification, and actual direction/stop tests.

[IMAGE PLACEHOLDER: Labeled early wiring diagram and close-up of STEP, DIR, EN, motor coils, and signal ground.]

[IMAGE PLACEHOLDER: Motor-only test output followed by a loaded rotation test of the same printed feeder.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
