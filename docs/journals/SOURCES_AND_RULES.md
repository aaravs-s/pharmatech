# Sources and rules — how this log is reconstructed

This log replaces the old AI-generated set (`ALL_JOURNALS.md`, J01–J33 in the pharmatech GitHub repo). That set was rejected because it was written retrospectively, ran to 3,218 lines, mixed later CAD versions into early steps, and missed whole sources. These rules exist so the new set does not repeat that.

## Source hierarchy (in order of trust for a fact)

1. **The file itself, dated correctly** — CAD version history, code files, test data tables, photos, videos.
2. **Milestone documents** (Drive: M1–M5 docs, 8 Powder Test, 8 Powder Behaviors, SOP) — my own contemporaneous write-ups.
3. **Email** — code exchanged Sep 12–13, 2026 is the final software state; competition mail fixes outer dates.
4. **Bill of Materials** (Drive sheet) — part names, quantities, costs, milestone tags.
5. **The old journals** — used only as a lead back to a primary source, never as evidence by themselves.

## Dating rules (the old set's biggest failure)

- **Photos:** EXIF capture time inside the file — never the Drive upload date. (The whole TEAM PHOTOS folder was uploaded Oct 23, 2026; the photos were actually taken Jun 12 – Sep 13, 2026.)
- **Videos:** the QuickTime creation date inside the file, read with ffprobe — Drive shows only duration and upload date.
- **CAD:** the Onshape version/branch timestamp in the **Pill Compounder** folder — never a screenshot date. A capture made later of an old version is captioned as exactly that.
- **Code:** the email date for emailed code; commit/file dates in the repo.
- **Documents:** Drive creation date, cross-checked against the events described.

## Voice rules

- First person, present tense, dated. Each entry only knows what I knew that day.
- No retrospective sections: no "notes added while reconstructing," no hindsight lessons from later milestones.
- Roadblocks are written when they happened, with the fix in the entry where the fix happened — even if that's weeks later.
- **Sound human, not generated** — full rules in [VOICE_GUIDE.md](VOICE_GUIDE.md), calibrated on the user's own project writing (his milestone docs and raw fix-it notes). In short: vary sentence length aggressively, use contractions and plain verbs, attach a real number or part name to every claim, allow reactions the record supports, leave sections uneven, and never invent a detail to sound human. The user flagged the first drafted entry as AI-sounding on 2026-11-07; that check ("does this sound like me explaining it to a friend?") is applied to every entry.
- Length is flexible (user, 2026-11-07): an entry may run longer than the original 150–350-word target whenever the step needs it.

## Photo rules

- Every journal includes at least one photo from its own stage.
- Captions state what the photo *proves*, the source file name, and its verified date.
- Video stills are labeled with the video file name and timestamp inside the video.
- Reference/internet images are labeled **Reference:** and never presented as my work. My CAD is labeled with its document and version.

## Accuracy rules

- Contradictions between sources are events, not errors to hide. Example: the M4 notes describe fixed-step, shortest-path disk motion; the final Arduino code (Sep 12) uses clockwise-only detent-switch indexing. Both get journals — the second one is the day the approach changed.
- Numbers are copied from data, not rounded into claims: at M3 the machine hit 0–0.3% error at 5 g and missed the 3% target at 55 mg for 5 of 8 powders. Both halves go in.
- Unverifiable details stay marked `[check: my memory — …]` until confirmed. They are never silently filled in.
