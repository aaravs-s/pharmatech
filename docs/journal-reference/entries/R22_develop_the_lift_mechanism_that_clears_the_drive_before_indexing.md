# R22 Develop the lift mechanism that clears the drive before indexing

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J32

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Move the shared motor away from the active hopper during carousel rotation and return it for dispensing.

## Design process

I needed the shared motor to clear the hopper drive before the rotary disk moved. I chose a lift arrangement that raises the motor during indexing and lowers it once the selected hopper is in position. This turned the shared-drive concept into a sequence that could be automated.

I initially considered building the linear mechanism myself, then decided to purchase one because of the cost constraints described in the milestone notes. The BOM lists a small lead-screw linear stage with a 50 mm travel option, while the CAD has several actuator-related tabs. Those references should not be treated as confirmation that every listed actuator was installed in the final machine.

The important geometry is the travel needed to disengage the coupling, the support for the motor, and the alignment when it returns. Too little lift leaves a collision risk during rotation; inconsistent lowering can prevent the coupling from seating. I would show the raised and lowered positions using the exact mechanism that was built.

## Construction and implementation detail

The shared-motor architecture required a motion sequence the single doser did not need. While a hopper is feeding, the motor must engage its auger. While the carousel indexes, that engagement must be clear of the rotating parts. The lift supplies the missing degree of freedom: raise the drive, index the disk, then lower the drive to the selected hopper.

The notes record an initial plan to construct a lift and a later decision to purchase one because of cost constraints. The B4 CAD branch preserves a servo/lead-screw lift arrangement, while the machine notes and later app describe a separate actuator controller. These are evidence of alternative stages, not one unchanged final lift. I include the branch and subassembly views together and ask for the installed unit to be identified.

A useful lift design record includes the required clearance stroke, motor mass carried, guide/support arrangement, screw or purchased actuator attachment, and cable motion. Stroke should be determined from the coupling overlap and interference envelope. A larger value in code is not enough to show that the motor clears all eight hoppers during rotation.

The later app sets a travel constant of 69,000 steps and sends ACTUATOR UP or ACTUATOR DOWN to a separate XIAO over USB serial, with a default actuator port of /dev/ttyACM1 at 115200 baud. That is a commanded step count, not millimetres. The mechanical conversion requires the actuator's steps per revolution, microsteps, and lead or gearing.

The app also starts from an assumption that the actuator is physically at its top reference. It has a SET CURRENT AS UP operation and blocks a recipe if the position is UNKNOWN. The source states there are no actuator limit switches in that operating arrangement. This reference-setting behavior must not be described as automatically sensing the top end of travel.

The next mechanical issue was engagement at the bottom of the stroke. Even with enough clearance to index, the coupler could fail if the auger and motor reached incompatible angular orientations. That motivated the separate coupling redesign rather than increasing actuator travel or motor speed.

## Image sequence

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

![B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_assembly.jpg)

B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Result and handoff

A lift was introduced to disengage the shared drive during indexing. The branch CAD, purchased mechanism, and 69,000-step control revision need to be matched to the installed hardware.

## Complete from your records

Identify installed actuator, actual stroke, step-to-distance conversion, load support, end references, and clearance throughout indexing.

[IMAGE PLACEHOLDER: Lift bracket/guide sketches and intermediate CAD before the branch assembly was completed.]

[IMAGE PLACEHOLDER: Installed actuator at UP and DOWN with measured coupling clearance and overlap.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
