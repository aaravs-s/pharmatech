# J32 Writing down the steps I was already taking for granted

*Milestone 5 | Retrospective build notes*

I wrote an operating procedure for someone who hadn't spent all this time in the code. Select powder, load it, tare the scale, enter the mass, start, check the result. Stop if it jams or malfunctions. Then empty and disassemble the contact parts for cleaning.

Putting that into instructions exposed how much setup I could otherwise skip over in a quick explanation. A target number is only useful with the right baseline. An automatic recipe is only useful when the disk and actuator references mean something physically.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

The later app also loses trust in position after force stop. That means recovery can't just be 'press start again' as though the interrupted move completed. The unknown state belongs in the operating explanation, even if it makes the process less effortless to describe.

The test materials were the eight household powders. A written procedure didn't turn the prototype into a clinically validated machine or establish that every surface was clean enough by a measured criterion. I wanted the instructions to describe what I had, not quietly expand the claims beyond the tests.

## Setup and recovery details

The later recipe app requires a known disk position and a meaningful actuator UP reference. UNKNOWN blocks a run. In the saved reference-based arrangement, physical alignment and SET CURRENT operations establish what the software will treat as its position; the app doesn't automatically sense an actuator top limit.

Force stop marks actuator and disk state unknown. That differs from normal completion and can require the operator to establish references again before continuing. Retaining an old slot number after interrupted motion would assume the disk finished a movement that may have stopped partway through.

Cleaning connects directly to the earlier interface decisions. The contact path includes the hopper interior, agitator, screw, outlet, and receiving area. Combining components removed a joint but left those surfaces to access and inspect. The source procedure calls for disassembly of the hopper and lid and lists an M3 wrench and screwdriver or Allen key among the tools.

## More views

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

This was useful work because it made the hidden assumptions harder to ignore. Setup, recovery, and cleaning were all connected to earlier design decisions. The procedure existed; independent usability and cleaning validation were still separate work.

<details>
<summary>Notes added while reconstructing this entry</summary>

The written SOP covers selecting powder, entering mass, dispensing, stopping, and cleaning. The original single-doser procedure and the later recipe app have different positioning requirements. I treated the documented procedure and later source behavior as distinct stages so a general START instruction didn't conceal the extra references required by the carousel.

The original procedure includes broad performance language and a capacity limit. The measured evidence in this account is narrower: individual household-powder results at 5 g and 0.055 g, including small-dose failures. I've kept that demonstrated range distinct from the hopper capacity target and from any clinical performance claim.

Writing the procedure didn't validate a cleaning chemistry or quantify residual powder. No compatibility study, contamination acceptance measurement, or independent usability trial is preserved in this record. The result of this stage was an operating document, with those additional questions left as future validation work.

</details>

## Sources

- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
