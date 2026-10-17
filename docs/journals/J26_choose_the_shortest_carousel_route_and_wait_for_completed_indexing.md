# J26 One slot backward instead of seven forward

*Milestone 4 | Retrospective build notes*

Always rotating in one direction wastes a lot of movement near the numbering boundary. From slot 1 to slot 8, I only need one station in reverse, not seven forward. I added the shorter-route calculation to the step-count version.

The four-station case needed a tie rule, so the code chooses forward when both distances are equal. Requesting the current slot doesn't need a move at all. These are simple cases, but they're exactly the sort of details that get lost if I just write 'shortest path added.'

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

The more consequential part was waiting. An OK response says the command started; it doesn't mean the disk has stopped at the target. The Pi needed the destination in DONE DISK SLOT before lowering the drive.

The timer counts the move, then the main loop updates the slot and reports completion. I kept the examples below as code-derived behavior. I don't have a full physical alignment table for every wraparound, tie, and interrupted move.

## Route calculation and completion

The step-count firmware calculates forward distance as (requested + 8 - current) modulo 8 and reverse distance as (current + 8 - requested) modulo 8. It chooses the smaller distance, with forward motion for a four-slot tie. This is a concrete implementation of the shortest-route note, rather than simply assuming the motor always turns in one direction.

For example, from slot 1 to slot 8, the forward distance is seven slots and the reverse distance is one, so the firmware requests one reverse slot. From slot 2 to slot 6, both distances are four, so it takes the documented forward tie. Requesting the current slot performs no index and immediately reports that slot while maintaining driver hold. These are derived examples of the code, not recorded physical tests.

startDiskMove() refuses indexing if the auger is moving, the disk is already busy, a disk alarm is latched, or the step calibration isn't integral. It sets direction, enables the driver, allows a 20 ms enable-settling interval and a 20 microsecond direction-settling interval, then starts Timer2. The disk is configured for 1000 pulses per second in the recovered configuration.

The number of timer compare events is twice the number of steps because the output toggles once high and once low for each full pulse. The interrupt decrements that count and disconnects the output when the move ends. Completion is then handled in the main loop, which updates the slot reference and emits DONE DISK SLOT n. That response separates an accepted command from a completed move.

The Pi-side recipe worker waits for a motion response and checks that the slot number in DONE DISK SLOT matches the requested target. It doesn't lower the actuator merely because an OK line says motion started. That matters here because the mechanical coupling must stay clear throughout indexing.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

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

Less rotation was useful, but it couldn't come at the expense of lowering into a moving disk. The completion response mattered more to the shared-drive sequence than the time saved by taking the shorter route.

<details>
<summary>Notes added while reconstructing this entry</summary>

These formulas and responses document the bidirectional step-count revision. Later switch and counterclockwise descriptions belong to a different state of the app. The available record contains the routing implementation, but no complete physical trial set for wraparound, ties, same-slot requests, and interruption recovery.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
