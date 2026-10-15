# R20 Evaluate the 0.055 g limit and separate accuracy from repeatability

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J29, J30

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Determine what the small-dose results actually support and identify the repeated trials still needed.

## Design process

I also tested a much smaller target recorded as 0.055 g, or 55 mg. At this mass, a 3% allowance is only 0.00165 g. Small absolute additions therefore produce much larger percentage changes than they do in a 5 g dispense.

The recorded final masses were 0.056 g for sugar, 0.058 g for salt, 0.054 g for cocoa, 0.052 g for cinnamon, 0.054 g for baking soda, 0.053 g for cornstarch, 0.049 g for powdered sugar, and 0.047 g for flour. Three of these eight recorded runs were within 3%: sugar, cocoa, and baking soda. The other five exceeded the target, with flour reaching approximately 14.55% absolute error.

This update is important because the successful 5 g tests do not establish successful dispensing at 55 mg. Possible contributors include the amount released per pulse, variable clump size, the scale response, and stopping behavior, but the sheet alone does not identify the root cause. I would retain this failure evidence and explain any later changes using the actual small-target tests.

I ran consecutive dispenses at the same target mass to check whether the single doser behaved consistently without recalibrating between runs. The milestone notes explicitly describe this repeatability work and comparing final weights to identify sources of error.

The separate eight-powder test sheet does not contain those repeated-run series. Its two trial headings refer to different target masses, not several replicates at the same target. I therefore need to add the actual repeatability data before describing a standard deviation, worst-case error, or success rate.

The useful comparison would keep the target and configuration consistent while recording each final mass and duration. Hopper fill and compaction are also worth noting because the material above the auger changes as it dispenses. The reference entry should explain the test I actually performed, then use the raw values to support the conclusion instead of turning the general milestone description into an invented numerical result.

## Construction and implementation detail

The 0.055 g target gives only 0.00165 g of allowed absolute error at 3%. The recorded sugar result is 0.056 g, salt 0.058 g, cocoa 0.054 g, cinnamon 0.052 g, baking soda 0.054 g, cornstarch 0.053 g, powdered sugar 0.049 g, and flour 0.047 g. Recomputed errors are 1.82%, 5.45%, 1.82%, 5.45%, 1.82%, 3.64%, 10.91%, and 14.55%, respectively.

Only sugar, cocoa, and baking soda meet 3% in those individual recorded runs. The results therefore do not support saying that every tested powder meets the same accuracy criterion at 0.055 g. The 5 g results and small-dose results need separate tables because combining them into one 'works with eight powders' statement hides the difficult operating range.

The small-dose times are 0:57, 0:54, 1:03, 1:10, 2:43, 2:49, 3:07, and 3:21 in the same powder order. The longer times for several fine/cohesive powders suggest that tiny finishing motions and settling consumed much of the run, but the sheet does not contain phase traces that prove the cause for each trial. The journals can connect this to the tuning problem while keeping that interpretation distinct from measured data.

The July 24 code's FINAL-only behavior below 0.100 g is a concrete response to the small-dose control problem. Without matched dates and traces, however, I cannot claim these specific results improved because of that revision. The source supports the code change and the test values independently. The missing link is which configuration was used for each measured result.

Repeatability requires multiple runs at the same target under documented conditions. The headings 'trial 1' and 'trial 2' in the available sheet refer to 0.055 g and 5 g, so they are different-dose tests rather than replicates. M3 notes say consecutive same-target dispenses were tested, but the raw repeated-run values have not been recovered.

The next record should retain every repeat's target, actual mass, duration, powder, fill level, code and print revision, tare/baseline procedure, and interruptions. Mean error, spread, and standard deviation can then be computed from the actual observations. The reference pack supplies the worksheet, but leaves its rows empty rather than creating successful repeats to make the final performance appear more complete.

## Image sequence

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

Three of eight recorded 0.055 g trials met 3%; all eight recorded 5 g trials did. Same-target repeatability data remains missing despite the milestone note describing repeated tests.

## Complete from your records

Recover repeated-run measurements and match small-dose tests to code revisions. Confirm how final scale readings were selected.

[IMAGE PLACEHOLDER: Small-dose phase trace and final stable reading for each powder.]

[IMAGE PLACEHOLDER: Consecutive same-target run log with all raw masses; no fabricated replicate rows are included.]

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
