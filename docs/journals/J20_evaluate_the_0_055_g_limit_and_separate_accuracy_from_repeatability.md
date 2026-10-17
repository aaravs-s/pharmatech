# J20 The 55 mg tests didn't go nearly as well

*Milestone 3 | Retrospective build notes*

The 5 g results made the smaller target worth trying. At 0.055 g, though, 3% only gives me 0.00165 g of room. That's 1.65 mg. A difference that barely looks noticeable on the scale becomes a large part of the whole dose.

Only three of the eight recorded runs met the target: sugar, cocoa, and baking soda. Salt overshot. Several others undershot, with flour ending at 0.047 g. That is about 14.55% absolute error. Definitely not a result I can smooth over with the successful 5 g table.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

There isn't one obvious correction hiding in the signs of the errors, either. Simply adding a fixed amount to every target wouldn't fix both the high and low results. Pulse size, clumps, delayed feedback, and the stopping logic could all be involved. I don't have the traces to separate their contributions here.

The notes mention consecutive same-target tests, but the eight-powder sheet isn't that repeated series. Its two sections are different requested masses. I can't use them as replicates just because they're called trials. I need the actual repeated values before calculating a spread or claiming this is consistent.

## Working through the small-dose result

At a 0.055 g target, the absolute allowance for 3% is 0.00165 g, or 1.65 mg. A 0.001 g difference already represents about 1.82% of the request. The recorded values and recalculated errors are shown in the table below; all error values use the same absolute percentage formula as the 5 g trials.

Run times ranged from 54 seconds for salt to 3 minutes 21 seconds for flour. Several finer or more cohesive materials took longer despite the very small target. Long finishing pauses and small additions are consistent with that pattern, but no phase trace identifies the cause of each trial's duration.

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

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## What I need next

This is where the limitation was obvious. A feeder that did well at 5 g was struggling at 55 mg. The next useful test would keep one small target and one configuration fixed, repeat it, and keep every result. More tuning without that comparison would leave me guessing at what helped.

<details>
<summary>Notes added while reconstructing this entry</summary>

Only sugar, cocoa, and baking soda met 3% in these individual runs. Salt overshot while several other powders undershot, so the result doesn't support a single universal correction to the target. Material delivery per motion, scale response, and the stopping logic remained possible interacting factors.

The July 24 FINAL-only behavior below 0.100 g addresses the same class of small-target problem. The code snapshots and test sheet don't establish that these specific results were produced before or after that change. I retained the program comparison as a separate documented revision rather than assigning an improvement to unmatched data.

The milestone notes describe consecutive same-target testing, but its raw series isn't present in the available test sheet. The two target groups in that sheet are different-dose comparisons, not replicates. They can't establish a repeated-run standard deviation or a general probability of meeting the criterion.

A useful next experiment would hold the target, powder, feeder, code, baseline method, and fill conditions fixed, then retain each delivered mass and duration. That would distinguish a consistent offset from variation between runs and provide a direct comparison for revised pulse behavior. It remained a proposed next experiment rather than an added result.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
