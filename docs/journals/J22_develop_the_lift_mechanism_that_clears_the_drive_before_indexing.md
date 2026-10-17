# J22 Develop the lift mechanism that clears the drive before indexing

*Milestone 4 | Personal retrospective journal*

## Design and iteration

The shared motor could not remain engaged while the carousel moved. I needed a way to lift it clear of the active hopper, rotate the disk, and return the motor to the selected auger. That added a vertical motion stage to a mechanism that previously only needed to feed powder.

I initially considered constructing the lift, then decided to purchase a linear mechanism under the cost constraints recorded in the milestone notes. The CAD includes a servo/lead-screw concept in the B4 branch, while later software controls an actuator through a separate XIAO. These represent different stages of the design, not confirmation that every modeled or listed actuator was installed.

The key mechanical requirement was clearance relative to the coupling overlap and surrounding hoppers. More commanded steps did not automatically mean more known physical travel. The later app also depended on an operator-established UP reference, making position knowledge part of the operating sequence as well as the mechanical layout.

## Technical detail

The shared-motor architecture required a motion sequence the single doser did not need. While a hopper is feeding, the motor must engage its auger. While the carousel indexes, that engagement must be clear of the rotating parts. The lift supplies the missing degree of freedom: raise the drive, index the disk, then lower the drive to the selected hopper.

The B4 branch preserves a servo/lead-screw lift concept. The notes record moving from a plan to construct the lift to purchasing a mechanism, and the later app communicates with a separate actuator controller. I kept these stages distinct because the saved sources do not identify one unchanged lift across the entire project.

The required clearance depends on coupling overlap, the nearby hopper envelope, and how the drive is guided. The motor and its wiring move with the stage, while the carousel passes beneath it. A commanded travel value only becomes a physical stroke after applying the actual microsteps, lead, and gearing; it is not an independent measurement of clearance.

The later app sets a travel constant of 69,000 steps and sends ACTUATOR UP or ACTUATOR DOWN to a separate XIAO over USB serial, with a default actuator port of /dev/ttyACM1 at 115200 baud. That is a commanded step count, not millimetres. The mechanical conversion requires the actuator's steps per revolution, microsteps, and lead or gearing.

The app also starts from an assumption that the actuator is physically at its top reference. It has a SET CURRENT AS UP operation and blocks a recipe if the position is UNKNOWN. The source states there are no actuator limit switches in that operating arrangement. This reference-setting behavior must not be described as automatically sensing the top end of travel.

The next mechanical issue was engagement at the bottom of the stroke. Even with enough clearance to index, the coupler could fail if the auger and motor reached incompatible angular orientations. That motivated the separate coupling redesign rather than increasing actuator travel or motor speed.

## Process images

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

![B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_assembly.jpg)

B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Outcome and reflection

The lift supplied the disengagement motion required by the shared-drive architecture. Its control also introduced a distinct position state and serial device. Clearing the disk was only half the problem: after lowering, the coupling still had to engage at the angular position left by the previous dispense, which led to the next redesign.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
