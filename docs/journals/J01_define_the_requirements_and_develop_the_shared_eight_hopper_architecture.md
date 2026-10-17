# J01 Define the requirements and develop the shared eight-hopper architecture

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I began by breaking automated powder compounding into a sequence I could build and test: choose an ingredient, move it to a dispensing position, add a requested mass, and stop using feedback from a scale. I organized the work into five milestones so the single-powder mechanism could be tested before I committed to a complete carousel.

My initial requirements were eight powder positions, a 100 g capacity per doser, a 50 by 50 by 50 cm operating envelope, and a final mass within 3% of the requested dose. These were design targets. I selected sugar, salt, cocoa, cinnamon, baking soda, cornstarch, powdered sugar, and flour because their different flow behavior would expose weaknesses that one easy material could hide.

The central layout decision was to share the active drive hardware at one dispensing station. Putting an auger motor and a separate agitation motor on every hopper could require sixteen motors. A shared station reduced that duplication, but introduced a harder mechanical interface: the drive had to disengage before the disk rotated and reconnect afterward. I accepted that tradeoff and focused first on one complete powder path.

## Technical detail

I separated the ingredient-selection problem from the mass-measurement problem. The disk chooses which powder path sits over the receiving container; the auger controls movement through that path; the scale measures the consequence of that motion. This distinction matters because selecting the correct hopper does not guarantee the correct mass, and controlling motor steps does not establish how much a particular powder actually dispensed.

The first architecture therefore had three interfaces to resolve: the hopper-to-feeder connection, the rotating disk-to-frame support, and the stationary motor-to-rotating auger engagement. Each powder retained its own contact path. Sharing a drive motor could reduce electrical duplication without requiring different ingredients to pass through the same auger. The contact surfaces would still need cleaning and inspection; independent paths alone do not demonstrate an absence of contamination.

For the eight-position layout, I used equal angular spacing as the starting constraint. A full revolution divided by eight gives 45 degrees per station. The later archived disk makes this concept concrete: eight pockets surround the central axis. I had to account for the hopper diameter, radial position, room around the center attachment, and the space needed by the fixed drive station. Those dimensions are coupled: enlarging a hopper can force a larger disk or reduce the material between stations.

I also distinguished capacity from dosing range. A 100 g hopper-capacity target describes how much material the hopper should hold; it does not by itself validate a 100 g dispensing run. Likewise, a 3% accuracy target needs a specified requested mass. At 5 g, 3% permits 0.150 g of error, while at 0.055 g it permits only 0.00165 g. I needed a test plan that included both useful larger doses and the difficult small-dose case rather than treating the percentage as one universal setting.

The shared drive station became the main architectural tradeoff. It reduced the number of motors carried around the carousel, but required reliable vertical engagement and disengagement. I deferred the complete carousel build while testing one powder path. That left a practical next step: obtain a printable single doser and learn whether its interfaces and powder movement were good enough to reproduce eight times.

## Process images

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

## Outcome and reflection

I finished this stage with a defined architecture and a useful order of development: prove one doser, add mass feedback, then reproduce the feeding station around the carousel. The largest lesson was that reducing the motor count transferred complexity into alignment and engagement. Those interfaces became design problems to solve deliberately, rather than details to leave until final assembly.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R01_define_the_requirements_and_develop_the_shared_eight_hopper_architecture.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
