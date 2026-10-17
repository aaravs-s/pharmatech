# J03 Build the auger from a helix and flight profile, then obtain a usable print

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I chose an auger because its rotation could move powder through a constrained path and provide a motion variable for later feedback control. I could command steps or pulses, then use the scale to measure their effect. I did not assume that one revolution would deliver the same mass for every powder.

The first manufacturing obstacle was bed adhesion. My early print attempts did not stay attached well enough to produce a usable part. Applying glue to the print surface helped the prototype remain attached and allowed me to continue. This mattered mechanically: a warped shaft or damaged flight changes the running clearance inside the feeder, even if the rest of the model is dimensionally correct.

I initially concentrated on the screw before adding a working agitator. The V5 construction views illustrate the later constant-pitch auger and its feature sequence. They are retrospective views of that saved model, rather than photographs of the first failed print. Keeping the revisions distinct lets me explain the construction without assigning an undocumented print setting or failure to the wrong version.

## Technical detail

The archived V5 model exposes the screw construction through Helix 1, Sketch 1, and Sweep 1. In Helix 1, the selected input is a circular edge from Extrude 2. The helix uses pitch input, a 2-degree start angle, a height end condition of 3.81 cm, a target pitch of 0.635 cm, and clockwise handedness. In millimetres, the height is 38.1 and the pitch is 6.35. Dividing height by pitch gives six turns for this helix definition.

The path alone is not a screw flight. Sketch 1 defines the section to be carried along it on the Top plane. In the construction view, the shaft and helix are present while the small flight section remains highlighted at the start of the path. Sweep 1 then selects the faces of Sketch 1, uses Curve 1 as its path, and adds the resulting material to the part named tube adapter. The archived feature has no additional profile-control mode, and Twist and Scale are unchecked.

These settings define a constant-pitch screw. A later planning note proposed flights that funnel downward, which is a different geometric idea. The six-turn helix shown here documents the uniform construction; it does not establish that the tapered alternative was manufactured or tested.

The manufacturing record identifies bed adhesion as the early printing problem and glue as the practical change that allowed a usable print. The failed print's exact revision and first-layer settings are not preserved. The later V5 views explain the screw construction, including the subsequently added arms, without claiming to depict that first failed part.

A successful print still had to function inside the housing. Flight thickness, shaft straightness, surface roughness, and seam position all affect the space between the screw and its enclosure. Adhesion solved the immediate manufacturing obstacle, while the following powder trials tested the suitability of the feeding geometry.

The result of this update was a usable prototype for powder trials. It was not a calibrated grams-per-revolution device yet. Sugar loading and cornstarch movement supplied the next information about whether the outlet resistance and flight geometry suited different materials.

## Process images

![V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_helix.jpg)

V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

## Outcome and reflection

Resolving adhesion produced a usable prototype for powder trials. The helix and sweep gave me a controllable screw geometry, but a printed screw was only the start of the feeding problem. The following tests with sugar and cornstarch determined whether the outlet resistance, flight geometry, and hopper circulation suited the materials.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R03_build_the_auger_from_a_helix_and_flight_profile_then_obtain_a_usable_print.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
