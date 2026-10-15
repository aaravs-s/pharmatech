# R17 Replace the barcode plan with selectable profiles and run the doser from the Pi

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J24, J25

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Make the single-doser workflow self-contained and reduce configuration work for the eight test powders.

## Design process

I considered using a barcode scanner to identify powder containers and retrieve their behavior from a database. That would have linked each powder to a more specific control profile, but it added another integration step and a larger set of information to maintain.

As I tested the eight materials, I found enough similarity in their feeding behavior to simplify the control setup into free-flowing and non-free-flowing profiles. The notes describe abandoning the scanner-and-database direction because the simpler categories were more practical for this prototype. The BOM still lists a scanner, which records that it was considered or sourced; it does not prove that scanning remained in the final workflow.

The classification should be described as a result of these tests. For example, the behavior notes describe cocoa and cinnamon as feeding more readily in this setup, even though powder names alone do not guarantee a fixed flow behavior. The final journal should show the actual profile assignment used by the interface and any exceptions that needed separate tuning.

I moved the operating workflow onto the Raspberry Pi so the doser could run without a laptop attached. The milestone notes describe integrating the interface and control code on the Pi, allowing powder selection, target entry, dispensing, and result display from the device.

This update needs to be distinguished from initially connecting the touchscreen. A display attached to the Pi is one hardware step; making the complete control program run there with access to the scale and motor is the deployment step. The journal should identify which parts still depended on the laptop before this change and what was moved or configured.

The result described in the notes was an on-device workflow rather than requiring the user to edit code for each dispense. To make that reproducible, I would include the actual launch command, dependencies, serial-device configuration, and how the UI was started. An automatic startup claim belongs here only if it was implemented and tested.

## Construction and implementation detail

The barcode concept would have required a scanner, a mapping from container identifiers to powder records, and a database containing useful behavior settings. M3 notes record abandoning that route after recognizing that the tested powders could be handled through two control families. The important simplification was removing a dependency from the operating workflow, not claiming that all powders behave identically.

The standalone workflow needed more than displaying a window on the Pi. The app and controller files had to be available together, Python needed the serial and UI dependencies, device paths had to resolve, and the screen needed a usable input method. The later app's subprocess path is based on its own directory, which avoids relying on whichever working directory happened to launch it.

The interface stores a powder name for each of eight slots and a requested mass for each slot separately. Only items with positive requested amounts enter the active recipe. EMPTY is a distinct slot state, and the later start function rejects a positive amount assigned to an EMPTY slot. That separation prevents an amount entry from silently inventing the contents of a hopper.

Serial discovery became important as more controllers were attached. The later app enumerates its preferred path, stable /dev/serial/by-id aliases, /dev/ttyACM devices, and /dev/ttyUSB devices. It removes duplicate real paths and excludes the scale and an already-open actuator device. It then checks responses to identify the Uno rather than assuming that every ACM device is the auger/disk controller.

Once identified, the app passes the verified Arduino path and baud rate to the controller child process. This avoids the app testing one port while the child falls back to a different default. The final dispensing process also receives a disk-slot reference when known. Those port and state handoffs belong to later integration updates, while the M3 standalone achievement is that the user could choose a powder, enter a target, start, and see a result without a laptop.

The evidence for standalone operation should include a cold start on the Pi, the installed file layout, a target entered on the touchscreen, and a complete single-doser run. The code architecture supports that workflow, but a photograph of the powered screen alone does not establish that serial discovery, motor launch, and result reporting all succeeded.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

### app_later.py · lines 212–219

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def get_active_recipe_items():
    items = []
    for i in range(1, 9):
        name = slots[i]["name"]
        amount = recipe[i]
        if amount > 0:
            items.append({"slot": i, "name": name, "amount": amount})
    return items
```

### app_later.py · lines 313–336

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def disk_arduino_candidates():
    # Enumerate live ports, including ACM2/ACM3 and stable USB device aliases.
    candidates = (
        [ARDUINO_PORT]
        + sorted(glob.glob("/dev/serial/by-id/*"))
        + sorted(glob.glob("/dev/ttyACM*"))
        + sorted(glob.glob("/dev/ttyUSB*"))
    )
    excluded = {os.path.realpath(SCALE_PORT)}
    if actuator_serial is not None and actuator_serial.is_open:
        actuator_port = getattr(actuator_serial, "port", None)
        if actuator_port:
            excluded.add(os.path.realpath(actuator_port))
    unique = []
    seen = set()
    for port in candidates:
        if not port or not os.path.exists(port):
            continue
        actual_port = os.path.realpath(port)
        if actual_port in excluded or actual_port in seen:
            continue
        seen.add(actual_port)
        unique.append(port)
    return unique
```

## Image sequence

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

The control workflow moved onto the Pi and used selectable powder profiles. Later code documents device discovery and verified-port handoff as the system gained multiple controllers.

## Complete from your records

Add Pi OS/startup method, installed dependencies, the original standalone app revision, device identification, and a complete cold-start run.

[IMAGE PLACEHOLDER: Pi file layout and startup sequence, then powder selection, target entry, live run, and result screen.]

[IMAGE PLACEHOLDER: Serial-discovery output demonstrating that scale, Uno, and actuator are assigned to the correct roles.]

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
