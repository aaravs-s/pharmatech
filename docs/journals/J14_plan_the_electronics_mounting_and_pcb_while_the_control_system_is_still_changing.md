# J14 A PCB sounded like the way out of the wiring

*Milestone 2 | Retrospective build notes*

The breadboard was useful, but it was getting awkward to package. Loose wiring is one thing on a bench and another when it has to live on the frame. I started planning a PCB to organize the controller connections and give the electronics a more manageable footprint.

The schematic image records that direction. It wasn't a finished board running the machine, even though I expected the PCB work to lead into a later milestone. The circuit was still changing underneath that plan.

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

That was the catch. A board for the early Pi and TMC2209 arrangement wouldn't automatically suit the later Arduino interface or integrated NEMA 23 drive. Pins, enable behavior, alarms, actuator connections: those were still moving targets.

I didn't end up finalizing the PCB. It's easy to make that sound like a small omitted step, but it was a real change of direction. I still needed to mount the circuit and keep testing; I just hadn't reached a stable enough electrical design to freeze into that board.

## Why the board never stabilized

The challenge was that the electrical architecture was still evolving. The first Pi/TMC2209 arrangement, the later Arduino command interface, and the eventual integrated NEMA 23 drivers didn't share one unchanged pin map. A board layout based on an early configuration could become obsolete when motor, enable polarity, pulse generation, or actuator control changed.

## More views

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

The packaging problem stayed with the project. A PCB could eventually make it neater, but trying to lock down the wrong revision wouldn't save much work. For now I kept the electronics changeable and came back to mounting later.

<details>
<summary>Notes added while reconstructing this entry</summary>

By the end of early feedback development, the breadboard combined power, motor-control, and Pi connections. The PCB proposal aimed to reduce loose wiring and improve mounting. The M2 notes anticipated that improvement in M3, but the record doesn't establish a fabricated board operating in the machine.

The electrical functions spanned supply connections, controller logic, STEP/DIR/EN, serial scale feedback, and later alarm and actuator paths. A fixed board would need compatible interfaces for the chosen revision. The available schematic image records the proposal, while a complete verified schematic and routed-board revision aren't preserved.

I later abandoned the custom PCB because the design had not stabilized enough to finalize it. This explains the continued use of adaptable connections and a printed mount. The decision was a change in implementation strategy, rather than a missing fabricated-board success.

Keeping the circuit modifiable allowed motor control and integration to continue. The tradeoff was retaining more manual wiring and a greater dependence on version-specific pin maps. A permanent board could address those issues after the electrical architecture settled, rather than forcing the prototype to conform to an early layout.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
