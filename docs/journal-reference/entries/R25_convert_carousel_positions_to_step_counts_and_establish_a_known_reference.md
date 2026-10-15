# R25 Convert carousel positions to step counts and establish a known reference

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J37, J38

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Relate slot numbers to controlled disk motion and make the starting-position assumption explicit.

## Design process

I used the disk geometry to relate a hopper number to commanded stepper motion. With eight stations, adjacent slots are separated by one eighth of a revolution. The controller can translate that into a fixed count if the motor, microstepping, and any transmission ratio are known.

The rough milestone note has an ambiguous total-step description. Earlier project discussion described 200 full steps per revolution and 32 microsteps per full step, which would give 6400 input pulses per motor revolution and 800 pulses per station for a direct-drive disk. That calculation is a reference to check against the actual driver settings, not proof of the final installed configuration. A gear or belt ratio would change it.

I wanted an integral count for each station so the commanded positions did not accumulate rounding error. The journal should record the exact settings and the physical alignment check at all eight slots. Step counts provide a commanded position; they do not detect missed motion on their own.

I needed a physical reference so the controller could know which hopper was at the dispensing position after startup. A fixed step count between stations only becomes useful once one known station has been established.

The milestone note mentions homing at the beginning. Earlier project discussion describes a detent and limit-switch arrangement, with the switch normally pressed and opening when a detent passes. The final journal needs to identify the actual switch location, signal polarity, and event used as the home reference. It should also state how the machine handles starting with the switch already in the active state.

This update connects the mechanical indexing features to the software's slot numbering. The important result is whether repeated homing returns the same hopper to the same dispensing alignment. The notes do not include a measured home-position error, so that needs to be added from a real test rather than inferred from the presence of a switch.

## Construction and implementation detail

The later timer-based firmware defines eight slots, 200 motor full steps per revolution, 32 driver microsteps, and a motor-to-disk ratio of 1:1. The resulting calculation is 200 times 32 divided by eight, or 800 step pulses per slot. One full disk revolution is therefore 6400 pulses for that configuration. This resolves the rough '640 hundred steps' wording in the M4 notes for the recovered firmware, but the installed driver switches still need to match it.

The geometry gives 45 degrees per slot, while the motor configuration gives electrical pulses per slot. They agree only if the gearing, microstep mode, direction, and physical reference are correct. Changing the driver microstep switch without updating the software would change disk travel even though the slot-number arithmetic remains unchanged.

The step-count firmware starts with position unknown. SET SLOT n validates the requested range 1 through 8, refuses while auger or disk motion is active, stores the current slot, marks position known, and enables the disk driver. It does not rotate to a sensor or discover the physical location; the operator must already align the disk correctly before declaring the slot.

A requested movement is rejected when the reference is unknown. DISK STOP and DISK DISABLE stop motion and invalidate position as appropriate. That state handling prevents the program from continuing to treat an interrupted movement as a completed index. A later open/reset cycle also needs the known slot restored if the physical disk has not moved.

The later app includes text about a slot switch, an indent, and counterclockwise indexing, whereas the recovered firmware calculates bidirectional steps and contains no corresponding switch-based homing implementation. Those are different source states. I cannot merge them into one description of a validated final controller. The final matched firmware, switch wiring, and reference procedure are a specific remaining evidence gap.

For the step-count revision, a useful test record includes physical alignment of the initial slot, one commanded move, the actual hopper reached, and a return to the original reference. It should repeat around the full disk and after interrupted motion. Commanded pulse counts describe the intended motion; photographs or measured position show whether the installed disk followed it.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### timer_controller_later.ino · lines 59–75

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t DISK_SLOT_COUNT = 8;
const uint32_t DISK_MOTOR_FULL_STEPS_PER_REV = 200UL;
const uint32_t DISK_DRIVER_MICROSTEPS = 32UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR = 1UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR = 1UL;

const uint32_t DISK_STEP_CALCULATION_NUMERATOR =
    DISK_MOTOR_FULL_STEPS_PER_REV * DISK_DRIVER_MICROSTEPS *
    DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR;
const uint32_t DISK_STEP_CALCULATION_DENOMINATOR =
    DISK_SLOT_COUNT * DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR;
const uint32_t DISK_STEPS_PER_SLOT =
    DISK_STEP_CALCULATION_NUMERATOR / DISK_STEP_CALCULATION_DENOMINATOR;

const uint32_t DISK_STEP_FREQUENCY_HZ = 1000UL;
const uint16_t DISK_ENABLE_SETTLE_MS = 20;
const uint16_t DISK_DIRECTION_SETTLE_US = 20;
```

### timer_controller_later.ino · lines 776–795

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
  if (parseSlotArgument("SET SLOT ", requestedSlot)) {
    if (requestedSlot == 0) {
      Serial.println(F("ERR SLOT MUST BE 1..8"));
      return;
    }

    if (augerMode != AUGER_STOPPED || diskMoveActive) {
      Serial.println(F("ERR MOTION ACTIVE"));
      return;
    }

    diskCurrentSlot = requestedSlot;
    diskPositionKnown = true;
    setDiskDriverEnabled(true);
    Serial.print(F("OK DISK SLOT SET "));
    Serial.println(diskCurrentSlot);
    return;
  }

  requestedSlot = 0;
```

## Image sequence

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Result and handoff

The recovered step-count configuration uses 800 pulses per slot and requires an explicitly established physical reference. The later switch-based app description needs its matching firmware.

## Complete from your records

Confirm installed microstep switches/gearing, initial reference procedure, switch hardware if used, and final paired app/firmware versions.

[IMAGE PLACEHOLDER: Driver microstep settings, slot marks, and the physical alignment used before SET SLOT 1.]

[IMAGE PLACEHOLDER: Matching switch-based firmware and switch wiring if that was the final indexing method.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
