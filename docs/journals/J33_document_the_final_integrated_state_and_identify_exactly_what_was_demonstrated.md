# J33 Bring the prototype together and assess the documented results

*Milestone 5 | Personal retrospective journal*

## Design and iteration

By the final milestone, I had brought the feeder, agitation, rotary selection, lifted drive, scale feedback, and touchscreen interface into an integrated prototype. The remaining work described in the notes concentrated on motor control, fault visibility, mounting, and wiring organization.

Looking back across the iterations, the major decisions were connected. Sharing the motors created the lift-and-coupling problem. Sugar required resistance to passive discharge and careful stopping. Cornstarch required attention to both the screw and the powder outside its active region. Moving to recipes made state, references, and completion messages as important as the motion itself.

The clearest measured outcome is the powder test sheet: all eight recorded 5 g runs met the 3% target, while only three of eight at 0.055 g did. I kept that distinction in the closing account. The available source set does not establish a fully matched final software configuration or an ingredient-by-ingredient autonomous run, so the completed narrative closes the documented development without claiming those missing measurements.

## Technical detail

The integrated system spans feeder and disk CAD, printed interfaces, motor and actuator hardware, driver settings, wiring, the touchscreen app, the mass controller, and separate motion firmware. The archive preserves several real revisions of those elements, but not a confirmed final manifest matching every file to the installed hardware.

Two version boundaries remain especially important. The app describes switch-based indexing while the recovered disk firmware uses counted steps, and the later controller's 120 s timeout is shorter than several recorded powder trials. Those mismatches do not erase the trials; they prevent attributing all earlier results to one assumed final code set.

The intended integrated flow covers reference setup, recipe entry, lift clearance, disk movement, engagement, mass-controlled feeding, and the transition to the next ingredient. The saved app implements that ordering with state and completion checks. The available evidence does not include an uncut run and corresponding ingredient-by-ingredient data that establish the complete sequence's measured performance.

Per-item CSV fields in the app can retain target, actual mass, error, remaining amount, and status. Those fields are part of the logging design; they are not populated test results in this account. Recipe duration, manual interventions, and final mixture measurements are therefore not assigned values that the source does not provide.

The strongest numerical distinction remains the target size: eight of eight recorded 5 g trials met 3%, compared with three of eight at 0.055 g. These are single-powder results. The full assembly CAD shows one populated hopper, so its appearance does not independently establish the hopper count or success of a physical eight-ingredient demonstration.

My next priorities would be to freeze one matched hardware-and-code configuration, retain a complete integrated run, and repeat fixed-target measurements with controlled conditions. Those experiments would build directly on the documented mechanism and expose whether remaining error came from dispensing variability, feedback timing, positioning, or engagement. They are future work rather than additional completed tests.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### controller_later.py · lines 107–108

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
MAX_DISPENSE_TIME_S = 120.0
HEARTBEAT_INTERVAL_S = 0.50
```

### app_later.py · lines 1108–1112

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
                     "limit switch is OPEN in its indent, then press SET CURRENT AS "
                     "SLOT 1. After that one-time setup, START "
                     "will move through the complete recipe automatically.")
        return
    if actuator_position == "UNKNOWN":
```

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Outcome and reflection

The project developed from a printable feeder into a coordinated powder-dispensing prototype with meaningful feedback and integration challenges. Its strongest measured evidence was at 5 g; its clearest remaining performance limitation was small-dose consistency. The next useful work was a version-matched integrated trial and repeated fixed-target measurements, building on the mechanisms and control structure already developed.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
