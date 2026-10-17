# J29 Add driver-alarm handling and an interactive motor-speed test

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I added an interactive speed-test workflow so I could enter a new requested speed without editing and uploading the program for every setting. The milestone notes describe recording the commanded speed associated with a driver-reported problem. That shortened the experiment cycle and made a fault more informative than an unexplained stop.

The later production firmware also contains explicit alarm handling. A fault can stop motion, latch a state, and produce a serial message. I kept those paths distinct from the communication watchdog and from ordinary status reporting, because each responds to different information.

A generic driver alarm did not identify the underlying cause by itself. I did not turn that signal into a specific overcurrent, temperature, or stall diagnosis without supporting status data. The standalone test transcript is not available in the source record, so this account documents the workflow and implemented fault paths without assigning a numerical failure-speed limit.

## Technical detail

The M5 speed-test workflow accepted a typed speed and recorded the requested rate associated with a driver fault. This reduced recompilation between experiments. The standalone test source and captured output are not preserved in the available set, so no numerical fault-speed threshold is reconstructed from that description.

The later production firmware does contain concrete fault paths. Auger alarm is pin 7 and disk alarm is pin 6. The auger alarm check reads LOW as a fault while the mechanism is running, stops auger motion, latches faulted state, and emits FAULT DRIVER ALARM. The source uses INPUT_PULLUP and notes that an unconnected alarm line reads HIGH, so an unused input does not establish functional driver fault detection.

RESET FAULT clears the latched fault states and stops the auger. STATUS reports the run mode, current frequency, target frequency, and OCR1A. The 2000 ms serial watchdog stops active auger motion if serial contact disappears. These are distinct mechanisms: driver alarm reports the driver signal, status describes configured motion, and watchdog detects lost controller communication.

FAULT DRIVER ALARM identifies the received fault signal, rather than a detailed cause. Without the installed driver's corresponding status information, it does not separately diagnose temperature, current, or position error. The active-LOW interpretation in the saved source is a wiring assumption tied to that revision.

Requested frequency, microsteps, acceleration, supply, and powder load all affect how a speed test is interpreted. An unloaded shaft test and an auger moving cornstarch are different operating conditions. I did not infer a grams-per-second rate or universal speed ceiling from the presence of a regular timer output.

Alarm latching, fault reset, status output, and the watchdog are directly visible in the later firmware. The milestone notes separately describe the interactive test version. Together they document a more observable development process, while the missing raw speed trials limit quantitative conclusions.

## Archived implementation

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

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

## Outcome and reflection

The controller became easier to investigate because requested speed, reported state, and alarm handling had explicit roles. Fault latching and reset behavior are present in the saved firmware. The milestone record supports the interactive test version, while the absence of its raw transcript limits the numerical conclusions I can draw from it.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
