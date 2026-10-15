# R26 Choose the shortest carousel route and wait for completed indexing

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J39

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Reduce unnecessary rotation while retaining a definite completion boundary before lowering the drive.

## Design process

I added logic for the rotary disk to move toward the target hopper by the shorter route rather than always turning in one direction. With eight stations, some transitions are much faster if the disk reverses direction.

For example, moving from slot 0 to slot 7 is one station in reverse instead of seven stations forward. A move of four stations has equal distances in both directions, so the controller needs a consistent tie rule. This is an explanatory example of the geometry; the actual indexing convention and tie behavior should be taken from the program.

The shorter-route calculation still needed to fit the mechanical sequence. The drive must be disengaged before rotating, and the disk must stop at the intended alignment before the drive lowers. Reducing travel would not help if direction reversal introduced play that prevented reliable engagement. I would show representative slot transitions and the real observed alignment at their endpoints.

## Construction and implementation detail

The step-count firmware calculates forward distance as (requested + 8 - current) modulo 8 and reverse distance as (current + 8 - requested) modulo 8. It chooses the smaller distance, with forward motion for a four-slot tie. This is a concrete implementation of the shortest-route note, rather than simply assuming the motor always turns in one direction.

For example, from slot 1 to slot 8, the forward distance is seven slots and the reverse distance is one, so the firmware requests one reverse slot. From slot 2 to slot 6, both distances are four, so it takes the documented forward tie. Requesting the current slot performs no index and immediately reports that slot while maintaining driver hold. These are derived examples of the code, not recorded physical tests.

startDiskMove() refuses indexing if the auger is moving, the disk is already busy, a disk alarm is latched, or the step calibration is not integral. It sets direction, enables the driver, allows a 20 ms enable-settling interval and a 20 microsecond direction-settling interval, then starts Timer2. The nominal disk frequency is 1000 pulses per second in the recovered configuration.

The number of timer compare events is twice the number of steps because the output toggles once high and once low for each full pulse. The interrupt decrements that count and disconnects the output when the move ends. Completion is then handled in the main loop, which updates the slot reference and emits DONE DISK SLOT n. That response separates an accepted command from a completed move.

The Pi-side recipe worker waits for a motion response and checks that the slot number in DONE DISK SLOT matches the requested target. It does not lower the actuator merely because an OK line says motion started. That distinction matters because the mechanical coupling must stay clear throughout indexing.

A complete journal needs both the derived route table and actual trials for wraparound, equal-distance routes, same-slot requests, and interrupted motion. The later switch/counterclockwise app description is a separate revision and may no longer use this bidirectional method. The record should keep the shortest-path implementation with the firmware that actually contains it.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### timer_controller_later.ino · lines 552–578

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void goToDiskSlot(uint8_t requestedSlot) {
  if (!diskPositionKnown) {
    Serial.println(F("ERR DISK POSITION UNKNOWN - SEND SET SLOT n"));
    return;
  }

  uint8_t forwardDistance =
      (requestedSlot + DISK_SLOT_COUNT - diskCurrentSlot) %
      DISK_SLOT_COUNT;
  uint8_t reverseDistance =
      (diskCurrentSlot + DISK_SLOT_COUNT - requestedSlot) %
      DISK_SLOT_COUNT;

  if (forwardDistance == 0) {
    setDiskDriverEnabled(true);
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
    return;
  }

  // For the four-slot tie, use the forward direction.
  if (forwardDistance <= reverseDistance) {
    startDiskMove(1, forwardDistance, requestedSlot);
  } else {
    startDiskMove(-1, reverseDistance, requestedSlot);
  }
}
```

### timer_controller_later.ino · lines 525–550

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateDiskCompletion() {
  if (!diskMoveFinished) {
    return;
  }

  noInterrupts();
  diskMoveFinished = false;
  interrupts();

  digitalWrite(DISK_STEP_PIN, LOW);

  if (diskPositionKnown && diskPendingTargetSlot >= 1 &&
      diskPendingTargetSlot <= DISK_SLOT_COUNT) {
    diskCurrentSlot = diskPendingTargetSlot;
  }

  diskPendingDirection = 0;
  diskPendingTargetSlot = 0;

  if (diskPositionKnown) {
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
  } else {
    Serial.println(F("DONE DISK SLOT UNKNOWN"));
  }
}
```

## Image sequence

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Result and handoff

The step-count revision implements bidirectional shortest routes and emits a checked completion response. Physical indexing trials and the final revision choice remain to be matched.

## Complete from your records

Add real route tests, slot accuracy, motion time, alarm/interrupt behavior, and whether the final machine retained bidirectional indexing.

[IMAGE PLACEHOLDER: Route-selection function during development, timer completion code, and final serial response from a real move.]

[IMAGE PLACEHOLDER: Physical wraparound, four-slot tie, and interrupted-index tests with before/after slot views.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
