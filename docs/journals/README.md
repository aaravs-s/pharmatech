# PharmaTech Rx — Engineering Design Log

The build journal for my pill compounder: an 8-hopper rotary machine that dispenses powders to a target mass within ±3%, closed-loop on a 0.001 g balance, run from a Raspberry Pi touchscreen.

**May 25 – Sep 13, 2026.** From studying a reference auger filler to demoing the finished machine.

## How this log is organised

- **As many journals as the build needs, as long as the step needs.** Each entry is one achievement, one roadblock + lesson, or one working result — dated, written as if on the day in my own voice ([VOICE_GUIDE.md](VOICE_GUIDE.md)), explaining what I did, why, and what broke, with photos and CAD screenshots from that stage (including messy intermediates and version-by-version CAD). Entries are merged, not padded, when one step alone can't carry its hours. No "Sources" tags: the log itself is the record.
- `journals/` — the entries, named `YYYY-MM-DD_NNN_title.md`, in build order.
- `assets/` — every photo, video still, CAD capture, reference image and code file the journals use, organised by type. File names start with the verified date of the thing in them.
- [RECREATE_FROM_SCRATCH.md](RECREATE_FROM_SCRATCH.md) — the straight-line rebuild guide: BOM, electronics map, software, build order.
- [JOURNAL_TEMPLATE.md](JOURNAL_TEMPLATE.md) — the entry format. [SOURCES_AND_RULES.md](SOURCES_AND_RULES.md) — how dates and facts are verified (EXIF/QuickTime/CAD-version dates, never upload dates).

## Journal map

Status: 56 entries, May 25 – Sep 13, 2026. Entry 005, the June 15 thread test, was merged into 006 on 2026-11-21 because one test alone couldn't carry its hours — the merged June 13–15 entry covers the thread, the test, and the latch that replaced it. The freed-up number 005 was reassigned the same day to a new entry, the June 16 CAD marathon (doser V7–V13), which had no journal and was the biggest CAD gap in M1. Entries are being rebuilt to the Forge standard: decisions explained, CAD shown evolving version by version, mistakes described and fixed. Rebuilt so far: all 56 entries (001–056), 214 hours total, every entry with 2+ images. Images de-repeated 2026-11-21: 132 image slots across 93 distinct images, no image used more than twice (was 146 slots / 71 distinct, worst 6 uses), with 14 new CAD views captured from Onshape — section cuts, sketch views with dimensions, coupler attempts, the displaced/broken assembly state. Rule of thumb from 2026-11-21: no entry over 5–6 hours except outliers (003 and 006 are 8 hours each and kept as approved; 046 is 8 hours, the all-night wiring session). Entries are written dense enough that the logged hours read as conservative. Reference designs are captioned as reference, never as the author's own work.

### Before Milestone 1 — May 2026
| # | Date | Journal | Status |
|---|---|---|---|
| 001 | 2026-05-25 | Studying an auger filler before designing mine | ✅ |
| 002 | 2026-06-09 | Eight hoppers, but not sixteen motors | ✅ |

### Milestone 1 — Mechanical doser (Jun 2026)
| # | Date | Journal | Status |
|---|---|---|---|
| 003 | 2026-06-10 | First hopper in CAD: tube, funnel, screw | ✅ |
| 004 | 2026-06-16 | The auger print won't stick — glue fixes it | ✅ |
| 005 | 2026-06-16 | Seven versions in one day (doser V7–V13; number reassigned, was the thread test) | ✅ |
| 006 | 2026-06-13 to 2026-06-15 | The thread fails and the latch replaces it (merged: was 005 + 006) | ✅ |
| 007 | 2026-06-17 | No detachable hopper at all: carving them into the disk | ✅ |
| 008 | 2026-06-16 | Sugar falls out before the motor even starts | ✅ |
| 009 | 2026-06-16 | Sugar dispensing consistently | ✅ |
| 010 | 2026-06-17 | Cornstarch jams the auger solid | ✅ |
| 011 | 2026-06-17 | A wider auger with bigger threads for cornstarch | ✅ |
| 012 | 2026-06-17 | The agitator print fails — it doesn't reach the walls | ✅ |
| 013 | 2026-06-17 | Tonight's fix list: two agitators + a tapered auger | ✅ |
| 014 | 2026-06-20 | Starting a second CAD document: newauger | ✅ |
| 015 | 2026-06-23 | Sketching the whole system on paper | ✅ |
| 016 | 2026-06-26 | Electronics start: breadboard, driver, and a lot of wires | ✅ |
| 017 | 2026-06-27 | Wiring the scale's serial adapter | ✅ |
| 018 | 2026-06-30 | Powder test with an agitator actually in the hopper | ✅ |
| 019 | 2026-06-20 | Studying a second reference dispenser (PowderDispenser import) | ✅ |

### Milestone 2 — Doser + scale closed loop (Jul 3–7, 2026)
| # | Date | Journal | Status |
|---|---|---|---|
| 020 | 2026-07-03 | The motor system: NEMA 17 and a TMC2209 on a breadboard | ✅ |
| 021 | 2026-07-03 | The scale and the screen join the Pi | ✅ |
| 022 | 2026-07-05 | Two programs, not one | ✅ |
| 023 | 2026-07-05 | Closed loop: it stops itself at 5.003 g | ✅ |
| 024 | 2026-07-06 | Sugar settings make cornstarch crawl: splitting powder profiles | ✅ |
| 025 | 2026-07-07 | The program ends but the motor keeps turning | ✅ |
| 026 | 2026-07-08 | Designing a PCB to escape the breadboard | ✅ |

### Milestone 3 — Single doser, full coverage (Jul 2026)
| # | Date | Journal | Status |
|---|---|---|---|
| 027 | 2026-07-04 | The speed problem isn't software | ✅ |
| 028 | 2026-07-04 | Fast, then slow: the two-speed rule | ✅ |
| 029 | 2026-07-05 | The 55-milligram test: 5 g is solved, 55 mg is not | ✅ |
| 030 | 2026-07-05 | The 5-gram test: all eight within 0.3% | ✅ |
| 031 | 2026-07-06 | Two kinds of powder, and no barcode | ✅ |
| 032 | 2026-07-23 | The NEMA 23 swap | ✅ |
| 033 | 2026-07-24 | Everything on the Pi: no laptop required | ✅ |
| 034 | 2026-07-26 | Repeatability runs, and writing the SOP | ✅ |
| 035 | 2026-07-27 | M3 done: what the single doser proved | ✅ |
| 036 | 2026-07-15 | The purple agitator takes shape | ✅ |
| 037 | 2026-07-17 | The print that turned into spaghetti | ✅ |
| 038 | 2026-07-26 | Hoppers with lids, and the disk fitting | ✅ |
| 039 | 2026-07-28 | The PCB schematic, on screen | ✅ |

### Milestone 4 — Multi-doser compounding (Aug 2026)
| # | Date | Journal | Status |
|---|---|---|---|
| 040 | 2026-08-01 | The disk concept becomes real CAD | ✅ |
| 041 | 2026-08-05 | The actuator: bought, not built | ✅ |
| 042 | 2026-08-10 | The coupler that only worked at one angle | ✅ |
| 043 | 2026-08-15 | Sawing 3030 extrusion for the frame | ✅ |
| 044 | 2026-08-21 | Frame and disk, together | ✅ |
| 045 | 2026-08-26 | First full assembly | ✅ |
| 046 | 2026-08-28 | The all-night wiring session | ✅ |

### Milestone 5 — Autonomous compounding (Aug 29, 2026)
| # | Date | Journal | Status |
|---|---|---|---|
| 047 | 2026-08-29 | My step code is the bottleneck, not the motor | ✅ |
| 048 | 2026-08-29 | Hardware-timer pulses: version 2 | ✅ |
| 049 | 2026-08-29 | Version 3: fault checking and type-in speeds | ✅ |
| 050 | 2026-08-30 | The PCB is scrapped, the perf board fails | ✅ |
| 051 | 2026-08-31 | Wire covers and one clean extrusion | ✅ |

### September 2026 — final code and demo
| # | Date | Journal | Status |
|---|---|---|---|
| 052 | 2026-09-05 | September: the assembly in CAD, again | ✅ |
| 053 | 2026-09-07 | Printing the last hopper parts | ✅ |
| 054 | 2026-09-12 | The disk doesn't trust steps anymore | ✅ |
| 055 | 2026-09-12 | The final code: three pieces | ✅ |
| 056 | 2026-09-13 | Demo day: it works end to end | ✅ |

The map grows if the Onshape version history or the videos split a planned entry into two — splitting is always preferred over one long entry.
