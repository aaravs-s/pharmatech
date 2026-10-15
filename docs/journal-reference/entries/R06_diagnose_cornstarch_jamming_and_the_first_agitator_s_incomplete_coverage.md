# R06 Diagnose cornstarch jamming and the first agitator's incomplete coverage

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J10, J11

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Distinguish a feeder-clearance problem from stagnant powder in the hopper and identify the geometry needed for the next iteration.

## Design process

Cornstarch showed that the sugar configuration was not a universal feeder. It clumped, jammed, and sometimes remained in areas of the hopper that the auger did not disturb. Changing only the drive speed would not necessarily solve a situation where powder was not reaching the feeding region.

I revised the cornstarch auger to have more width and larger flights. The milestone notes report that this helped the powder move through the mechanism and reduced the tight compression associated with the earlier configuration. The important comparison is the actual before-and-after geometry, so the final journal should include the diameters, pitch, and housing clearance rather than simply saying the new auger was bigger.

This was the point where I stopped treating powder consistency as a minor setting. The feeder geometry and the control behavior both needed to respond to how the material moved. The change improved the prototype according to the notes, but a numerical accuracy claim belongs with a weighed test rather than a visual impression of smoother flow.

I found that powder could remain around the sides of the hopper while the auger continued rotating. That meant the feeder could appear active even though some material was not being cycled toward the outlet. This was especially relevant to cornstarch, which did not behave like freely flowing sugar.

I attempted to model and print an agitator, but the notes describe two problems: the print failed, and the design did not cover the full width of the hopper. Those are separate issues. Producing a successful print would not have fixed the limited sweep area, and extending the agitator would not by itself solve the printing failure.

The next revision needed to reach the powder near the edges while maintaining enough clearance to rotate without scraping the housing unintentionally. I would document the actual print failure and then show the sweep area in CAD. That makes the reason for the next geometry change clear instead of presenting the successful agitator without the failed intermediate design.

## Construction and implementation detail

Cornstarch produced two related but different symptoms. It was hard to push through the auger consistently and sometimes jammed; it also remained in regions of the hopper the screw did not reach. A larger motor might help overcome resistance, but it would not automatically bring stationary powder from the wall into the active feed region. I needed to treat transport through the screw and circulation inside the hopper as separate design problems.

The notes record increasing the auger's width and using bigger flights for cornstarch. The reported aim was to reduce tight compression in the feeding space and give the material a more useful surface to engage. That is a geometric response to the observed powder behavior. It is not evidence of a measured torque reduction or a universal optimum flight profile; those quantities were not recorded in the milestone text.

The first agitator attempt failed in printing and did not account for the full width of the hopper. Even a successful print of an undersized arm would have left the stagnant wall region largely untouched. The redesign therefore needed an arm envelope that approached the hopper boundary while leaving enough clearance to rotate after printing and assembly.

For recreation, the useful comparison is the relationship among auger outside diameter, housing bore, flight pitch, arm radius, and hopper wall. Those values should be tied to model versions. The V5 and V10 saved views establish that auger-and-arm geometry existed, but they do not identify the exact original cornstarch prototype or quantify how much each clearance changed. I leave those details for the actual print and test records instead of selecting dimensions from whichever model is easiest to view.

A test of this revision should also document the hopper after dispensing, because a mass collected at the outlet can conceal poor coverage inside. The important observation was that some cornstarch stayed untouched. Photographs of the remaining powder, together with a view of the rotating sweep envelope, explain why an agitator was necessary more clearly than a final render of a screw.

The next design combined rotation of the screw and a pair of agitator arms. That provided a route to move powder from the walls toward the feeder while the screw conveyed it outward. I would preserve the failure and redesign as separate states so the reader can see what problem each new feature addressed.

## Image sequence

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

## Result and handoff

A wider/larger-flight cornstarch auger was tried, and the failed undersized agitator motivated an arm redesign for hopper coverage. Quantitative clearance and torque comparisons are missing.

## Complete from your records

Identify failed and revised print versions, flight dimensions, arm reach, wall clearance, and whether the failure was adhesion, unsupported geometry, or another print issue.

[IMAGE PLACEHOLDER: Original cornstarch screw next to the wider revision, with measured diameters and pitch.]

[IMAGE PLACEHOLDER: Failed agitator print and a photograph of stagnant wall powder after a run.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
