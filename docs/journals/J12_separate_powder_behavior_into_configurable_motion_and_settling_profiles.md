# J12 Separate powder behavior into configurable motion and settling profiles

*Milestone 2 | Personal retrospective journal*

## Design and iteration

The settings that limited sugar overshoot made cornstarch extremely slow near completion. A small command could release useful material from sugar or salt but almost nothing from a clumpier powder. I stopped treating the powder name as a label used only by the interface and made it select motion behavior.

I grouped the tested materials into two control families and gave each family its own speed, pulse size, and settling settings. This reduced the number of separate programs to maintain while preserving a way to make the more resistant materials move.

The family names describe controller configuration, not a universal classification of powder physics. For example, the notes describe cocoa and cinnamon as feeding relatively readily in this mechanism, while the archived program assigns both to NON_FREE_FLOWING. The actual mapping matters more than an intuitive reading of the label. Moisture, compaction, and geometry could also change how a material behaved.

## Technical detail

A small finishing motion that limited sugar overshoot could deliver very little cornstarch. I made powder selection affect two layers: the mapping from a name to a control family and the motion and settling parameters assigned to that family. This preserved one control structure while allowing different behavior.

The July Python archive maps granulated sugar and table salt to FREE_FLOWING. Powdered sugar, baking soda, cornstarch, ground cinnamon, flour, and cocoa are mapped to NON_FREE_FLOWING. The descriptive behavior notes call cocoa and cinnamon fine and relatively free-flowing, so the software family name is not a universal physical classification. It identifies a chosen control profile for this implementation.

In the July Arduino configuration, free-flowing APPROACH/FINE/FINAL pulses contain 8, 4, and 1 steps at 1100, 700, and 400 pulses per second. The other family uses 20, 10, and 3 steps at 1500, 1000, and 650 pulses per second. Continuous FREE rates are 4000 TURBO and 2500 NORMAL, while NONFREE uses 6000 and 4000. These values are electrical step pulses, not rotations per minute or grams dispensed.

The distinction between pulse size and pulse speed is important. Changing step rate alters how fast a commanded movement occurs; changing the number of steps changes its angular extent. Neither has a fixed mass conversion across all powders. Settling time adds a third variable because the controller may need to wait for discharged material to arrive and for the averaged scale value to catch up.

The later controller stores editable profiles in dictionaries, normalizes case and spacing in powder names, rejects unknown names, and checks for finite, ordered thresholds. It also contains a per-powder override dictionary, empty in the recovered file. That provides an extension point without establishing that all eight materials received individual calibration.

The practical result was a smaller configuration space than eight completely independent programs or a barcode database. I still needed to retain the final measured result for each powder. Shared parameters can simplify operation, but the powder tests determine whether that simplification is adequate at the intended mass.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

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

## Process images

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

Two parameter families gave me a manageable configuration structure for the eight test powders. Separating pulse extent, pulse rate, and settling time clarified what each change could affect. Shared settings simplified operation, but the recorded mass tests still had to establish the performance of each powder at each requested dose.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R12_separate_powder_behavior_into_configurable_motion_and_settling_profiles.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
