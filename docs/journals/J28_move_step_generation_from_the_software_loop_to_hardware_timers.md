# J28 The pulse generator was another speed limit

*Milestone 5 | Retrospective build notes*

After changing the drive hardware, I still had to look at what the Arduino was actually asking it to do. The early version toggled STEP in software. The main loop also had commands and timing work to handle, so pulse generation could become a bottleneck of its own.

I moved the later version to hardware timers. Timer1 handled the auger and Timer2 handled the disk. That let the hardware generate the repeated transitions while software still counted finite motions and reported when they ended.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

The pin change was part of the work, not a footnote. OC1A means the auger STEP output is on pin 9 in this setup, and the disk uses pin 11. Keeping the earlier wiring while loading this firmware would defeat the whole change.

I kept the timer calculation with the configured rates below. It tells me the intended electrical waveform. It doesn't prove the loaded motor can follow every pulse at 20 kHz. Getting the timing source out of the busy loop was one problem; getting the mechanism through resistant powder was still another.

## Timers, pins, and rates

The M5 notes distinguish a basic pulse-generation version from a hardware-timer version. The early July firmware calculates halfPeriodMicros as 500000 divided by the current step rate and toggles STEP in software. That arrangement depends on how often the main loop returns to the timing check. Serial handling, acceleration updates, and other work compete with pulse timing.

The later firmware assigns auger STEP to pin 9, the AVR OC1A output, and uses Timer1 in CTC mode with prescaler 1. The output toggles on each compare match. The source's conversion is frequency = F_CPU divided by twice (OCR1A + 1). On a 16 MHz configuration, 20,000 pulses per second corresponds to OCR1A = 399. This is a calculated timer setting, not a measured maximum loaded motor speed.

Continuous auger motion starts at 2000 Hz and changes by 500 Hz on nominal 10 ms ramp updates. The timer-based settings use 20,000 Hz TURBO for both families, 2400 Hz FREE NORMAL, and 9000 Hz NONFREE NORMAL. These are later parameters and differ from the early July rates; they aren't one speed configuration carried unchanged through the project.

Finite auger pulses enable the Timer1 compare interrupt and count two compare matches per requested step. When the count reaches zero, the interrupt disconnects the timer output and sets a completion flag. The main loop reports completion separately. Hardware creates the waveform while software retains a defined end to the motion and command reporting.

The disk uses Timer2 and pin 11, OC2A, with a prescaler of 64 and its own compare-match count. Timer selection therefore changes the wiring: auger STEP moves from the early pin 2 to pin 9, and disk STEP uses pin 11. The later integrated drive also uses HIGH for enable and LOW for disable. These pin and polarity changes must accompany the firmware change.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 175–192

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
uint16_t frequencyToOcr(uint32_t frequencyHz) {
  if (frequencyHz < 123) {
    frequencyHz = 123;
  }

  // Timer1 CTC, prescaler = 1, OC1A toggles on every compare match.
  // STEP frequency = F_CPU / (2 * (OCR1A + 1)).
  uint32_t ocr = (F_CPU / (2UL * frequencyHz)) - 1UL;

  if (ocr > 65535UL) {
    ocr = 65535UL;
  }
  if (ocr < 1UL) {
    ocr = 1UL;
  }

  return (uint16_t)ocr;
}
```

### timer_controller_later.ino · lines 303–315

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
ISR(TIMER1_COMPA_vect) {
  if (augerMode != AUGER_PULSE || pulseCompareMatchesRemaining == 0) {
    return;
  }

  pulseCompareMatchesRemaining--;

  if (pulseCompareMatchesRemaining == 0) {
    TCCR1A &= ~_BV(COM1A0);
    TIMSK1 &= ~_BV(OCIE1A);
    pulseFinishedFlag = true;
  }
}
```

### timer_controller_later.ino · lines 317–354

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateContinuousRamp() {
  if (augerMode != AUGER_CONTINUOUS) {
    return;
  }

  uint32_t now = millis();
  if ((uint32_t)(now - lastRampUpdateMs) < RAMP_UPDATE_MS) {
    return;
  }
  lastRampUpdateMs = now;

  if (currentContinuousHz == targetContinuousHz) {
    return;
  }

  if (currentContinuousHz < targetContinuousHz) {
    uint32_t next = currentContinuousHz + RAMP_STEP_HZ;
    if (next > targetContinuousHz) {
      next = targetContinuousHz;
    }
    currentContinuousHz = next;
  } else {
    if (currentContinuousHz > RAMP_STEP_HZ) {
      uint32_t next = currentContinuousHz - RAMP_STEP_HZ;
      if (next < targetContinuousHz) {
        next = targetContinuousHz;
      }
      currentContinuousHz = next;
    } else {
      currentContinuousHz = targetContinuousHz;
    }
  }

  noInterrupts();
  setTimerFrequency(currentContinuousHz);
  TCNT1 = 0;
  interrupts();
}
```

This was a more concrete improvement than just raising the requested speed again. I had changed how the waveform was produced. A measured pulse trace paired with a loaded run would be the next way to check both halves of that change; that paired measurement isn't in the saved record.

<details>
<summary>Notes added while reconstructing this entry</summary>

Timer configuration establishes the intended electrical timing, while the motor and powder load determine whether the shaft follows it. The record contains no preserved waveform measurement paired with a loaded-speed series. The configured 20 kHz rate is therefore reported as a command setting, without assigning it the meaning of a demonstrated reliable mechanical limit.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R28_move_step_generation_from_the_software_loop_to_hardware_timers.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
