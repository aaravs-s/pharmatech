# J33 Putting the build in perspective

*Milestone 5 | Retrospective build notes*

By the final milestone, the project had the feeder, agitator, carousel, lifted drive, scale feedback, and touchscreen brought together into a prototype. The notes had shifted toward pulse generation, fault reporting, mounting, and wiring. Those last integration details were a lot less simple than the original raise-rotate-lower description made them sound.

Looking back, the failures connect fairly clearly. Sharing motors created the engagement problem. Sugar needed to stay put while idle and stop being added before the scale caught up. Cornstarch needed help both inside the screw and out near the hopper walls. Recipes added another layer where position and completion messages mattered as much as the motion itself.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The 5 g table is still the strongest numerical result: eight of eight listed runs inside 3%. The 55 mg table is the uncomfortable one: only three of eight. Both belong in the project. Leaving out the small-target failures would give a much cleaner ending and a much less useful picture of the machine.

There are gaps in the archive too. I don't have one confirmed final set matching every software file to the installed hardware, or the full per-ingredient data from an autonomous recipe run. That limits what I can conclude here. It doesn't erase the design work, but it does tell me what evidence to keep next.

## More views

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Code for this revision

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

## Next

The next priority would be freezing one matched configuration and running it repeatedly, with the raw results kept alongside it. Especially at the small target. There's a real prototype and a lot of useful engineering behind it; the remaining job is to make the performance as clear as the mechanism.

<details>
<summary>Notes added while reconstructing this entry</summary>

The integrated system spans feeder and disk CAD, printed interfaces, motor and actuator hardware, driver settings, wiring, the touchscreen app, the mass controller, and separate motion firmware. The archive preserves several real revisions of those elements, but not a confirmed final manifest matching every file to the installed hardware.

Two version boundaries remain especially important. The app describes switch-based indexing while the recovered disk firmware uses counted steps, and the later controller's 120 s timeout is shorter than several recorded powder trials. Those mismatches don't erase the trials; they prevent attributing all earlier results to one assumed final code set.

The intended integrated flow covers reference setup, recipe entry, lift clearance, disk movement, engagement, mass-controlled feeding, and the transition to the next ingredient. The saved app implements that ordering with state and completion checks. The available evidence doesn't include an uncut run and corresponding ingredient-by-ingredient data that establish the complete sequence's measured performance.

Per-item CSV fields in the app can retain target, actual mass, error, remaining amount, and status. Those fields are part of the logging design; they aren't populated test results in this account. Recipe duration, manual interventions, and final mixture measurements are therefore not assigned values that the source doesn't provide.

The strongest numerical distinction remains the target size: eight of eight recorded 5 g trials met 3%, compared with three of eight at 0.055 g. These are single-powder results. The full assembly CAD shows one populated hopper, so its appearance doesn't independently establish the hopper count or success of a physical eight-ingredient demonstration.

My next priorities would be to freeze one matched hardware-and-code configuration, retain a complete integrated run, and repeat fixed-target measurements with controlled conditions. Those experiments would build directly on the documented mechanism and expose whether remaining error came from dispensing variability, feedback timing, positioning, or engagement. They are future work rather than additional completed tests.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
