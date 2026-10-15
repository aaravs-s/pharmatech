# R12 Separate powder behavior into configurable motion and settling profiles

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J18

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Give the controller useful behavior for both fast-flowing granular powders and powders that need more motion to leave the feeder.

## Design process

I found that settings that worked for sugar could make cornstarch dispense extremely slowly near the end. Sugar and salt could move readily with small commands, while finer, clumpier materials sometimes produced almost no powder under those same conditions.

I split the control behavior into categories based on powder consistency. The interface could select the appropriate controller behavior from the powder entered by the user. This let me adjust speed, pulse size, and waiting time for the materials that needed more active feeding without giving freely flowing powders an unnecessarily aggressive final step.

The distinction was practical and based on the powders I tested. It did not establish a universal material classification for every brand or condition. Moisture, compaction, hopper fill, and geometry could change the result. The most useful evidence for this entry is a comparison showing the same target mass with the unsuitable settings and then with the revised settings.

## Construction and implementation detail

A setting that protected sugar from overshoot could make cornstarch take too long because the same small finishing motion delivered very little material. The notes therefore describe changing speed and timing according to powder consistency. The implementation needs two layers: the mapping from a powder name to a family, and the motion/settling settings used by that family.

The July Python archive maps granulated sugar and table salt to FREE_FLOWING. Powdered sugar, baking soda, cornstarch, ground cinnamon, flour, and cocoa are mapped to NON_FREE_FLOWING. The descriptive behavior notes call cocoa and cinnamon fine and relatively free-flowing, so the software family name is not a universal physical classification. It identifies a chosen control profile for this implementation.

In the July Arduino configuration, free-flowing APPROACH/FINE/FINAL pulses contain 8, 4, and 1 steps at 1100, 700, and 400 pulses per second. The other family uses 20, 10, and 3 steps at 1500, 1000, and 650 pulses per second. Continuous FREE rates are 4000 TURBO and 2500 NORMAL, while NONFREE uses 6000 and 4000. These values are electrical step pulses, not rotations per minute or grams dispensed.

The distinction between pulse size and pulse speed is important. Changing step rate alters how fast a commanded movement occurs; changing the number of steps changes its angular extent. Neither has a fixed mass conversion across all powders. Settling time adds a third variable because the controller may need to wait for discharged material to arrive and for the averaged scale value to catch up.

The later controller makes profiles editable in dictionaries, normalizes powder-name spacing and case, rejects unknown powder names, and checks that thresholds are finite and ordered. It also supports a per-powder override dictionary, which is empty in the recovered file. Those are useful implementation details to document when introduced, but an empty override dictionary is not evidence that all eight powders were individually calibrated.

The practical result was a smaller configuration space than eight completely independent programs or a barcode database. I still needed to retain the final measured result for each powder. Shared parameters can simplify operation, but the powder tests determine whether that simplification is adequate at the intended mass.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### auger_july.ino · lines 43–80

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t FREE_TURBO_RATE = 4000;
const uint32_t FREE_NORMAL_RATE = 2500;

const uint32_t NONFREE_TURBO_RATE = 6000;
const uint32_t NONFREE_NORMAL_RATE = 4000;

// Ramp continuous motion up instead of jumping instantly to full speed.
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;

// ============================================================
// PULSE TUNING
// ============================================================

const uint16_t FREE_APPROACH_STEPS = 8;
const uint32_t FREE_APPROACH_RATE = 1100;

const uint16_t FREE_FINE_STEPS = 4;
const uint32_t FREE_FINE_RATE = 700;

const uint16_t FREE_FINAL_STEPS = 1;
const uint32_t FREE_FINAL_RATE = 400;

const uint16_t NONFREE_APPROACH_STEPS = 20;
const uint32_t NONFREE_APPROACH_RATE = 1500;

const uint16_t NONFREE_FINE_STEPS = 10;
const uint32_t NONFREE_FINE_RATE = 1000;

const uint16_t NONFREE_FINAL_STEPS = 3;
const uint32_t NONFREE_FINAL_RATE = 650;

// If the Pi disappears while the auger is moving, stop automatically.
const uint32_t SERIAL_WATCHDOG_MS = 2000;

// ============================================================
// MOTOR STATE
```

### controller_later.py · lines 81–100

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
def get_profile(powder_name: str) -> tuple[str, dict]:
    key = " ".join(powder_name.lower().split())
    if key not in POWDER_CATEGORIES:
        raise ValueError(f"Add {powder_name!r} to POWDER_CATEGORIES before dispensing.")
    category = POWDER_CATEGORIES[key]
    if category not in ("FREE", "NONFREE"):
        raise ValueError(f"Invalid category for {powder_name!r}: {category}")
    settings = CATEGORY_PROFILES[category].copy()
    overrides = POWDER_OVERRIDES.get(key, {})
    unknown = overrides.keys() - settings.keys()
    if unknown:
        raise ValueError(f"Unknown profile settings: {sorted(unknown)}")
    settings.update(overrides)
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0
           for v in settings.values()):
        raise ValueError("Profile values must be finite, nonnegative numbers.")
    if not (settings["tolerance_g"] < settings["fine_to_final_g"] <
            settings["normal_to_fine_g"] < settings["turbo_to_normal_g"]):
        raise ValueError("Thresholds must increase: tolerance < final < fine < normal.")
    return category, settings
```

## Image sequence

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

Two motion families allowed different feed and settling behavior. The archived family names, pulse settings, and later configurable profiles are documented without treating them as physical classifications or proven calibration.

## Complete from your records

Identify which parameter set was used in each recorded powder trial and add a table of observed mass per pulse, jams, and final error.

[IMAGE PLACEHOLDER: Profile mapping during implementation, Arduino pulse-size table, and a successful family-selection trace.]

[IMAGE PLACEHOLDER: Side-by-side sugar/cornstarch finishing trials using the same target and identified code revision.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
