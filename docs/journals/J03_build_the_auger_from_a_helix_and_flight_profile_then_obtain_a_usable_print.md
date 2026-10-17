# J03 The auger print had to work first

*Milestone 1 | Retrospective build notes*

Before I could learn anything useful about powder flow, I had to get a usable auger off the printer. The early attempts had bed-adhesion problems. Applying glue helped keep the print attached, which finally let me move past that immediate obstacle.

It's a frustrating kind of delay because it isn't the feeding problem I set out to solve. But a warped screw or damaged flight would change the clearance inside the housing, so carrying a bad print into the next test would only make the diagnosis messier.

![V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_helix.jpg)

V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

I used an auger because I could control its motion and then measure what that motion delivered. I didn't expect a fixed grams-per-revolution number to work across all eight powders. The scale would eventually handle the mass; the screw first needed to give me a reasonably controllable way of adding it.

The construction views here are from the later V5 model. They show the helix, flight profile, and sweep clearly, along with the arms added later. They aren't pictures of the failed first print. I don't have its exact settings or model revision in the saved record.

## Helix and sweep settings

The archived V5 model exposes the screw construction through Helix 1, Sketch 1, and Sweep 1. In Helix 1, the selected input is a circular edge from Extrude 2. The helix uses pitch input, a 2-degree start angle, a height end condition of 3.81 cm, a target pitch of 0.635 cm, and clockwise handedness. In millimetres, the height is 38.1 and the pitch is 6.35. Dividing height by pitch gives six turns for this helix definition.

The path alone isn't a screw flight. Sketch 1 defines the section to be carried along it on the Top plane. In the construction view, the shaft and helix are present while the small flight section remains highlighted at the start of the path. Sweep 1 then selects the faces of Sketch 1, uses Curve 1 as its path, and adds the resulting material to the part named tube adapter. The archived feature has no additional profile-control mode, and Twist and Scale are unchecked.

These settings define a constant-pitch screw. A later planning note proposed flights that funnel downward, which is a different geometric idea. The six-turn helix shown here documents the uniform construction; it doesn't establish that the tapered alternative was manufactured or tested.

A successful print still had to function inside the housing. Flight thickness, shaft straightness, surface roughness, and seam position all affect the space between the screw and its enclosure. Adhesion solved the immediate manufacturing obstacle, while the following powder trials tested the suitability of the feeding geometry.

## From profile to screw

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

Getting a usable print only cleared the first hurdle. It still had to rotate inside the housing and move actual powder. Sugar and cornstarch were going to be much more informative than judging the flight by how clean it looked on the screen.

<details>
<summary>Notes added while reconstructing this entry</summary>

The manufacturing record identifies bed adhesion as the early printing problem and glue as the practical change that allowed a usable print. The failed print's exact revision and first-layer settings aren't preserved. The later V5 views explain the screw construction, including the subsequently added arms, without claiming to depict that first failed part.

The result of this update was a usable prototype for powder trials. It wasn't a calibrated grams-per-revolution device yet. Sugar loading and cornstarch movement supplied the next information about whether the outlet resistance and flight geometry suited different materials.

</details>

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R03_build_the_auger_from_a_helix_and_flight_profile_then_obtain_a_usable_print.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
