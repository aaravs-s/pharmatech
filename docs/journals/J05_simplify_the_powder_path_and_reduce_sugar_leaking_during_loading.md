# J05 Simplify the powder path and reduce sugar leaking during loading

*Milestone 1 | Personal retrospective journal*

## Design and iteration

After working through the detachable interfaces, I reconsidered whether the hopper and funnel needed to be separate. Both components still had internal surfaces to clean, and the joint added recesses and assembly work. Combining the funnel and enclosure reduced the number of parts and removed one interface from the powder path.

I also explored an integrated rotary-disk concept containing eight hopper cavities. That concept belonged to the early solid carousel; the supporting structure changed again later. At this stage, the useful idea was reducing unnecessary interfaces while continuing to test one feeder.

Sugar exposed a separate mechanical problem. It moved readily, but some escaped from the outlet during loading before I intentionally rotated the auger. I narrowed the opening near the auger exit to resist this passive flow while retaining a route for material driven by the screw. My milestone record describes that change resolving the immediate loading problem. It did not establish a leakage rate across different fill levels or powders.

## Technical detail

The removable hopper was initially a means to make cleaning easier, not an end in itself. I revisited it after the thread and locking iterations. If both the hopper and funnel still needed their internal surfaces wiped, separation could add cleaning work at the joint instead of reducing it. Combining the funnel and enclosure reduced the number of parts and removed an interface from the powder path.

The early integrated-cavity concept appears in the solid carousel. The later skeletal two-plate structure is a subsequent revision with a different support arrangement. Comparing them preserves the evolution of the machine: reducing interfaces was an early design direction, while the eventual carousel continued to change during integration.

Sugar exposed another issue during loading. Material escaped from the downstream end before the auger was intentionally turning. That was uncontrolled discharge, so adjusting a software stop threshold would not address it. The mechanical path needed enough resistance to retain the powder while the machine was idle and being filled.

I narrowed the opening at the auger end according to the milestone notes. The aim was to restrict the bypass path through which sugar could fall immediately, while retaining a route for material pushed by the screw. This connects outlet geometry to the intended control model: the scale loop is most useful when auger motion is the main cause of additional material entering the cup.

My milestone notes report that narrowing the end addressed the immediate sugar-loading spill and that sugar did not require agitation in those trials. The record contains neither the before-and-after aperture dimensions nor a measured leakage series. I regard the result as a practical response to the observed loading problem, with performance across other materials left to their own tests.

The outcome was a simpler contact path and improved control over sugar before motion began. Cornstarch then challenged the same geometry in the opposite way: instead of passing too easily, it clumped, jammed, and left material untouched. That gave the next update a concrete reason to change the flights and add agitation.

## Process images

![Cross-section CAD illustrating the internal hopper, auger path, and base.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_8.jpg)

Cross-section CAD illustrating the internal hopper, auger path, and base.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

## Outcome and reflection

I left this iteration with a simpler contact path and better control of sugar during loading. The important distinction was between powder released by a command and powder falling out while the machine was idle. Feedback control could regulate the former, but the latter first required a mechanical correction. Cornstarch then exposed the opposite problem: material that would not move consistently enough.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R05_simplify_the_powder_path_and_reduce_sugar_leaking_during_loading.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
