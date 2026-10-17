# J13 The program ended. The motor kept moving.

*Milestone 2 | Retrospective build notes*

The slow rotation after motor_scale terminated was a problem I couldn't leave in place. The software had finished, but the feeder could still be adding powder. From the machine's point of view, the run wasn't actually over.

I rerouted EN to a Pi GPIO, which is the fix described in my M2 notes. Those notes call it electrical noise. I don't have a waveform showing the cause, so I can stand behind the symptom and wiring change without pretending the diagnosis went further than it did.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

That also pushed me to stop relying on one program exiting neatly. The July Python code explicitly sends STOP ALL during cleanup and handles termination signals. The firmware has a communication watchdog. Later, the app had its own cancellation work to do with the child process and positioning states.

It isn't exciting compared with adding a carousel, but this is the sort of behavior that can ruin an otherwise decent dispense. Every way out of a run needs attention, not only the one where the target is reached and everything cooperates.

## The stop paths in the code

Enable control provides a way to deactivate the driver as well as stop step commands. The July firmware uses LOW to enable, while the later integrated motor setup uses HIGH. Those are version-specific electrical assumptions: reversing the intended polarity could leave a driver active when software believes it is disabled.

The July Python shutdown function guards against repeated cleanup, sets its running state false, prints its shutdown action, sends STOP ALL through the Arduino client, waits briefly, closes connections, and exits. SIGINT and SIGTERM both call that path. This turns an ordinary process stop into an explicit motor-control action rather than assuming closing the terminal is enough.

The firmware adds another layer: it stops automatically if serial contact is absent for 2000 ms while motion is active. Python sends a heartbeat approximately every 0.50 s during continuous feeding. The intent is to stop if the Pi program disappears even when it can't deliver its normal shutdown command. That watchdog complements EN control; it doesn't prove that every wiring or power fault has been handled.

In the later app, cancellation sends stop commands, signals the child process, marks actuator position UNKNOWN, and invalidates the disk reference. If the child remains alive, the app escalates to a kill after a delay. This is a later coordination layer in addition to the initial GPIO change and firmware watchdog.

## More views

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Code for this revision

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

I ended up with several stop paths, each for a different failure or exit case. I still don't have measured shaft-stop times for all of them. The practical change was that stopping had become something the programs deliberately requested, instead of something I assumed would follow from closing them.

<details>
<summary>Notes added while reconstructing this entry</summary>

The early symptom was slow rotation after motor_scale terminated. I rerouted EN to a Pi GPIO as recorded in the M2 notes. Although those notes attribute the behavior to noise, no waveform or comparable measurement establishes the exact electrical mechanism. The observed unwanted motion and the enable-wiring change are the supported parts of the diagnosis.

The saved code shows normal cleanup, signal handling, and lost-communication stop routes. It doesn't contain a measured physical stop time for each case. I kept the distinction between sending a stop and observing the shaft stopped, especially because residual motion could add powder after apparent software completion.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
