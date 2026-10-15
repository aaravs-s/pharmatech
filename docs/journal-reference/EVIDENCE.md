# Evidence and version distinctions

- The CAD construction views are read-only historical feature inspections captured on October 13, 2026. They are not original editing-session screenshots.
- Early holder, solid carousel, later skeletal carousel, and final assembly are distinct model revisions.
- The constant-pitch auger views do not establish that the tapered-flight proposal was printed and tested.
- July 21 and July 24 code-email dates establish availability, not active working time.
- The later app describes switch-based disk indexing; the recovered Uno firmware uses bidirectional step counts. Identify the final matched files before claiming an integrated configuration.
- The later controller has a 120 s maximum dispense time. Several recorded powder tests take about five minutes and cannot be attributed to that revision without confirmation.
- The powder sheet contains one recorded run per powder at each of two targets, not raw same-target repeatability data.
- At 5 g, all eight recorded results meet 3% error. At 0.055 g, three of eight meet 3%.
- Flour recorded as 4.993 g at a 5 g target yields 0.14% absolute error; the source lists 0.18%. Confirm the original reading.

## Source documents

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [STUFF TO FIX TONIGHT](https://docs.google.com/document/d/1usu-M_TCbRc7j5A3ndAVeFQoTAXTW40O4JjwxquL32A/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

## Recorded results

| Powder | Target g | Actual g | Absolute error % | Within 3% | Time |
| --- | --- | --- | --- | --- | --- |
| Granulated sugar | 0.055 | 0.056 | 1.8182 | yes | 0:57 |
| Table salt | 0.055 | 0.058 | 5.4545 | no | 0:54 |
| Cocoa powder | 0.055 | 0.054 | 1.8182 | yes | 1:03 |
| Ground cinnamon | 0.055 | 0.052 | 5.4545 | no | 1:10 |
| Baking soda | 0.055 | 0.054 | 1.8182 | yes | 2:43 |
| Cornstarch | 0.055 | 0.053 | 3.6364 | no | 2:49 |
| Powdered sugar | 0.055 | 0.049 | 10.9091 | no | 3:07 |
| All purpose flour | 0.055 | 0.047 | 14.5455 | no | 3:21 |
| Granulated sugar | 5 | 5 | 0.0 | yes | 1:54 |
| Table salt | 5 | 5 | 0.0 | yes | 1:49 |
| Cocoa powder | 5 | 5.006 | 0.12 | yes | 3:32 |
| Ground cinnamon | 5 | 4.985 | 0.3 | yes | 3:05 |
| Baking soda | 5 | 4.994 | 0.12 | yes | 5:01 |
| Cornstarch | 5 | 4.991 | 0.18 | yes | 4:55 |
| Powdered sugar | 5 | 4.996 | 0.08 | yes | 4:57 |
| All purpose flour | 5 | 4.993 | 0.14 | yes | 4:39 |
