# R05 Simplify the powder path and reduce sugar leaking during loading

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J08, J09

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Reduce unnecessary cleaning interfaces and address discharge that occurs before commanded auger motion.

## Design process

I reconsidered the assumption that the hopper and funnel needed to be separate. Even if the hopper detached easily, the interface still introduced extra surfaces and recesses to clean. Combining the funnel and enclosure could reduce the part count, filament use, print time, and assembly steps.

The milestone notes then describe extending that simplification to an integrated rotary-disk concept with eight hopper cavities. That was a design direction at this stage, not evidence that the later physical carousel used an identical one-piece geometry. The later CAD and assembly photos show additional evolution, including a more open supporting structure.

The useful lesson from this update was that making a part removable does not automatically make the machine easier to clean. I needed to judge how much residue could remain at each interface and how the full powder path could be accessed. Reducing interfaces was one way to simplify the geometry, while the final cleaning procedure would still need to address the auger and internal surfaces.

Sugar was a useful first test material because it moved readily through the prototype. The auger produced relatively consistent movement, but loading sugar into the hopper exposed an unwanted behavior: some powder fell out of the outlet before I intentionally dispensed it.

I modified the auger configuration to create a narrower opening near the exit. The aim was to add resistance to the passive flow without preventing the auger from moving powder when it rotated. According to the notes, that change addressed the immediate spill during loading. This is different from tuning a motor stopping threshold; it changes the mechanical path that powder can take while the drive is stationary.

The update needed to preserve both sides of that tradeoff. An outlet that is too open can leak free-flowing material, while an outlet that is too restrictive can increase the chance of packing or jamming. I used sugar to assess the immediate-flow problem before checking whether the same geometry was appropriate for finer, more cohesive powders.

## Construction and implementation detail

The removable hopper was initially a means to make cleaning easier, not an end in itself. I revisited it after the thread and locking iterations. If both the hopper and funnel still needed their internal surfaces wiped, separation could add cleaning work at the joint instead of reducing it. Combining the funnel and enclosure reduced the number of parts and removed an interface from the powder path.

The notes also describe an integrated disk with eight hopper cavities. That direction appears in the early solid carousel, but it should not be treated as the final structural arrangement. The later skeletal two-plate disk is a further iteration. I would keep both states in the journal: the integrated cavity concept explains the decision to reduce interfaces, and the later open structure explains how the larger machine changed after considering weight and assembly.

Sugar exposed another issue during loading. Material escaped from the downstream end before the auger was intentionally turning. That was uncontrolled discharge, so adjusting a software stop threshold would not address it. The mechanical path needed enough resistance to retain the powder while the machine was idle and being filled.

I narrowed the opening at the auger end according to the milestone notes. The aim was to restrict the bypass path through which sugar could fall immediately, while retaining a route for material pushed by the screw. This connects outlet geometry to the intended control model: the scale loop is most useful when auger motion is the main cause of additional material entering the cup.

The record states that the narrower end solved the immediate sugar-loading problem and that sugar did not require agitation for the trials described. It does not establish a general zero-leakage guarantee, nor does it give the before/after aperture dimensions. Those are the critical missing items for recreation. A useful image sequence would show the original outlet profile, the narrowing feature, the final section, and equal loading trials with the motor stopped.

The outcome was a simpler contact path and improved control over sugar before motion began. Cornstarch then challenged the same geometry in the opposite way: instead of passing too easily, it clumped, jammed, and left material untouched. That gave the next update a concrete reason to change the flights and add agitation.

## Image sequence

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

## Result and handoff

The design moved toward fewer powder-path interfaces, and the sugar outlet was narrowed to reduce immediate escape during filling. The later disk revision remained a separate decision.

## Complete from your records

Supply the actual original/revised outlet dimensions, fill mass, idle observation duration, and which integrated geometry was printed.

[IMAGE PLACEHOLDER: Original sugar outlet sketch, the feature reducing its opening, and a section of the revised outlet.]

[IMAGE PLACEHOLDER: Before/after loading test with the auger stationary; show any collected leakage mass.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
