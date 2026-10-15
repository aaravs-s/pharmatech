# R15 Investigate loaded speed limits and upgrade the NEMA 17 drive

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J21, J22

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Determine whether slow dispensing comes from controller timing, powder transport, or the motor's ability to move the loaded mechanism.

## Design process

I first treated the slow dispensing behavior as a control problem. I adjusted motor speed, acceleration behavior, and powder profiles to see whether the single doser could move faster while still stopping accurately.

That investigation mattered because increasing the requested speed does not guarantee that the shaft actually turns faster under load. The pulse-generation code, driver settings, motor torque, and powder resistance all affect what the mechanism can do. The milestone notes describe trying software changes before concluding that the NEMA 17 was limiting the usable performance.

I would make this entry concrete with the speed commands I tried, what the motor visibly did, and whether the auger stalled or simply remained too slow. Without those details, it would be easy to overstate the diagnosis. The recorded conclusion supports the decision to try a different motor, but not a precise torque or maximum-speed measurement.

I replaced the NEMA 17 configuration with a NEMA 23 to improve the drive capability of the doser. The milestone notes report increased usable dispensing speed while maintaining controlled motion after the change.

The BOM later lists integrated closed-loop NEMA 23 motors using pulse-and-direction control, with model UIM5756PM in the item description. That part listing is useful for identifying the purchased hardware, but the exact model label on the installed motor should be checked before the journal treats it as the final configuration. Motor frame size alone does not define its torque-speed performance.

Changing the motor also affected the packaging: the mount, coupling, supply, and control signals had to fit the new hardware. I would include those mechanical and electrical changes along with the performance comparison. The clearest evidence would show the old setup and the new one running the same powder and target mass, rather than relying only on the statement that the larger motor was better.

## Construction and implementation detail

The single doser was usable but slow. I first investigated software because requested speed, acceleration, and finishing behavior all influence a run's duration. That investigation was reasonable, but a higher command rate is not proof that the physical shaft follows every step under powder load. I needed to compare commanded motion with actual rotation and powder output.

The early Arduino implementation starts continuous motion at 400 pulses per second and ramps at a configured 9000 steps per second squared, with updates every 5000 microseconds. It generates high and low STEP intervals in software. The available standalone repository test instead runs a fixed AccelStepper speed of 600. These files represent different control experiments and should not be described as one unchanged firmware configuration.

M3 notes state that the investigation eventually identified the NEMA 17 as a limitation and that it was replaced by a NEMA 23. The BOM lists integrated closed-loop NEMA 23 motors with pulse/direction control. That later motor architecture also changed driver handling and wiring, so the hardware upgrade was more than increasing a speed constant in Python.

The detailed comparison needs the same printed feeder and powder load before and after the upgrade. Otherwise a different auger, fill level, or finishing profile could explain some of the apparent speed gain. The source notes report the improvement, but do not give a controlled before/after torque or time series. I leave a table for requested pulse rate, driver settings, actual shaft behavior, jams, final mass, and total duration.

The larger motor did not remove the need to slow near the target. A machine can feed rapidly in the bulk phase while still requiring short movements and settling pauses in the final phase. I retained phased dosing after the hardware change so that improving throughput would not simply recreate the sugar-overshoot problem.

Later M5 notes describe a further bottleneck in software-generated pulses, followed by timer-based generation. That is a second investigation. The journal should not collapse the M3 motor upgrade and M5 timer change into a single diagnosis: one concerns the loaded drive capability, while the other concerns how reliably the controller generates the requested waveform.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Result and handoff

The source records a NEMA 23 upgrade after software tuning of the NEMA 17. Quantitative comparisons still need the actual loaded trials; the timer-generation change is documented separately.

## Complete from your records

Add exact motor/driver models, supply voltage, microsteps, load, coupling changes, before/after rates, and matched dispense times.

[IMAGE PLACEHOLDER: Speed/acceleration tuning version before the motor change and a trace of the unsuccessful loaded behavior.]

[IMAGE PLACEHOLDER: NEMA 17 and NEMA 23 installation comparison, followed by matched powder tests.]

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
