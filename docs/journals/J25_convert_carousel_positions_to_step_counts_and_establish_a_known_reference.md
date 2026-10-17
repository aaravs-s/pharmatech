# J25 The controller needs to know which hopper is there

*Milestone 4 | Retrospective build notes*

Eight positions gives me 45 degrees per station, but the controller can't do much with that until it's tied to the driver configuration. The saved direct-drive setup uses 200 full steps and 32 microsteps: 6400 pulses per revolution, 800 per slot.

The integral count was useful. I didn't want rounding at each station gradually changing the commanded alignment. But having a clean calculation didn't make the starting slot known, and it didn't detect missed motion.

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

In the recovered step-count firmware, position starts UNKNOWN. The operator aligns a hopper and declares its slot with SET SLOT. That's a reference-setting operation, not automatic homing. It matters because a program can keep perfectly tidy counts from a wrong starting assumption.

There's still a version mismatch in the archive: later app wording mentions a switch and indent, while the recovered disk code uses bidirectional counted steps without that switch-homing implementation. I can explain each version, but I can't merge them into a final setup the source doesn't identify.

## Steps, slots, and UNKNOWN

The timer-based disk firmware specifies eight slots, 200 full steps per motor revolution, 32 microsteps, and a 1:1 motor-to-disk ratio. The calibration is therefore 200 times 32 divided by eight, or 800 step pulses per station and 6400 per revolution. This is the configuration actually declared in the saved file; the driver must physically use the matching microstep mode for the calculation to hold.

The geometry gives 45 degrees per slot, while the motor configuration gives electrical pulses per slot. They agree only if the gearing, microstep mode, direction, and physical reference are correct. Changing the driver microstep switch without updating the software would change disk travel even though the slot-number arithmetic remains unchanged.

The step-count firmware starts with position unknown. SET SLOT n validates the requested range 1 through 8, refuses while auger or disk motion is active, stores the current slot, marks position known, and enables the disk driver. It doesn't rotate to a sensor or discover the physical location; the operator must already align the disk correctly before declaring the slot.

A requested movement is rejected when the reference is unknown. DISK STOP and DISK DISABLE stop motion and invalidate position as appropriate. That state handling prevents the program from continuing to treat an interrupted movement as a completed index. A later open/reset cycle also needs the known slot restored if the physical disk has not moved.

The later app mentions a switch, an indent, and counterclockwise indexing. The recovered disk firmware instead uses bidirectional counted steps and no matching switch-homing implementation. These are different source states. The account therefore describes the SET SLOT reference procedure for the saved firmware, while the final matched switch-based configuration remains unidentified.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

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

For this firmware, 800 pulses means one intended station, starting from a position the operator has established. Interrupt a move and that position may no longer be trustworthy. Keeping UNKNOWN as a real state was more useful than pretending the last requested slot was where the disk must have ended up.

<details>
<summary>Notes added while reconstructing this entry</summary>

The pulse count defines intended travel, while a known physical starting alignment gives slot numbers their meaning. Repeated alignment around all eight stations and recovery after interruption are separate physical checks. No measured home-position error or full station-error series is preserved with this revision.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
