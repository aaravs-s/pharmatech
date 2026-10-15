# R11 Replace continuous feeding near the target with stop, settle, and pulse phases

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J17

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Reduce overshoot caused by powder still falling and delayed mass feedback near the requested dose.

## Design process

Fast-flowing powders created a stopping problem. With sugar, the reported mass could look close to the target while additional powder was still moving through the outlet or had not yet appeared in the scale reading. Continuing at the same rate near the target could therefore produce an overshoot.

I changed the control behavior so the motor moved faster when there was a larger amount left, then slowed down and allowed more time between pulses near completion. This gave the scale more opportunity to reflect the last addition before the next command. The notes specifically describe this strategy for sugar and later applying similar behavior to salt.

The tradeoff was speed against final control. Very small movements and long pauses can improve the opportunity to observe each addition, but they can also make a dispense unnecessarily slow. I needed to tune the switching threshold and pulse behavior using the actual powder and scale response. The source does not give enough information to claim a measured latency or a universally correct delay.

## Construction and implementation detail

The central control problem was that motor stop and mass stop were not simultaneous. Powder could already be in the outlet or falling toward the cup, and the scale could report that mass after a delay. If I continued feeding until the displayed mass reached the target, the last commanded material could arrive too late to be accounted for. The notes identify this clearly for sugar and salt.

The July 21 controller selects among continuous TURBO, continuous NORMAL, and APPROACH/FINE/FINAL pulses. For a free-flowing profile, continuous motion ends at 1.250 g remaining; APPROACH changes to FINE at 0.120 g remaining; FINE changes to FINAL at 0.030 g remaining. The corresponding non-free-flowing cutoffs are 0.500, 0.120, and 0.050 g. These are grams remaining, not percentages of the target and not elapsed times.

The transition out of continuous mode is deliberately a separate action. The controller sends an auger stop, clears its active-command state, waits for the profile's continuous-settling interval, and restarts the loop using a later mass reading. It does not immediately issue the first pulse using the same pre-stop value. That separation is the key implementation detail behind 'slow down near the target.'

For free-flowing material, the July 21 settling values are 0.650 s after continuous motion, 0.220 s after APPROACH, 0.450 s after FINE, and 0.750 s after FINAL. For the other family, they are 0.300, 0.100, 0.160, and 0.220 s. The Arduino owns how many steps are in each pulse; Python owns the decision about when to issue one and how long to wait before re-evaluating mass.

Targets below 0.500 g bypass continuous motion in that archive. For a 0.055 g sugar target at the start, the remaining amount is below 0.120 but above 0.030, so the old logic chooses a FINE pulse. The later July 24 revision changes that behavior. This example makes the evolution visible: a small target cannot safely inherit the bulk-feed behavior of a large dose just because the powder name is the same.

The recorded 3% project target and the code's absolute 0.001 g stop tolerance are different quantities. Also, the July loop tests remaining <= tolerance before its separate overshoot branch, so an overshoot can satisfy the first condition. I keep that source limitation in the technical annotation; a successful exit or 'target reached' message is not sufficient evidence that the measured dose met the requested error bound. The journal result must use the final scale mass.

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

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

The controller implemented stop-and-settle transitions and progressively smaller feeding pulses. Accuracy is assessed from final measured mass, not from the program's success message.

## Complete from your records

Add before/after dispense traces, pulse mass per powder, measured scale settling time, and actual tuning iterations rather than assigning all archived constants to one session.

[IMAGE PLACEHOLDER: Old continuous-only loop, revised stop/settle branch, and final phase-selection source excerpt.]

[IMAGE PLACEHOLDER: Mass-versus-time trace showing a continuous stop, post-stop increase, and finishing pulses.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
