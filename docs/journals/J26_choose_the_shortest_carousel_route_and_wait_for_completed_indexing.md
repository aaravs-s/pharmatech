# J26 Choose the shortest carousel route and wait for completed indexing

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I added shortest-route selection so the carousel could reverse rather than make nearly a full revolution to reach a nearby hopper across the slot-number boundary. The step-count firmware compares forward and reverse distances and uses a consistent forward choice for a four-station tie.

Reducing travel did not change the required mechanical order. The drive had to stay clear throughout the index, and the next action had to wait for completion. An accepted command was therefore not enough information for the Pi to lower the actuator.

I used separate command and completion responses, including the destination slot in the completion message. The code-derived examples below explain wraparound and tie behavior. They are calculations of what this revision requests, rather than a substituted set of measured physical alignment trials.

## Technical detail

The step-count firmware calculates forward distance as (requested + 8 - current) modulo 8 and reverse distance as (current + 8 - requested) modulo 8. It chooses the smaller distance, with forward motion for a four-slot tie. This is a concrete implementation of the shortest-route note, rather than simply assuming the motor always turns in one direction.

For example, from slot 1 to slot 8, the forward distance is seven slots and the reverse distance is one, so the firmware requests one reverse slot. From slot 2 to slot 6, both distances are four, so it takes the documented forward tie. Requesting the current slot performs no index and immediately reports that slot while maintaining driver hold. These are derived examples of the code, not recorded physical tests.

startDiskMove() refuses indexing if the auger is moving, the disk is already busy, a disk alarm is latched, or the step calibration is not integral. It sets direction, enables the driver, allows a 20 ms enable-settling interval and a 20 microsecond direction-settling interval, then starts Timer2. The nominal disk frequency is 1000 pulses per second in the recovered configuration.

The number of timer compare events is twice the number of steps because the output toggles once high and once low for each full pulse. The interrupt decrements that count and disconnects the output when the move ends. Completion is then handled in the main loop, which updates the slot reference and emits DONE DISK SLOT n. That response separates an accepted command from a completed move.

The Pi-side recipe worker waits for a motion response and checks that the slot number in DONE DISK SLOT matches the requested target. It does not lower the actuator merely because an OK line says motion started. That distinction matters because the mechanical coupling must stay clear throughout indexing.

These formulas and responses document the bidirectional step-count revision. Later switch and counterclockwise descriptions belong to a different state of the app. The available record contains the routing implementation, but no complete physical trial set for wraparound, ties, same-slot requests, and interruption recovery.

## Archived implementation

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

## Process images

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The routing logic reduced unnecessary commanded travel while preserving a clear completion boundary. The more significant integration detail was waiting for the correct DONE response before lowering the drive. Shorter rotation helped efficiency, but mechanical endpoint accuracy still depended on the reference, calibration, and installed disk following the motion.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
