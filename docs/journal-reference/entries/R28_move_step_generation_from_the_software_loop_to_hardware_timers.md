# R28 Move STEP generation from the software loop to hardware timers

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J41, J42

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Remove pulse-generation timing from the busy main loop while preserving phase commands and finite pulse counts.

## Design process

I investigated the motor-speed limit at the pulse-generation level. The milestone notes describe an early version using basic Arduino commands to generate step pulses, where the software itself became a bottleneck as the requested speed increased.

The repository also contains a simple AccelStepper runSpeed test, but it is not enough to reconstruct all three controller versions mentioned in the milestone. I would use it as a small baseline example and add the actual early pulse-generation code if it is available. Library polling, digital output overhead, delays, and other work in the loop can affect pulse timing, but the notes do not identify a measured contribution for each one.

The key question was whether the motor was being commanded with the intended pulse rate. I needed to separate a limit in the code from a limit in the motor and loaded mechanism. This made a hardware-timer approach worth trying before drawing conclusions about the maximum usable mechanical speed.

I changed the controller to use a hardware timer for step-pulse generation. Instead of producing every transition through the main software loop, the timer could generate a regular output while the program handled commands and other logic.

The milestone notes describe this as removing the earlier software slowdown and allowing the motor's behavior to be tested at higher requested rates. Earlier project discussion includes a Timer1-based Arduino variant, but the repository inspected for this pack does not contain that final code. I therefore need to add the actual board, timer mode, prescaler, output pin, and frequency calculation to this entry.

Using a timer does not remove the motor's torque limit or guarantee that every commanded step is completed. It improves the timing source. The result should be demonstrated with a pulse-rate check and then a mechanical test under the intended load. That distinction makes the speed optimization more technically useful than saying the motor became faster because the code was rewritten.

## Construction and implementation detail

The M5 notes distinguish a basic pulse-generation version from a hardware-timer version. The early July firmware calculates halfPeriodMicros as 500000 divided by the current step rate and toggles STEP in software. That arrangement depends on how often the main loop returns to the timing check. Serial handling, acceleration updates, and other work compete with pulse timing.

The later firmware assigns auger STEP to pin 9, the AVR OC1A output, and uses Timer1 in CTC mode with prescaler 1. The output toggles on each compare match. The source's conversion is frequency = F_CPU divided by twice (OCR1A + 1). On a 16 MHz configuration, 20,000 pulses per second corresponds to OCR1A = 399. This is a calculated timer setting, not a measured maximum loaded motor speed.

Continuous motion starts at 2000 Hz and changes in 500 Hz increments on nominal 10 ms ramp updates. The recovered settings use 20,000 Hz TURBO for both families, 2400 Hz FREE NORMAL, and 9000 Hz NONFREE NORMAL. Those differ substantially from the early July settings. A journal should retain each version's values instead of describing all of them as a single final speed.

Finite auger pulses enable the Timer1 compare interrupt and count two compare matches per requested step. When the count reaches zero, the interrupt disconnects the timer output and sets a completion flag. The main loop reports completion separately. Hardware creates the waveform while software retains a finite-motion boundary and command reporting.

The disk uses Timer2 and pin 11, OC2A, with a prescaler of 64 and its own compare-match count. Timer selection therefore changes the wiring: auger STEP moves from the early pin 2 to pin 9, and disk STEP uses pin 11. The later integrated drive also uses HIGH for enable and LOW for disable. These pin and polarity changes must accompany the firmware change.

The useful verification is a measured STEP waveform and actual loaded shaft behavior at each tested rate. The source explains how the waveform is generated, but an oscilloscope/logic-analyzer trace and a successful powder run would establish that the timing and mechanical load worked together. The journal must not turn a configured 20 kHz value into a demonstrated reliable speed without that test.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Result and handoff

The later firmware generates auger and disk waveforms through AVR timers and counts finite pulses in interrupts. The configured frequencies are documented separately from measured motor limits.

## Complete from your records

Add board clock, timer waveform measurements, loaded speed trials, exact pin/polarity wiring change, and timer-version date.

[IMAGE PLACEHOLDER: Software-toggle timing function, timer configuration/ISR during development, and final pin map.]

[IMAGE PLACEHOLDER: Measured STEP waveform at selected speeds and the corresponding loaded shaft/powder behavior.]

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
