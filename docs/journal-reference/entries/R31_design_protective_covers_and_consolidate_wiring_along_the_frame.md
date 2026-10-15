# R31 Design protective covers and consolidate wiring along the frame

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J46

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Route and support the wiring so the assembled mechanisms remain accessible and movement does not disturb connections.

## Design process

I printed wire covers, an Arduino cover, and mounting parts to organize the electronics. I secured the wires along the side of the machine and concentrated routing along one extrusion to reduce the amount of exposed wiring.

This update was about the physical arrangement of a working prototype. The covers needed to fit the real connectors and allow the required wires to enter and leave without being pinched. Routes near the lifting drive or rotary disk also needed enough clearance and slack for motion. The notes describe the organization work, but do not provide a verified final wiring diagram or a complete enclosure specification.

I would use close-up photographs to show what changed instead of relying on a distant overall assembly view. The important comparison is where the wiring used to be, how it was restrained, and how the printed covers attach. Any claimed protection or strain relief should match the features actually present in those parts.

## Construction and implementation detail

M5 notes describe printed wire covers, an Arduino cover, and a breadboard mount, with wiring secured to the side and consolidated around one extrusion. This was a final integration task because the motor, lift, disk, scale, and screen positions determined where the cable routes could run.

The cover design needed to follow the actual cable bundle and mounting surface. Its useful dimensions include the internal channel, wall thickness, length, attachment spacing, and exits near connectors. A cover can appear neat while pinching a wire or blocking access to the board underneath, so the construction sequence should show the empty cover and the routed bundle before closure.

The lifted drive required a moving cable section, while most electronics stayed on the frame. The moving segment needed enough travel allowance at both UP and DOWN positions. A cable photographed with the actuator in only one position cannot show whether it becomes taut or catches during the other part of the stroke.

I would document where power and control connections run, where the wires are supported, and which connectors must be disconnected for service. The notes report consolidation but do not give wire gauges, terminal types, strain-relief details, or a measured electrical-noise improvement. The journal should state the physical organization change rather than infer that it solved every electrical issue.

The verification sequence is an inspection at full travel followed by a complete index/engage/dispense cycle. Look for cables rubbing against the disk, pulling at the driver or breadboard, obstructing the coupler, or crossing the scale's cup path. The actual observations from that cycle belong beside the installed-cover photograph.

The final frame image remains useful as the overview, but it now follows placeholders for the cable-channel sketch, cover extrusion, attachment features, and fit trial. Those are the missing stages another builder needs to recreate the cover without guessing its entire internal geometry from an exterior photograph.

## Image sequence

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Result and handoff

The built prototype used printed covers and wiring consolidated along the frame. Exact cover geometry, cable-travel checks, and final wiring details remain to be added.

## Complete from your records

Add cover files/dimensions, actual wire/connector choices, attachment points, access procedure, and observed cable behavior at full actuator travel.

[IMAGE PLACEHOLDER: Wire-channel and Arduino-cover sketches, intermediate walls/cutouts, and final CAD.]

[IMAGE PLACEHOLDER: Cable routing before closure, covers installed, and moving cable slack at both actuator endpoints.]

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
