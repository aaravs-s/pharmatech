# J07 Model the two-arm agitator and compare uniform and tapered-flight concepts

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I developed a two-arm agitator connected to the rotating auger-related component. The intention was for one rotating connection to drive both powder circulation in the hopper and transport through the screw. The saved V5 and V10 views show the resulting auger-and-arm geometry.

I also considered a second screw configuration with flights that funnel downward. That was an alternative to the uniform-flight construction, rather than another name for the same saved model. The available design note establishes the proposal, but does not establish a successful comparative print-and-test series for both versions.

For the modeled arms, the important relationship was their reach inside the hopper. Extending the rotating envelope could disturb powder left near the wall, while too much reach could cause contact after printing and assembly. Connecting the arms to the screw also increased the load on the same drive and printed roots. Those consequences linked this mechanical revision to the later loaded-speed investigation.

## Technical detail

I proposed attaching two agitator arms beneath the rotating component so the same connection could turn the screw and agitation features. The design note considered both an existing-style screw with added arms and an alternative with downward-funneling flights. Only the saved configurations and explicitly recorded trials are treated as completed work in this account.

The V5 feature history shows the arm geometry in Sketch 10 on the Top plane. The construction view highlights the arm profiles around the existing shaft and screw. Extrude 8 then selects two faces of that sketch, uses Add, enables Symmetric extrusion, sets the displayed depth to 0.318 cm, and merges into the part named tube adapter. The archived depth is approximately 3.18 mm. Recreating this feature requires the arm sketch and merge target as well as the thickness.

The open triangular arms extend the rotating envelope beyond the screw. Their purpose is to encounter powder outside the narrow feeding region and move it toward the feeder. The clearance requirement belongs to the complete hopper assembly: an isolated arm view cannot establish the minimum gap throughout rotation.

The saved Helix 1 has a single target pitch over its height. I kept that uniform screw distinct from the funneling proposal because their profiles are not interchangeable. The recovered record does not establish a comparative result for the tapered alternative.

Adding arms also introduced a mechanical load change. The drive now moved the screw and encountered powder through the agitator at the same time. That made loaded rotation, powder accumulation near the arm roots, and the printed attachment points relevant to later speed testing. The notes describe agitation helping with clumps, but do not record stresses or a measured power comparison.

The mechanical platform now combined a single powder path with a driven screw and an agitation design for stagnant material. Closed-loop operation still required a separate set of electrical and software interfaces: motor wiring, valid scale readings, profile commands, and reliable stopping. Those became the focus of M2.

## Process images

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

## Outcome and reflection

This stage produced a documented two-arm agitation configuration and a separate tapered-flight proposal. The single-doser mechanism now had a powder path, a screw construction, and a way to disturb stagnant material. The next milestone was to make that mechanism respond to measured mass through wiring, scale communication, and explicit stop behavior.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [STUFF TO FIX TONIGHT](https://docs.google.com/document/d/1usu-M_TCbRc7j5A3ndAVeFQoTAXTW40O4JjwxquL32A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R07_model_the_two_arm_agitator_and_compare_uniform_and_tapered_flight_concepts.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
