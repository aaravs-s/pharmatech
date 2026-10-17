# J19 Close to 5 g, but it took a while

*Milestone 3 | Retrospective build notes*

The four clumpier powders all ended up close to the 5 g target in the recorded tests. That was encouraging after the earlier cornstarch trouble. The agitator and feeding changes had given me something that could reach the requested mass with these materials.

The times were harder to ignore. Baking soda took 5:01, cornstarch 4:55, powdered sugar 4:57, and flour 4:39. Reaching a good final reading after that long is useful, but I wouldn't call the speed problem solved.

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

The notes describe uneven release, including clumps and much smaller additions between them. That fits the practical difficulty: a slow command might do very little until the material changes and more comes out together. The final mass doesn't show all of that behavior along the way.

I also caught an arithmetic mismatch while working through the sheet. Flour is listed at 4.993 g. Against 5 g, that is 0.14% absolute error, not the 0.18% written in the source. I kept the recorded mass and recalculated from it. There's also a later 120 s controller limit, so these roughly five-minute runs can't just be attributed to that newer file.

## Mass, time, and configuration

The earlier mechanical changes addressed different regions: larger flights changed the feeding space, while agitator reach addressed powder outside the screw's active region. These final results don't isolate the contribution of either change because there is no matched one-variable comparison in the available sheet.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Baking soda | 5 | 4.994 | 0.12% | 5:01 | Yes |
| Cornstarch | 5 | 4.991 | 0.18% | 4:55 | Yes |
| Powdered sugar | 5 | 4.996 | 0.08% | 4:57 | Yes |
| All purpose flour | 5 | 4.993 | 0.14% | 4:39 | Yes |

## More views

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

The 5 g result was good across all eight powders when combined with the previous group. The slow, uneven feeding was still something to work on. And I still hadn't earned the right to assume the same percentage accuracy would hold when the target dropped by almost two orders of magnitude.

<details>
<summary>Notes added while reconstructing this entry</summary>

The 5.000 g results were baking soda at 4.994 g in 5:01, cornstarch at 4.991 g in 4:55, powdered sugar at 4.996 g in 4:57, and flour at 4.993 g in 4:39. Recalculated absolute errors are 0.12%, 0.18%, 0.08%, and 0.14%. The source's flour percentage is inconsistent with its recorded mass, so the calculation here uses the listed 4.993 g reading.

All four final readings met 3%, while the durations exposed the cost of slower feeding and finishing. Intermittent discharge and clumps could coexist with a close final mass. I treated the time and transport observations as part of performance rather than reducing the result to a pass label.

The record contains no measured residual-powder mass or post-run coverage series for these trials. I don't interpret successful collection as proof that the hopper fully cleared or that no powder remained around walls and arm roots. Those internal states are distinct from the final cup reading.

The later controller's 120 s maximum dispense duration is shorter than all four of these runs. I kept their original recorded times and didn't attribute them to that file. Version matching matters here because a configuration that times out after two minutes could not complete an uninterrupted five-minute test under the same limit.

The outcome gives me one 5 g result for each tested cohesive powder. It doesn't establish general flow behavior for other materials, repeatability across refill levels, or an autonomous recipe containing all four. Those are separate tests with separate evidence.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R19_validate_5_g_dispensing_of_the_four_cohesive_powders.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
