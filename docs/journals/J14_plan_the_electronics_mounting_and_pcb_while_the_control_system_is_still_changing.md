# J14 Plan the electronics mounting and PCB while the control system is still changing

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I began planning a PCB because the breadboard wiring was awkward to mount and service. The idea was to organize the controller connections into a more compact arrangement rather than leave the working circuit spread across the bench.

The schematic image records this direction, but the board did not become a finalized, validated part of the prototype. At the time I expected a more permanent electrical arrangement in a later milestone. The architecture was still changing, including the motor hardware, controller interface, and actuator requirements.

That made the PCB decision dependent on more than whether I could draw a board. A layout based on the early Pi and TMC2209 configuration could become obsolete when pins, enable polarity, or driver alarm connections changed. I kept development moving while that boundary remained unsettled, and eventually returned to a modular mounting approach.

## Technical detail

By the end of early feedback development, the breadboard combined power, motor-control, and Pi connections. The PCB proposal aimed to reduce loose wiring and improve mounting. The M2 notes anticipated that improvement in M3, but the record does not establish a fabricated board operating in the machine.

The challenge was that the electrical architecture was still evolving. The first Pi/TMC2209 arrangement, the later Arduino command interface, and the eventual integrated NEMA 23 drivers did not share one unchanged pin map. A board layout based on an early configuration could become obsolete when motor, enable polarity, pulse generation, or actuator control changed.

The electrical functions spanned supply connections, controller logic, STEP/DIR/EN, serial scale feedback, and later alarm and actuator paths. A fixed board would need compatible interfaces for the chosen revision. The available schematic image records the proposal, while a complete verified schematic and routed-board revision are not preserved.

I later abandoned the custom PCB because the design had not stabilized enough to finalize it. This explains the continued use of adaptable connections and a printed mount. The decision was a change in implementation strategy, rather than a missing fabricated-board success.

Keeping the circuit modifiable allowed motor control and integration to continue. The tradeoff was retaining more manual wiring and a greater dependence on version-specific pin maps. A permanent board could address those issues after the electrical architecture settled, rather than forcing the prototype to conform to an early layout.

## Process images

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

## Outcome and reflection

The PCB proposal identified a real packaging problem, but committing to a fixed layout before the interfaces stabilized would have locked in an early revision. The board remained a proposal. The later perfboard attempt and half-size breadboard mount were responses to that continuing need for adaptability.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
