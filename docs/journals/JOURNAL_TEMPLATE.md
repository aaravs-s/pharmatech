# Journal template — copy this for every entry

File name: `journals/YYYY-MM-DD_NNN_short-title.md`
Example: `journals/2026-06-15_007_sugar-leaks-before-the-motor-starts.md`

Rules baked into this template (do not remove sections to save space — keep entries short by keeping each section short):

- **One entry = one thing.** One achievement, OR one roadblock + the lesson from it, OR one working result. If two things happened, write two journals.
- **Written in the moment.** Present-tense, first person, what I know *on that date*. Never "looking back," never knowledge from later milestones.
- **Every journal has at least one photo** taken at that stage (Drive photo, video still, or CAD capture from that version). Never illustrate an early step with a later version's image.
- **Recreate test:** a reader must be able to redo this step from this entry alone — exact dimensions, settings, part names, pin numbers, or code go in the entry itself (in *What happened* / *Today's results*), not left in the photos. There is no separate build-notes section (user, 2026-11-07); the collected specs live in RECREATE_FROM_SCRATCH.md.
- **Length follows the step:** usually a few hundred words, shorter when the step was short, longer when it needs it (user confirmed 2026-11-07: entries may run longer than the original 150–350 target as needed — never pad, never cut real detail to fit).
- **Voice:** follow [VOICE_GUIDE.md](VOICE_GUIDE.md) — modeled on my own project writing, varied sentence rhythm, contractions, plain verbs, concrete numbers, rough edges left in. If it reads like a report, it gets another pass.
- Anything I can't verify from a source is written as `[check: my memory — …]` in the draft and resolved before the entry is marked final. Nothing is smoothed over or invented.

---

```markdown
# NNN — Title: the one thing that happened

**Date:** YYYY-MM-DD
**Milestone:** M1 / M2 / M3 / M4 / M5
**Type:** Achievement / Roadblock / Working result

## What I'm doing

Two or three sentences: the goal for today, in today's terms.

## What happened

The short story. What I built, tried, measured, or watched fail — in the order it happened.

![Caption that says what this photo proves, not just what it shows.](../assets/photos/YYYY-MM-DD_name.jpg)
*Source: Drive photo IMG_0000, taken YYYY-MM-DD. / Video still from IMG_0000.MOV at 0:12, recorded YYYY-MM-DD. / Onshape, Pill Compounder > Document name, version/branch, YYYY-MM-DD.*

## Today's results

The measurable outcome: it works / it jammed / 5.006 g against a 5 g target / the coupler slipped at any angle except one. Any decision made today goes here too.

## What's still left to do next time

What's unfinished, what still needs figuring out, and the very next steps. Plain list or a couple of sentences, however it comes out.
```

Status line to keep at the very bottom while drafting: `Status: draft — sources: <list>`
Remove it, or change it to `Status: final`, only after every fact and photo in the entry is source-checked.
