# J23 Lowering the motor wasn't enough to connect it

*Milestone 4 | Retrospective build notes*

This coupling problem held up the integrated machine. I could select a hopper and bring the motor down, but the two mating features didn't necessarily arrive at an angle where they could engage.

It was especially awkward because the connection could work once assembled. That wasn't the same job as reconnecting after an independent auger stop. The mechanism had to find engagement from whatever relative orientation was left, without me lining the faces up by hand.

![V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_sketch.jpg)

V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.

![V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_extrude.jpg)

V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.

I tried different interface ideas and moved to serrated mating teeth. The notes describe that as the practical solution. More repeated teeth reduced the dependence on one particular angular alignment, although I don't have an orientation sweep or engagement failure-rate log to put numbers behind it.

The earlier keyed adapter in V18 is worth showing because it makes the registration issue visible. It isn't a recovered feature history for the later serrations, and I haven't matched it to the exact failed print. I don't want a convenient saved model to quietly stand in for a different physical part.

## The earlier adapter and the tooth redesign

The V18 auger studio preserves a keyed motor-adapter stage. Sketch 15 is on a face of Extrude 2 with a displayed 2.5 cm circular profile. Extrude 13 adds two selected regions at 0.2 cm depth into Part 4. Sketch 13 lies on a face of that extrusion, displays a 2.3 cm circular boundary, and divides the profile into keyed regions; Onshape marks it not fully defined. Extrude 11 adds two regions at 0.75 cm depth into Part 4. These features explain an angularly registered geometry, but this archive isn't matched to the exact failed printed coupler or to the later serrated tooth dimensions.

I changed the interface to repeated serrated teeth. More repeated mating features reduced dependence on one relative orientation, and the milestone notes report that change as the practical solution. No orientation sweep or engagement success-rate series is preserved, so the reported behavior remains distinct from a guarantee for every possible initial angle.

## Saved adapter stages

![V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_sketch.jpg)

V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.

![V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_extrude.jpg)

V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.

![V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_complete.jpg)

V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

The shared-drive idea depended on this detail more than the early layout made it seem. The disk could get to the right hopper and the lift could get to the right height, yet neither would help if the faces couldn't seat. I needed a connection that could form again, not just one that could transmit torque when already together.

<details>
<summary>Notes added while reconstructing this entry</summary>

The first coupling concept had an angular-registration problem. The motor-side feature and auger-side feature could mate only when they arrived at a specific orientation. The carousel selected the correct hopper, but lowering the drive didn't guarantee that the coupling features lined up. The notes describe this as a roadblock because unsuccessful engagement prevented further integrated tests.

The failure showed that coincident shaft axes were necessary but insufficient. Angular orientation and engagement depth determined whether the features could lower into place. A model could appear concentric while opposing projections still collided during the approach, explaining why a connection that transmitted torque when assembled could fail during automatic re-engagement.

Tooth count, spacing, height, flank shape, lead-in, clearance, and axial overlap govern whether the halves seat or meet tip-to-tip. Both halves also need a secure shaft connection. The notes establish the serrated redesign, but its detailed tooth-generating sketch and dimensions aren't available in this source set.

The relevant performance question was repeatable seating after independent auger stops, followed by torque transfer. A single assembled connection could not address the original failure mode. The record doesn't supply a measured failure rate or a controlled old-versus-new engagement series, so I've not assigned one to the redesign.

The lift, disk, and coupling now had complementary jobs: separate the drive, select a hopper, and reconnect to transmit torque. That relationship dictated the later application's order of operations. It also explained why changing only actuator travel or motor speed would not solve a misregistered engagement face.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R23_replace_the_angle_sensitive_drive_coupling_with_serrated_mating_teeth.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
