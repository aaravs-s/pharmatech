# J04 Test the removable threaded hopper and replace it with a short locking interface

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I first made the hopper removable using a threaded connection to its funnel. The thread offered both retention and a straightforward way to take the parts apart for cleaning, without adding separate catches or a complicated fastening system.

The physical fit was worse than the CAD suggested. As I screwed the printed parts together, resistance increased and the material began to fray or deform instead of seating smoothly. A connection intended to simplify maintenance was becoming a source of damage. I did not have a controlled clearance study that isolated a single cause, so the reliable observation was the progressive binding itself.

I reconsidered the connection and adapted the short locking movement used by a blender container. The replacement used slots and projecting tabs rather than several turns of printed thread. This changed the engagement path and concentrated attention on insertion clearance, full seating, and the surfaces that located the hopper.

## Technical detail

The connection was supposed to satisfy two requirements at once: constrain the hopper during operation and allow removal for cleaning. A thread looked attractive because it combined retention and alignment in one printed interface. The physical trial showed why nominal mating geometry was not enough. The parts printed, but resistance increased as they were screwed together, and the surfaces crumpled or frayed rather than seating cleanly.

The observation was progressive binding and damage. Clearance, pitch mismatch, surface roughness, first-layer distortion, and alignment were plausible contributors, but no controlled measurement series isolated one of them. I changed the engagement approach rather than assigning the failure to an unmeasured tolerance error.

The alternative changed the engagement path. Instead of sliding along several turns of printed thread, the hopper would insert into an interface with slots and projecting tabs, then lock through a short movement. The blender mechanism supplied the general reference. The important design variables became tab thickness, slot width, the insertion clearance, the locking stop, and the supporting surface that made the hopper sit flush.

The locking interface still had to locate the hopper, not merely retain it. Insertion clearance could make the connection easier to assemble while allowing unwanted rotation or lift. Full seating also mattered because an off-center outlet would undermine the powder path even if the tabs could be pushed into their slots.

This revision exposed another design question: even if a short locking connection was easier to use, did the added joint actually simplify cleaning? Both sides still introduced contact surfaces and recesses. That led me to revisit the separation of the hopper and funnel in the next iteration.

## Process images

![Printed blue threaded hopper components from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_1.jpg)

Printed blue threaded hopper components from the M1 notes.

![Printed cylindrical hopper or receiver component from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_6.jpg)

Printed cylindrical hopper or receiver component from the M1 notes.

![Annotated hopper section showing the screw-in funnel concept and internal drive.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_5.jpg)

Annotated hopper section showing the screw-in funnel concept and internal drive.

![Hopper interface with locking features from the M1 notes; exact CAD revision not identified.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_3.jpg)

Hopper interface with locking features from the M1 notes; exact CAD revision not identified.

## Outcome and reflection

The failed thread led to a tab-and-slot alternative with a shorter engagement path. It also made me question the underlying requirement: a removable joint only helps if it reduces the work needed to clean the complete powder path. That question led directly to the next simplification of the hopper and funnel.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R04_test_the_removable_threaded_hopper_and_replace_it_with_a_short_locking_interface.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
