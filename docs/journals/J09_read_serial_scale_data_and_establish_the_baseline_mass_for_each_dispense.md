# J09 Read serial scale data and establish the baseline mass for each dispense

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I connected the balance's RS232 output to the Pi through a USB-to-serial adapter. The BOM lists a PL2303-based CableCreation adapter and a Bonvoisin balance advertised with a 0.001 g display resolution. The useful change was access to mass readings during motion, rather than relying on elapsed motor time as a substitute for quantity.

The controller needed a clear definition of newly dispensed mass. I used a starting baseline and calculated the increase from that value, allowing the receiving cup to remain on the scale. This also provided the right conceptual model for later recipes, where earlier ingredients would already be in the container.

Reading a number was not enough. The balance could update after powder had landed, averaging could add delay, and disconnected serial hardware could leave an old value in memory. I separated the reader from the control loop, kept a timestamp for accepted readings, and included a stale-data stop condition. The archived implementation makes those choices explicit.

## Technical detail

The controller defaults to /dev/ttyUSB0 at 9600 baud for the scale and /dev/ttyACM0 at 115200 baud for Arduino commands. These are separate serial devices with different roles. The mass data comes from the balance protocol through the RS232 adapter; it is not a measurement mode created by the color of a USB socket.

In the July controller, parse_weight() finds the first signed decimal number in a received line and converts it to a float. Invalid lines produce no accepted reading. This simple parser assumes that the first numeric field is mass and the unit is grams. The raw balance message is not preserved in the record, so stability and unit interpretation cannot be inferred beyond the parser's assumptions.

The scale reader runs in a background thread. It appends accepted values to a deque with a maximum length of eight, computes their mean, and records the time of the last valid update while holding a lock. The control loop reads that shared state rather than waiting on a serial line each time. That keeps serial I/O separate from control decisions, but averaging eight samples also means the displayed/control mass can lag behind a changing physical load.

Startup waits for at least five accepted readings, with a six-second timeout. The initial baseline routine samples the current averaged mass into another ten-value window and looks for a spread no larger than 0.003 g over a four-second interval. If it does not find that condition, it returns the latest value. This routine is an attempt at a stable starting mass, not a metrological proof of balance accuracy or ten independent balance transmissions.

The dispense amount is calculated as current mass minus the starting mass; remaining mass is requested target minus that difference. This allows a cup already on the scale to become the reference rather than assuming the raw balance reading starts at zero. The same distinction becomes important in a multi-ingredient recipe, where the next ingredient starts above the mass of earlier ingredients.

The July control loop stops if 2.50 seconds pass without a valid scale update. This gives feedback validity a physical consequence: an old low mass cannot remain a reason to feed indefinitely. The saved code establishes the timeout path, while no unplugged-scale timing measurement is available for that revision.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

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

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The scale connection supplied feedback tied to the result of feeding rather than only the command sent to the motor. The main lesson was that feedback has timing and validity requirements: a smooth mass display can still be delayed, and an old reading must not keep the auger running. Those constraints shaped the phased controller that followed.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
