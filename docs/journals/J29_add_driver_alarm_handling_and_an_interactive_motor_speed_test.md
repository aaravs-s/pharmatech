# J29 Changing speed without uploading another sketch

*Milestone 5 | Retrospective build notes*

Recompiling and uploading for every new speed setting was an unnecessary part of the test cycle. I added an interactive speed-test workflow so I could type a rate, observe the response, and try another. The M5 notes describe recording the commanded speed associated with a driver fault too.

That made a stopped motor more informative. Instead of only noticing something had gone wrong, there was a requested operating point to connect to it. I don't have the standalone transcript, though, so there isn't a failure-speed number I can honestly recover from this account.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The later production firmware has explicit alarm paths: stop motion, latch the fault, report it. Status and the communication watchdog do different jobs. I wanted to keep those distinctions because 'fault handling' can hide quite a few unrelated behaviors.

The alarm message itself stays generic. It doesn't tell me whether the cause was current, temperature, or position error without more information from the driver. I shouldn't turn a useful fault signal into a more detailed diagnosis than it actually provides.

## Alarm and watchdog behavior

The later production firmware does contain concrete fault paths. Auger alarm is pin 7 and disk alarm is pin 6. The auger alarm check reads LOW as a fault while the mechanism is running, stops auger motion, latches faulted state, and emits FAULT DRIVER ALARM. The source uses INPUT_PULLUP and notes that an unconnected alarm line reads HIGH, so an unused input doesn't establish functional driver fault detection.

RESET FAULT clears the latched fault states and stops the auger. STATUS reports the run mode, current frequency, target frequency, and OCR1A. The 2000 ms serial watchdog stops active auger motion if serial contact disappears. These are distinct mechanisms: driver alarm reports the driver signal, status describes configured motion, and watchdog detects lost controller communication.

FAULT DRIVER ALARM identifies the received fault signal, rather than a detailed cause. Without the installed driver's corresponding status information, it doesn't separately diagnose temperature, current, or position error. The active-LOW interpretation in the saved source is a wiring assumption tied to that revision.

Requested frequency, microsteps, acceleration, supply, and powder load all affect how a speed test is interpreted. An unloaded shaft test and an auger moving cornstarch are different operating conditions. I didn't infer a grams-per-second rate or universal speed ceiling from the presence of a regular timer output.

## More views

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 662–674

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void checkAlarm() {
  if (augerMode == AUGER_STOPPED || faulted) {
    return;
  }

  // With nothing connected, INPUT_PULLUP reads HIGH and will not fault.
  // Confirm your driver's ALM polarity before wiring this input.
  if (digitalRead(AUGER_ALM_PIN) == LOW) {
    stopAugerImmediate(false);
    faulted = true;
    Serial.println(F("FAULT DRIVER ALARM"));
  }
}
```

### timer_controller_later.ino · lines 635–660

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void printStatus() {
  Serial.print(F("STATUS MODE="));

  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(F("CONTINUOUS"));
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(F("PULSE"));
  } else {
    Serial.print(F("STOPPED"));
  }

  Serial.print(F(" CURRENT_HZ="));
  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(currentContinuousHz);
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(activePulseHz);
  } else {
    Serial.print(0);
  }

  Serial.print(F(" TARGET_HZ="));
  Serial.print(targetContinuousHz);

  Serial.print(F(" OCR1A="));
  Serial.println(OCR1A);
}
```

### timer_controller_later.ino · lines 676–685

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateWatchdog() {
  if (augerMode == AUGER_STOPPED) {
    return;
  }

  if ((uint32_t)(millis() - lastSerialContactMs) > SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false);
    Serial.println(F("FAULT WATCHDOG"));
  }
}
```

The testing workflow became easier to adjust, and the controller had clearer ways to expose its state. The numerical speed limit is still missing from the archive. What I can keep is the method and the fault logic, without pretending a source-code setting was a measured ceiling.

<details>
<summary>Notes added while reconstructing this entry</summary>

The M5 speed-test workflow accepted a typed speed and recorded the requested rate associated with a driver fault. This reduced recompilation between experiments. The standalone test source and captured output aren't preserved in the available set, so no numerical fault-speed threshold is reconstructed from that description.

Alarm latching, fault reset, status output, and the watchdog are directly visible in the later firmware. The milestone notes separately describe the interactive test version. Together they document a more observable development process, while the missing raw speed trials limit quantitative conclusions.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
