# J09 The scale reading is behind the powder

*Milestone 2 | Retrospective build notes*

I connected the balance to the Pi through its RS232 output and a USB-to-serial adapter. Now the program could use what reached the cup instead of estimating mass from how long the motor ran. That was the feedback I needed, but it came with some awkward timing.

Powder could already be in the cup before the new mass appeared in the serial reading. Smoothing the readings could make them look calmer while adding more delay. So a clean number on screen wasn't automatically a current number.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

I used a starting baseline and calculated the increase from it. That handled the cup mass and gave me a sensible way to deal with later ingredients already sitting on the scale. I also kept the scale reader separate from the control loop, with a timestamp for the last valid update.

The other obvious bad case was a disconnected scale leaving an old low reading in memory. The auger couldn't be allowed to keep feeding against that forever. The July code has a stale-data timeout for that reason. I don't have a timed disconnect test for this version, but the stop path itself is in the source.

## Reading and using the mass

The controller defaults to /dev/ttyUSB0 at 9600 baud for the scale and /dev/ttyACM0 at 115200 baud for Arduino commands. These are separate serial devices with different roles. The mass data comes from the balance protocol through the RS232 adapter; it isn't a measurement mode created by the color of a USB socket.

In the July controller, parse_weight() finds the first signed decimal number in a received line and converts it to a float. Invalid lines produce no accepted reading. This simple parser assumes that the first numeric field is mass and the unit is grams. The raw balance message isn't preserved in the record, so stability and unit interpretation can't be inferred beyond the parser's assumptions.

The scale reader runs in a background thread. It appends accepted values to a deque with a maximum length of eight, computes their mean, and records the time of the last valid update while holding a lock. The control loop reads that shared state rather than waiting on a serial line each time. That keeps serial I/O separate from control decisions, but averaging eight samples also means the displayed/control mass can lag behind a changing physical load.

Startup waits for at least five accepted readings, with a six-second timeout. The initial baseline routine samples the current averaged mass into another ten-value window and looks for a spread no larger than 0.003 g over a four-second interval. If it doesn't find that condition, it returns the latest value. This routine is an attempt at a stable starting mass, not a metrological proof of balance accuracy or ten independent balance transmissions.

The dispense amount is calculated as current mass minus the starting mass; remaining mass is requested target minus that difference. This allows a cup already on the scale to become the reference rather than assuming the raw balance reading starts at zero. The same distinction becomes important in a multi-ingredient recipe, where the next ingredient starts above the mass of earlier ingredients.

The July control loop stops if 2.50 seconds pass without a valid scale update. This gives feedback validity a physical consequence: an old low mass can't remain a reason to feed indefinitely. The saved code establishes the timeout path, while no unplugged-scale timing measurement is available for that revision.

## Code for this revision

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

Getting serial data was a big step, but it didn't remove uncertainty. The controller still had to deal with delay, averaging, and invalid input. That is why the next change couldn't just be 'stop when the display equals the target.' Too much could happen between those readings.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
