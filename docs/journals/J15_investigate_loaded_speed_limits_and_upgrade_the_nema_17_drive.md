# J15 Trying to get more out of the NEMA 17

*Milestone 3 | Retrospective build notes*

The feeder was slow enough that I started with the software. I changed speed requests, acceleration behavior, and powder settings to see how much more useful motion I could get. Replacing the motor before understanding the delays would have made it harder to tell what actually helped.

But a bigger requested rate doesn't mean the loaded shaft follows it. The notes describe reaching the NEMA 17's practical limit in this setup and changing to a NEMA 23. They report an improvement in usable dispensing speed afterward.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

That was encouraging, though it wasn't a controlled torque or throughput comparison. I don't have a matching series with the same fill, feeder, and finishing settings before and after. I can describe the upgrade without attaching a made-up percentage improvement to it.

The larger hardware also brought mounting, coupling, power, and signal changes along with it. And I still needed the slow finishing phases. More bulk-feed capability didn't make the scale instant or turn a clump into a predictable amount of powder.

## Drive and timing notes

The early Arduino implementation starts continuous motion at 400 pulses/s and ramps at a configured 9000 steps/s squared, updating every 5000 microseconds. STEP high and low intervals are generated in software. A separate AccelStepper test uses a fixed 600-step/s command. These are distinct experiments with different timing and pin assumptions.

M3 notes state that the investigation eventually identified the NEMA 17 as a limitation and that it was replaced by a NEMA 23. The BOM lists integrated closed-loop NEMA 23 motors with pulse/direction control. That later motor architecture also changed driver handling and wiring, so the hardware upgrade was more than increasing a speed constant in Python.

The larger motor didn't remove the need to slow near the target. A machine can feed rapidly in the bulk phase while still requiring short movements and settling pauses in the final phase. I retained phased dosing after the hardware change so that improving throughput would not simply recreate the sugar-overshoot problem.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

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

The motor upgrade moved the project forward, but it wasn't the last speed problem. Later I had to look at how the Arduino generated the pulses themselves. Different bottleneck, different change. I don't want to collapse both into 'the old motor was too slow.'

<details>
<summary>Notes added while reconstructing this entry</summary>

The single doser was usable but slow. I first investigated software because requested speed, acceleration, and finishing behavior all influence a run's duration. That investigation was reasonable, but a higher command rate isn't proof that the physical shaft follows every step under powder load. I needed to compare commanded motion with actual rotation and powder output.

The notes report improved usable speed after the motor replacement, but contain no controlled before-and-after torque or duration series. Feeder geometry, hopper fill, and finishing parameters could also affect throughput. I retained the qualitative upgrade result without assigning a numerical gain to the motor alone.

The later M5 timing revision addressed software-generated pulses, which is a separate issue from loaded motor capability. Changing the motor and changing the pulse source occurred at different stages and solved different parts of the system. That distinction helped keep a requested frequency separate from verified shaft behavior.

</details>

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
