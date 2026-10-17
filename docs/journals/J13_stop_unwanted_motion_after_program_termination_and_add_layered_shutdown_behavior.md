# J13 Stop unwanted motion after program termination and add layered shutdown behavior

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I observed slow motor motion after the motor-and-scale program terminated. That meant ending the software task was not consistently ending the physical feeding action. I rerouted the driver's enable connection to a Pi GPIO as the response recorded in the milestone notes.

The notes suspected electrical noise, but I did not have a waveform measurement establishing that cause. The observation I could support was the unwanted motion and the change to enable control. That was enough to make shutdown a design requirement rather than an assumption about what closing a program would do.

As the controller developed, I added explicit stop commands, cleanup on process termination, and a firmware communication watchdog. The later app also handled cancellation across its child process and positioning state. These were successive layers with different responsibilities, rather than one wiring change that guaranteed every possible fault was covered.

## Technical detail

The early symptom was slow rotation after motor_scale terminated. I rerouted EN to a Pi GPIO as recorded in the M2 notes. Although those notes attribute the behavior to noise, no waveform or comparable measurement establishes the exact electrical mechanism. The observed unwanted motion and the enable-wiring change are the supported parts of the diagnosis.

Enable control provides a way to deactivate the driver as well as stop step commands. The July firmware uses LOW to enable, while the later integrated motor setup uses HIGH. Those are version-specific electrical assumptions: reversing the intended polarity could leave a driver active when software believes it is disabled.

The July Python shutdown function guards against repeated cleanup, sets its running state false, prints its shutdown action, sends STOP ALL through the Arduino client, waits briefly, closes connections, and exits. SIGINT and SIGTERM both call that path. This turns an ordinary process stop into an explicit motor-control action rather than assuming closing the terminal is enough.

The firmware adds another layer: it stops automatically if serial contact is absent for 2000 ms while motion is active. Python sends a heartbeat approximately every 0.50 s during continuous feeding. The intent is to stop if the Pi program disappears even when it cannot deliver its normal shutdown command. That watchdog complements EN control; it does not prove that every wiring or power fault has been handled.

In the later app, cancellation sends stop commands, signals the child process, marks actuator position UNKNOWN, and invalidates the disk reference. If the child remains alive, the app escalates to a kill after a delay. This is a later coordination layer in addition to the initial GPIO change and firmware watchdog.

The saved code shows normal cleanup, signal handling, and lost-communication stop routes. It does not contain a measured physical stop time for each case. I kept the distinction between sending a stop and observing the shaft stopped, especially because residual motion could add powder after apparent software completion.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

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

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Outcome and reflection

Stopping became an explicit part of the control protocol. Enable handling, Python cleanup, heartbeat loss, and later application cancellation each addressed a different way an operation could end. The remaining distinction was between code taking a stop path and a measured physical stop; the saved files establish the former without supplying timing measurements for every termination case.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
