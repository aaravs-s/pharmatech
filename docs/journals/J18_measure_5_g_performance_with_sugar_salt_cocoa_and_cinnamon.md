# J18 The 5 g results were encouraging, with a lid problem

*Milestone 3 | Retrospective build notes*

The 5 g results were a good sign. Sugar and salt both had a recorded final reading of 5 g, with times of 1:54 and 1:49. Cocoa and cinnamon took longer, but their listed masses were still comfortably inside the 3% target.

I needed that numerical check after so much time changing geometry and control behavior. 'It seems to feed better' only goes so far. Here there were actual final masses and durations to compare.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

Cocoa still had an annoying side problem: powder escaped near the lid. The scale could end up close to target while some material went somewhere it shouldn't. So a good number in the cup didn't mean containment was finished. I don't have a documented lid change resolving that in this record.

The exact-looking sugar and salt values also need some restraint. They're what was recorded at the shown precision, not proof of literally zero physical error. And each powder has one listed 5 g run here. Useful results, but not the same as repeatedly getting that result under the same conditions.

## What the readings do and do not show

A displayed 5.000 g reading doesn't mean literally zero physical error. It means the recorded reading equals the requested value at the shown precision. The balance's resolution, calibration, drift, and final settling affect how closely that reading represents the actual delivered mass. Those quantities aren't established by the test sheet, so I report the values as recorded rather than adding unsupported measurement certainty.

The behavior notes describe sugar as easy to move but difficult to finish without overshoot because of rapid flow and scale delay. Salt behaved similarly. Cocoa and cinnamon were fine and delivered smaller quantities, leading to longer runs. Cocoa also escaped upward from the lid. That observation matters because material leaving the intended powder path can make the collected mass and total material removed from the hopper differ.

The next comparison used cohesive powders and a much smaller target. That was necessary because success at 5 g provides a comparatively large absolute error allowance and can't establish that the same mechanism can dispense tens of milligrams to the same percentage error.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 5 | 5 | 0.00% | 1:54 | Yes |
| Table salt | 5 | 5 | 0.00% | 1:49 | Yes |
| Cocoa powder | 5 | 5.006 | 0.12% | 3:32 | Yes |
| Ground cinnamon | 5 | 4.985 | 0.30% | 3:05 | Yes |

## More views

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

All four passed the 3% check in these runs. Cocoa took 3:32 compared with sugar's 1:54, so the time difference was still there even when both final readings looked good. Next were the clumpier powders, then the much less forgiving small target.

<details>
<summary>Notes added while reconstructing this entry</summary>

For the 5.000 g target, the sheet records sugar at 5.000 g in 1:54, salt at 5.000 g in 1:49, cocoa at 5.006 g in 3:32, and cinnamon at 4.985 g in 3:05. Absolute percentage error is abs(actual - target) / target times 100, giving 0.00%, 0.00%, 0.12%, and 0.30%. All four recorded values meet 3% at this target.

Containment and dosing error described different outcomes. Cocoa escaping near the lid could increase material removed from the hopper without increasing the amount collected by the scale. The record identifies that symptom, but doesn't preserve a measured escaped-mass result or a confirmed lid change resolving it.

I kept throughput and final error separate. Cocoa took longer than sugar even though both listed results met the criterion. The sheet provides one 5 g result per powder, rather than repeated runs or a matched tuning comparison. That limits the conclusions to the measured trials without discarding their usefulness.

</details>

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R18_measure_5_g_performance_with_sugar_salt_cocoa_and_cinnamon.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
