# R19 Validate 5 g dispensing of the four cohesive powders

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J28

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Check whether agitation and the revised feed path provide useful dosing results with powders prone to clumping.

## Design process

I tested baking soda, cornstarch, powdered sugar, and all-purpose flour with the feeding behavior developed for clumpier powders. The notes describe inconsistent release, including occasional clumps followed by much smaller additions. The agitator helped keep material moving toward the auger.

For the 5 g target, the recorded final masses were 4.994 g, 4.991 g, 4.996 g, and 4.993 g respectively. Recalculating absolute percentage error gives 0.12%, 0.18%, 0.08%, and 0.14%. The original sheet lists flour as 0.18%, which does not match its recorded 4.993 g mass; that arithmetic should be checked against the original measurement.

The listed durations were 5:01 for baking soda, 4:55 for cornstarch, 4:57 for powdered sugar, and 4:39 for flour. These runs support the statement that all four reached the 3% target at 5 g in the recorded tests. They also show the time cost of the slower feeding and finishing behavior, without proving the same result across the entire intended dose range.

## Construction and implementation detail

The test sheet records baking soda at 4.994 g in 5:01, cornstarch at 4.991 g in 4:55, powdered sugar at 4.996 g in 4:57, and flour at 4.993 g in 4:39 for a 5.000 g target. Recomputed absolute errors are 0.12%, 0.18%, 0.08%, and 0.14%. The sheet lists flour as 0.18%, which does not match 4.993 g; that arithmetic discrepancy needs confirmation against the original reading.

All four recorded masses are inside 3% at 5 g, but their roughly five-minute durations show the performance cost of the feeding behavior. The behavior notes describe clumps, intermittent discharge, and the agitator helping move powder through the hopper. A run can reach a suitable final mass while still pausing or delivering unevenly along the way, so the result should include both final accuracy and the observed transport behavior.

This is where the earlier mechanical diagnosis becomes relevant. Larger flights addressed the feed-space problem, and agitator reach addressed powder left outside the auger's active region. The measured final masses do not isolate how much each change contributed. To establish that, the record would need matched trials before and after one geometric change while holding the rest of the configuration constant.

The images should show the hopper after a run as well as the cup. Remaining material near the wall, powder stuck to the arm roots, or a bridge above the screw would explain why a run slowed down even if it eventually completed. The test sheet has no residual-powder measurement, so the reference includes a specific placeholder for that observation instead of calling the hopper fully cleared.

The software revision also matters here. A later controller sets a 120 s maximum dispense time, shorter than every one of these recorded durations. That later file cannot be assumed to be the program that generated the approximately five-minute results. I keep the recorded times intact and flag the revision mismatch rather than rewriting the results to fit the newest code.

The outcome supports an individual 5 g dosing result for each tested cohesive powder. It does not establish general flow behavior for other materials, repeatability across refill levels, or an autonomous recipe containing all four. Those are separate tests with separate evidence.

## Image sequence

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

## Result and handoff

The four recorded cohesive-powder runs met 3% at 5 g, but took about five minutes. Flour's reported error and the code revision used for these runs need reconciliation.

## Complete from your records

Match test date and software revision, confirm flour's raw reading, and add observations of bridging, jams, hopper residue, and repeated trials.

[IMAGE PLACEHOLDER: Loaded hopper, mid-run clumping/agitation, post-run residual powder, and final mass for each powder.]

[IMAGE PLACEHOLDER: Phase/time log from the actual program used for the long tests; do not substitute the later 120 s timeout version.]

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
