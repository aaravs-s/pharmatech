# J24 Getting the separate mechanisms onto one frame

*Milestone 4 | Retrospective build notes*

I built the frame from aluminum extrusion, cutting the members with an electric saw and assembling the structure around the mechanisms. The BOM lists 3030 T-slot parts and connectors. This was where the project stopped being a set of things that could sit separately on the bench.

The alignment chain was pretty unforgiving. Motor to auger, auger and hopper to outlet, outlet to receiving cup, cup on the scale. Moving one mounting position could affect several of those relationships.

![V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_sketch.jpg)

V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.

![V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_rails.jpg)

V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.

The screen and electronics needed places too. I wanted the controls reachable, but not at the cost of blocking powder loading, cleaning access, or the drive's raised space. Everything that looked like spare room in one isolated CAD model was potentially needed by something else.

The archived frame sequence below shows the layout, rails, uprights, and plates. Those are nominal design dimensions. I don't have the complete physical cut list or measured overall envelope in this record. The assembly photo is the bridge to the actual build, not a substitute for every fitting adjustment made during it.

## Frame construction notes

The V18 Superstructure studio begins with Sketch 1 on the Top plane, containing the frame layout and repeated rail and attachment geometry. Visible dimensions include 50 and 35 in the centimetre-based studio. Extrude 1 creates the first base rail solids from multiple selected sketch faces at a 3 cm depth.

Subsequent features build the structure upward and add plates. Extrude 3 uses selected Sketch 1 regions at a 0.5 cm depth, with existing uprights and new base plate geometry visible in the preview. Further sketches, extrusions, and mirrors lead to the saved superstructure, preserving the order from layout to rails, uprights, and plates.

Extrude 2 selects four faces of Sketch 1, creates New solids, and uses a 48 cm blind depth for the uprights. That is the archived CAD member height. Attachments and supports can extend the overall machine beyond a nominal rail length, so it doesn't independently establish the measured assembled envelope.

Integration brought several alignment requirements together. The disk axis had to be supported by the frame, the selected hopper outlet had to sit over the receiving container, and the lifted motor's axis had to meet the auger coupling when lowered. The scale also needed access for the cup and a support arrangement that didn't mechanically interfere with the powder path.

## Building up the frame

![V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_baseplates.jpg)

V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.

![V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_complete.jpg)

V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.

![V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_uprights.jpg)

V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

The machine had an overall structure now. That made the next software work less abstract: a slot number had to correspond to the hopper under a real lifted drive, above a real cup. Good-looking packaging wasn't enough if that chain of alignment didn't survive motion.

<details>
<summary>Notes added while reconstructing this entry</summary>

I used the 3030 extrusion and connectors identified in the BOM, cutting and assembling the frame as described in M4. The saved CAD contains nominal design dimensions; the fabrication record doesn't preserve a complete measured cut list, kerf allowances, and bracket offsets. Those remain limits on dimensional reproduction from this account alone.

The frame also carried the screen and electronics. Their placement affected control access, visibility of mass feedback, removal of contact parts, and wiring service. The later full assembly CAD shows one populated hopper and linked or mate warnings. It records packaging, without constituting a resolved simulation of a fully loaded eight-hopper machine.

The physical assembly photograph shows the carousel and drive packaged into the frame. The archived construction views provide the preceding CAD stages, while photographs of every physical installation step aren't preserved. I kept those two forms of evidence separate rather than treating a final view as a record of frame squaring and every fitting adjustment.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R24_construct_the_extrusion_frame_and_integrate_the_carousel_scale_lift_and_screen.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
