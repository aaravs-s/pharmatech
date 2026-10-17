# J30 Drop the fixed-board plan, troubleshoot perfboard, and mount a half-size breadboard

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I returned to electronics packaging once the mechanisms were assembled. The PCB plan had not reached a stable layout, and the original full-size breadboard arrangement was bulky and difficult to mount cleanly.

I tried perfboard as a more permanent alternative, but it did not provide the working connections I needed. The notes do not identify a confirmed soldering or mapping fault, so I have kept the failed connection attempt separate from a diagnosis. I returned to a breadboard to keep development moving.

I reduced the footprint with a half-size breadboard and a custom printed mount. That retained access to change the circuit while making it more practical to attach to the machine. The decision prioritized a serviceable prototype over finalizing a permanent board while motor, alarm, and actuator interfaces were still evolving.

## Technical detail

The early PCB plan never reached a finalized design according to M5 notes. As motor control, timers, alarm lines, and the actuator changed, a fixed board layout would have needed repeated revision. The eventual prototype needed an adaptable arrangement that could support continued testing.

A perfboard was tried after the larger breadboard proved bulky and messy. The notes say the perfboard failed to connect, then record returning to a breadboard. That establishes a failed implementation attempt, but does not identify whether the failure came from a solder joint, a trace break, a wrong connection, or another electrical cause. The comparison photo shows both arrangements; it does not diagnose the failure.

The final mounting response was a half-size breadboard and a custom printed mount. The design task shifted from creating a permanent electrical circuit to constraining an interchangeable board mechanically. Relevant CAD details are the board footprint, retaining edges, access to connection rows, mounting-hole positions, standoff height, and clearance around the frame fasteners.

The mount had to hold the breadboard without covering useful connection rows or making routine changes awkward. Wire movement could pull at contacts, while excessive retention could distort the board. These were packaging constraints on the printed part, rather than evidence of a measured vibration or pullout rating.

The comparison imagery records the electrical arrangements, and the notes identify the custom mount. Its detailed retaining geometry and a diagnosed perfboard fault are not preserved. I therefore describe the reported transition and its practical purpose without adding a particular joint failure or an invented mount dimension.

The result was a prototype arrangement that kept the electronics accessible and modifiable. The decision explains why a breadboard remained in the assembled machine despite the earlier PCB proposal. A permanent board could become useful once the circuit stabilized, but it was not a prerequisite for completing this integration stage.

## Process images

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Outcome and reflection

The final packaging choice for this stage was a half-size breadboard in a printed mount. It addressed the immediate mounting problem while keeping the circuit modifiable. The abandoned PCB and failed perfboard were useful parts of that decision: a more permanent construction method only helped if the electrical implementation was ready for it.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
