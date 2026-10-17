# J17 Replace the barcode plan with selectable profiles and run the doser from the Pi

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I considered identifying powder containers with a barcode scanner and retrieving settings from a database. That would have added container records, scanner integration, and another source of configuration to maintain. Testing the eight materials suggested a simpler operating workflow based on selecting their control profiles directly.

I abandoned the scanner-and-database direction for this prototype and moved the complete single-doser workflow onto the Pi. The result described in my notes was operation without a laptop: choose a powder, enter a mass, start dispensing, and see the result on the device. Connecting a display had been an earlier hardware step; running the interface and controller together with access to the serial devices was the integration step.

The later app shows how that workflow grew as more controllers were attached. It stores powder assignments separately from requested amounts, resolves serial devices, and passes the selected device to the dispensing child process. I have kept those later implementation details distinguishable from the earlier single-doser deployment.

## Technical detail

The barcode concept would have required a scanner, a mapping from container identifiers to powder records, and a database containing useful behavior settings. M3 notes record abandoning that route after recognizing that the tested powders could be handled through two control families. The important simplification was removing a dependency from the operating workflow, not claiming that all powders behave identically.

The standalone workflow needed more than displaying a window on the Pi. The app and controller files had to be available together, Python needed the serial and UI dependencies, device paths had to resolve, and the screen needed a usable input method. The later app's subprocess path is based on its own directory, which avoids relying on whichever working directory happened to launch it.

The interface stores a powder name for each of eight slots and a requested mass for each slot separately. Only items with positive requested amounts enter the active recipe. EMPTY is a distinct slot state, and the later start function rejects a positive amount assigned to an EMPTY slot. That separation prevents an amount entry from silently inventing the contents of a hopper.

Serial discovery became important as more controllers were attached. The later app enumerates its preferred path, stable /dev/serial/by-id aliases, /dev/ttyACM devices, and /dev/ttyUSB devices. It removes duplicate real paths and excludes the scale and an already-open actuator device. It then checks responses to identify the Uno rather than assuming that every ACM device is the auger/disk controller.

The later app passes the verified Arduino path and baud rate to the controller child, avoiding a handoff where the app checks one device and the child opens another default. It also passes the known disk slot. These details belong to later multi-device integration, while the M3 milestone establishes the reported single-doser workflow on the Pi without a laptop.

The source supports the file-location and device-discovery architecture, and the milestone notes describe standalone operation. The record does not establish automatic startup after a cold boot or preserve a complete deployment transcript. I have not added those behaviors to the reported on-device achievement.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

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

## Process images

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The standalone Pi workflow removed the laptop and barcode database from the normal single-doser interaction. A simpler user choice was useful only if it still selected the correct profile and device, so process paths, slot contents, and serial discovery became explicit application responsibilities as the machine expanded.

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R17_replace_the_barcode_plan_with_selectable_profiles_and_run_the_doser_from_the_pi.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
