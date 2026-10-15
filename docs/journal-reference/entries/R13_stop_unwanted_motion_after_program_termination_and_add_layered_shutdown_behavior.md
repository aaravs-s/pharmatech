# R13 Stop unwanted motion after program termination and add layered shutdown behavior

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J19

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Ensure that terminating the dispensing program also stops the physical feeder, including when serial feedback disappears.

## Design process

I observed that the motor could continue spinning slowly after the motor-and-scale program terminated. That was a problem because completing a software operation should leave the hardware stopped rather than allowing additional powder to enter the container.

I troubleshot the enable connection and rerouted EN to a Raspberry Pi GPIO pin. The milestone notes report that change as the response to the unwanted motion. They also mention electrical noise, but the notes do not contain measurements that prove noise was the root cause. In the journal, I would distinguish the observed behavior from the suspected explanation.

The useful implementation detail is the actual state of the driver before, during, and after a run. That includes the enable polarity, any pull-up or pull-down arrangement, and what happens when the program exits unexpectedly. The entry should explain the wiring change and the specific stop test used to check it, without inventing an oscilloscope diagnosis that was not recorded.

## Construction and implementation detail

The M2 notes describe the motor continuing to rotate slowly after motor_scale terminated. They attribute the problem to electrical noise and record rerouting EN to a Pi GPIO as the fix. The observed symptom and wiring change belong in the journal; the notes do not include an oscilloscope trace or other measurement proving the exact noise mechanism.

An enable connection gives software a way to deactivate the driver in addition to stopping step commands. Its polarity must match the installed driver. The July firmware's LOW-enabled configuration differs from the later integrated motor's HIGH-enabled configuration. Applying the wrong assumption could keep the driver active when the program believes it has disabled it, so the pin map and polarity should be shown beside the exact wiring revision.

The July Python shutdown function guards against repeated cleanup, sets its running state false, prints its shutdown action, sends STOP ALL through the Arduino client, waits briefly, closes connections, and exits. SIGINT and SIGTERM both call that path. This turns an ordinary process stop into an explicit motor-control action rather than assuming closing the terminal is enough.

The firmware adds another layer: it stops automatically if serial contact is absent for 2000 ms while motion is active. Python sends a heartbeat approximately every 0.50 s during continuous feeding. The intent is to stop if the Pi program disappears even when it cannot deliver its normal shutdown command. That watchdog complements EN control; it does not prove that every wiring or power fault has been handled.

The later app also separates user cancellation from completion. It requests stop commands, signals a running child process, marks actuator position UNKNOWN, and invalidates the disk reference. If the process remains alive, it escalates to a kill after a delay. That later sequence should be logged where it was developed rather than attributed to the first GPIO fix.

The relevant physical verification is the same for each layer: observe actual motion stopping after normal completion, a user stop, application termination, and lost communication. A program message alone cannot establish that the shaft stopped. The available code explains the implemented routes; a video or logged stop test would connect them to the installed hardware.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### motor_2026-07-21.py · lines 409–430

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def shutdown(exit_code: int = 0) -> None:
    global running, shutdown_started

    if shutdown_started:
        return
    shutdown_started = True
    running = False

    print("SHUTDOWN -> sending STOP ALL", flush=True)

    if arduino is not None:
        arduino.emergency_stop()
        time.sleep(0.05)
        arduino.close()

    if scale_serial is not None:
        try:
            scale_serial.close()
        except Exception:
            pass

    raise SystemExit(exit_code)
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

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Result and handoff

The initial EN wiring change addressed the unwanted-motion observation, and later software added explicit shutdown commands, signals, and a serial watchdog.

## Complete from your records

Add before/after wiring, driver polarity, timing of actual shaft stop, and observed behavior for normal exit, Ctrl-C, lost serial, and user cancellation.

[IMAGE PLACEHOLDER: EN wiring before and after rerouting, with the correct driver-active level labeled.]

[IMAGE PLACEHOLDER: Stop-test video or trace showing the physical shaft and corresponding shutdown/watchdog message.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
