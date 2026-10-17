# J31 The wiring needed somewhere to live

*Milestone 5 | Retrospective build notes*

Once the parts were on the frame, the wiring needed attention. I printed wire covers, an Arduino cover, and mounting pieces, then secured the connections along the side and concentrated the route around one extrusion.

It was tempting to treat this as the tidy-up at the end. But the motor moved with the lift, the disk rotated, and the cup still needed access. A wire route that looked fine with everything stationary could get in the way somewhere else in the sequence.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

The covers also had to fit actual connectors and leave the boards accessible. Covering a mess without being able to reach the next connection wouldn't make later debugging much nicer.

The notes establish the routing and printed parts, not an electrical-noise measurement or a full endpoint inspection. I can describe the organization change. I can't say a neater cable bundle proved every electrical issue was gone.

## Cable routes and clearance

The cable bundle and actual mounting surface constrained the covers. Internal space, wall thickness, connector exits, and attachment positions affected whether the parts could organize wiring without pinching it or blocking board access. The milestone record identifies the printed parts but doesn't provide all of their feature dimensions.

The lifted drive required a moving cable section, while most electronics stayed on the frame. The moving segment needed enough travel allowance at both UP and DOWN positions. A cable photographed with the actuator in only one position can't show whether it becomes taut or catches during the other part of the stroke.

Cable clearance has to be considered over the full index-and-lift sequence. A route could rub at the disk, pull at a driver or breadboard, obstruct coupling, or cross the cup access area. Those are relevant inspection conditions; a recorded full-travel result for each route isn't available here.

## More views

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

The wiring had a more deliberate place on the machine now. The moving section was still the part to judge through the whole stroke, not from one nice photo. Packaging only helps if it keeps access and movement workable.

<details>
<summary>Notes added while reconstructing this entry</summary>

M5 notes describe printed wire covers, an Arduino cover, and a breadboard mount, with wiring secured to the side and consolidated around one extrusion. This was a final integration task because the motor, lift, disk, scale, and screen positions determined where the cable routes could run.

The reported change was consolidation and physical support of wiring. The source doesn't establish final wire gauges, terminal specifications, a quantified strain-relief rating, or a measured noise reduction. Those outcomes can't be deduced from the cleaner layout alone.

The assembly views show the wider packaging context, while the notes supply the description of covers and consolidated routing. I retained the actual images without adding a substitute construction sequence for unrecovered channel and enclosure features.

</details>

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R31_design_protective_covers_and_consolidate_wiring_along_the_frame.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
