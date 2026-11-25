# Voice guide — how these journals should sound

Goal: like I actually wrote them at my table that night, because the whole point of this log is that it's mine. The old AI set failed this too — every entry the same shape, same polish, same "lesson learned" voice.

## The calibration sample is my own writing

The journals are modeled on how I already write in the project docs, e.g.:

> "Ok so we need a agitator, currently if you look in cad… you need to attach an agitator to the bottom of blue thing so when the blue thing spins it turns both auger and agitator" — my Jun 17 fix-it note

> "We troubleshooted this by rerouting the EN to a GPIO pin on the Pi 4." — M2 doc

> "Make short write up" — the entire content of my "Augur Mechanism Details" doc, May 25

Traits to keep: plain words, sentences that run long when I'm explaining and stop short when something just worked or just broke, "ok so" / "at first" / "turns out" openers, specifics everywhere (part names, pin numbers, grams), and rough edges left in. Traits to drop from the milestone docs: the formal "we" competition voice.

## What makes writing sound AI (from the references below)

- Sentences all landing in the same 15–20 word band, paragraphs all the same size
- Predictable, "safe" word choices and stock phrases (delve, crucial, pivotal, "it's important to note")
- Performed significance: announcing that something matters instead of just showing it
- Abstraction: claims with no name, number, or measurement attached
- No person behind it: hedged, both-sides, no reaction to anything
- Punctuation tells: em dashes for drama, semicolons linking everything, a rule-of-three for every list
- Perfectly balanced structure, every section filled out to the same depth, a summary sentence closing every section

## Rules for every journal here

1. **Vary the rhythm on purpose.** A few very short sentences. Then one long one that takes a while because the mechanism needs three clauses to explain properly. If every paragraph looks the same length, rewrite it.
2. **Concrete or cut.** Every claim needs a number, a part name, a file name, or a measurement from the sources — but *never invent a detail to sound human*. If the detail isn't in a source, it doesn't go in, or it gets a `[check: my memory]` mark.
3. **React like a person.** It's fine to say the thread crumpling was annoying or that 5 g landing at 0% error felt great — where the record supports the reaction. No fake drama.
4. **Plain verbs.** Turns, jams, sticks, slips, leaks. Not "utilizes," "facilitates," "leverages."
5. **Contractions, always.** Nobody writes "it does not" in their own build journal.
6. **Uneven sections are good.** Some entries Today's results is one line. Some days what's left to do is the whole point. The template is a checklist, not a mold.
7. **Length follows the step.** Short when the step was short. Longer when it needs it — a coupler redesign is allowed more words than a glue fix. No padding to hit a target, no cutting real detail to hit one either.
8. **Read it aloud before calling it final.** If it sounds like a report, it gets another pass. If it sounds like me explaining the build to a friend, it's done.

## Added 2026-11-23 (user's rule — supersedes the Nov 22 one-mistake rule)

Sound like Aarav's own Imperium journal, not like a polished draft and not like one tidy mistake per entry. The reference is `hidden_files/research/imperium_voice/JOURNAL.md` (8 logs, May–Jun 2025), analyzed in `hidden_files/research/imperium_voice.md`. Dense, long, unbroken paragraphs; technical explanation woven into the narration (explain how/why the mechanism works as part of telling what happened); his explainer phrases — "One thing to note is…", "One thing you might be wondering is…", "the reason for this is…", "What I mean by that is…", "By convention…", "The first thing I needed was…", "Now, the hard part is…"; research narration ("I researched… and I landed on…", "I looked at the specifications and differences between…"); self-deprecating asides ("My drawing skills arent the best…", "(I hope)"). Numbers everywhere, stated plainly. Typos happen naturally throughout, roughly one every 2–4 sentences, in his shapes: missing apostrophes (dont, im, isnt, doesnt, wont, arent, thats), misspelled long/technical words (componenets, pararell, manafactur, effecient, muliplexer, capicitor, milimeters, diagnal), doubled words ("a a pulley"), missing spaces after periods occasionally, long run-on comma sentences. Never a typo in a number, date, dimension, pin, measurement, file name, part name, code, header, or hours line. The Nov 22 per-entry mistake log (`hidden_files/research/voice_rewrite_log.md`) is history; the Imperium rewrite log is `hidden_files/research/imperium_voice_rewrite_log.md`.

## References used for this guide

- [How to Make AI Writing Sound Human — Surfer](https://surfer.ai/blog/make-ai-sound-human/) — perplexity and burstiness; feed the model snippets of your own writing
- [How to Make AI Writing Sound Human: The Craft Guide — WriteHybrid](https://www.writehybrid.com/guides/how-to-make-ai-writing-sound-human) — rhythm first: a few sentences under 10 words, some over 25, rest mixed; voice as a through-line
- [humanize-writing skill — GitHub (JMO-CEO/ceo-substack)](https://github.com/jmo-ceo/ceo-substack/blob/HEAD/.opencode/skills/humanize-writing/SKILL.md) — fix the cause (uniformity, performed significance, abstraction, no person) not the word list; never invent specifics
- [Humanize Text Skill — GitHub (ourostack/ouroboros-skills)](https://github.com/ourostack/ouroboros-skills/blob/HEAD/plugins/desk/skills/humanize/SKILL.md) — the nine detector signals, incl. the punctuation fingerprint
- Wikipedia, "Signs of AI writing" (via the humanizer skills above) — the long pattern list behind most of these tools
