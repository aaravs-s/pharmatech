# J02 Getting the first powder path into CAD

*Milestone 1 | Retrospective build notes*

I started with the holder, tube adapter, and bottom feeder. Nothing especially dramatic yet, but these were the parts that had to agree with each other. The shaft centerline mattered across all three. Getting each part to look right separately wasn't going to help if they forced the auger off-axis when assembled.

I also wanted to be able to take the feeder apart. Powder would touch the hopper, screw, outlet, and the joints between them, so cleaning couldn't be something I considered after everything was mounted. At this point, separate parts seemed like a sensible way to keep access and make revisions less painful.

![V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_sketch.jpg)

V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.

![V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_extrude.jpg)

V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.

The V1 model below is useful because I can follow the actual features instead of trying to explain the whole shape from an assembly screenshot. Sketch, extrusion, adapter, then the geometry around the lower shaft support. The dimensions are for this early model. The design kept changing after it.

Having a complete path to assemble was the goal here. I needed something physical to push back against the CAD assumptions, especially around fit and shaft support.

## The V1 features

The V1 Part Studio contains three main groups: powder holder, tube adapter, and bottom feeder. The holder is built through Sketch 2 and Extrude 1, the adapter through Sketch 3 and Extrude 2, and the feeder through subsequent sketches, extrusions, and Revolve 1. Separating these features preserved the construction of each interface while keeping them in one assembly context.

The holder starts with concentric circular geometry on the Front plane. The displayed sketch diameters are approximately 1.476 in and 1.777 in. Those values correspond to about 37.49 mm and 45.14 mm; their radial difference is about 3.82 mm. This is the early holder's wall geometry, not a claim that the eventual hopper used those same dimensions. Extrude 1 creates a new solid from the selected sketch face to a blind depth of 4.724 in, approximately 119.99 mm.

The adapter is created separately. Its archived Extrude 2 uses two sketch regions, a 5.118 in blind depth, and a checked starting offset of 0.197 in. Converted for comparison, those are approximately 130.00 mm and 5.00 mm. The offset is an important part of the feature definition: omitting it when recreating the model would change where the adapter begins relative to the holder and feeder.

The bottom feeder adds geometry around the shaft end. Revolve 1 selects faces of Sketch 6 and uses an edge of that sketch as its axis. A full Add revolve merges the result into the bottom-feeder part. The profile determines the section around the axis, while the axis itself determines how that section becomes the rounded support geometry.

I treated the separate parts as one assembly problem. The adapter bore, shaft centerline, and feeder support have to remain concentric; a small offset can make a nominally suitable shaft bind. The construction views follow the holder sketch, extrusion, adapter definition, feeder revolution, and complete V1 model, retaining the relationships behind the finished shape.

## The rest of the V1 construction

![V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_adapter_extrude.jpg)

V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.

![V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_feeder_revolve.jpg)

V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.

![V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_complete.jpg)

V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.

![Physical single-hopper prototype during powder handling.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_4.jpg)

Physical single-hopper prototype during powder handling.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

There was now a single doser I could put above the receiving container. That felt like a much more useful starting point than adding more of the carousel. Next was the screw itself, and finding out which parts of the nice concentric model survived printing and assembly.

<details>
<summary>Notes added while reconstructing this entry</summary>

The physical prototype established an assembled hopper and an outlet above the receiving container. The saved record doesn't contain a complete tolerance stack or dimensional inspection of that print. I use V1 to explain the nominal construction and assembly relationships, with later trials supplying evidence of feeding behavior.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R02_construct_the_first_hopper_adapter_and_bottom_feeder_cad.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
