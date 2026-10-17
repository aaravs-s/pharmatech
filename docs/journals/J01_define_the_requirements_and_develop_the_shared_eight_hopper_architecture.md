# J01 Eight hoppers, but start with one

*Milestone 1 | Retrospective build notes*

Eight hoppers sounded manageable until I started counting the motors. One for the auger and another for agitation on each hopper would mean sixteen motors. Then all the wiring, mounting, and weight that came with them. I didn't want to build that much hardware before knowing whether one feeder even worked properly.

So I settled on a carousel with a shared drive station. Rotate the selected powder into position over the scale, engage the drive, dispense, then move on. Simple enough to describe. The awkward bit was already there, though: the motor would have to disconnect and reconnect every time the disk moved. Saving motors was going to make that connection much more important.

![Early eight-position solid rotary disk concept from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_2.jpg)

Early eight-position solid rotary disk concept from the M1 notes.

I wrote down the targets: eight positions, 100 g capacity per doser, a 50 x 50 x 50 cm envelope, and final mass within 3%. I also chose the eight test powders: sugar, salt, cocoa, cinnamon, baking soda, cornstarch, powdered sugar, and flour. I wanted differences in behavior, because a machine that only worked with sugar wouldn't tell me much about the other ingredients.

For now, one powder path. A hopper, an auger, an outlet, and somewhere for the powder to land. I could come back to the full disk once there was something worth copying eight times.

## Layout notes

I kept coming back to three separate jobs. The disk selects the powder, the auger moves it, and the scale tells me what arrived. Getting the right hopper into position won't make its dose right. Counting screw steps won't tell me the mass unless the powder behaves consistently enough, which is the thing I still needed to test.

That left three mechanical connections to work through: hopper to feeder, disk to frame, and fixed drive to the auger on the rotating disk. Each powder would keep its own contact path. Sharing the drive didn't mean sharing one screw between ingredients, and it didn't remove the cleaning work on those separate paths.

Eight equally spaced stations means 45 degrees between them. The later disk model makes the layout easier to see, but even at the concept stage the dimensions pulled on each other. Larger hoppers need more room around the disk. They also leave less material between stations and less space near the fixed drive and center attachment.

The 100 g target was hopper capacity. It wasn't evidence that a 100 g dispense worked. The percentage target also hides how different the small doses are: at 5 g, 3% gives 0.150 g of room; at 0.055 g it gives only 0.00165 g. I needed both ends in the testing plan rather than one comfortable example that made the percentage look easy.

I kept the full carousel behind the single feeder in the build order. A shared station saved motors, but it also depended on vertical clearance and repeatable engagement. Those were already real design obligations. I wanted one powder path worth repeating before I committed to the larger structure.

## More views

![Early rotary and fixed-drive concept in top view.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_10.jpg)

Early rotary and fixed-drive concept in top view.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

## First build target

The layout was taking shape, but there was still a lot hidden in the word 'engage.' The drive couldn't just sit permanently on one shaft anymore. I put that problem aside long enough to get one doser built; making eight untested feeders would only multiply whatever was wrong with the first one.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R01_define_the_requirements_and_develop_the_shared_eight_hopper_architecture.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
