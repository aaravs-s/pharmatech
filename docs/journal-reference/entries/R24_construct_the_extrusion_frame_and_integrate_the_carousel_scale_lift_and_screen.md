# R24 Construct the extrusion frame and integrate the carousel, scale, lift, and screen

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J35, J36

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Place the mechanisms in one supported assembly while preserving alignment, access, and the required envelope.

## Design process

I built the superstructure from aluminum extrusion to connect the rotary disk, drive station, scale, and electronics into one machine. The milestone notes describe cutting the extrusions with an electric saw and assembling them around the required operating volume.

The BOM lists 3030 T-slot extrusion, corner connectors, and T-nuts. The CAD view shows upright supports, base members, braces, and mounting plates. These parts established the relative positions of the disk and lifting motor, which matters because a coupling can only reengage reliably if the structure holds that alignment.

This update needs the actual cut list and fastener arrangement. A general picture of the frame is useful, but it does not tell another builder how long each member was or where the brackets were positioned. I would also note any adjustments made during assembly, especially if the manufactured frame differed from the nominal CAD dimensions.

I assembled the major subsystems into the frame. The rotary disk was supported near the center, the lifting drive sat above the active hopper position, and the receiving container rested on the scale below. I also placed the screen and control electronics where they could be accessed on the machine.

The full assembly CAD and physical photo show the overall packaging. The useful design relationship is the chain of alignment from motor shaft to auger, hopper outlet, receiving container, and scale. Each component can work individually while the combined machine still fails if that chain is offset or the disk cannot clear the fixed hardware.

I would explain the assembly order and the clearances I checked using the built revision. That includes access to the hopper, the motor's raised envelope, the scale's usable area, and wire routing around moving parts. The CAD screenshot supports the arrangement; a claim that there were no collisions needs the actual motion checks or operation footage.

## Construction and implementation detail

The V18 Superstructure studio preserves a construction sequence before the complete assembly. Sketch 1 is on the Top plane and includes the frame layout and repeated rail/attachment geometry. The visible layout dimensions include 50 and 35 in the centimetre-based studio. Extrude 1 selects multiple faces from that sketch and creates new solids at a depth of 3 cm, yielding the first base rails in the construction view.

Later extrusions add the upright members and plates. Extrude 3 uses selected regions of Sketch 1 at a depth of 0.5 cm; the preview shows the existing uprights and newly added base plate geometry. The tree continues through additional sketches, extrusions, and mirrors before the saved superstructure. These intermediate views now show an actual progression from a flat layout to rails, uprights, plates, and the complete structure.

Extrude 2 provides the upright height directly: it selects four faces of Sketch 1, creates New solids, and uses a 48 cm blind depth. The saved V18 frame view follows the rail, upright, and plate previews. These values describe the archived CAD; the assembled outer height still needs measurement because supports and attached parts can extend beyond a nominal rail length.

The BOM identifies 3030 T-slot aluminum extrusion and connectors. M4 notes record cutting extrusion with an electric saw and assembling the frame. The CAD dimensions are a design record; the actual cut list, saw kerf allowance, connector offsets, and measured assembled size belong to the fabrication record. A rail's nominal length does not necessarily equal the outer machine dimension once brackets and attachments are included.

Integration brought several alignment requirements together. The disk axis had to be supported by the frame, the selected hopper outlet had to sit over the receiving container, and the lifted motor's axis had to meet the auger coupling when lowered. The scale also needed access for the cup and a support arrangement that did not mechanically interfere with the powder path.

The frame carried the screen and electronics as well as the mechanisms. Their placement affected whether the user could reach controls, see mass feedback, remove powder-contact parts, and inspect wiring. The later full assembly CAD contains one populated hopper and linked/mate warnings; it is useful for layout but should not be called a fully resolved eight-hopper simulation simply from its appearance.

The physical assembly photograph connects the layout to the built machine. To finish the process record, I would add photos while the frame was being squared, the disk support was mounted, the scale station was aligned, and the lift was positioned. A final complete-machine photograph cannot replace those installation steps or show which dimensions were adjusted during fitting.

## Image sequence

![V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_sketch.jpg)

V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.

![V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_rails.jpg)

V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.

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

## Result and handoff

The frame and mechanisms were integrated physically; V18 provides intermediate CAD stages. Actual cut lengths, alignment measurements, and resolution of CAD warnings still need the build record.

## Complete from your records

Add the actual cut list, assembled envelope, extrusion connections, mounting fasteners, scale isolation, and alignment adjustments.

[IMAGE PLACEHOLDER: Extrusion cut list and frame assembly photos before the carousel/lift/electronics were installed.]

[IMAGE PLACEHOLDER: Measurements of disk-to-scale alignment and motor-to-auger alignment at the engaged position.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
