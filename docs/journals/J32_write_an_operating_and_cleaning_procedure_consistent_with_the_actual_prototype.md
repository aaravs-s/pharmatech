# J32 Write an operating and cleaning procedure consistent with the actual prototype

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I wrote an operating procedure to make the doser usable without requiring someone to understand the control code first. It covered powder selection, loading, taring, target entry, starting a run, checking the result, stopping, and cleaning the removable powder-contact components.

The procedure also exposed assumptions that were easy to overlook during development. A correct mass command depends on the baseline, and an automatic recipe depends on meaningful disk and actuator references. The later app's unknown-position state therefore mattered to operation, not just to debugging.

I kept the documented household-powder tests as the operating evidence for this account. A capacity target and a written cleaning procedure do not establish performance across every dose or validated sanitation. The practical achievement was recording how to use and recover the prototype, while identifying the limits of the available measurements.

## Technical detail

The written SOP covers selecting powder, entering mass, dispensing, stopping, and cleaning. The original single-doser procedure and the later recipe app have different positioning requirements. I treated the documented procedure and later source behavior as distinct stages so a general START instruction did not conceal the extra references required by the carousel.

The later recipe app requires a known disk position and a meaningful actuator UP reference. UNKNOWN blocks a run. In the saved reference-based arrangement, physical alignment and SET CURRENT operations establish what the software will treat as its position; the app does not automatically sense an actuator top limit.

Force stop marks actuator and disk state unknown. That differs from normal completion and can require the operator to establish references again before continuing. Retaining an old slot number after interrupted motion would assume the disk finished a movement that may have stopped partway through.

Cleaning connects directly to the earlier interface decisions. The contact path includes the hopper interior, agitator, screw, outlet, and receiving area. Combining components removed a joint but left those surfaces to access and inspect. The source procedure calls for disassembly of the hopper and lid and lists an M3 wrench and screwdriver or Allen key among the tools.

The original procedure includes broad performance language and a capacity limit. The measured evidence in this account is narrower: individual household-powder results at 5 g and 0.055 g, including small-dose failures. I have kept that demonstrated range distinct from the hopper capacity target and from any clinical performance claim.

Writing the procedure did not validate a cleaning chemistry or quantify residual powder. No compatibility study, contamination acceptance measurement, or independent usability trial is preserved in this record. The result of this stage was an operating document, with those additional questions left as future validation work.

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The operating document brought setup, feeding, stopping, and cleaning into one workflow. It also tied usability back to engineering decisions: detachable surfaces, baseline mass, and lost position after interruption all affect the operator. The written procedure did not create new validation results, so its claims remain bounded by the actual powder tests and implemented reference behavior.

## Sources

- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
