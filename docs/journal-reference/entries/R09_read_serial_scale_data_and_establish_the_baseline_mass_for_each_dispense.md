# R09 Read serial scale data and establish the baseline mass for each dispense

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J14

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Convert the balance's serial output into usable mass feedback while retaining enough timing information to detect stale readings.

## Design process

I connected the scale's RS232 port to the Raspberry Pi through a USB-to-serial adapter so the software could read mass during dispensing. The BOM lists a CableCreation adapter using a PL2303 chipset and a Bonvoisin balance advertised with a 0.001 g display resolution. The exact scale command format and serial settings still need to be added from the working program.

This changed the machine from controlling motion for a fixed amount of time to responding to a measured quantity. The controller could compare the requested mass with the mass already dispensed and stop or slow the auger as it approached the target. However, display resolution is not the same as verified measurement accuracy, and a serial reading can arrive after the physical powder has already landed.

The early notes describe the blue USB port as continuously supplying information. More precisely, the data comes from the scale and its serial protocol through the adapter; the USB port's color does not create a special continuous measurement mode. I would include the actual message format and update interval in the journal so the scale integration is reproducible.

## Construction and implementation detail

The scale connected to the Pi through a USB-to-RS232 path. The documented controller defaults to /dev/ttyUSB0 at 9600 baud, while the Arduino command connection uses /dev/ttyACM0 at 115200 baud. These are separate devices and separate baud rates. The USB socket's color does not establish how scale updates work; the useful evidence is the device path, serial configuration, and actual received lines.

In the July controller, parse_weight() searches a scale line for the first signed decimal number and converts it to a float. Invalid lines return no reading. This makes the parser simple, but it assumes the first numeric field really is the mass and that the transmitted unit matches grams. To recreate the input reliably, the journal should include a raw line from the balance, its sign/unit/stability fields, and the parser result.

The scale reader runs in a background thread. It appends accepted values to a deque with a maximum length of eight, computes their mean, and records the time of the last valid update while holding a lock. The control loop reads that shared state rather than waiting on a serial line each time. That keeps serial I/O separate from control decisions, but averaging eight samples also means the displayed/control mass can lag behind a changing physical load.

Startup waits for at least five accepted readings, with a six-second timeout. The initial baseline routine samples the current averaged mass into another ten-value window and looks for a spread no larger than 0.003 g over a four-second interval. If it does not find that condition, it returns the latest value. This routine is an attempt at a stable starting mass, not a metrological proof of balance accuracy or ten independent balance transmissions.

The dispense amount is calculated as current mass minus the starting mass; remaining mass is requested target minus that difference. This allows a cup already on the scale to become the reference rather than assuming the raw balance reading starts at zero. The same distinction becomes important in a multi-ingredient recipe, where the next ingredient starts above the mass of earlier ingredients.

The July loop stops if no valid scale update has arrived for 2.50 seconds. A disconnected balance must not leave the auger running indefinitely on an old low reading. The recovered source therefore supplies a concrete stale-data behavior to document, while the actual unplugged-scale test and the original raw output still need evidence.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### motor_2026-07-21.py · lines 108–116

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def parse_weight(line: str) -> Optional[float]:
    """Extract the first signed decimal number from a scale line."""
    match = re.search(r"[-+]?\d*\.?\d+", line)
    if match is None:
        return None
    try:
        return float(match.group())
    except ValueError:
        return None
```

### motor_2026-07-21.py · lines 346–366

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def read_scale() -> None:
    global current_weight, last_scale_update

    while running:
        try:
            if scale_serial is None:
                return
            line = scale_serial.readline().decode(errors="ignore").strip()
            if not line:
                continue
            value = parse_weight(line)
            if value is None:
                continue
            with weight_lock:
                weight_buffer.append(value)
                current_weight = sum(weight_buffer) / len(weight_buffer)
                last_scale_update = time.monotonic()
        except Exception as exc:
            if running:
                print(f"Scale read warning: {exc}", flush=True)
            time.sleep(0.05)
```

### motor_2026-07-21.py · lines 390–401

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def get_stable_weight(timeout: float = 4.0, spread: float = 0.003) -> float:
    readings: deque[float] = deque(maxlen=10)
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        value = get_weight()
        readings.append(value)
        if len(readings) == readings.maxlen and max(readings) - min(readings) <= spread:
            return sum(readings) / len(readings)
        time.sleep(0.05)

    return get_weight()
```

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

The controller parsed serial mass data, averaged readings, captured a baseline, and rejected stale feedback. The parser and smoothing settings are source-code facts; scale calibration and update-rate measurements remain separate.

## Complete from your records

Add scale model/configuration, raw serial lines, observed update interval, unit handling, calibration checks, and an actual stale-data stop trial.

[IMAGE PLACEHOLDER: Terminal screenshot of raw balance messages beside parsed gram values.]

[IMAGE PLACEHOLDER: Plot or logged rows of scale readings after a known mass change and after disconnecting the balance.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
