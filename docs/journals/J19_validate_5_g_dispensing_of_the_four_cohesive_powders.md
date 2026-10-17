# J19 Test 5 g dispensing with baking soda, cornstarch, powdered sugar, and flour

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I tested baking soda, cornstarch, powdered sugar, and flour after the changes intended to help clumpier materials. The notes describe intermittent release, sometimes in clumps, and agitation helping keep powder moving toward the screw. Those behaviors could make a run slow even when its eventual final mass was close to target.

All four recorded 5 g results were within 3%, but their durations were around five minutes. I treated that as useful performance with an obvious throughput cost, rather than describing the machine as equally fast for every ingredient.

I recalculated percentage error directly from the listed masses. Flour's recorded 4.993 g gives 0.14% absolute error against 5.000 g, while the source sheet lists 0.18%. I retained the original mass and reported the arithmetic discrepancy. I also kept these trials distinct from the later controller with a 120 s timeout, which is shorter than every run in this group.

## Technical detail

The 5.000 g results were baking soda at 4.994 g in 5:01, cornstarch at 4.991 g in 4:55, powdered sugar at 4.996 g in 4:57, and flour at 4.993 g in 4:39. Recalculated absolute errors are 0.12%, 0.18%, 0.08%, and 0.14%. The source's flour percentage is inconsistent with its recorded mass, so the calculation here uses the listed 4.993 g reading.

All four final readings met 3%, while the durations exposed the cost of slower feeding and finishing. Intermittent discharge and clumps could coexist with a close final mass. I treated the time and transport observations as part of performance rather than reducing the result to a pass label.

The earlier mechanical changes addressed different regions: larger flights changed the feeding space, while agitator reach addressed powder outside the screw's active region. These final results do not isolate the contribution of either change because there is no matched one-variable comparison in the available sheet.

The record contains no measured residual-powder mass or post-run coverage series for these trials. I therefore do not interpret successful collection as proof that the hopper fully cleared or that no powder remained around walls and arm roots. Those internal states are distinct from the final cup reading.

The later controller's 120 s maximum dispense duration is shorter than all four of these runs. I kept their original recorded times and did not attribute them to that file. Version matching matters here because a configuration that times out after two minutes could not complete an uninterrupted five-minute test under the same limit.

The outcome supports an individual 5 g dosing result for each tested cohesive powder. It does not establish general flow behavior for other materials, repeatability across refill levels, or an autonomous recipe containing all four. Those are separate tests with separate evidence.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Baking soda | 5 | 4.994 | 0.12% | 5:01 | Yes |
| Cornstarch | 5 | 4.991 | 0.18% | 4:55 | Yes |
| Powdered sugar | 5 | 4.996 | 0.08% | 4:57 | Yes |
| All purpose flour | 5 | 4.993 | 0.14% | 4:39 | Yes |

## Process images

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

## Outcome and reflection

The tests supported a successful individual 5 g result for each cohesive powder, with substantially longer dispensing times than sugar or salt. They did not isolate the contribution of each mechanical change or establish repeatability across hopper fill levels. The next challenge was whether the same system could meet the percentage target at only 55 mg.

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R19_validate_5_g_dispensing_of_the_four_cohesive_powders.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
