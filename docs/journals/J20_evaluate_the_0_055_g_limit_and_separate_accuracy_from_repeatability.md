# J20 Evaluate the 0.055 g limit and separate accuracy from repeatability

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I reduced the requested mass to 0.055 g to examine the difficult end of the dosing range. At 55 mg, the project's 3% criterion permits only 0.00165 g of absolute error. A small clump or a milligram-scale difference therefore matters far more than it does in a 5 g trial.

The results were mixed. Sugar, cocoa, and baking soda met the criterion in their recorded runs; salt, cinnamon, cornstarch, powdered sugar, and flour did not. The worst listed result was flour at 0.047 g, or about 14.55% below target in absolute percentage terms.

My milestone notes also describe consecutive same-target dispenses, but the available eight-powder sheet is not that repeatability series. Its two sections use different target masses. I therefore kept the small-dose accuracy observations separate from any statistical claim about repeated performance, and treated pulse size, clumping, feedback delay, and stopping behavior as possible contributors rather than a proven single cause.

## Technical detail

At a 0.055 g target, the absolute allowance for 3% is 0.00165 g, or 1.65 mg. A 0.001 g difference already represents about 1.82% of the request. The recorded values and recalculated errors are shown in the table below; all error values use the same absolute percentage formula as the 5 g trials.

Only sugar, cocoa, and baking soda met 3% in these individual runs. Salt overshot while several other powders undershot, so the result does not support a single universal correction to the target. Material delivery per motion, scale response, and the stopping logic remained possible interacting factors.

Run times ranged from 54 seconds for salt to 3 minutes 21 seconds for flour. Several finer or more cohesive materials took longer despite the very small target. Long finishing pauses and small additions are consistent with that pattern, but no phase trace identifies the cause of each trial's duration.

The July 24 FINAL-only behavior below 0.100 g addresses the same class of small-target problem. The code snapshots and test sheet do not establish that these specific results were produced before or after that change. I retained the program comparison as a separate documented revision rather than assigning an improvement to unmatched data.

The milestone notes describe consecutive same-target testing, but its raw series is not present in the available test sheet. The two target groups in that sheet are different-dose comparisons, not replicates. They cannot establish a repeated-run standard deviation or a general probability of meeting the criterion.

A useful next experiment would hold the target, powder, feeder, code, baseline method, and fill conditions fixed, then retain each delivered mass and duration. That would distinguish a consistent offset from variation between runs and provide a direct comparison for revised pulse behavior. It remained a proposed next experiment rather than an added result.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 0.055 | 0.056 | 1.82% | 0:57 | Yes |
| Table salt | 0.055 | 0.058 | 5.45% | 0:54 | No |
| Cocoa powder | 0.055 | 0.054 | 1.82% | 1:03 | Yes |
| Ground cinnamon | 0.055 | 0.052 | 5.45% | 1:10 | No |
| Baking soda | 0.055 | 0.054 | 1.82% | 2:43 | Yes |
| Cornstarch | 0.055 | 0.053 | 3.64% | 2:49 | No |
| Powdered sugar | 0.055 | 0.049 | 10.91% | 3:07 | No |
| All purpose flour | 0.055 | 0.047 | 14.55% | 3:21 | No |

## Process images

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The 55 mg trials established a real limitation: the eight successful 5 g results did not carry over to the smaller target. Three of eight small-dose runs met 3%. The next experimental priority was a matched series at a fixed target and configuration, so I could distinguish occasional accuracy from consistent delivery and evaluate changes such as FINAL-only control.

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
