# J02 Construct the first hopper, adapter, and bottom-feeder CAD

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I modeled the first complete single doser as a set of related parts: a powder holder, a tube adapter, and a bottom feeder. The purpose was to create a physical route from the loaded hopper to a receiving container, with enough access to assemble the auger and remove powder-contact components.

I treated cleaning access and shaft alignment as design requirements from the beginning. Separate parts made it possible to change an interface without redrawing the entire machine, but each added joint also created another place for residue or misalignment. The holder, adapter, and feeder therefore had to work as an assembly rather than as three attractive individual models.

The archived V1 features preserve the construction order below. They show the profiles and feature settings behind the model, including dimensions that would be invisible in a finished assembly view. These are nominal CAD dimensions for this early revision; I have not substituted them for measurements of the later printed machine.

## Technical detail

The V1 Part Studio contains three main groups: powder holder, tube adapter, and bottom feeder. The holder is built through Sketch 2 and Extrude 1, the adapter through Sketch 3 and Extrude 2, and the feeder through subsequent sketches, extrusions, and Revolve 1. Separating these features preserved the construction of each interface while keeping them in one assembly context.

The holder starts with concentric circular geometry on the Front plane. The displayed sketch diameters are approximately 1.476 in and 1.777 in. Those values correspond to about 37.49 mm and 45.14 mm; their radial difference is about 3.82 mm. This is the early holder's wall geometry, not a claim that the eventual hopper used those same dimensions. Extrude 1 creates a new solid from the selected sketch face to a blind depth of 4.724 in, approximately 119.99 mm.

The adapter is created separately. Its archived Extrude 2 uses two sketch regions, a 5.118 in blind depth, and a checked starting offset of 0.197 in. Converted for comparison, those are approximately 130.00 mm and 5.00 mm. The offset is an important part of the feature definition: omitting it when recreating the model would change where the adapter begins relative to the holder and feeder.

The bottom feeder adds geometry around the shaft end. Revolve 1 selects faces of Sketch 6 and uses an edge of that sketch as its axis. A full Add revolve merges the result into the bottom-feeder part. The profile determines the section around the axis, while the axis itself determines how that section becomes the rounded support geometry.

I treated the separate parts as one assembly problem. The adapter bore, shaft centerline, and feeder support have to remain concentric; a small offset can make a nominally suitable shaft bind. The construction views follow the holder sketch, extrusion, adapter definition, feeder revolution, and complete V1 model, retaining the relationships behind the finished shape.

The physical prototype established an assembled hopper and an outlet above the receiving container. The saved record does not contain a complete tolerance stack or dimensional inspection of that print. I therefore use V1 to explain the nominal construction and assembly relationships, with later trials supplying evidence of feeding behavior.

## Process images

![V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_sketch.jpg)

V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.

![V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_extrude.jpg)

V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.

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

## Outcome and reflection

The assembled single doser gave me a practical platform for testing fit, powder movement, and the auger drive. Modeling the support and outlet together made the next problems easier to identify: an auger could look correct in isolation and still rub or feed poorly once constrained by its housing. I moved next to producing a usable screw and checking the real printed interfaces.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R02_construct_the_first_hopper_adapter_and_bottom_feeder_cad.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
