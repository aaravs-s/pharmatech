# J30 Back to a breadboard, but make it fit

*Milestone 5 | Retrospective build notes*

The PCB plan hadn't become a stable board, and the full-size breadboard was still awkward to put on the frame. I tried perfboard as a more permanent arrangement. That attempt didn't give me the working connections I needed.

So I went back to a breadboard. Not the most satisfying-looking end to the PCB idea, but I needed to keep changing and testing the circuit. The notes don't identify the exact perfboard fault, so I'm not going to retrofit a solder-bridge story onto it.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

I used a half-size breadboard and printed a custom mount to reduce the footprint. That dealt with the immediate physical problem while keeping the connection rows accessible. The circuit could still change without making another permanent board.

This was one of the less glamorous parts of getting the machine together. A working circuit spread across the bench wasn't the same thing as a circuit that could stay on the frame while the mechanisms moved around it.

## Mounting notes

The final mounting response was a half-size breadboard and a custom printed mount. The design task shifted from creating a permanent electrical circuit to constraining an interchangeable board mechanically. Relevant CAD details are the board footprint, retaining edges, access to connection rows, mounting-hole positions, standoff height, and clearance around the frame fasteners.

The mount had to hold the breadboard without covering useful connection rows or making routine changes awkward. Wire movement could pull at contacts, while excessive retention could distort the board. These were packaging constraints on the printed part, rather than evidence of a measured vibration or pullout rating.

## More views

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The half-size board and mount were the practical choice for this stage. I still wanted more permanent electronics eventually, but the circuit had to be ready for that. Forcing the PCB plan to look finished wouldn't have made the machine easier to debug.

<details>
<summary>Notes added while reconstructing this entry</summary>

The early PCB plan never reached a finalized design according to M5 notes. As motor control, timers, alarm lines, and the actuator changed, a fixed board layout would have needed repeated revision. The eventual prototype needed an adaptable arrangement that could support continued testing.

A perfboard was tried after the larger breadboard proved bulky and messy. The notes say the perfboard failed to connect, then record returning to a breadboard. That establishes a failed implementation attempt, but doesn't identify whether the failure came from a solder joint, a trace break, a wrong connection, or another electrical cause. The comparison photo shows both arrangements; it doesn't diagnose the failure.

The comparison imagery records the electrical arrangements, and the notes identify the custom mount. Its detailed retaining geometry and a diagnosed perfboard fault aren't preserved. I describe the reported transition and its practical purpose without adding a particular joint failure or an invented mount dimension.

The result was a prototype arrangement that kept the electronics accessible and modifiable. The decision explains why a breadboard remained in the assembled machine despite the earlier PCB proposal. A permanent board could become useful once the circuit stabilized, but it wasn't a prerequisite for completing this integration stage.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
