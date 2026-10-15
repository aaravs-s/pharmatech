# R29 Add driver-alarm handling and an interactive motor-speed test

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J43

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Make failures observable while testing rates without repeatedly recompiling the speed-test program.

## Design process

I added fault monitoring and an interactive way to set the test speed. The milestone notes describe a third controller version that recorded the speed associated with a driver-reported problem and allowed a new speed to be entered without rewriting and uploading the sketch each time.

This shortened the test cycle. I could change a command, observe the motor, and compare the behavior without making a new firmware build for every setting. Recording the commanded rate alongside a fault also made the test more informative than simply noticing that the motor stopped.

The journal should name the actual alarm signal and explain what the driver reports through it. A generic alarm does not necessarily distinguish a stall from overcurrent unless the hardware or status data provides that detail. I would include the real output from a test, the rate being commanded, and what action the controller took after detecting the fault.

## Construction and implementation detail

M5 notes describe a third speed-test version that accepts a typed speed and records the speed at which a driver fault occurs. That is more informative than increasing a constant until motion looks unreliable, because each failure can be associated with the requested operating point. The exact standalone interactive test source and its captured output have not been recovered.

The later production firmware does contain concrete fault paths. Auger alarm is pin 7 and disk alarm is pin 6. The auger alarm check reads LOW as a fault while the mechanism is running, stops auger motion, latches faulted state, and emits FAULT DRIVER ALARM. The source uses INPUT_PULLUP and notes that an unconnected alarm line reads HIGH, so an unused input does not establish functional driver fault detection.

RESET FAULT clears the latched fault states and stops the auger. STATUS reports the run mode, current frequency, target frequency, and OCR1A. The 2000 ms serial watchdog stops active auger motion if serial contact disappears. These are distinct mechanisms: driver alarm reports the driver signal, status describes configured motion, and watchdog detects lost controller communication.

A driver alarm should be recorded as the actual received alarm signal unless the driver documentation and test establish the cause. It may relate to a stall or another fault, but the code's generic message does not identify current, temperature, or position error individually. The journal therefore needs the installed driver's alarm behavior and polarity alongside the recorded test.

The test matrix should identify requested frequency, acceleration, microsteps, supply voltage, powder load, motion duration, and observed outcome. An unloaded free-running result is not interchangeable with a screw rotating through cornstarch. Likewise, a fault-free electrical pulse train does not prove a specific mass rate. Those distinctions make the speed investigation useful to another builder.

The available source supports alarm latching and watchdog behavior in the production firmware, while the milestone text supports the separate interactive-test concept. I keep those evidence levels visible and leave a placeholder for the actual typed-speed transcript and fault-speed record. That preserves the design story without fabricating numerical limits.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

## Result and handoff

Fault handling is present in the recovered production firmware; an interactive speed-test revision is described by the notes but its source and measured limit log are still missing.

## Complete from your records

Recover interactive-test code, driver alarm documentation/wiring, typed commands, fault-speed readings, load conditions, and reset behavior.

[IMAGE PLACEHOLDER: Interactive test parser and a terminal run changing speed without recompilation.]

[IMAGE PLACEHOLDER: Actual fault-speed log and physical alarm wiring, followed by reset and restart verification.]

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
