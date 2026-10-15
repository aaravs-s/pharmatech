# R14 Plan the electronics mounting and PCB while the control system is still changing

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J20

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Organize the electrical interfaces and decide what must be stabilized before committing to a fixed board.

## Design process

I began planning a PCB to organize the controller connections and make the electronics easier to mount. The breadboard was useful while the circuit was changing, but the loose wiring was awkward to package on the machine.

The intended board would bring together the Raspberry Pi connections, motor-control signals, and supporting circuitry. The schematic image in the milestone notes provides evidence of that design direction. It should be described as the schematic or proposal it actually was, rather than as a fabricated and validated board.

At this point I still expected the PCB to become part of a later milestone. That plan eventually changed as the mechanism and electronics continued evolving. Keeping this entry separate from the later abandonment makes the design process understandable: there was a reasonable motivation for a board, followed by practical reasons why a fixed design no longer fit the development stage.

## Construction and implementation detail

By the end of the early scale-feedback work, the breadboard held a mixture of power, motor-control, and Pi connections. The PCB proposal aimed to make those connections easier to mount and maintain, and to reduce loose wiring. It was a planned improvement in the M2 notes, with an expectation of arrival by M3, rather than a board already proven in the machine.

The challenge was that the electrical architecture was still evolving. The first Pi/TMC2209 arrangement, the later Arduino command interface, and the eventual integrated NEMA 23 drivers did not share one unchanged pin map. A board layout based on an early configuration could become obsolete when motor, enable polarity, pulse generation, or actuator control changed.

For a useful process record, I would identify the schematic blocks before describing a board render: supply inputs, logic supply regulation, controller connectors, STEP/DIR/EN signals, driver alarms, scale communication, and actuator communication. The available notes do not contain a verified PCB schematic or routed-board revision, so the reference pack cannot provide a recreation-ready custom PCB merely from a breadboard photograph.

The later decision was to abandon the custom PCB because the design never stabilized enough to finalize it. That is an important outcome, not a missing success to fill in. It explains why the completed prototype continued with adaptable connections and a printed mount. The PCB proposal belongs here as a design plan, while the perfboard attempt and return to a half-size breadboard belong in the later electronics update.

The practical handoff was to keep the machine testable while documenting wiring changes as the controller developed. A consistent connector and pin table would have made those changes easier to track even without a custom board. The journal needs the actual early schematic or a clearly marked missing-diagram placeholder, then the revised electronics decision at the correct milestone.

## Image sequence

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

## Result and handoff

A PCB was proposed for organization and mounting, but the source record does not establish a finalized or installed board. Later iterations returned to adaptable breadboard wiring.

## Complete from your records

Find any schematic/PCB drafts and their dates; list which connections were stable and which changed before the plan was dropped.

[IMAGE PLACEHOLDER: Actual early schematic or PCB draft with revision date; no verified board design was recovered.]

[IMAGE PLACEHOLDER: Connector/pin table for the M2 wiring and the intended mounting arrangement.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
