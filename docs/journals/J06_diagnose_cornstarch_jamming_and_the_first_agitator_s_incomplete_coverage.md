# J06 Cornstarch changed the problem

*Milestone 1 | Retrospective build notes*

Cornstarch didn't behave like sugar at all. It clumped, jammed, and left powder around the hopper that the screw wasn't touching. Watching the auger rotate wasn't enough to tell whether the material was actually feeding.

I made the auger wider and used larger flights. The notes describe better movement after that change, with less of the tight compression I was getting in the earlier arrangement. I don't have a torque comparison for it, so 'better movement' is as far as that result goes.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

The untouched material near the sides was another issue. A bigger drive wouldn't magically bring it into the screw. I tried an agitator, but that attempt had both a failed print and an arm that didn't cover the full hopper width. Two separate problems, which was annoying: even a successful print of that shape wouldn't have reached the powder I needed it to reach.

The next geometry needed more sweep near the walls, with enough clearance to rotate after printing. I had to think about what volume of powder the mechanism actually disturbed, rather than only how much material appeared at the outlet.

## Two problems to separate

The first agitator attempt failed in printing and didn't account for the full width of the hopper. Even a successful print of an undersized arm would have left the stagnant wall region largely untouched. The redesign therefore needed an arm envelope that approached the hopper boundary while leaving enough clearance to rotate after printing and assembly.

The untouched powder near the hopper wall was an important result in its own right. Material collected in the cup could conceal that inactive region. It explained why an agitator needed to influence powder outside the screw's immediate sweep instead of only improving movement at the outlet.

## More views

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

I couldn't treat this as one generic 'powder isn't flowing' fault anymore. There was the screw's transport problem and the hopper's stagnant-region problem. The next arm design needed to address the second one without creating another rubbing or printing problem.

<details>
<summary>Notes added while reconstructing this entry</summary>

Cornstarch produced two related but different symptoms. It was hard to push through the auger consistently and sometimes jammed; it also remained in regions of the hopper the screw didn't reach. A larger motor might help overcome resistance, but it would not automatically bring stationary powder from the wall into the active feed region. I needed to treat transport through the screw and circulation inside the hopper as separate design problems.

I increased the auger's width and flight size for cornstarch. The intention was to reduce tight compression in the feeding space and give the material a larger surface to engage. The reported improvement was qualitative powder movement; the record doesn't contain a measured torque reduction or an optimum-profile study.

The dimensions all affected each other: screw outside diameter, housing bore, flight pitch, arm reach, and hopper wall position. Changing one affected both feeding and clearance. The saved V5 and V10 models show later auger-and-arm states, but the exact dimensional progression of the first cornstarch prototype isn't preserved.

The subsequent two-arm configuration connected circulation to screw rotation. That created a way to encounter powder farther from the center while the screw conveyed material through the feeder. The initial failed print and limited reach explain why adding those features was a functional redesign rather than an aesthetic change.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R06_diagnose_cornstarch_jamming_and_the_first_agitator_s_incomplete_coverage.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
