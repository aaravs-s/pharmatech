# R02 Construct the first hopper, adapter, and bottom-feeder CAD

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J05

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Build a complete single powder path from separate CAD features and check how the printed parts must fit together.

## Design process

I built a single hopper so I could test the feeding mechanism as an assembled system. The hopper had to guide powder toward the auger while supporting the shaft and leaving a controlled outlet below. A part that looked reasonable in CAD could still bind, leak powder, or be difficult to assemble after printing.

I treated access for cleaning as part of the mechanism rather than something to add after the doser worked. The initial design aimed for removal with minimal tools. That required thinking about how the lid, funnel, enclosure, and auger came apart, and whether their interfaces created extra surfaces that could retain residue.

The assembled prototype also established the physical relationship between the outlet and the scale. The photos show the single doser above a receiving container, which is useful context for later closed-loop work. They do not establish a particular accuracy result by themselves. The purpose of this stage was to make one complete feeding path available for testing before reproducing it around the rotary disk.

## Construction and implementation detail

The V1 Part Studio preserves the model as three main groups: powder holder, tube adapter, and bottom feeder. I can trace the holder through Sketch 2 and Extrude 1, the adapter through Sketch 3 and Extrude 2, and the feeder through its subsequent sketches, extrusions, and Revolve 1. This is more useful than a finished assembly image because it records the profiles and operations that generated the interfaces.

The holder starts with concentric circular geometry on the Front plane. The displayed sketch diameters are approximately 1.476 in and 1.777 in. Those values correspond to about 37.49 mm and 45.14 mm; their radial difference is about 3.82 mm. This is the early holder's wall geometry, not a claim that the eventual hopper used those same dimensions. Extrude 1 creates a new solid from the selected sketch face to a blind depth of 4.724 in, approximately 119.99 mm.

The adapter is created separately. Its archived Extrude 2 uses two sketch regions, a 5.118 in blind depth, and a checked starting offset of 0.197 in. Converted for comparison, those are approximately 130.00 mm and 5.00 mm. The offset is an important part of the feature definition: omitting it when recreating the model would change where the adapter begins relative to the holder and feeder.

The bottom feeder introduces geometry around the shaft end rather than simply extending the holder. Revolve 1 selects faces of Sketch 6, uses an edge of that sketch as the revolution axis, performs a full revolve, and merges into the bottom-feeder part. The displayed operation is Add. A recreation needs the sketch profile and its axis together; a screenshot of the resulting rounded feature alone would not explain how it was made.

I treated the parts as one assembly problem even while modeling them separately. The adapter's bore, the shaft centerline, and the feeder support have to remain concentric. A printed holder can be dimensionally close to the CAD and still bind if the shaft is constrained off-axis. The reference images now show the holder sketch, its extrusion, the adapter definition, the feeder revolution, and the complete V1 model, so the reader can follow the construction order instead of seeing only the final shape.

For the physical prototype, the relevant checks were whether the parts could be seated without damage, whether the shaft could move through the housing, and whether the outlet could be positioned above a receiving container. The notes establish that a single assembled hopper was built; they do not record a full tolerance stack or dimensional inspection. I would put those measurements alongside the exact printed revision before presenting this early CAD as a reproduction specification.

## Image sequence

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

## Result and handoff

A complete single-feeder model and physical prototype were available for fit and powder-flow testing. The V1 parameters describe that archived revision only.

## Complete from your records

Add actual shaft diameter, printed clearances, fasteners, filament, print orientation, and measured rather than nominal part dimensions.

[IMAGE PLACEHOLDER: Dimensioned exploded view or assembly photograph showing how the V1 interfaces seated.]

[IMAGE PLACEHOLDER: Close-up of shaft support and housing clearance with the printed revision identified.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
