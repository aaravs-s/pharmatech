# J11 Replace continuous feeding near the target with stop, settle, and pulse phases

*Milestone 2 | Personal retrospective journal*

## Design and iteration

Sugar made the stopping problem clear. A displayed reading near the target did not mean all the powder already released had reached the cup or appeared in the scale's output. Continuing at the bulk-feed rate until the display reached the requested mass could overshoot.

I changed the control strategy to use fast movement while much of the target remained, followed by slower, finite additions near completion. After stopping continuous motion, the controller waited before deciding whether another pulse was needed. The notes describe developing this behavior with sugar and applying similar reasoning to salt.

The tradeoff was dispensing time. Small motions and long pauses created more opportunities to observe the last addition, but too much finishing time made the machine slow. I therefore treated thresholds, pulse lengths, and settling delays as separate tuning variables. The July 21 source below records one specific configuration, rather than a universal setting for every dose.

## Technical detail

The central control problem was that motor stop and mass stop were not simultaneous. Powder could already be in the outlet or falling toward the cup, and the scale could report that mass after a delay. If I continued feeding until the displayed mass reached the target, the last commanded material could arrive too late to be accounted for. The notes identify this clearly for sugar and salt.

The July 21 controller selects among continuous TURBO, continuous NORMAL, and APPROACH/FINE/FINAL pulses. For a free-flowing profile, continuous motion ends at 1.250 g remaining; APPROACH changes to FINE at 0.120 g remaining; FINE changes to FINAL at 0.030 g remaining. The corresponding non-free-flowing cutoffs are 0.500, 0.120, and 0.050 g. These are grams remaining, not percentages of the target and not elapsed times.

The transition out of continuous mode is deliberately a separate action. The controller sends an auger stop, clears its active-command state, waits for the profile's continuous-settling interval, and restarts the loop using a later mass reading. It does not immediately issue the first pulse using the same pre-stop value. That separation is the key implementation detail behind 'slow down near the target.'

For free-flowing material, the July 21 settling values are 0.650 s after continuous motion, 0.220 s after APPROACH, 0.450 s after FINE, and 0.750 s after FINAL. For the other family, they are 0.300, 0.100, 0.160, and 0.220 s. The Arduino owns how many steps are in each pulse; Python owns the decision about when to issue one and how long to wait before re-evaluating mass.

Targets below 0.500 g bypass continuous motion in that archive. For a 0.055 g sugar target at the start, the remaining amount is below 0.120 but above 0.030, so the old logic chooses a FINE pulse. The later July 24 revision changes that behavior. This example makes the evolution visible: a small target cannot safely inherit the bulk-feed behavior of a large dose just because the powder name is the same.

The 3% project criterion differs from the code's absolute 0.001 g stop tolerance. In the July loop, remaining <= tolerance is tested before the separate overshoot branch, so an overshoot can satisfy the first condition. That implementation detail limits what the 'target reached' path means. I assessed dose error from the recorded final mass rather than treating a successful process exit as proof of accuracy.

## Archived implementation

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

### motor_2026-07-21.py · lines 540–564

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
        # The first transition out of continuous mode always stops and
        # settles before any pulse is issued. The next loop uses the new
        # scale reading and may already decide that the target is reached.
        if is_continuous_command(active_command):
            arduino.stop_auger()
            active_command = None
            print(
                f"Continuous phase complete; settling {profile.continuous_settle:.2f} s",
                flush=True,
            )
            time.sleep(profile.continuous_settle)
            continue

        if is_pulse_command(desired_command):
            print(f"PULSE -> {desired_command}", flush=True)
            arduino.run_pulse(desired_command)
            active_command = None
            time.sleep(settle_time_for(desired_command, powder_mode))
            continue

        raise RuntimeError(f"Unhandled auger command: {desired_command}")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_stop_signal)
```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The controller gained an explicit stop-settle-reassess step between bulk feeding and final pulses. That was more useful than simply reducing speed: it prevented the first finishing command from being based on the same delayed reading that ended continuous motion. Final scale mass remained the measure of success, because a software completion message alone could also occur after an overshoot.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R11_replace_continuous_feeding_near_the_target_with_stop_settle_and_pulse_phases.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
