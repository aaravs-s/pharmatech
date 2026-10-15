# R33 Document the final integrated state and identify exactly what was demonstrated

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J48

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Connect the final assembly, matching code, and measured run evidence without treating a completed-looking machine as proof of every target.

## Design process

I brought the mechanical selection, drive engagement, scale feedback, and on-device interface together into the integrated prototype. The milestone notes describe the components working together by M5 and then focusing on motor performance and electronics organization.

The final journal needs the actual demonstration that defines what finished meant for this machine. I would record the powders loaded, the requested mass of each ingredient, the sequence of selected hoppers, and the final measured results. [Add the real outcome here: what completed automatically, what required intervention, and what failed.] The media folder contains several recordings, but their generic filenames do not establish the content of every clip, so no complete autonomous result is inferred from their presence.

The final state should be compared against the original requirements. The recorded 5 g tests support those particular single-powder runs; they do not establish the full 100 g range, every recipe, repeated coupling reliability, or pharmacy suitability. A strong ending can show the working capabilities clearly while stating the remaining limitations and the next concrete improvement.

## Construction and implementation detail

The final project record should identify a reproducible configuration: disk and feeder CAD revisions, printed components, motor and actuator models, driver settings, wiring map, app file, mass-controller file, Uno firmware, and actuator firmware. The recovered sources include several genuine stages, but not yet a confirmed final set of mutually matching files.

The most important source mismatch is the later app's switch-based indexing description versus the recovered step-count disk firmware. A second is the later controller's 120 s run limit versus the roughly five-minute cohesive-powder tests. These do not invalidate the original recorded results; they show why the final demonstration needs its own dated configuration and run data rather than inheriting every result from earlier milestones.

A complete demonstration should show startup and reference establishment, recipe entry, lift clearance, disk indexing, engagement, feedback-controlled feeding, the next ingredient transition, and the completed result. The video should retain enough context to see the scale and mechanisms together. Separate close-ups can explain the coupler and wiring, but an assembly photograph alone cannot establish that the sequence ran autonomously.

The result table should retain per-ingredient target and final mass, total duration, final mixture mass where recorded, interventions, alarms, and any incomplete steps. A recipe that needed manual alignment or a refill can still be useful evidence, but the intervention belongs in the result. The CSV fields in the app offer a place to retain these facts; empty or example rows should not be described as measured runs.

The household-powder tests show stronger results at 5 g than at 0.055 g. The final summary should preserve that distinction and identify whether the carousel sequence itself was tested with one, several, or all eight hoppers. The current full assembly CAD shows one populated hopper, so the number of hoppers in a physical demonstration must come from the video or build record.

This closes the design reference while keeping the remaining evidence specific: matched final files, intermediate coupler/cover stages, repeated same-target measurements, and an uncut integrated run. Dates and active work hours still come from the actual sessions. A detailed machine can plausibly take substantial time, but CAD saves, email dates, and the number of reference entries cannot establish a 200-hour claim.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Result and handoff

The pack documents the recovered design and control progression. Final autonomous performance must be stated from the actual integrated run and matching configuration; the missing evidence is listed explicitly.

## Complete from your records

Identify the actual final configuration, demonstration date, hopper count, recipe targets/masses, duration, interventions, and actual active hours.

[IMAGE PLACEHOLDER: Final matched app/controller/Uno/XIAO files and their wiring/configuration manifest.]

[IMAGE PLACEHOLDER: Uncut final recipe video, per-ingredient CSV from the same run, and final stable scale reading.]

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
