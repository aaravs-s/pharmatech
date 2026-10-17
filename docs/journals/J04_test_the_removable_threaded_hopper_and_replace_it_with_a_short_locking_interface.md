# J04 The thread looked better in CAD

*Milestone 1 | Retrospective build notes*

The threaded hopper connection seemed like a good idea. Screw it in, keep it secure, unscrew it for cleaning. No separate latch to design. I liked how much that one interface was supposed to do.

Then I tried the printed parts. The farther they screwed together, the harder they became to turn. Instead of seating smoothly, the material started to fray and deform. That was a pretty direct answer to whether this version was usable.

![Printed blue threaded hopper components from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_1.jpg)

Printed blue threaded hopper components from the M1 notes.

I couldn't pin it on one measured cause. Clearance, rough surfaces, thread geometry, alignment, print distortion: several things could have contributed. What I did know was that a cleaning interface shouldn't damage itself during assembly. Forcing it harder wasn't much of a design strategy.

I looked at the short locking movement on a blender container and tried a slot-and-tab arrangement instead. Insert the hopper, make a short movement to lock it, and let a seating surface locate it. That reduced the long sliding contact of the thread. It still left the fit, retention, and outlet alignment to get right.

## What the two interfaces ask of the print

The alternative changed the engagement path. Instead of sliding along several turns of printed thread, the hopper would insert into an interface with slots and projecting tabs, then lock through a short movement. The blender mechanism supplied the general reference. The details to work out were tab thickness, slot width, the insertion clearance, the locking stop, and the supporting surface that made the hopper sit flush.

The locking interface still had to locate the hopper, not merely retain it. Insertion clearance could make the connection easier to assemble while allowing unwanted rotation or lift. Full seating also mattered because an off-center outlet would undermine the powder path even if the tabs could be pushed into their slots.

## More views

![Printed cylindrical hopper or receiver component from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_6.jpg)

Printed cylindrical hopper or receiver component from the M1 notes.

![Annotated hopper section showing the screw-in funnel concept and internal drive.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_5.jpg)

Annotated hopper section showing the screw-in funnel concept and internal drive.

![Hopper interface with locking features from the M1 notes; exact CAD revision not identified.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_3.jpg)

Hopper interface with locking features from the M1 notes; exact CAD revision not identified.

The tab-and-slot idea gave me another route, but I was also starting to question why this joint existed at all. If both sides still needed cleaning, was making them separate actually saving any work? That question ended up mattering more than making the original thread fit.

<details>
<summary>Notes added while reconstructing this entry</summary>

The connection was supposed to satisfy two requirements at once: constrain the hopper during operation and allow removal for cleaning. A thread looked attractive because it combined retention and alignment in one printed interface. The physical trial showed why nominal mating geometry wasn't enough. The parts printed, but resistance increased as they were screwed together, and the surfaces crumpled or frayed rather than seating cleanly.

The observation was progressive binding and damage. Clearance, pitch mismatch, surface roughness, first-layer distortion, and alignment were plausible contributors, but no controlled measurement series isolated one of them. I changed the engagement approach rather than assigning the failure to an unmeasured tolerance error.

This revision exposed another design question: even if a short locking connection was easier to use, did the added joint actually simplify cleaning? Both sides still introduced contact surfaces and recesses. That led me to revisit the separation of the hopper and funnel in the next iteration.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R04_test_the_removable_threaded_hopper_and_replace_it_with_a_short_locking_interface.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
