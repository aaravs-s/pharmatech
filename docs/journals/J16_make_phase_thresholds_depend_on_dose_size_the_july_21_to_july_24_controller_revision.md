# J16 A 55 mg request shouldn't start like a large dose

*Milestone 3 | Retrospective build notes*

The fixed thresholds were getting awkward across different target sizes. The bulk phase could be too cautious for a larger request and still be too aggressive for a tiny one. I kept revising where the controller changed behavior instead of only increasing motor speed.

The July 21 and July 24 snapshots give me a useful comparison. In the older code, a 5 g request didn't begin in TURBO because the condition was greater than a fixed 5 g remaining. The later version made that cutoff depend on the target.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

At the small end, the change was more direct. Below 0.100 g, start with FINAL pulses. A 0.055 g sugar request had begun in FINE under the July 21 logic; the July 24 version treated it as FINAL from the beginning. That is a much clearer description of the change than simply saying I made the small doses more precise.

I also lengthened the near-target waits for the free-flowing profile. It cost time. The hope was to stop asking for more powder before the previous addition was fully reflected in the reading. I can't attach the recorded 55 mg results to one snapshot because the test sheet doesn't identify its code revision.

## What changed between the snapshots

The dated code emails provide an actual before/after pair. The July 21 motor_scale.py used a fixed 5.000 g TURBO cutoff and a 0.500 g micro-mode limit. At exactly a 5 g target, its initial remaining value wasn't greater than 5.000, so it didn't start in TURBO. The July 24 motor_scale_control.py introduced target-size-aware cutoffs instead of using that fixed bulk threshold for every request.

The July 24 code introduces an ultra-small limit of 0.100 g and a micro-dose limit of 0.500 g. Requests below 0.100 g start with FINAL pulses. Requests from 0.100 g to below 0.500 g use FINE followed by FINAL. A 0.055 g sugar request therefore changes from an initial FINE pulse in the July 21 logic to FINAL in the July 24 logic.

For free-flowing targets below 1.500 g, the TURBO cutoff becomes the larger of 0.250 g and 30% of the target. Targets up to 10.000 g use a 1.000 g cutoff, and larger targets use 2.000 g. For the other family, the respective choices are max(0.150 g, 20% of target), 0.600 g, and 1.000 g. These values define when the bulk phase ends; they don't mean the complete dose must stay inside those errors.

The July 24 free-flowing profile also changes continuous-to-pulse, APPROACH-to-FINE, and FINE-to-FINAL cutoffs to 0.500, 0.150, and 0.050 g remaining. Its settling intervals become 0.800 s after continuous motion, 0.300 s after APPROACH, and 2.0 s after each FINE or FINAL pulse. The non-free-flowing settings become 0.300, 0.120, and 0.040 g, with settling intervals of 0.350, 0.120, 0.220, and 0.300 s.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 119–145

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose the Arduino command for the current amount remaining."""
    profile = PROFILES[powder_mode]
    powder_token = profile.command_name

    # Tiny targets never enter continuous mode because there is too
    # little mass available to absorb startup and chute overshoot.
    if target < MICRO_MODE_LIMIT:
        if remaining > profile.pulse_approach_to_fine:
            return f"AUGER PULSE {powder_token} APPROACH"
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    if remaining > TURBO_REMAINING:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 121–144

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def turbo_cutoff_remaining(target: float, powder_mode: str) -> float:
    """Return the remaining mass where TURBO changes to a slower mode.

    Free-flowing examples:
    - 1.000 g target: TURBO until about 0.300 g remains.
    - 2.000-10.000 g target: TURBO until 1.000 g remains.
    - Above 10.000 g: TURBO ends at 2.000 g remaining to leave extra
      room for material momentum and powder already falling.

    Non-free-flowing powder receives smaller headroom because its flow is
    slower and normally stops more quickly.
    """
    if powder_mode == FREE_FLOWING:
        if target < SMALL_TARGET_LIMIT:
            return max(0.250, target * 0.30)
        if target <= LARGE_TARGET_LIMIT:
            return 1.000
        return 2.000

    if target < SMALL_TARGET_LIMIT:
        return max(0.150, target * 0.20)
    if target <= LARGE_TARGET_LIMIT:
        return 0.600
    return 1.000
```

### motor_2026-07-24.py · lines 157–187

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose a target-aware Arduino command for the current remaining mass."""
    profile = profile_for(target, powder_mode)
    powder_token = profile.command_name

    # 20-90 mg-style doses start with the smallest physical movement.
    if target < ULTRA_SMALL_DOSE_LIMIT:
        return f"AUGER PULSE {powder_token} FINAL"

    # Small sub-gram doses do not use continuous movement. They use FINE
    # pulses first, then switch to the one-step/tiny FINAL pulse near target.
    if target < MICRO_DOSE_LIMIT:
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    turbo_cutoff = turbo_cutoff_remaining(target, powder_mode)

    if remaining > turbo_cutoff:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 89–112

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
PROFILES = {
    FREE_FLOWING: PowderProfile(
        # Free-flowing powder has more material in flight after fast motion.
        continuous_to_pulse=0.500,
        pulse_approach_to_fine=0.150,
        pulse_fine_to_final=0.050,
        continuous_settle=0.800,
        approach_settle=0.300,
        fine_settle=2.0,
        final_settle=2.0,
        command_name="FREE",
    ),
    NON_FREE_FLOWING: PowderProfile(
        # Non-free-flowing powder can normally run closer to the target.
        continuous_to_pulse=0.300,
        pulse_approach_to_fine=0.120,
        pulse_fine_to_final=0.040,
        continuous_settle=0.350,
        approach_settle=0.120,
        fine_settle=0.220,
        final_settle=0.300,
        command_name="NONFREE",
    ),
}
```

This gave the program a better way to distinguish tiny requests from multi-gram ones. The code change is clear; its measured benefit isn't established by the unmatched test sheet. I would need the same target and configuration on both sides of the revision to make that comparison properly.

<details>
<summary>Notes added while reconstructing this entry</summary>

The longer near-target delays, particularly the 2.0 s free-flowing FINE and FINAL intervals, trade run time for additional observation of the last addition. The July 24 email establishes availability of the revision, but doesn't connect each listed powder result to that version. The measured trials and the code comparison remain separate pieces of evidence.

The later cleaned controller uses another arrangement, including a 0.005 g tolerance and a 120 s maximum duration. Those settings describe a subsequent source state. They don't establish an improvement over the July versions without a matched measured run, and the larger absolute tolerance is particularly relevant to evaluating small targets.

</details>

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R16_make_phase_thresholds_depend_on_dose_size_the_july_21_to_july_24_controller_revision.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
