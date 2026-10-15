# R21 Build the solid eight-pocket carousel and evolve it into an open two-plate structure

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J31

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Turn the rotary concept into reproducible CAD and then revise its structure for the assembled machine.

## Design process

I returned to the rotary architecture after developing the single-doser mechanism. The milestone images show an early disk with eight cavities and a later, more open structure that supports the hopper positions. Comparing those views makes the physical evolution much clearer than using only the final machine photo.

The multi-doser assembly needed to maintain alignment around the disk while allowing room for the feeding components, drive station, and supports. The later view includes large openings and a network of structural material. That geometry is visible in the CAD, but the notes do not explicitly state every reason for changing from the earlier disk, so I need to add my actual reasoning about mass, printing, access, or stiffness.

This update should describe the revision I made rather than merely announcing that the carousel was finished. The dimensions, support locations, and interfaces explain how one tested doser became a repeatable station on the larger mechanism. It is also the right place to clarify which parts were integrated into the disk and which were separate in the manufactured design.

## Construction and implementation detail

The V5 Rotary Disk studio now supplies a full construction sequence. Sketch 1 places a 33 cm diameter circle on the Top plane. Extrude 1 creates a new solid with a blind depth of 6 cm. This is a substantial 330 mm diameter, 60 mm thick blank, so its material volume and rotating mass become relevant when moving from a concept to a physical build.

Sketch 2 is on a face of that blank and lays out the eight pockets. Its displayed dimensions include a 12 cm center-to-pocket radial dimension and a 7 cm pocket diameter. Eight equally spaced pocket centers imply 45-degree spacing. For this geometry, adjacent centers are approximately 91.84 mm apart, calculated as twice the 120 mm radius times sin(22.5 degrees). A 70 mm pocket leaves approximately 21.84 mm between adjacent circular boundaries before any further cuts.

The outer edge also has limited material around each pocket. The disk radius is 165 mm; the station radius plus pocket radius is 120 + 35 = 155 mm. The nominal radial material outside a pocket is therefore about 10 mm at its outermost point. These calculations are geometric interpretations of this archived sketch, not finite-element results or measurements of a printed disk.

Extrude 2 removes the eight sketch regions to a blind depth of 3 cm. The recovered view shows the blank first, then the pocket layout, then the removed pockets and the completed saved model. Subsequent features remain in the tree. The journal needs that order because the final eight-pocket render cannot show whether the pockets were built into one sketch, patterned, or assembled from separate components; here the archived feature explicitly selects the faces of Sketch 2.

The later Rotary Disk V2 view is a different structural state, with an open supporting arrangement rather than the same massive solid blank. M4 notes show a first and final iteration and describe the eventual multi-doser assembly. I keep the old solid construction and later arrangement side by side, with their source versions, so the design tradeoff is visible without suggesting the earliest blank was the final installed part.

The V18 Rotary Disk V2 archive gives more specific detail for the open structure. Sketch 1 retains a displayed 33 cm outer diameter but shows an 8.5 cm pocket diameter, larger than the earlier 7 cm pockets. Extrude 1 creates an initial plate at 0.635 cm depth, or 6.35 mm. The custom Part Lightening feature uses Manual mode, selects a face of Extrude 2 and 32 rib lines from Sketch 2, and sets wall and rib thicknesses to 0.5 cm each. Its tool-diameter parameter is 0.67 cm and its blind cut depth is 2.5 cm. The feature reports a 42.4% part-weight reduction in CAD; that is not a measured weight reduction of the printed machine. Plane 1 is offset 3 cm from the selected face of Sketch 1. Mirror 1 uses Part mirror in Add mode, selects Part 2, mirrors about Plane 1, and lists Part 1 as the merge scope. Those references define the repeated plate arrangement. The new views preserve the sketch, initial plate, lightening parameters, mirror reference, mirror operation, and saved disk state separately.

To recreate the later structure, the reader also needs plate thicknesses, separation, center support, fastening points, hopper seating geometry, and the connection to the disk motor. The saved CAD views do not by themselves prove loaded rigidity or successful indexing. The physical build photograph and a loaded alignment trial are the final evidence needed to connect this CAD iteration to the machine.

## Image sequence

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

![Earlier solid eight-cavity rotary disk for comparison with the open structure.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_3.jpg)

Earlier solid eight-cavity rotary disk for comparison with the open structure.

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_sketch.jpg)

V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.

![V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plate.jpg)

V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.

![V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_lightening.jpg)

V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.

![V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plane.jpg)

V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.

![V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_mirror.jpg)

V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.

![V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_complete.jpg)

V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.

![Later open rotary structure with upper and lower plates and spacers.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_1.jpg)

Later open rotary structure with upper and lower plates and spacers.

## Result and handoff

The early solid disk's sketches and cuts are recoverable, and later CAD shows a different open structure. Structural and loaded-indexing performance require physical measurements.

## Complete from your records

Identify which disk revisions were printed, actual mass/print time, final plate dimensions, fasteners, support bearings, and observed deflection/alignment.

[IMAGE PLACEHOLDER: Later two-plate geometry: generating sketches, plate/spacing features, and final assembled section if not present in the recovered sequence.]

[IMAGE PLACEHOLDER: Loaded carousel alignment/deflection check and actual printed disk comparison.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
