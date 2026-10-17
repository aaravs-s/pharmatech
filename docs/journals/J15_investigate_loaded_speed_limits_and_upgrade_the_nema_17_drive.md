# J15 Investigate loaded speed limits and upgrade the NEMA 17 drive

*Milestone 3 | Personal retrospective journal*

## Design and iteration

The single doser was usable but slow, so I first investigated the software settings. I adjusted requested motor speed, acceleration behavior, and feeding profiles before changing the hardware. That order mattered because slow dispensing could come from conservative finishing behavior as well as limited drive capability.

The milestone record describes eventually identifying the NEMA 17 as a limitation and replacing it with a NEMA 23. It reports greater usable dispensing speed after the change. I have not converted that qualitative improvement into a numerical torque gain or a controlled before-and-after throughput result.

The replacement also affected mounting, coupling, power, and control signals. The BOM identifies integrated closed-loop NEMA 23 hardware, so this was more than increasing one speed constant. I retained phased feeding because a stronger bulk drive did not eliminate the scale delay or the need for fine additions near the target.

## Technical detail

The single doser was usable but slow. I first investigated software because requested speed, acceleration, and finishing behavior all influence a run's duration. That investigation was reasonable, but a higher command rate is not proof that the physical shaft follows every step under powder load. I needed to compare commanded motion with actual rotation and powder output.

The early Arduino implementation starts continuous motion at 400 pulses/s and ramps at a configured 9000 steps/s squared, updating every 5000 microseconds. STEP high and low intervals are generated in software. A separate AccelStepper test uses a fixed 600-step/s command. These are distinct experiments with different timing and pin assumptions.

M3 notes state that the investigation eventually identified the NEMA 17 as a limitation and that it was replaced by a NEMA 23. The BOM lists integrated closed-loop NEMA 23 motors with pulse/direction control. That later motor architecture also changed driver handling and wiring, so the hardware upgrade was more than increasing a speed constant in Python.

The notes report improved usable speed after the motor replacement, but contain no controlled before-and-after torque or duration series. Feeder geometry, hopper fill, and finishing parameters could also affect throughput. I therefore retained the qualitative upgrade result without assigning a numerical gain to the motor alone.

The larger motor did not remove the need to slow near the target. A machine can feed rapidly in the bulk phase while still requiring short movements and settling pauses in the final phase. I retained phased dosing after the hardware change so that improving throughput would not simply recreate the sugar-overshoot problem.

The later M5 timing revision addressed software-generated pulses, which is a separate issue from loaded motor capability. Changing the motor and changing the pulse source occurred at different stages and solved different parts of the system. That distinction helped keep a requested frequency separate from verified shaft behavior.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 50–52

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;
```

### timer_controller_later.ino · lines 83–95

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint32_t FREE_TURBO_HZ  = 20000;
const uint32_t FREE_NORMAL_HZ = 2400;

// Cornstarch/non-free-flowing values.
// 20 kHz is the user's measured sweet spot: ~1 g every ~2 seconds.
const uint32_t NONFREE_TURBO_HZ  = 20000;
const uint32_t NONFREE_NORMAL_HZ = 9000;

// Fast but controlled ramp for continuous modes.
const uint32_t CONTINUOUS_START_HZ = 2000;
const uint32_t RAMP_STEP_HZ        = 500;
const uint32_t RAMP_UPDATE_MS      = 10;

```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The motor upgrade addressed the loaded drive limitation described in the milestone notes while preserving mass-based finishing control. It did not settle every speed question. The later timer investigation concerned pulse generation, a separate bottleneck from the motor and powder load, so I kept those changes as distinct engineering decisions.

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
