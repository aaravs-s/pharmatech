# R32 Write an operating and cleaning procedure consistent with the actual prototype

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J47

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Convert the implemented machine states and powder-contact layout into a repeatable operating sequence.

## Design process

I wrote an operating procedure to make the doser usable by someone who had not developed the code. The procedure explains powder selection, loading, taring the scale, entering the target, starting the run, checking the final result, and returning to the home screen.

It also tells the user to stop if the auger jams or another malfunction appears, then discard remaining powder and disassemble the hopper and lid for cleaning. The listed tool requirement includes an M3 wrench and screwdriver or Allen key. The tare step is important because an incorrect baseline can make a correctly functioning controller produce the wrong amount.

The documented prototype tests used the eight listed household powders. Pharmacy-grade sanitation, cross-contamination control, and clinical suitability remain separate questions; a procedure and a material label do not establish those outcomes. For this journal, I would describe the real usability and cleaning checks performed with the prototype and add the observations from someone following the instructions.

## Construction and implementation detail

The SOP source describes powder selection, mass entry, dispensing, stopping, and cleaning. To make that procedure reproducible, the journal needs to tie each step to the actual installed mechanism and software revision. The original single-doser workflow and the later automatic recipe workflow have different reference and positioning requirements.

For the later recipe app, startup requires a known disk reference and a meaningful actuator UP reference. Unknown position blocks the recipe. The operator's physical alignment and SET CURRENT operations must therefore be part of the documented setup where used; they cannot be omitted under a general instruction to press START.

The procedure also needs to distinguish normal completion, force stop, an error, and an interrupted position. The app marks actuator and disk state unknown during force stop, so a restart can require re-establishing references. Recording what state is lost helps explain why the machine should not simply resume indexing from its old slot number after an interruption.

Cleaning relates back to the M1 interface decisions. The contact path includes the hopper interior, agitator, screw, outlet, and receiving area. Combining hopper and funnel reduced interfaces but did not remove the need to inspect those surfaces. The document should show which printed components can be removed, how they are accessed, and where powder remains after use.

The source SOP includes broad performance language and a capacity limit. The available tests support individual results for eight household powders at the recorded targets, with small-dose failures. I would revise the operating claims to match that demonstrated range rather than treating the prototype as clinically validated or asserting that every dose up to the capacity limit was tested.

This journal records the development of an operating document, not a newly validated cleaning method. Any cleaning agent, material compatibility, residual-powder acceptance criterion, or contamination claim needs its own evidence. The reference pack leaves those details to the actual chosen procedure and observations rather than adding an untested chemical recommendation.

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Result and handoff

An SOP was drafted; it needs to reflect the final reference-setting, interruption recovery, removable parts, and measured powder-test limits.

## Complete from your records

Match SOP to installed software/hardware; add actual disassembly, residue observations, chosen cleaning method, and supported operating range.

[IMAGE PLACEHOLDER: Annotated startup/reference-setting screens and the actual stop/recovery sequence.]

[IMAGE PLACEHOLDER: Disassembly/contact-surface photographs and observed condition before/after the chosen cleaning procedure.]

## Sources

- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
