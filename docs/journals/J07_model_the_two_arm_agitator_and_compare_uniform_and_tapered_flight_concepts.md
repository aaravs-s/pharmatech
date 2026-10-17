# J07 Adding arms without losing the screw

*Milestone 1 | Retrospective build notes*

I worked on a two-arm agitator connected to the same rotating component as the auger. That way one drive connection could move the screw and disturb powder farther out in the hopper. The saved models show the open triangular arms extending beyond the screw's narrow sweep.

The reach mattered more than the isolated shape. An arm could look large on its own and still miss the wall region once it was inside the hopper. Go too far the other way and it could scrape the housing. This was exactly the part the first attempt hadn't accounted for well enough.

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

I also considered a second screw with flights that funnel downward. That's in the planning note, but I don't have a documented comparison showing both alternatives successfully printed and tested. The constant-pitch model and the tapered proposal need to stay separate.

Adding the arms also asked more of the drive. It now had to push through powder at the agitator as well as at the screw. That was going to matter when I started trying to run the loaded feeder faster. For this stage, I was getting the mechanical arrangement into a form I could actually control.

## Arm geometry

The V5 feature history shows the arm geometry in Sketch 10 on the Top plane. The construction view highlights the arm profiles around the existing shaft and screw. Extrude 8 then selects two faces of that sketch, uses Add, enables Symmetric extrusion, sets the displayed depth to 0.318 cm, and merges into the part named tube adapter. The archived depth is approximately 3.18 mm. Recreating this feature requires the arm sketch and merge target as well as the thickness.

The open triangular arms extend the rotating envelope beyond the screw. Their purpose is to encounter powder outside the narrow feeding region and move it toward the feeder. The clearance requirement belongs to the complete hopper assembly: an isolated arm view can't establish the minimum gap throughout rotation.

Adding arms also introduced a mechanical load change. The drive now moved the screw and encountered powder through the agitator at the same time. That made loaded rotation, powder accumulation near the arm roots, and the printed attachment points relevant to later speed testing. The notes describe agitation helping with clumps, but don't record stresses or a measured power comparison.

## Saved arm and screw views

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

The feeder was no longer just a screw sitting in a hopper. There was a reason for the arm reach and a route for moving powder toward the feeding region. Next came the wiring and scale feedback. Plenty left to do before any of this could stop at a requested mass.

<details>
<summary>Notes added while reconstructing this entry</summary>

I proposed attaching two agitator arms beneath the rotating component so the same connection could turn the screw and agitation features. The design note considered both an existing-style screw with added arms and an alternative with downward-funneling flights. Only the saved configurations and explicitly recorded trials are treated as completed work in this account.

The saved Helix 1 has a single target pitch over its height. I kept that uniform screw distinct from the funneling proposal because their profiles aren't interchangeable. The recovered record doesn't establish a comparative result for the tapered alternative.

The mechanical platform now combined a single powder path with a driven screw and an agitation design for stagnant material. Closed-loop operation still required a separate set of electrical and software interfaces: motor wiring, valid scale readings, profile commands, and reliable stopping. Those became the focus of M2.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [STUFF TO FIX TONIGHT](https://docs.google.com/document/d/1usu-M_TCbRc7j5A3ndAVeFQoTAXTW40O4JjwxquL32A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R07_model_the_two_arm_agitator_and_compare_uniform_and_tapered_flight_concepts.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
