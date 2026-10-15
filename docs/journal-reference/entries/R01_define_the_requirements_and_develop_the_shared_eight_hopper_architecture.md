# R01 Define the requirements and develop the shared eight-hopper architecture

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J01, J02, J03

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Translate the compounding workflow into a machine layout and decide which hardware belongs on each hopper versus at the fixed dispensing station.

## Design process

I started by turning the idea of automated compounding into requirements I could design around. The machine needed to select an ingredient, dispense a requested mass, and use a scale to decide when to stop. I organized the project into five milestones so I could first prove the powder-feeding mechanism, then add feedback control, improve the single doser, expand to several powders, and finally integrate the complete sequence.

The original targets included eight powder positions, a 100 g capacity per doser, a 50 × 50 × 50 cm operating envelope, and final mass within 3% of the requested dose. I chose granulated sugar, table salt, cocoa, cinnamon, baking soda, cornstarch, powdered sugar, and flour to expose different feeding problems. Those were design targets rather than proof that every condition was already satisfied. The powder-contact geometry also needed attention because trapped residue and difficult disassembly could make an otherwise functional feeder impractical to clean.

This gave me a way to judge each iteration: does the change improve powder movement, reduce uncontrolled discharge, simplify cleaning, or help automate the sequence? It also kept me from building the entire carousel before I knew one doser would work.

I chose a rotary disk with eight hopper positions so several powders could share a dispensing station above one scale. Each powder would have its own hopper and feeding path, while the disk would bring the selected ingredient to the active position. This made the layout compact and gave the mechanism a clear route from one powder to a recipe containing several ingredients.

Eight evenly spaced positions imply 45 degrees between adjacent stations. That geometry matters later because the controller needs a repeatable relationship between a slot number and disk motion. At this point, though, the priority was the mechanical arrangement: leave room for the hopper, auger shaft, outlet, drive engagement, and receiving container. The disk also needed enough structure around the cavities to carry the loaded hoppers without distorting the alignment.

I deliberately separated the carousel concept from the first physical prototype. Printing all eight positions immediately would have repeated the same unknown feeder geometry eight times. A single doser let me test the part that actually moves the powder before committing to the larger structure.

I realized that an auger motor and agitator motor on every hopper could require sixteen motors for the eight-position machine. That would add cost, wiring, rotating mass, and maintenance points. I instead developed a shared drive concept in which the motors remain at the dispensing station and engage only the hopper currently above the scale.

The early idea used a motor for the auger and another for agitation. Later notes also explore driving both elements through a common rotating component, so the exact motor arrangement needs to be tied to the revision being described. The consistent design decision was to share the active drive hardware rather than duplicate motors around the carousel.

This made the coupling interface a central engineering problem. The disk needs to move freely while the drive is disengaged, but the shaft needs to transfer torque when a hopper reaches the active position. Angular alignment, engagement depth, and clearance could all prevent that transition. Reducing the motor count therefore simplified the overall machine while making the engagement mechanism more important.

## Construction and implementation detail

I separated the ingredient-selection problem from the mass-measurement problem. The disk chooses which powder path sits over the receiving container; the auger controls movement through that path; the scale measures the consequence of that motion. This distinction matters because selecting the correct hopper does not guarantee the correct mass, and controlling motor steps does not establish how much a particular powder actually dispensed.

The first architecture therefore had three interfaces to resolve: the hopper-to-feeder connection, the rotating disk-to-frame support, and the stationary motor-to-rotating auger engagement. Each powder retained its own contact path. Sharing a drive motor could reduce electrical duplication without requiring different ingredients to pass through the same auger. The contact surfaces would still need cleaning and inspection; independent paths alone do not demonstrate an absence of contamination.

For the eight-position layout, I used equal angular spacing as the starting constraint. A full revolution divided by eight gives 45 degrees per station. The later archived disk makes this concept concrete: eight pockets surround the central axis. I had to account for the hopper diameter, radial position, room around the center attachment, and the space needed by the fixed drive station. Those dimensions are coupled: enlarging a hopper can force a larger disk or reduce the material between stations.

I also distinguished capacity from dosing range. A 100 g hopper-capacity target describes how much material the hopper should hold; it does not by itself validate a 100 g dispensing run. Likewise, a 3% accuracy target needs a specified requested mass. At 5 g, 3% permits 0.150 g of error, while at 0.055 g it permits only 0.00165 g. I needed a test plan that included both useful larger doses and the difficult small-dose case rather than treating the percentage as one universal setting.

The shared drive station became the main architectural tradeoff. It reduced the number of motors carried around the carousel, but required reliable vertical engagement and disengagement. I deferred the complete carousel build while testing one powder path. That left a practical next step: obtain a printable single doser and learn whether its interfaces and powder movement were good enough to reproduce eight times.

## Image sequence

![Early eight-position solid rotary disk concept from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_2.jpg)

Early eight-position solid rotary disk concept from the M1 notes.

![Early rotary and fixed-drive concept in top view.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_10.jpg)

Early rotary and fixed-drive concept in top view.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

## Result and handoff

The design direction was an eight-position carousel feeding one scale through separate powder paths and a shared active drive station. These were requirements and layout decisions, not completed-system test results.

## Complete from your records

Record the original requirement sheet, intended dose range, frame envelope, hopper capacity measurement, and the actual motor count for this revision.

[IMAGE PLACEHOLDER: Original annotated system sketch showing the rotating parts, stationary drive, and receiving scale.]

[IMAGE PLACEHOLDER: Early top-view CAD layout before the disk pockets were cut; use the archived V5 sequence as a later construction reference, not a contemporaneous sketch.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
