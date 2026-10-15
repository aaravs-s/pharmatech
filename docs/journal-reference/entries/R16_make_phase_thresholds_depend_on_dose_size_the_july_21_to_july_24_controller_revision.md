# R16 Make phase thresholds depend on dose size: the July 21 to July 24 controller revision

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J23

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Keep tiny doses controlled while allowing larger doses to use faster bulk feeding.

## Design process

I retained the variable-speed strategy even after addressing the motor limitation. A faster drive could move most of the requested powder quickly, but the final part of the dispense still needed finer control because of scale lag and the amount released per movement.

The milestone notes give being roughly 1 g from the target as an example of when a slower phase could begin. That is an illustrative threshold, not a confirmed final setting for every powder. I experimented with the point at which the controller changed behavior so it would not spend the entire run in a slow finishing mode.

The design problem was to make the bulk phase productive without letting the finishing phase inherit too much powder already in flight. I would show the actual phase thresholds, speed values, and pulse sizes from the revision being logged. If later versions had additional fine or final phases, those should be introduced when they were added rather than retroactively assigned to this first variable-speed implementation.

## Construction and implementation detail

The dated code emails provide an actual before/after pair. The July 21 motor_scale.py used a fixed 5.000 g TURBO cutoff and a 0.500 g micro-mode limit. At exactly a 5 g target, its initial remaining value was not greater than 5.000, so it did not start in TURBO. The July 24 motor_scale_control.py introduced target-size-aware cutoffs instead of using that fixed bulk threshold for every request.

The new code sets an ultra-small limit of 0.100 g and a micro-dose limit of 0.500 g. Requests below 0.100 g use FINAL pulses from the beginning. Requests from 0.100 g to below 0.500 g use FINE followed by FINAL. A 0.055 g sugar request therefore changes from an initial FINE pulse in the July 21 logic to FINAL in the July 24 logic. This is a precise behavioral change supported by the files, not an invented tuning anecdote.

For free-flowing targets below 1.500 g, the TURBO cutoff becomes the larger of 0.250 g and 30% of the target. Targets up to 10.000 g use a 1.000 g cutoff, and larger targets use 2.000 g. For the other family, the respective choices are max(0.150 g, 20% of target), 0.600 g, and 1.000 g. These values define when the bulk phase ends; they do not mean the complete dose must stay inside those errors.

The July 24 free-flowing profile also changes continuous-to-pulse, APPROACH-to-FINE, and FINE-to-FINAL cutoffs to 0.500, 0.150, and 0.050 g remaining. Its settling intervals become 0.800 s after continuous motion, 0.300 s after APPROACH, and 2.0 s after each FINE or FINAL pulse. The non-free-flowing settings become 0.300, 0.120, and 0.040 g, with settling intervals of 0.350, 0.120, 0.220, and 0.300 s.

Those changes trade speed for additional observation time near the end, particularly for sugar and salt. The code email establishes that this revision existed by July 24; it does not establish how many hours the tuning took or which recorded powder runs used it. The 0.055 g test results should therefore remain associated with their test sheet unless the test date and code revision can be matched.

The later cleaned controller uses another parameter arrangement, including a 0.005 g tolerance and a 120 s maximum dispense time. I keep that as a later source state, not the final proof that the July settings were improved. A reproducible journal records the configuration used for the test, the actual measured mass and duration, and then the change made in response.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

A dated revision changed tiny-dose starting phases, bulk cutoffs, and settling intervals. The before/after logic is recoverable; its experimental impact still needs matching run records.

## Complete from your records

Add actual work dates, which trials used each revision, before/after final masses, and the reason for each parameter change.

[IMAGE PLACEHOLDER: July 21 phase-selection excerpt beside the July 24 dose-size branches and profile table.]

[IMAGE PLACEHOLDER: Matched 0.055 g and 5 g dispense traces for each revision, including the first phase chosen.]

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
