# R03 Build the auger from a helix and flight profile, then obtain a usable print

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J04

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Create the screw-flight geometry and resolve the print failure that prevented a usable first prototype.

## Design process

I chose an auger as the feeding mechanism because its rotation can move powder through a constrained path. A continuously open outlet could let a free-flowing powder escape without any commanded motion. The auger gave me a mechanical variable I could later control through stepper motion, although the mass per turn still needed to be measured rather than assumed.

The first printing attempts had bed-adhesion problems. I used glue on the print surface, which helped the prototype stay attached and allowed me to obtain a usable part. This was relevant to the feeder itself: damaged flights, rough surfaces, and warped geometry could change the clearance inside the housing and interfere with powder movement.

I initially focused on the auger before adding a working agitator. That narrowed the test to the basic feeding path. The V5 CAD view included here shows a later auger with agitator arms; it illustrates the geometry but should not be described as a photo of the first failed print. The missing first-print evidence should be added separately if it still exists.

## Construction and implementation detail

The archived V5 model exposes the screw construction through Helix 1, Sketch 1, and Sweep 1. In Helix 1, the selected input is a circular edge from Extrude 2. The helix uses pitch input, a 2-degree start angle, a height end condition of 3.81 cm, a target pitch of 0.635 cm, and clockwise handedness. In millimetres, the height is 38.1 and the pitch is 6.35. Dividing height by pitch gives six turns for this helix definition.

The path alone is not a screw flight. Sketch 1 defines the section to be carried along it on the Top plane. In the construction view, the shaft and helix are present while the small flight section remains highlighted at the start of the path. Sweep 1 then selects the faces of Sketch 1, uses Curve 1 as its path, and adds the resulting material to the part named tube adapter. The archived feature has no additional profile-control mode, and Twist and Scale are unchecked.

Those settings describe a particular constant-pitch construction. They should not be mixed with the later planning note proposing flights that funnel downward. That note is a separate geometric idea. The journals need to show when the uniform screw existed, when the tapered proposal was made, and which revision was actually printed. A reader otherwise has no way to tell whether a proposed improvement was tested or merely drawn.

The printing problem was a separate implementation step. Bed adhesion failed during the first attempts, and glue helped obtain a usable print. The notes do not record the exact first-layer settings or the failed model's version. I therefore keep the archived helix/sweep views as construction evidence and leave space for the first failed print. I cannot identify the V5 screw with its later agitator arms as the exact first printed auger simply because it is available in the history.

Once the print stayed attached, the next question was mechanical rather than cosmetic: could the flight move through its housing without rubbing enough to stall, and did the printed section remain intact? The flight thickness, seam, surface roughness, and shaft straightness all affect that check. The photographs needed for this step are the failed first layer, the successful print before installation, and the installed screw beside the housing. The final CAD image now follows the path and sweep views instead of replacing them.

The result of this update was a usable prototype for powder trials. It was not a calibrated grams-per-revolution device yet. Sugar loading and cornstarch movement supplied the next information about whether the outlet resistance and flight geometry suited different materials.

## Image sequence

![V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_helix.jpg)

V5 screw path: Helix 1, circular edge input, 2 deg start angle, 3.81 cm height, 0.635 cm target pitch, clockwise.

![V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sketch.jpg)

V5 flight section: Sketch 1 on Top plane before Sweep 1. The highlighted section supplies the profile for the helix sweep.

![V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_flight_sweep.jpg)

V5 flight: Sweep 1 adds the Sketch 1 faces along Curve 1 into tube adapter; no extra Twist or Scale is enabled.

![V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_auger_agitator.jpg)

V5 Part Studio 1, saved July 2 2026. Auger geometry with two agitator arms.

## Result and handoff

The auger could be printed after addressing adhesion, and the recovered CAD shows how a later constant-pitch screw was constructed. The first-print revision remains unidentified.

## Complete from your records

Identify the exact model used for the first print, printer settings, glue change, support strategy, and housing-clearance check.

[IMAGE PLACEHOLDER: Failed first layer or warped auger before the adhesion change.]

[IMAGE PLACEHOLDER: Successful auger print before installation, followed by a photograph of it inside the housing.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
