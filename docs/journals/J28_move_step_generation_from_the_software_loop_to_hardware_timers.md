# J28 Move STEP generation from the software loop to hardware timers

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I revisited motor speed at the pulse-generation level after the mechanical drive upgrade. The early controller toggled STEP through software timing checks. As the main loop handled other work, generating the intended waveform became a separate question from whether the loaded motor could follow it.

I changed the later firmware to use hardware timers for the step outputs. Timer1 generated the auger waveform, while Timer2 handled the disk. This moved repeated output transitions away from ordinary loop timing and still allowed software to count finite motions and report their completion.

The change also affected wiring. Hardware output-compare channels use particular pins, so retaining an old pin map with the new timing code would not produce the intended system. I documented the timer equation, configured rates, pins, and enable behavior together. Those settings describe the program; they are not a measured maximum loaded speed.

## Technical detail

The M5 notes distinguish a basic pulse-generation version from a hardware-timer version. The early July firmware calculates halfPeriodMicros as 500000 divided by the current step rate and toggles STEP in software. That arrangement depends on how often the main loop returns to the timing check. Serial handling, acceleration updates, and other work compete with pulse timing.

The later firmware assigns auger STEP to pin 9, the AVR OC1A output, and uses Timer1 in CTC mode with prescaler 1. The output toggles on each compare match. The source's conversion is frequency = F_CPU divided by twice (OCR1A + 1). On a 16 MHz configuration, 20,000 pulses per second corresponds to OCR1A = 399. This is a calculated timer setting, not a measured maximum loaded motor speed.

Continuous auger motion starts at 2000 Hz and changes by 500 Hz on nominal 10 ms ramp updates. The timer-based settings use 20,000 Hz TURBO for both families, 2400 Hz FREE NORMAL, and 9000 Hz NONFREE NORMAL. These are later parameters and differ from the early July rates; they are not one speed configuration carried unchanged through the project.

Finite auger pulses enable the Timer1 compare interrupt and count two compare matches per requested step. When the count reaches zero, the interrupt disconnects the timer output and sets a completion flag. The main loop reports completion separately. Hardware creates the waveform while software retains a finite-motion boundary and command reporting.

The disk uses Timer2 and pin 11, OC2A, with a prescaler of 64 and its own compare-match count. Timer selection therefore changes the wiring: auger STEP moves from the early pin 2 to pin 9, and disk STEP uses pin 11. The later integrated drive also uses HIGH for enable and LOW for disable. These pin and polarity changes must accompany the firmware change.

Timer configuration establishes the intended electrical timing, while the motor and powder load determine whether the shaft follows it. The record contains no preserved waveform measurement paired with a loaded-speed series. The configured 20 kHz rate is therefore reported as a command setting, without assigning it the meaning of a demonstrated reliable mechanical limit.

## Archived implementation

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

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

Hardware timers provided a more regular timing source while preserving phase commands and bounded pulses. The optimization addressed how steps were generated, leaving motor torque and powder resistance as separate limits. Keeping the frequency calculation and pin map with the firmware made this revision more reproducible than describing it only as a faster controller.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R28_move_step_generation_from_the_software_loop_to_hardware_timers.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
