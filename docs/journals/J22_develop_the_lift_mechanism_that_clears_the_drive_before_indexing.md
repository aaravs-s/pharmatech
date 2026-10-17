# J22 The drive has to get out of the way

*Milestone 4 | Retrospective build notes*

Sharing the motor saved hardware, but now I had to physically move it out of the carousel's way. Leave it engaged and the disk can't index. Lower it too soon and it can meet the wrong part of the moving mechanism.

The sequence I needed was straightforward: raise, rotate, lower. Making the mechanism follow it with known positions was the less straightforward part.

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

I initially considered building the lift and then chose to buy a mechanism under the cost constraints in the notes. The B4 branch still has the servo/lead-screw concept, while the later app talks to a separate actuator controller. Those are different stages, not a collection of actuators that were all installed at once.

I also had to be careful with the travel value in software. The later app uses 69,000 steps, which looks very definite but isn't a stroke measurement by itself. Without the actual lead, gearing, and microsteps it doesn't tell me millimeters. The app's UP position is an operator-established reference too, not an automatically sensed top limit.

## Lift geometry and references

The required clearance depends on coupling overlap, the nearby hopper envelope, and how the drive is guided. The motor and its wiring move with the stage, while the carousel passes beneath it. A commanded travel value only becomes a physical stroke after applying the actual microsteps, lead, and gearing; it isn't an independent measurement of clearance.

The later app sets a travel constant of 69,000 steps and sends ACTUATOR UP or ACTUATOR DOWN to a separate XIAO over USB serial, with a default actuator port of /dev/ttyACM1 at 115200 baud. That is a commanded step count, not millimetres. The mechanical conversion requires the actuator's steps per revolution, microsteps, and lead or gearing.

The app also starts from an assumption that the actuator is physically at its top reference. It has a SET CURRENT AS UP operation and blocks a recipe if the position is UNKNOWN. The source states there are no actuator limit switches in that operating arrangement. This reference-setting behavior must not be described as automatically sensing the top end of travel.

## More views

![B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_assembly.jpg)

B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The lift gave the carousel room to move. It didn't guarantee the drive would connect when it came back down. That became the next roadblock: the axes could line up and the coupling could still land at the wrong angle.

<details>
<summary>Notes added while reconstructing this entry</summary>

The shared-motor architecture required a motion sequence the single doser didn't need. While a hopper is feeding, the motor must engage its auger. While the carousel indexes, that engagement must be clear of the rotating parts. The lift supplies the missing degree of freedom: raise the drive, index the disk, then lower the drive to the selected hopper.

The B4 branch preserves a servo/lead-screw lift concept. The notes record moving from a plan to construct the lift to purchasing a mechanism, and the later app communicates with a separate actuator controller. I kept these stages distinct because the saved sources don't identify one unchanged lift across the entire project.

The next mechanical issue was engagement at the bottom of the stroke. Even with enough clearance to index, the coupler could fail if the auger and motor reached incompatible angular orientations. That motivated the separate coupling redesign rather than increasing actuator travel or motor speed.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
