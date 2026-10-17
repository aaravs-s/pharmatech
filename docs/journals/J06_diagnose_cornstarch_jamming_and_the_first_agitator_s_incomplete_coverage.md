# J06 Diagnose cornstarch jamming and the first agitator's incomplete coverage

*Milestone 1 | Personal retrospective journal*

## Design and iteration

Cornstarch behaved very differently from sugar. It clumped, jammed, and remained in parts of the hopper that the screw did not disturb. The motor could be turning while some of the powder stayed effectively outside the feeding process.

I widened the auger configuration and used larger flights to address the tight, inconsistent transport through the feeder. My milestone notes report improved movement after that change. I also tried adding an agitator, but the initial attempt had two independent problems: the print failed, and the arm geometry did not cover the full hopper width.

That combination changed how I approached the redesign. Fixing the print alone would leave the untouched wall region; increasing motor speed alone would not bring stagnant material into the screw. I separated transport through the feeder from circulation inside the hopper, then developed an agitator envelope that reached farther toward the walls while retaining rotational clearance.

## Technical detail

Cornstarch produced two related but different symptoms. It was hard to push through the auger consistently and sometimes jammed; it also remained in regions of the hopper the screw did not reach. A larger motor might help overcome resistance, but it would not automatically bring stationary powder from the wall into the active feed region. I needed to treat transport through the screw and circulation inside the hopper as separate design problems.

I increased the auger's width and flight size for cornstarch. The intention was to reduce tight compression in the feeding space and give the material a larger surface to engage. The reported improvement was qualitative powder movement; the record does not contain a measured torque reduction or an optimum-profile study.

The first agitator attempt failed in printing and did not account for the full width of the hopper. Even a successful print of an undersized arm would have left the stagnant wall region largely untouched. The redesign therefore needed an arm envelope that approached the hopper boundary while leaving enough clearance to rotate after printing and assembly.

The relevant geometry was a coupled set: screw outside diameter, housing bore, flight pitch, arm reach, and hopper wall position. Changing one affected both feeding and clearance. The saved V5 and V10 models show later auger-and-arm states, but the exact dimensional progression of the first cornstarch prototype is not preserved.

The untouched powder near the hopper wall was an important result in its own right. Material collected in the cup could conceal that inactive region. It explained why an agitator needed to influence powder outside the screw's immediate sweep instead of only improving movement at the outlet.

The subsequent two-arm configuration connected circulation to screw rotation. That created a way to encounter powder farther from the center while the screw conveyed material through the feeder. The initial failed print and limited reach explain why adding those features was a functional redesign rather than an aesthetic change.

## Process images

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

## Outcome and reflection

The cornstarch trials showed why one powder could not stand in for the whole test set. Larger flights addressed the feeding region, while greater agitator reach addressed material outside it. I carried those two problems into the next CAD revision instead of treating a stronger motor or one successful print as a complete solution.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R06_diagnose_cornstarch_jamming_and_the_first_agitator_s_incomplete_coverage.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
