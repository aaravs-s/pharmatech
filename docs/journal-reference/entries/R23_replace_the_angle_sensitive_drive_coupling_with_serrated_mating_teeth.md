# R23 Replace the angle-sensitive drive coupling with serrated mating teeth

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J33, J34

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Make repeated vertical engagement practical when the auger stops at different angular orientations.

## Design process

I found that simply lowering the motor onto the auger did not guarantee engagement. The first coupling arrangement required the auger and motor-side features to be at a particular relative angle. After moving to another hopper, the coupling could meet in the wrong orientation and fail to connect.

This blocked progress on the integrated system because I could not reliably drive the selected hopper. It was not just a question of transmitting torque once connected; the interface first had to make that connection from the position left by the previous operation.

The notes describe several experiments but do not list each intermediate geometry. The reference journal should preserve the actual failure and then leave room to add those versions from the CAD history or your memory. The best evidence is a close-up of the two mating faces and a clip showing what happened when the drive lowered at an unfavorable angle.

I changed the coupling interface to use serrated teeth so the motor could engage the auger across a broader range of relative shaft orientations. The milestone notes describe this as the solution reached after experimenting with the earlier connection.

The design still needed to transfer torque and seat to a predictable depth. Tooth spacing, lead-in shape, clearance, and any axial compliance determine whether the teeth guide into engagement or meet tip-to-tip. The wording in the notes says it aligned at any angle, but the journal should explain what actually enabled that behavior and what engagement tests were performed.

I would distinguish this disengaging drive interface from a conventional permanently connected flexible shaft coupling. A standard flexible coupling can accommodate some misalignment while connected; it does not automatically solve repeated disconnecting and reconnecting. Showing the mating teeth separately is necessary for another builder to understand the mechanism.

## Construction and implementation detail

The first coupling concept had an angular-registration problem. The motor-side feature and auger-side feature could mate only when they arrived at a specific orientation. The carousel selected the correct hopper, but lowering the drive did not guarantee that the coupling features lined up. The notes describe this as a roadblock because unsuccessful engagement prevented further integrated tests.

The failed assumption was that vertical alignment of the shaft axes was sufficient. It was necessary, but angular alignment and engagement depth also mattered. A coupling can appear concentric in CAD while opposing features collide when lowered. To document the failure, the journal should show at least two relative angular positions, the contact that prevented seating, and the intended fully engaged state.

The V18 auger studio preserves a keyed motor-adapter stage that makes the angular-registration issue visible. Sketch 15 lies on a face of Extrude 2 and displays a 2.5 cm circular profile. Extrude 13 adds two selected regions at 0.2 cm depth into Part 4. Sketch 13 then lies on a face of that new extrusion, displays a 2.3 cm circular boundary, and divides the engagement profile into keyed regions. Onshape marks that sketch as not fully defined. Extrude 11 adds two selected regions from it at 0.75 cm depth into Part 4. The recovered sequence now shows the base profile, base solid, keyed profile, keyed extrusion, and saved adapter separately. This geometry requires angular registration, but the archive has not been matched to the exact failed printed coupler. It is an earlier design reference, not evidence that the later serrated interface used those same dimensions.

The recorded response was to line the coupling with serrated teeth. More repeated engagement features reduce the dependence on one particular angular orientation. The notes describe the teeth as aligning at any angle, but there is no recorded sweep of every orientation, so I describe this as the design intent and reported practical solution rather than an unlimited guarantee.

The recreation details are tooth count, spacing, tooth height, flank shape, lead-in, clearance, and engagement depth. The two halves also need a secure connection to their respective shafts. Those dimensions determine whether lowering tends to guide the parts into place or press tooth tips together. The recovered photographs show the assembled drive region, but the original tooth-generating sketches and intermediate cuts have not been recovered.

The appropriate comparison is an engagement test with the earlier geometry, then the serrated revision under the same lift arrangement. I would record unsuccessful seatings, required manual adjustment, and whether the shaft can transfer torque after seating. A successful single lowering is useful evidence, but several re-engagements after independent auger stops better address the actual failure mode.

This update closes the mechanical loop of the shared-drive idea: lift provides disengagement, disk rotation selects the hopper, and the coupling provides torque transfer after the drive returns. The later recipe controller must enforce those actions in the same order. The mechanism photographs now belong alongside the explicit missing construction stages rather than standing in for the entire coupler design process.

## Image sequence

![V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_sketch.jpg)

V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.

![V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_extrude.jpg)

V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.

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

## Result and handoff

The source records replacing the orientation-sensitive interface with serrated mating teeth. Exact tooth geometry and quantified re-engagement reliability remain to be supplied.

## Complete from your records

Recover the failed and serrated CAD versions, tooth parameters, shaft retention, engagement depth, and repeated lowering/torque-transfer results.

[IMAGE PLACEHOLDER: Failed coupling profile and collision view at an unfavorable angular offset.]

[IMAGE PLACEHOLDER: Serration sketch/pattern, intermediate tooth cut, final mating section, and repeated engagement test.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
