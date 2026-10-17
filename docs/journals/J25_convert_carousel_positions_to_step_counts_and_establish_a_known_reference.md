# J25 Convert carousel positions to step counts and establish a known reference

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I translated the carousel's eight equal positions into motor commands. Geometrically, adjacent stations are 45 degrees apart. Electrically, the corresponding pulse count depends on full steps, microsteps, and any motor-to-disk transmission ratio.

The saved step-count firmware uses 200 full steps per revolution, 32 microsteps, and direct drive. That gives 6400 pulses per disk revolution and 800 per station. An integral station count avoids rounding accumulation, but it still assumes that the installed driver settings match the program and that the disk follows the commanded motion.

I also separated a known reference from the ability to move between slots. The recovered firmware starts with position unknown and requires the operator to declare an aligned slot. Later application text describes a switch and detent arrangement. Because those are different source states, I documented the manual reference behavior actually present in the step-count code rather than combining them into an automatic homing claim.

## Technical detail

The timer-based disk firmware specifies eight slots, 200 full steps per motor revolution, 32 microsteps, and a 1:1 motor-to-disk ratio. The calibration is therefore 200 times 32 divided by eight, or 800 step pulses per station and 6400 per revolution. This is the configuration actually declared in the saved file; the driver must physically use the matching microstep mode for the calculation to hold.

The geometry gives 45 degrees per slot, while the motor configuration gives electrical pulses per slot. They agree only if the gearing, microstep mode, direction, and physical reference are correct. Changing the driver microstep switch without updating the software would change disk travel even though the slot-number arithmetic remains unchanged.

The step-count firmware starts with position unknown. SET SLOT n validates the requested range 1 through 8, refuses while auger or disk motion is active, stores the current slot, marks position known, and enables the disk driver. It does not rotate to a sensor or discover the physical location; the operator must already align the disk correctly before declaring the slot.

A requested movement is rejected when the reference is unknown. DISK STOP and DISK DISABLE stop motion and invalidate position as appropriate. That state handling prevents the program from continuing to treat an interrupted movement as a completed index. A later open/reset cycle also needs the known slot restored if the physical disk has not moved.

The later app mentions a switch, an indent, and counterclockwise indexing. The recovered disk firmware instead uses bidirectional counted steps and no matching switch-homing implementation. These are different source states. The account therefore describes the SET SLOT reference procedure for the saved firmware, while the final matched switch-based configuration remains unidentified.

The pulse count defines intended travel, while a known physical starting alignment gives slot numbers their meaning. Repeated alignment around all eight stations and recovery after interruption are separate physical checks. No measured home-position error or full station-error series is preserved with this revision.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

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

## Process images

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

Slot motion became an explicit combination of geometry, pulse calibration, and a known starting reference. The recovered code also invalidates position after interrupted motion instead of trusting an unfinished index. The unresolved switch-based versus step-count revision remains a configuration limitation, while the 800-pulse station calculation is fully specified for the archived direct-drive setup.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
