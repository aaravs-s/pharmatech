# J21 Back to the carousel, and a lot less solid material

*Milestone 4 | Retrospective build notes*

Once the single doser had real work behind it, I went back to the carousel. The early model was a solid disk with eight pockets. The later one opened that up into a much lighter-looking plate-and-rib arrangement. It was a fairly visible change, but the feature sequence is more useful than just putting two finished renders beside each other.

The original blank was 330 mm across and 60 mm thick. That's a substantial piece of geometry to carry into a rotating assembly. The pocket layout also constrained what could change: make a hopper opening bigger and I lose material between stations or near the edge.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

The later model kept the overall diameter but changed the pockets and supporting structure. The lightening feature reports a 42.4% weight reduction in CAD. I don't have a weighed before-and-after print comparison or a stiffness test, so that number stays a CAD result.

I wanted the construction stages kept visible here: the circle and blank, the pockets, then the later plate, ribs, and mirror. Otherwise it's too easy to make the carousel sound like one decision, when the saved geometry shows a fairly different support arrangement by the later revision.

## The saved construction sequence

The V5 Rotary Disk studio starts with Sketch 1, a 33 cm diameter circle on the Top plane. Extrude 1 makes a new solid with a 6 cm blind depth, giving a nominal 330 mm diameter and 60 mm thickness. That is the early blank, rather than the later installed open structure.

Sketch 2 is on a face of that blank and lays out the eight pockets. Its displayed dimensions include a 12 cm center-to-pocket radial dimension and a 7 cm pocket diameter. Eight equally spaced pocket centers imply 45-degree spacing. For this geometry, adjacent centers are approximately 91.84 mm apart, calculated as twice the 120 mm radius times sin(22.5 degrees). A 70 mm pocket leaves approximately 21.84 mm between adjacent circular boundaries before any further cuts.

The outer edge also has limited material around each pocket. The disk radius is 165 mm; the station radius plus pocket radius is 120 + 35 = 155 mm. The nominal radial material outside a pocket is therefore about 10 mm at its outermost point. These calculations are geometric interpretations of this archived sketch, not finite-element results or measurements of a printed disk.

Extrude 2 removes the eight regions of Sketch 2 to a blind depth of 3 cm. The sequence shows the solid blank, pocket layout, cut preview, and saved pocketed model. In this revision the pocket feature selects faces from one sketch; the construction isn't inferred from the appearance of eight completed recesses.

Rotary Disk V2 is a later open supporting arrangement. I compared its saved state with the earlier solid construction so the two revisions remained distinguishable. The change visibly altered the load-carrying material and access around the hopper stations, while measured stiffness and print-mass comparisons aren't preserved in the record.

The V18 Rotary Disk V2 archive gives more specific detail for the open structure. Sketch 1 retains a displayed 33 cm outer diameter but shows an 8.5 cm pocket diameter, larger than the earlier 7 cm pockets. Extrude 1 creates an initial plate at 0.635 cm depth, or 6.35 mm. The custom Part Lightening feature uses Manual mode, selects a face of Extrude 2 and 32 rib lines from Sketch 2, and sets wall and rib thicknesses to 0.5 cm each. Its tool-diameter parameter is 0.67 cm and its blind cut depth is 2.5 cm. The feature reports a 42.4% part-weight reduction in CAD; that isn't a measured weight reduction of the printed machine. Plane 1 is offset 3 cm from the selected face of Sketch 1. Mirror 1 uses Part mirror in Add mode, selects Part 2, mirrors about Plane 1, and lists Part 1 as the merge scope. Those references define the repeated plate arrangement. The new views preserve the sketch, initial plate, lightening parameters, mirror reference, mirror operation, and saved disk state separately.

## Pocket cuts, ribs, and the later plates

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

There was now much more to the disk than repeating one hopper eight times. Pocket size, material between stations, support, and drive alignment all had to coexist. The open model gave the assembly its later form; the frame and lifted drive still had to make that form useful.

<details>
<summary>Notes added while reconstructing this entry</summary>

Support, fastening, plate spacing, hopper seating, and the connection to the disk drive are assembly constraints in addition to the modeled pocket geometry. The CAD sequence explains how the saved parts were constructed, while the physical photograph establishes that a carousel assembly was built. Neither alone supplies a loaded deflection or indexing-error measurement.

</details>

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R21_build_the_solid_eight_pocket_carousel_and_evolve_it_into_an_open_two_plate_structure.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
