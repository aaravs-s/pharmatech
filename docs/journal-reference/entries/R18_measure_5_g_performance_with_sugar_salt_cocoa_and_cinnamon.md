# R18 Measure 5 g performance with sugar, salt, cocoa, and cinnamon

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 3 · Previous topics J26, J27

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Check final mass and elapsed time for granular and fine powders while recording behavior differences.

## Design process

I compared the recorded results for granulated sugar and table salt at a 5 g target. The test sheet lists 5 g dispensed for both powders, with run times of 1 minute 54 seconds for sugar and 1 minute 49 seconds for salt. Using the recorded values, both have zero calculated error, although the displayed precision and measurement uncertainty still matter.

The behavior notes explain why these two powders were useful together. Both fed readily, and their main control issue was stopping near the target without overshooting the delayed scale reading. The settings developed with sugar could be applied to salt with relatively little change according to those notes.

This is evidence of the listed runs, not a repeatability study. The file has one reported 5 g result for each powder, so it cannot establish a distribution of errors or prove that every run landed exactly on target. I would add the scale photo or video corresponding to each measurement and explain any changes in settings between them.

I tested cocoa powder and ground cinnamon after establishing the behavior of sugar and salt. The notes describe both as fine powders that fed readily in this mechanism. Cocoa needed faster or longer movement than the sugar-and-salt settings, and I also observed powder escaping near the lid.

At the 5 g target, the test sheet lists cocoa at 5.006 g in 3 minutes 32 seconds and cinnamon at 4.985 g in 3 minutes 5 seconds. Those recorded masses correspond to 0.12% and 0.30% absolute error. Both runs met the 3% design target, while taking longer than the listed sugar and salt runs.

Cocoa escaping from the top was a separate issue from final mass accuracy. A scale result can look good while some material is scattered outside the intended path. I would document what changed at the lid or operating speed if I addressed that issue, rather than treating a successful final weight as evidence that containment had been solved.

## Construction and implementation detail

The 5 g test sheet gives concrete values for these four powders. Granulated sugar finished at 5.000 g in 1:54, table salt at 5.000 g in 1:49, cocoa at 5.006 g in 3:32, and cinnamon at 4.985 g in 3:05. Their absolute percentage errors, calculated from the recorded masses, are 0.00%, 0.00%, 0.12%, and 0.30%. All four recorded runs are inside the project's 3% target at this requested mass.

A displayed 5.000 g reading does not mean literally zero physical error. It means the recorded reading equals the requested value at the shown precision. The balance's resolution, calibration, drift, and final settling affect how closely that reading represents the actual delivered mass. Those quantities are not established by the test sheet, so I report the values as recorded rather than adding unsupported measurement certainty.

The behavior notes describe sugar as easy to move but difficult to finish without overshoot because of rapid flow and scale delay. Salt behaved similarly. Cocoa and cinnamon were fine and delivered smaller quantities, leading to longer runs. Cocoa also escaped upward from the lid. That observation matters because material leaving the intended powder path can make the collected mass and total material removed from the hopper differ.

The images for this update should connect setup and result: the loaded powder, the receiving cup on the scale, the identified controller profile, the last feeding phase, and the final stable display. For cocoa, a lid close-up or escaped residue is useful additional evidence. A final mass alone does not explain the containment change that the powder behavior motivated.

I kept throughput and error as separate results. Cocoa's 3:32 duration is longer than sugar's 1:54, but both recorded masses meet the chosen error criterion. To claim an improvement after tuning, I would need another run using the same target and hardware revision. The present sheet supplies one recorded result per powder at 5 g, not a controlled before/after series or repeated-run standard deviation.

The next comparison used cohesive powders and a much smaller target. That was necessary because success at 5 g provides a comparatively large absolute error allowance and cannot establish that the same mechanism can dispense tens of milligrams to the same percentage error.

## Image sequence

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

All four recorded 5 g runs met the 3% criterion, with different durations and a cocoa containment issue. Each is an individual recorded run, not a repeatability statistic.

## Complete from your records

Add test date, code/print revision, fill level, actual scale resolution and final-settling rule, lid change, and any repeated runs.

[IMAGE PLACEHOLDER: Setup and final stable reading for each of the four tests, paired with the controller's phase output.]

[IMAGE PLACEHOLDER: Cocoa residue at the lid and any before/after containment redesign.]

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
