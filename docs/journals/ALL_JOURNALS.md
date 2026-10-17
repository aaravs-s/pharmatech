# Pill Compounder: Complete Personal Journal

AI-assisted retrospective narratives for personal documentation. No session dates or hours are assigned. These are not Forge submissions. See the [collection notes](README.md) for scope and image provenance.

## Contents

- [J01: Define the requirements and develop the shared eight-hopper architecture](#j01)
- [J02: Construct the first hopper, adapter, and bottom-feeder CAD](#j02)
- [J03: Build the auger from a helix and flight profile, then obtain a usable print](#j03)
- [J04: Test the removable threaded hopper and replace it with a short locking interface](#j04)
- [J05: Simplify the powder path and reduce sugar leaking during loading](#j05)
- [J06: Diagnose cornstarch jamming and the first agitator's incomplete coverage](#j06)
- [J07: Model the two-arm agitator and compare uniform and tapered-flight concepts](#j07)
- [J08: Wire the first NEMA 17 and TMC2209 drive and establish controlled motion](#j08)
- [J09: Read serial scale data and establish the baseline mass for each dispense](#j09)
- [J10: Build the touchscreen workflow and hand targets to a separate controller process](#j10)
- [J11: Replace continuous feeding near the target with stop, settle, and pulse phases](#j11)
- [J12: Separate powder behavior into configurable motion and settling profiles](#j12)
- [J13: Stop unwanted motion after program termination and add layered shutdown behavior](#j13)
- [J14: Plan the electronics mounting and PCB while the control system is still changing](#j14)
- [J15: Investigate loaded speed limits and upgrade the NEMA 17 drive](#j15)
- [J16: Make phase thresholds depend on dose size: the July 21 to July 24 controller revision](#j16)
- [J17: Replace the barcode plan with selectable profiles and run the doser from the Pi](#j17)
- [J18: Measure 5 g performance with sugar, salt, cocoa, and cinnamon](#j18)
- [J19: Test 5 g dispensing with baking soda, cornstarch, powdered sugar, and flour](#j19)
- [J20: Evaluate the 0.055 g limit and separate accuracy from repeatability](#j20)
- [J21: Build the solid eight-pocket carousel and evolve it into an open two-plate structure](#j21)
- [J22: Develop the lift mechanism that clears the drive before indexing](#j22)
- [J23: Replace the angle-sensitive drive coupling with serrated mating teeth](#j23)
- [J24: Construct the extrusion frame and integrate the carousel, scale, lift, and screen](#j24)
- [J25: Convert carousel positions to step counts and establish a known reference](#j25)
- [J26: Choose the shortest carousel route and wait for completed indexing](#j26)
- [J27: Sequence lift, indexing, engagement, and mass feedback for a multi-powder recipe](#j27)
- [J28: Move STEP generation from the software loop to hardware timers](#j28)
- [J29: Add driver-alarm handling and an interactive motor-speed test](#j29)
- [J30: Drop the fixed-board plan, troubleshoot perfboard, and mount a half-size breadboard](#j30)
- [J31: Design protective covers and consolidate wiring along the frame](#j31)
- [J32: Write an operating and cleaning procedure consistent with the actual prototype](#j32)
- [J33: Bring the prototype together and assess the documented results](#j33)

---

<a id="j01"></a>

# J01 Define the requirements and develop the shared eight-hopper architecture

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I began by breaking automated powder compounding into a sequence I could build and test: choose an ingredient, move it to a dispensing position, add a requested mass, and stop using feedback from a scale. I organized the work into five milestones so the single-powder mechanism could be tested before I committed to a complete carousel.

My initial requirements were eight powder positions, a 100 g capacity per doser, a 50 by 50 by 50 cm operating envelope, and a final mass within 3% of the requested dose. These were design targets. I selected sugar, salt, cocoa, cinnamon, baking soda, cornstarch, powdered sugar, and flour because their different flow behavior would expose weaknesses that one easy material could hide.

The central layout decision was to share the active drive hardware at one dispensing station. Putting an auger motor and a separate agitation motor on every hopper could require sixteen motors. A shared station reduced that duplication, but introduced a harder mechanical interface: the drive had to disengage before the disk rotated and reconnect afterward. I accepted that tradeoff and focused first on one complete powder path.

## Technical detail

I separated the ingredient-selection problem from the mass-measurement problem. The disk chooses which powder path sits over the receiving container; the auger controls movement through that path; the scale measures the consequence of that motion. This distinction matters because selecting the correct hopper does not guarantee the correct mass, and controlling motor steps does not establish how much a particular powder actually dispensed.

The first architecture therefore had three interfaces to resolve: the hopper-to-feeder connection, the rotating disk-to-frame support, and the stationary motor-to-rotating auger engagement. Each powder retained its own contact path. Sharing a drive motor could reduce electrical duplication without requiring different ingredients to pass through the same auger. The contact surfaces would still need cleaning and inspection; independent paths alone do not demonstrate an absence of contamination.

For the eight-position layout, I used equal angular spacing as the starting constraint. A full revolution divided by eight gives 45 degrees per station. The later archived disk makes this concept concrete: eight pockets surround the central axis. I had to account for the hopper diameter, radial position, room around the center attachment, and the space needed by the fixed drive station. Those dimensions are coupled: enlarging a hopper can force a larger disk or reduce the material between stations.

I also distinguished capacity from dosing range. A 100 g hopper-capacity target describes how much material the hopper should hold; it does not by itself validate a 100 g dispensing run. Likewise, a 3% accuracy target needs a specified requested mass. At 5 g, 3% permits 0.150 g of error, while at 0.055 g it permits only 0.00165 g. I needed a test plan that included both useful larger doses and the difficult small-dose case rather than treating the percentage as one universal setting.

The shared drive station became the main architectural tradeoff. It reduced the number of motors carried around the carousel, but required reliable vertical engagement and disengagement. I deferred the complete carousel build while testing one powder path. That left a practical next step: obtain a printable single doser and learn whether its interfaces and powder movement were good enough to reproduce eight times.

## Process images

![Early eight-position solid rotary disk concept from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_2.jpg)

Early eight-position solid rotary disk concept from the M1 notes.

![Early rotary and fixed-drive concept in top view.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_10.jpg)

Early rotary and fixed-drive concept in top view.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

## Outcome and reflection

I finished this stage with a defined architecture and a useful order of development: prove one doser, add mass feedback, then reproduce the feeding station around the carousel. The largest lesson was that reducing the motor count transferred complexity into alignment and engagement. Those interfaces became design problems to solve deliberately, rather than details to leave until final assembly.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R01_define_the_requirements_and_develop_the_shared_eight_hopper_architecture.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j02"></a>

# J02 Construct the first hopper, adapter, and bottom-feeder CAD

*Milestone 1 | Personal retrospective journal*

## Design and iteration

I modeled the first complete single doser as a set of related parts: a powder holder, a tube adapter, and a bottom feeder. The purpose was to create a physical route from the loaded hopper to a receiving container, with enough access to assemble the auger and remove powder-contact components.

I treated cleaning access and shaft alignment as design requirements from the beginning. Separate parts made it possible to change an interface without redrawing the entire machine, but each added joint also created another place for residue or misalignment. The holder, adapter, and feeder therefore had to work as an assembly rather than as three attractive individual models.

The archived V1 features preserve the construction order below. They show the profiles and feature settings behind the model, including dimensions that would be invisible in a finished assembly view. These are nominal CAD dimensions for this early revision; I have not substituted them for measurements of the later printed machine.

## Technical detail

The V1 Part Studio contains three main groups: powder holder, tube adapter, and bottom feeder. The holder is built through Sketch 2 and Extrude 1, the adapter through Sketch 3 and Extrude 2, and the feeder through subsequent sketches, extrusions, and Revolve 1. Separating these features preserved the construction of each interface while keeping them in one assembly context.

The holder starts with concentric circular geometry on the Front plane. The displayed sketch diameters are approximately 1.476 in and 1.777 in. Those values correspond to about 37.49 mm and 45.14 mm; their radial difference is about 3.82 mm. This is the early holder's wall geometry, not a claim that the eventual hopper used those same dimensions. Extrude 1 creates a new solid from the selected sketch face to a blind depth of 4.724 in, approximately 119.99 mm.

The adapter is created separately. Its archived Extrude 2 uses two sketch regions, a 5.118 in blind depth, and a checked starting offset of 0.197 in. Converted for comparison, those are approximately 130.00 mm and 5.00 mm. The offset is an important part of the feature definition: omitting it when recreating the model would change where the adapter begins relative to the holder and feeder.

The bottom feeder adds geometry around the shaft end. Revolve 1 selects faces of Sketch 6 and uses an edge of that sketch as its axis. A full Add revolve merges the result into the bottom-feeder part. The profile determines the section around the axis, while the axis itself determines how that section becomes the rounded support geometry.

I treated the separate parts as one assembly problem. The adapter bore, shaft centerline, and feeder support have to remain concentric; a small offset can make a nominally suitable shaft bind. The construction views follow the holder sketch, extrusion, adapter definition, feeder revolution, and complete V1 model, retaining the relationships behind the finished shape.

The physical prototype established an assembled hopper and an outlet above the receiving container. The saved record does not contain a complete tolerance stack or dimensional inspection of that print. I therefore use V1 to explain the nominal construction and assembly relationships, with later trials supplying evidence of feeding behavior.

## Process images

![V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_sketch.jpg)

V1 holder: Sketch 2 on Front plane, before holder extrusion; displayed concentric diameters approximately 1.476 in and 1.777 in.

![V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_hopper_extrude.jpg)

V1 holder: Extrude 1, New solid, blind depth 4.724 in. Read-only feature construction preview.

![V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_adapter_extrude.jpg)

V1 adapter: Extrude 2, New solid, depth 5.118 in, starting offset 0.197 in. Read-only feature construction preview.

![V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_feeder_revolve.jpg)

V1 feeder: Revolve 1 adds faces of Sketch 6 around its selected edge, full revolve, merged into bottom feeder.

![V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v1_complete.jpg)

V1 complete saved feeder model, after closing the feature preview. Holder, adapter, and bottom feeder are present.

![Physical single-hopper prototype during powder handling.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_4.jpg)

Physical single-hopper prototype during powder handling.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

## Outcome and reflection

The assembled single doser gave me a practical platform for testing fit, powder movement, and the auger drive. Modeling the support and outlet together made the next problems easier to identify: an auger could look correct in isolation and still rub or feed poorly once constrained by its housing. I moved next to producing a usable screw and checking the real printed interfaces.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R02_construct_the_first_hopper_adapter_and_bottom_feeder_cad.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j03"></a>

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


---

<a id="j04"></a>

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


---

<a id="j05"></a>

# J05 Simplify the powder path and reduce sugar leaking during loading

*Milestone 1 | Personal retrospective journal*

## Design and iteration

After working through the detachable interfaces, I reconsidered whether the hopper and funnel needed to be separate. Both components still had internal surfaces to clean, and the joint added recesses and assembly work. Combining the funnel and enclosure reduced the number of parts and removed one interface from the powder path.

I also explored an integrated rotary-disk concept containing eight hopper cavities. That concept belonged to the early solid carousel; the supporting structure changed again later. At this stage, the useful idea was reducing unnecessary interfaces while continuing to test one feeder.

Sugar exposed a separate mechanical problem. It moved readily, but some escaped from the outlet during loading before I intentionally rotated the auger. I narrowed the opening near the auger exit to resist this passive flow while retaining a route for material driven by the screw. My milestone record describes that change resolving the immediate loading problem. It did not establish a leakage rate across different fill levels or powders.

## Technical detail

The removable hopper was initially a means to make cleaning easier, not an end in itself. I revisited it after the thread and locking iterations. If both the hopper and funnel still needed their internal surfaces wiped, separation could add cleaning work at the joint instead of reducing it. Combining the funnel and enclosure reduced the number of parts and removed an interface from the powder path.

The early integrated-cavity concept appears in the solid carousel. The later skeletal two-plate structure is a subsequent revision with a different support arrangement. Comparing them preserves the evolution of the machine: reducing interfaces was an early design direction, while the eventual carousel continued to change during integration.

Sugar exposed another issue during loading. Material escaped from the downstream end before the auger was intentionally turning. That was uncontrolled discharge, so adjusting a software stop threshold would not address it. The mechanical path needed enough resistance to retain the powder while the machine was idle and being filled.

I narrowed the opening at the auger end according to the milestone notes. The aim was to restrict the bypass path through which sugar could fall immediately, while retaining a route for material pushed by the screw. This connects outlet geometry to the intended control model: the scale loop is most useful when auger motion is the main cause of additional material entering the cup.

My milestone notes report that narrowing the end addressed the immediate sugar-loading spill and that sugar did not require agitation in those trials. The record contains neither the before-and-after aperture dimensions nor a measured leakage series. I regard the result as a practical response to the observed loading problem, with performance across other materials left to their own tests.

The outcome was a simpler contact path and improved control over sugar before motion began. Cornstarch then challenged the same geometry in the opposite way: instead of passing too easily, it clumped, jammed, and left material untouched. That gave the next update a concrete reason to change the flights and add agitation.

## Process images

![Cross-section CAD illustrating the internal hopper, auger path, and base.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_8.jpg)

Cross-section CAD illustrating the internal hopper, auger path, and base.

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

## Outcome and reflection

I left this iteration with a simpler contact path and better control of sugar during loading. The important distinction was between powder released by a command and powder falling out while the machine was idle. Feedback control could regulate the former, but the latter first required a mechanical correction. Cornstarch then exposed the opposite problem: material that would not move consistently enough.

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R05_simplify_the_powder_path_and_reduce_sugar_leaking_during_loading.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j06"></a>

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


---

<a id="j07"></a>

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


---

<a id="j08"></a>

# J08 Wire the first NEMA 17 and TMC2209 drive and establish controlled motion

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I assembled the initial electrical drive using a NEMA 17, a TMC2209 driver, and a breadboard. The Raspberry Pi 4 provided the first control connection, with a touchscreen for the user interface. This moved the project from mechanical powder trials toward commanded feeding.

I kept the basic motion task separate from target-mass accuracy. STEP pulses, direction, and driver enable determine what the motor is asked to do; none of them measure how much powder reaches the cup. Before a closed-loop controller could be useful, the feeder needed an electrical interface that could start, change behavior, and stop.

The saved code includes multiple wiring stages. A small AccelStepper test uses STEP on pin 3 and DIR on pin 2, while the July controller assigns those signals differently. I have kept those configurations separate below. The exact original Pi GPIO map and driver current setting are not recorded in the material used for this account.

## Technical detail

M2 began with one active hopper, so the electrical prototype used one NEMA 17 and a TMC2209 on a breadboard. The Raspberry Pi 4 provided the initial control connection, and the touchscreen added the user interface. At this point I needed to prove direction, enable control, and repeatable commanded motion separately from target-mass accuracy.

STEP, DIR, and EN control different aspects of the drive. STEP requests incremental motion, DIR selects its direction, and EN activates or disables the driver according to its polarity. The motor winding connections and shared signal reference are separate from those logic functions. A breadboard layout records packaging, while the corresponding pin assignments identify a particular controller revision.

The later July Arduino source makes the eventual command interface concrete: auger STEP is pin 2, DIR is pin 3, and ENABLE is pin 4. In that file, LOW enables the driver and HIGH disables it, while HIGH is the dispensing direction. This is an archived Arduino configuration, not the original Pi GPIO map. The timer-based firmware later uses different pins and the opposite enable level, so those diagrams must be kept version-specific.

The standalone repository test uses AccelStepper::DRIVER with stepPin 3 and directionPin 2, sets a 1000-step/s maximum, and calls runSpeed() at 600 steps/s. That is a motor-only test with a different pin order from the July controller. It does not contain the mass-feedback loop or establish the final integrated wiring.

The source record establishes the breadboard components and the motion-test configurations. It does not preserve a complete electrical test sequence, supply measurements, or the TMC2209 current setting for the initial setup. I have retained that boundary while documenting the actual code values, rather than describing unrecorded checks as successful trials.

The outcome was the motor system used for the first scale-controlled doser. The next step was to read meaningful mass data, because a rotating motor alone cannot tell the machine how much powder reached the cup.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 20–37

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint8_t AUGER_STEP_PIN = 2;
const uint8_t AUGER_DIR_PIN = 3;
const uint8_t AUGER_ENABLE_PIN = 4;

// Most stepper drivers use LOW = enabled and HIGH = disabled.
const uint8_t DRIVER_ENABLE_LEVEL = LOW;
const uint8_t DRIVER_DISABLE_LEVEL = HIGH;

// Change HIGH to LOW if the auger turns in the wrong direction.
const uint8_t DISPENSE_DIRECTION = HIGH;

// ============================================================
// SPEED TUNING
// ============================================================
// Values are STEP pulses per second, not motor RPM.
// At 1/16 microstepping on a 200-step motor:
//   3200 steps/s = 60 RPM
//   4000 steps/s = 75 RPM
```

### timer_controller_later.ino · lines 39–55

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t AUGER_STEP_PIN   = 9;   // OC1A
const uint8_t AUGER_DIR_PIN    = 8;
const uint8_t AUGER_ENABLE_PIN = 10;
const uint8_t AUGER_ALM_PIN    = 7;

const uint8_t DISK_STEP_PIN    = 11;  // OC2A
const uint8_t DISK_DIR_PIN     = 12;
const uint8_t DISK_ENABLE_PIN  = 4;
const uint8_t DISK_ALM_PIN     = 6;

const uint8_t DRIVER_ENABLE_LEVEL  = HIGH;
const uint8_t DRIVER_DISABLE_LEVEL = LOW;
const uint8_t DISPENSE_DIR_LEVEL   = LOW;
const uint8_t DISK_FORWARD_DIR_LEVEL = HIGH;
const uint8_t DISK_REVERSE_DIR_LEVEL = LOW;

// ============================================================
```

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Outcome and reflection

The first motor setup gave the single doser an electrically commanded drive. It also established the need to track wiring together with firmware: a pin assignment from a standalone test cannot be carried into a different controller by assumption. I then added scale feedback so the machine could act on the mass actually collected.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j09"></a>

# J09 Read serial scale data and establish the baseline mass for each dispense

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I connected the balance's RS232 output to the Pi through a USB-to-serial adapter. The BOM lists a PL2303-based CableCreation adapter and a Bonvoisin balance advertised with a 0.001 g display resolution. The useful change was access to mass readings during motion, rather than relying on elapsed motor time as a substitute for quantity.

The controller needed a clear definition of newly dispensed mass. I used a starting baseline and calculated the increase from that value, allowing the receiving cup to remain on the scale. This also provided the right conceptual model for later recipes, where earlier ingredients would already be in the container.

Reading a number was not enough. The balance could update after powder had landed, averaging could add delay, and disconnected serial hardware could leave an old value in memory. I separated the reader from the control loop, kept a timestamp for accepted readings, and included a stale-data stop condition. The archived implementation makes those choices explicit.

## Technical detail

The controller defaults to /dev/ttyUSB0 at 9600 baud for the scale and /dev/ttyACM0 at 115200 baud for Arduino commands. These are separate serial devices with different roles. The mass data comes from the balance protocol through the RS232 adapter; it is not a measurement mode created by the color of a USB socket.

In the July controller, parse_weight() finds the first signed decimal number in a received line and converts it to a float. Invalid lines produce no accepted reading. This simple parser assumes that the first numeric field is mass and the unit is grams. The raw balance message is not preserved in the record, so stability and unit interpretation cannot be inferred beyond the parser's assumptions.

The scale reader runs in a background thread. It appends accepted values to a deque with a maximum length of eight, computes their mean, and records the time of the last valid update while holding a lock. The control loop reads that shared state rather than waiting on a serial line each time. That keeps serial I/O separate from control decisions, but averaging eight samples also means the displayed/control mass can lag behind a changing physical load.

Startup waits for at least five accepted readings, with a six-second timeout. The initial baseline routine samples the current averaged mass into another ten-value window and looks for a spread no larger than 0.003 g over a four-second interval. If it does not find that condition, it returns the latest value. This routine is an attempt at a stable starting mass, not a metrological proof of balance accuracy or ten independent balance transmissions.

The dispense amount is calculated as current mass minus the starting mass; remaining mass is requested target minus that difference. This allows a cup already on the scale to become the reference rather than assuming the raw balance reading starts at zero. The same distinction becomes important in a multi-ingredient recipe, where the next ingredient starts above the mass of earlier ingredients.

The July control loop stops if 2.50 seconds pass without a valid scale update. This gives feedback validity a physical consequence: an old low mass cannot remain a reason to feed indefinitely. The saved code establishes the timeout path, while no unplugged-scale timing measurement is available for that revision.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 108–116

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def parse_weight(line: str) -> Optional[float]:
    """Extract the first signed decimal number from a scale line."""
    match = re.search(r"[-+]?\d*\.?\d+", line)
    if match is None:
        return None
    try:
        return float(match.group())
    except ValueError:
        return None
```

### motor_2026-07-21.py · lines 346–366

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def read_scale() -> None:
    global current_weight, last_scale_update

    while running:
        try:
            if scale_serial is None:
                return
            line = scale_serial.readline().decode(errors="ignore").strip()
            if not line:
                continue
            value = parse_weight(line)
            if value is None:
                continue
            with weight_lock:
                weight_buffer.append(value)
                current_weight = sum(weight_buffer) / len(weight_buffer)
                last_scale_update = time.monotonic()
        except Exception as exc:
            if running:
                print(f"Scale read warning: {exc}", flush=True)
            time.sleep(0.05)
```

### motor_2026-07-21.py · lines 390–401

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def get_stable_weight(timeout: float = 4.0, spread: float = 0.003) -> float:
    readings: deque[float] = deque(maxlen=10)
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        value = get_weight()
        readings.append(value)
        if len(readings) == readings.maxlen and max(readings) - min(readings) <= spread:
            return sum(readings) / len(readings)
        time.sleep(0.05)

    return get_weight()
```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The scale connection supplied feedback tied to the result of feeding rather than only the command sent to the motor. The main lesson was that feedback has timing and validity requirements: a smooth mass display can still be delayed, and an old reading must not keep the auger running. Those constraints shaped the phased controller that followed.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j10"></a>

# J10 Build the touchscreen workflow and hand targets to a separate controller process

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I added a touchscreen workflow so a user could choose a powder and enter a requested mass without editing the control program. The hardware used a seven-inch DSI touchscreen connected to the Raspberry Pi 4. Although I was still developing a single active doser, the slot-based layout anticipated the later eight-position machine.

I separated the visible application from the motor-and-scale program. The app collected the request; the controller handled serial scale readings and phase decisions. That boundary kept recipe interaction distinct from the faster feedback work and gave me a clear place to pass the target and powder profile.

The operating procedure captures the early interaction: edit slot 1, select and load the powder, tare the scale, enter the mass, save, and start. The later app preserves a fuller implementation of the same division, including queued subprocess output and recipe data. I describe those later mechanisms as later code, rather than assigning the complete recipe interface to the first touchscreen version.

## Technical detail

The interface gathers the powder and requested grams, displays progress, and exposes stop controls. The separate controller owns scale feedback and auger phase decisions. This division let the application describe the user's request while the controller translated measured mass into motion.

The later app archive gives a detailed implementation of that design: CustomTkinter creates a fullscreen 800 by 480 interface, maintains slot and recipe data separately, and includes an on-screen keyboard. The powder list contains EMPTY plus the eight tested household powders. A recipe item contains the slot, powder name, and requested amount. This is later implementation evidence, not a claim that all recipe features were present in the first M2 interface.

The launch function chooses motor_scale_control.py, builds its path relative to the app file, and starts it with sys.executable, unbuffered output, a target argument, and a powder-name argument. Standard error is merged into standard output. A background reader places each received line into a queue, and the Tk event loop checks that queue through after() callbacks. That avoids blocking the touchscreen while serial feedback and motor control continue.

The output labels 'Dispensed:' and 'Remaining:' form a contract between the programs. The app extracts their following numbers with regular expressions, and the controller retains those labels in its output. Changing one side alone could leave the display stale while feeding continued, making the text protocol part of the implemented interface.

The later app adds startup checks for empty recipe slots, unknown disk position, and active motion. Those safeguards belong to the later integrated source. The initial single-doser workflow and the complete recipe app share the process boundary, but they are not presented as one unchanged version.

The source excerpts preserve the launch arguments and progress-parsing mechanism even where original development screenshots are unavailable. They explain how a target entered in the interface becomes a controller process and how its reported progress returns to the screen.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 890–895

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def read_motor_output(process):
    try:
        for line in process.stdout:
            output_queue.put(line.strip())
    except Exception:
        pass
```

### app_later.py · lines 898–919

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def process_output_queue():
    global dispensed_this_run, remaining_to_dispense
    while not output_queue.empty():
        line = output_queue.get()
        print("[MOTOR]", line)
        dispensed_match = re.search(r"Dispensed:\s*([-+]?\d*\.?\d+)", line)
        remaining_match = re.search(r"Remaining:\s*([-+]?\d*\.?\d+)", line)
        if dispensed_match:
            try:
                dispensed_this_run = max(0.0, float(dispensed_match.group(1)))
            except Exception:
                pass
        if remaining_match:
            try:
                remaining_to_dispense = max(0.0, float(remaining_match.group(1)))
            except Exception:
                pass
        else:
            remaining_to_dispense = max(0.0, current_run_target - dispensed_this_run)
        update_progress_labels()
    if motor_process is not None:
        root.after(100, process_output_queue)
```

### app_later.py · lines 1050–1083

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def launch_motor(amount_to_dispense, powder_type=None):
    global motor_process
    global current_run_target, remaining_to_dispense, dispensed_this_run
    global stopped_by_user, active_run_script_name
    stopped_by_user = False
    current_run_target = max(0.0, amount_to_dispense)
    remaining_to_dispense = current_run_target
    dispensed_this_run = 0.0
    if current_run_target <= 0.001:
        completed_screen()
        return
    script_name = choose_motor_script(current_run_target)
    active_run_script_name = script_name
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    print(f"Using motor script: {script_name}")
    if powder_type is None:
        powder_type = active_run_items[recipe_run_index]["name"]
    # Hand off the same verified Uno port, not the original environment default.
    close_disk_serial()
    child_environment = os.environ.copy()
    child_environment["ARDUINO_PORT"] = ARDUINO_PORT
    child_environment["ARDUINO_BAUD"] = str(ARDUINO_BAUD)
    if disk_position_known:
        child_environment["DISK_CURRENT_SLOT"] = str(disk_current_slot)
    else:
        child_environment.pop("DISK_CURRENT_SLOT", None)
    motor_process = subprocess.Popen(
        [sys.executable, "-u", script_path, str(current_run_target), powder_type],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1,
        env=child_environment)
    threading.Thread(target=read_motor_output, args=(motor_process,), daemon=True).start()
    running_screen(script_name)
    process_output_queue()
    check_motor_process()
```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The interface made the doser easier to operate while the separate controller retained responsibility for feeding. The most important software dependency was the information crossing that boundary: powder, grams, progress messages, and exit state all had to mean the same thing in both programs. That contract became increasingly important as positioning and multi-item recipes were added.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R10_build_the_touchscreen_workflow_and_hand_targets_to_a_separate_controller_process.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j11"></a>

# J11 Replace continuous feeding near the target with stop, settle, and pulse phases

*Milestone 2 | Personal retrospective journal*

## Design and iteration

Sugar made the stopping problem clear. A displayed reading near the target did not mean all the powder already released had reached the cup or appeared in the scale's output. Continuing at the bulk-feed rate until the display reached the requested mass could overshoot.

I changed the control strategy to use fast movement while much of the target remained, followed by slower, finite additions near completion. After stopping continuous motion, the controller waited before deciding whether another pulse was needed. The notes describe developing this behavior with sugar and applying similar reasoning to salt.

The tradeoff was dispensing time. Small motions and long pauses created more opportunities to observe the last addition, but too much finishing time made the machine slow. I therefore treated thresholds, pulse lengths, and settling delays as separate tuning variables. The July 21 source below records one specific configuration, rather than a universal setting for every dose.

## Technical detail

The central control problem was that motor stop and mass stop were not simultaneous. Powder could already be in the outlet or falling toward the cup, and the scale could report that mass after a delay. If I continued feeding until the displayed mass reached the target, the last commanded material could arrive too late to be accounted for. The notes identify this clearly for sugar and salt.

The July 21 controller selects among continuous TURBO, continuous NORMAL, and APPROACH/FINE/FINAL pulses. For a free-flowing profile, continuous motion ends at 1.250 g remaining; APPROACH changes to FINE at 0.120 g remaining; FINE changes to FINAL at 0.030 g remaining. The corresponding non-free-flowing cutoffs are 0.500, 0.120, and 0.050 g. These are grams remaining, not percentages of the target and not elapsed times.

The transition out of continuous mode is deliberately a separate action. The controller sends an auger stop, clears its active-command state, waits for the profile's continuous-settling interval, and restarts the loop using a later mass reading. It does not immediately issue the first pulse using the same pre-stop value. That separation is the key implementation detail behind 'slow down near the target.'

For free-flowing material, the July 21 settling values are 0.650 s after continuous motion, 0.220 s after APPROACH, 0.450 s after FINE, and 0.750 s after FINAL. For the other family, they are 0.300, 0.100, 0.160, and 0.220 s. The Arduino owns how many steps are in each pulse; Python owns the decision about when to issue one and how long to wait before re-evaluating mass.

Targets below 0.500 g bypass continuous motion in that archive. For a 0.055 g sugar target at the start, the remaining amount is below 0.120 but above 0.030, so the old logic chooses a FINE pulse. The later July 24 revision changes that behavior. This example makes the evolution visible: a small target cannot safely inherit the bulk-feed behavior of a large dose just because the powder name is the same.

The 3% project criterion differs from the code's absolute 0.001 g stop tolerance. In the July loop, remaining <= tolerance is tested before the separate overshoot branch, so an overshoot can satisfy the first condition. That implementation detail limits what the 'target reached' path means. I assessed dose error from the recorded final mass rather than treating a successful process exit as proof of accuracy.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 119–145

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose the Arduino command for the current amount remaining."""
    profile = PROFILES[powder_mode]
    powder_token = profile.command_name

    # Tiny targets never enter continuous mode because there is too
    # little mass available to absorb startup and chute overshoot.
    if target < MICRO_MODE_LIMIT:
        if remaining > profile.pulse_approach_to_fine:
            return f"AUGER PULSE {powder_token} APPROACH"
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    if remaining > TURBO_REMAINING:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-21.py · lines 540–564

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
        # The first transition out of continuous mode always stops and
        # settles before any pulse is issued. The next loop uses the new
        # scale reading and may already decide that the target is reached.
        if is_continuous_command(active_command):
            arduino.stop_auger()
            active_command = None
            print(
                f"Continuous phase complete; settling {profile.continuous_settle:.2f} s",
                flush=True,
            )
            time.sleep(profile.continuous_settle)
            continue

        if is_pulse_command(desired_command):
            print(f"PULSE -> {desired_command}", flush=True)
            arduino.run_pulse(desired_command)
            active_command = None
            time.sleep(settle_time_for(desired_command, powder_mode))
            continue

        raise RuntimeError(f"Unhandled auger command: {desired_command}")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_stop_signal)
```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The controller gained an explicit stop-settle-reassess step between bulk feeding and final pulses. That was more useful than simply reducing speed: it prevented the first finishing command from being based on the same delayed reading that ended continuous motion. Final scale mass remained the measure of success, because a software completion message alone could also occur after an overshoot.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R11_replace_continuous_feeding_near_the_target_with_stop_settle_and_pulse_phases.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j12"></a>

# J12 Separate powder behavior into configurable motion and settling profiles

*Milestone 2 | Personal retrospective journal*

## Design and iteration

The settings that limited sugar overshoot made cornstarch extremely slow near completion. A small command could release useful material from sugar or salt but almost nothing from a clumpier powder. I stopped treating the powder name as a label used only by the interface and made it select motion behavior.

I grouped the tested materials into two control families and gave each family its own speed, pulse size, and settling settings. This reduced the number of separate programs to maintain while preserving a way to make the more resistant materials move.

The family names describe controller configuration, not a universal classification of powder physics. For example, the notes describe cocoa and cinnamon as feeding relatively readily in this mechanism, while the archived program assigns both to NON_FREE_FLOWING. The actual mapping matters more than an intuitive reading of the label. Moisture, compaction, and geometry could also change how a material behaved.

## Technical detail

A small finishing motion that limited sugar overshoot could deliver very little cornstarch. I made powder selection affect two layers: the mapping from a name to a control family and the motion and settling parameters assigned to that family. This preserved one control structure while allowing different behavior.

The July Python archive maps granulated sugar and table salt to FREE_FLOWING. Powdered sugar, baking soda, cornstarch, ground cinnamon, flour, and cocoa are mapped to NON_FREE_FLOWING. The descriptive behavior notes call cocoa and cinnamon fine and relatively free-flowing, so the software family name is not a universal physical classification. It identifies a chosen control profile for this implementation.

In the July Arduino configuration, free-flowing APPROACH/FINE/FINAL pulses contain 8, 4, and 1 steps at 1100, 700, and 400 pulses per second. The other family uses 20, 10, and 3 steps at 1500, 1000, and 650 pulses per second. Continuous FREE rates are 4000 TURBO and 2500 NORMAL, while NONFREE uses 6000 and 4000. These values are electrical step pulses, not rotations per minute or grams dispensed.

The distinction between pulse size and pulse speed is important. Changing step rate alters how fast a commanded movement occurs; changing the number of steps changes its angular extent. Neither has a fixed mass conversion across all powders. Settling time adds a third variable because the controller may need to wait for discharged material to arrive and for the averaged scale value to catch up.

The later controller stores editable profiles in dictionaries, normalizes case and spacing in powder names, rejects unknown names, and checks for finite, ordered thresholds. It also contains a per-powder override dictionary, empty in the recovered file. That provides an extension point without establishing that all eight materials received individual calibration.

The practical result was a smaller configuration space than eight completely independent programs or a barcode database. I still needed to retain the final measured result for each powder. Shared parameters can simplify operation, but the powder tests determine whether that simplification is adequate at the intended mass.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 43–80

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t FREE_TURBO_RATE = 4000;
const uint32_t FREE_NORMAL_RATE = 2500;

const uint32_t NONFREE_TURBO_RATE = 6000;
const uint32_t NONFREE_NORMAL_RATE = 4000;

// Ramp continuous motion up instead of jumping instantly to full speed.
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;

// ============================================================
// PULSE TUNING
// ============================================================

const uint16_t FREE_APPROACH_STEPS = 8;
const uint32_t FREE_APPROACH_RATE = 1100;

const uint16_t FREE_FINE_STEPS = 4;
const uint32_t FREE_FINE_RATE = 700;

const uint16_t FREE_FINAL_STEPS = 1;
const uint32_t FREE_FINAL_RATE = 400;

const uint16_t NONFREE_APPROACH_STEPS = 20;
const uint32_t NONFREE_APPROACH_RATE = 1500;

const uint16_t NONFREE_FINE_STEPS = 10;
const uint32_t NONFREE_FINE_RATE = 1000;

const uint16_t NONFREE_FINAL_STEPS = 3;
const uint32_t NONFREE_FINAL_RATE = 650;

// If the Pi disappears while the auger is moving, stop automatically.
const uint32_t SERIAL_WATCHDOG_MS = 2000;

// ============================================================
// MOTOR STATE
```

### controller_later.py · lines 81–100

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
def get_profile(powder_name: str) -> tuple[str, dict]:
    key = " ".join(powder_name.lower().split())
    if key not in POWDER_CATEGORIES:
        raise ValueError(f"Add {powder_name!r} to POWDER_CATEGORIES before dispensing.")
    category = POWDER_CATEGORIES[key]
    if category not in ("FREE", "NONFREE"):
        raise ValueError(f"Invalid category for {powder_name!r}: {category}")
    settings = CATEGORY_PROFILES[category].copy()
    overrides = POWDER_OVERRIDES.get(key, {})
    unknown = overrides.keys() - settings.keys()
    if unknown:
        raise ValueError(f"Unknown profile settings: {sorted(unknown)}")
    settings.update(overrides)
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0
           for v in settings.values()):
        raise ValueError("Profile values must be finite, nonnegative numbers.")
    if not (settings["tolerance_g"] < settings["fine_to_final_g"] <
            settings["normal_to_fine_g"] < settings["turbo_to_normal_g"]):
        raise ValueError("Thresholds must increase: tolerance < final < fine < normal.")
    return category, settings
```

## Process images

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

Two parameter families gave me a manageable configuration structure for the eight test powders. Separating pulse extent, pulse rate, and settling time clarified what each change could affect. Shared settings simplified operation, but the recorded mass tests still had to establish the performance of each powder at each requested dose.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R12_separate_powder_behavior_into_configurable_motion_and_settling_profiles.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j13"></a>

# J13 Stop unwanted motion after program termination and add layered shutdown behavior

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I observed slow motor motion after the motor-and-scale program terminated. That meant ending the software task was not consistently ending the physical feeding action. I rerouted the driver's enable connection to a Pi GPIO as the response recorded in the milestone notes.

The notes suspected electrical noise, but I did not have a waveform measurement establishing that cause. The observation I could support was the unwanted motion and the change to enable control. That was enough to make shutdown a design requirement rather than an assumption about what closing a program would do.

As the controller developed, I added explicit stop commands, cleanup on process termination, and a firmware communication watchdog. The later app also handled cancellation across its child process and positioning state. These were successive layers with different responsibilities, rather than one wiring change that guaranteed every possible fault was covered.

## Technical detail

The early symptom was slow rotation after motor_scale terminated. I rerouted EN to a Pi GPIO as recorded in the M2 notes. Although those notes attribute the behavior to noise, no waveform or comparable measurement establishes the exact electrical mechanism. The observed unwanted motion and the enable-wiring change are the supported parts of the diagnosis.

Enable control provides a way to deactivate the driver as well as stop step commands. The July firmware uses LOW to enable, while the later integrated motor setup uses HIGH. Those are version-specific electrical assumptions: reversing the intended polarity could leave a driver active when software believes it is disabled.

The July Python shutdown function guards against repeated cleanup, sets its running state false, prints its shutdown action, sends STOP ALL through the Arduino client, waits briefly, closes connections, and exits. SIGINT and SIGTERM both call that path. This turns an ordinary process stop into an explicit motor-control action rather than assuming closing the terminal is enough.

The firmware adds another layer: it stops automatically if serial contact is absent for 2000 ms while motion is active. Python sends a heartbeat approximately every 0.50 s during continuous feeding. The intent is to stop if the Pi program disappears even when it cannot deliver its normal shutdown command. That watchdog complements EN control; it does not prove that every wiring or power fault has been handled.

In the later app, cancellation sends stop commands, signals the child process, marks actuator position UNKNOWN, and invalidates the disk reference. If the child remains alive, the app escalates to a kill after a delay. This is a later coordination layer in addition to the initial GPIO change and firmware watchdog.

The saved code shows normal cleanup, signal handling, and lost-communication stop routes. It does not contain a measured physical stop time for each case. I kept the distinction between sending a stop and observing the shaft stopped, especially because residual motion could add powder after apparent software completion.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 409–430

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def shutdown(exit_code: int = 0) -> None:
    global running, shutdown_started

    if shutdown_started:
        return
    shutdown_started = True
    running = False

    print("SHUTDOWN -> sending STOP ALL", flush=True)

    if arduino is not None:
        arduino.emergency_stop()
        time.sleep(0.05)
        arduino.close()

    if scale_serial is not None:
        try:
            scale_serial.close()
        except Exception:
            pass

    raise SystemExit(exit_code)
```

### timer_controller_later.ino · lines 676–685

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateWatchdog() {
  if (augerMode == AUGER_STOPPED) {
    return;
  }

  if ((uint32_t)(millis() - lastSerialContactMs) > SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false);
    Serial.println(F("FAULT WATCHDOG"));
  }
}
```

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

## Outcome and reflection

Stopping became an explicit part of the control protocol. Enable handling, Python cleanup, heartbeat loss, and later application cancellation each addressed a different way an operation could end. The remaining distinction was between code taking a stop path and a measured physical stop; the saved files establish the former without supplying timing measurements for every termination case.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j14"></a>

# J14 Plan the electronics mounting and PCB while the control system is still changing

*Milestone 2 | Personal retrospective journal*

## Design and iteration

I began planning a PCB because the breadboard wiring was awkward to mount and service. The idea was to organize the controller connections into a more compact arrangement rather than leave the working circuit spread across the bench.

The schematic image records this direction, but the board did not become a finalized, validated part of the prototype. At the time I expected a more permanent electrical arrangement in a later milestone. The architecture was still changing, including the motor hardware, controller interface, and actuator requirements.

That made the PCB decision dependent on more than whether I could draw a board. A layout based on the early Pi and TMC2209 configuration could become obsolete when pins, enable polarity, or driver alarm connections changed. I kept development moving while that boundary remained unsettled, and eventually returned to a modular mounting approach.

## Technical detail

By the end of early feedback development, the breadboard combined power, motor-control, and Pi connections. The PCB proposal aimed to reduce loose wiring and improve mounting. The M2 notes anticipated that improvement in M3, but the record does not establish a fabricated board operating in the machine.

The challenge was that the electrical architecture was still evolving. The first Pi/TMC2209 arrangement, the later Arduino command interface, and the eventual integrated NEMA 23 drivers did not share one unchanged pin map. A board layout based on an early configuration could become obsolete when motor, enable polarity, pulse generation, or actuator control changed.

The electrical functions spanned supply connections, controller logic, STEP/DIR/EN, serial scale feedback, and later alarm and actuator paths. A fixed board would need compatible interfaces for the chosen revision. The available schematic image records the proposal, while a complete verified schematic and routed-board revision are not preserved.

I later abandoned the custom PCB because the design had not stabilized enough to finalize it. This explains the continued use of adaptable connections and a printed mount. The decision was a change in implementation strategy, rather than a missing fabricated-board success.

Keeping the circuit modifiable allowed motor control and integration to continue. The tradeoff was retaining more manual wiring and a greater dependence on version-specific pin maps. A permanent board could address those issues after the electrical architecture settled, rather than forcing the prototype to conform to an early layout.

## Process images

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

## Outcome and reflection

The PCB proposal identified a real packaging problem, but committing to a fixed layout before the interfaces stabilized would have locked in an early revision. The board remained a proposal. The later perfboard attempt and half-size breadboard mount were responses to that continuing need for adaptability.

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j15"></a>

# J15 Investigate loaded speed limits and upgrade the NEMA 17 drive

*Milestone 3 | Personal retrospective journal*

## Design and iteration

The single doser was usable but slow, so I first investigated the software settings. I adjusted requested motor speed, acceleration behavior, and feeding profiles before changing the hardware. That order mattered because slow dispensing could come from conservative finishing behavior as well as limited drive capability.

The milestone record describes eventually identifying the NEMA 17 as a limitation and replacing it with a NEMA 23. It reports greater usable dispensing speed after the change. I have not converted that qualitative improvement into a numerical torque gain or a controlled before-and-after throughput result.

The replacement also affected mounting, coupling, power, and control signals. The BOM identifies integrated closed-loop NEMA 23 hardware, so this was more than increasing one speed constant. I retained phased feeding because a stronger bulk drive did not eliminate the scale delay or the need for fine additions near the target.

## Technical detail

The single doser was usable but slow. I first investigated software because requested speed, acceleration, and finishing behavior all influence a run's duration. That investigation was reasonable, but a higher command rate is not proof that the physical shaft follows every step under powder load. I needed to compare commanded motion with actual rotation and powder output.

The early Arduino implementation starts continuous motion at 400 pulses/s and ramps at a configured 9000 steps/s squared, updating every 5000 microseconds. STEP high and low intervals are generated in software. A separate AccelStepper test uses a fixed 600-step/s command. These are distinct experiments with different timing and pin assumptions.

M3 notes state that the investigation eventually identified the NEMA 17 as a limitation and that it was replaced by a NEMA 23. The BOM lists integrated closed-loop NEMA 23 motors with pulse/direction control. That later motor architecture also changed driver handling and wiring, so the hardware upgrade was more than increasing a speed constant in Python.

The notes report improved usable speed after the motor replacement, but contain no controlled before-and-after torque or duration series. Feeder geometry, hopper fill, and finishing parameters could also affect throughput. I therefore retained the qualitative upgrade result without assigning a numerical gain to the motor alone.

The larger motor did not remove the need to slow near the target. A machine can feed rapidly in the bulk phase while still requiring short movements and settling pauses in the final phase. I retained phased dosing after the hardware change so that improving throughput would not simply recreate the sugar-overshoot problem.

The later M5 timing revision addressed software-generated pulses, which is a separate issue from loaded motor capability. Changing the motor and changing the pulse source occurred at different stages and solved different parts of the system. That distinction helped keep a requested frequency separate from verified shaft behavior.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### auger_july.ino · lines 50–52

Recovered Library auger-only source; its 10,932-byte size matches the July email attachment. Content identity was not proved by size alone.

```cpp
const uint32_t CONTINUOUS_START_RATE = 400;
const uint32_t ACCELERATION_STEPS_PER_SECOND_SQUARED = 9000;
const uint32_t ACCEL_UPDATE_INTERVAL_US = 5000;
```

### timer_controller_later.ino · lines 83–95

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint32_t FREE_TURBO_HZ  = 20000;
const uint32_t FREE_NORMAL_HZ = 2400;

// Cornstarch/non-free-flowing values.
// 20 kHz is the user's measured sweet spot: ~1 g every ~2 seconds.
const uint32_t NONFREE_TURBO_HZ  = 20000;
const uint32_t NONFREE_NORMAL_HZ = 9000;

// Fast but controlled ramp for continuous modes.
const uint32_t CONTINUOUS_START_HZ = 2000;
const uint32_t RAMP_STEP_HZ        = 500;
const uint32_t RAMP_UPDATE_MS      = 10;

```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The motor upgrade addressed the loaded drive limitation described in the milestone notes while preserving mass-based finishing control. It did not settle every speed question. The later timer investigation concerned pulse generation, a separate bottleneck from the motor and powder load, so I kept those changes as distinct engineering decisions.

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j16"></a>

# J16 Make phase thresholds depend on dose size: the July 21 to July 24 controller revision

*Milestone 3 | Personal retrospective journal*

## Design and iteration

After improving the drive, I continued revising how the controller changed phases for different target masses. A threshold suitable for a large dispense could force a tiny dose into an unnecessarily aggressive phase or keep a larger dose slow for too long.

The July 21 and July 24 code snapshots preserve a concrete revision. The earlier program used a fixed TURBO cutoff, while the later program introduced target-size-dependent cutoffs and explicit micro-dose behavior. This gave me a way to treat a 55 mg request differently from a multi-gram request even when the powder profile was the same.

I also increased observation time near the end for free-flowing powders. These changes addressed different parts of the problem: target-dependent bulk thresholds controlled when fast feeding ended, while pulse selection and settling intervals controlled the final additions. The code dates identify the saved revisions; the test sheet does not establish which revision produced each listed powder result.

## Technical detail

The dated code emails provide an actual before/after pair. The July 21 motor_scale.py used a fixed 5.000 g TURBO cutoff and a 0.500 g micro-mode limit. At exactly a 5 g target, its initial remaining value was not greater than 5.000, so it did not start in TURBO. The July 24 motor_scale_control.py introduced target-size-aware cutoffs instead of using that fixed bulk threshold for every request.

The July 24 code introduces an ultra-small limit of 0.100 g and a micro-dose limit of 0.500 g. Requests below 0.100 g start with FINAL pulses. Requests from 0.100 g to below 0.500 g use FINE followed by FINAL. A 0.055 g sugar request therefore changes from an initial FINE pulse in the July 21 logic to FINAL in the July 24 logic.

For free-flowing targets below 1.500 g, the TURBO cutoff becomes the larger of 0.250 g and 30% of the target. Targets up to 10.000 g use a 1.000 g cutoff, and larger targets use 2.000 g. For the other family, the respective choices are max(0.150 g, 20% of target), 0.600 g, and 1.000 g. These values define when the bulk phase ends; they do not mean the complete dose must stay inside those errors.

The July 24 free-flowing profile also changes continuous-to-pulse, APPROACH-to-FINE, and FINE-to-FINAL cutoffs to 0.500, 0.150, and 0.050 g remaining. Its settling intervals become 0.800 s after continuous motion, 0.300 s after APPROACH, and 2.0 s after each FINE or FINAL pulse. The non-free-flowing settings become 0.300, 0.120, and 0.040 g, with settling intervals of 0.350, 0.120, 0.220, and 0.300 s.

The longer near-target delays, particularly the 2.0 s free-flowing FINE and FINAL intervals, trade run time for additional observation of the last addition. The July 24 email establishes availability of the revision, but does not connect each listed powder result to that version. The measured trials and the code comparison remain separate pieces of evidence.

The later cleaned controller uses another arrangement, including a 0.005 g tolerance and a 120 s maximum duration. Those settings describe a subsequent source state. They do not establish an improvement over the July versions without a matched measured run, and the larger absolute tolerance is particularly relevant to evaluating small targets.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### motor_2026-07-21.py · lines 119–145

Code attachment sent July 21; a dated availability checkpoint, not a work-time record.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose the Arduino command for the current amount remaining."""
    profile = PROFILES[powder_mode]
    powder_token = profile.command_name

    # Tiny targets never enter continuous mode because there is too
    # little mass available to absorb startup and chute overshoot.
    if target < MICRO_MODE_LIMIT:
        if remaining > profile.pulse_approach_to_fine:
            return f"AUGER PULSE {powder_token} APPROACH"
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    if remaining > TURBO_REMAINING:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 121–144

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def turbo_cutoff_remaining(target: float, powder_mode: str) -> float:
    """Return the remaining mass where TURBO changes to a slower mode.

    Free-flowing examples:
    - 1.000 g target: TURBO until about 0.300 g remains.
    - 2.000-10.000 g target: TURBO until 1.000 g remains.
    - Above 10.000 g: TURBO ends at 2.000 g remaining to leave extra
      room for material momentum and powder already falling.

    Non-free-flowing powder receives smaller headroom because its flow is
    slower and normally stops more quickly.
    """
    if powder_mode == FREE_FLOWING:
        if target < SMALL_TARGET_LIMIT:
            return max(0.250, target * 0.30)
        if target <= LARGE_TARGET_LIMIT:
            return 1.000
        return 2.000

    if target < SMALL_TARGET_LIMIT:
        return max(0.150, target * 0.20)
    if target <= LARGE_TARGET_LIMIT:
        return 0.600
    return 1.000
```

### motor_2026-07-24.py · lines 157–187

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
def select_auger_command(target: float, remaining: float, powder_mode: str) -> str:
    """Choose a target-aware Arduino command for the current remaining mass."""
    profile = profile_for(target, powder_mode)
    powder_token = profile.command_name

    # 20-90 mg-style doses start with the smallest physical movement.
    if target < ULTRA_SMALL_DOSE_LIMIT:
        return f"AUGER PULSE {powder_token} FINAL"

    # Small sub-gram doses do not use continuous movement. They use FINE
    # pulses first, then switch to the one-step/tiny FINAL pulse near target.
    if target < MICRO_DOSE_LIMIT:
        if remaining > profile.pulse_fine_to_final:
            return f"AUGER PULSE {powder_token} FINE"
        return f"AUGER PULSE {powder_token} FINAL"

    turbo_cutoff = turbo_cutoff_remaining(target, powder_mode)

    if remaining > turbo_cutoff:
        return f"AUGER CONT {powder_token} TURBO"

    if remaining > profile.continuous_to_pulse:
        return f"AUGER CONT {powder_token} NORMAL"

    if remaining > profile.pulse_approach_to_fine:
        return f"AUGER PULSE {powder_token} APPROACH"

    if remaining > profile.pulse_fine_to_final:
        return f"AUGER PULSE {powder_token} FINE"

    return f"AUGER PULSE {powder_token} FINAL"
```

### motor_2026-07-24.py · lines 89–112

Code attachment sent July 24; adds dose-size-dependent phase selection.

```python
PROFILES = {
    FREE_FLOWING: PowderProfile(
        # Free-flowing powder has more material in flight after fast motion.
        continuous_to_pulse=0.500,
        pulse_approach_to_fine=0.150,
        pulse_fine_to_final=0.050,
        continuous_settle=0.800,
        approach_settle=0.300,
        fine_settle=2.0,
        final_settle=2.0,
        command_name="FREE",
    ),
    NON_FREE_FLOWING: PowderProfile(
        # Non-free-flowing powder can normally run closer to the target.
        continuous_to_pulse=0.300,
        pulse_approach_to_fine=0.120,
        pulse_fine_to_final=0.040,
        continuous_settle=0.350,
        approach_settle=0.120,
        fine_settle=0.220,
        final_settle=0.300,
        command_name="NONFREE",
    ),
}
```

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The revised controller made dose size an input to phase selection, rather than applying the same fixed boundaries to every request. The clearest example is a 0.055 g sugar target changing from an initial FINE pulse to FINAL-only behavior. That is a documented program change; its quantitative improvement still cannot be inferred without matched trial data.

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R16_make_phase_thresholds_depend_on_dose_size_the_july_21_to_july_24_controller_revision.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j17"></a>

# J17 Replace the barcode plan with selectable profiles and run the doser from the Pi

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I considered identifying powder containers with a barcode scanner and retrieving settings from a database. That would have added container records, scanner integration, and another source of configuration to maintain. Testing the eight materials suggested a simpler operating workflow based on selecting their control profiles directly.

I abandoned the scanner-and-database direction for this prototype and moved the complete single-doser workflow onto the Pi. The result described in my notes was operation without a laptop: choose a powder, enter a mass, start dispensing, and see the result on the device. Connecting a display had been an earlier hardware step; running the interface and controller together with access to the serial devices was the integration step.

The later app shows how that workflow grew as more controllers were attached. It stores powder assignments separately from requested amounts, resolves serial devices, and passes the selected device to the dispensing child process. I have kept those later implementation details distinguishable from the earlier single-doser deployment.

## Technical detail

The barcode concept would have required a scanner, a mapping from container identifiers to powder records, and a database containing useful behavior settings. M3 notes record abandoning that route after recognizing that the tested powders could be handled through two control families. The important simplification was removing a dependency from the operating workflow, not claiming that all powders behave identically.

The standalone workflow needed more than displaying a window on the Pi. The app and controller files had to be available together, Python needed the serial and UI dependencies, device paths had to resolve, and the screen needed a usable input method. The later app's subprocess path is based on its own directory, which avoids relying on whichever working directory happened to launch it.

The interface stores a powder name for each of eight slots and a requested mass for each slot separately. Only items with positive requested amounts enter the active recipe. EMPTY is a distinct slot state, and the later start function rejects a positive amount assigned to an EMPTY slot. That separation prevents an amount entry from silently inventing the contents of a hopper.

Serial discovery became important as more controllers were attached. The later app enumerates its preferred path, stable /dev/serial/by-id aliases, /dev/ttyACM devices, and /dev/ttyUSB devices. It removes duplicate real paths and excludes the scale and an already-open actuator device. It then checks responses to identify the Uno rather than assuming that every ACM device is the auger/disk controller.

The later app passes the verified Arduino path and baud rate to the controller child, avoiding a handoff where the app checks one device and the child opens another default. It also passes the known disk slot. These details belong to later multi-device integration, while the M3 milestone establishes the reported single-doser workflow on the Pi without a laptop.

The source supports the file-location and device-discovery architecture, and the milestone notes describe standalone operation. The record does not establish automatic startup after a cold boot or preserve a complete deployment transcript. I have not added those behaviors to the reported on-device achievement.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 212–219

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def get_active_recipe_items():
    items = []
    for i in range(1, 9):
        name = slots[i]["name"]
        amount = recipe[i]
        if amount > 0:
            items.append({"slot": i, "name": name, "amount": amount})
    return items
```

### app_later.py · lines 313–336

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def disk_arduino_candidates():
    # Enumerate live ports, including ACM2/ACM3 and stable USB device aliases.
    candidates = (
        [ARDUINO_PORT]
        + sorted(glob.glob("/dev/serial/by-id/*"))
        + sorted(glob.glob("/dev/ttyACM*"))
        + sorted(glob.glob("/dev/ttyUSB*"))
    )
    excluded = {os.path.realpath(SCALE_PORT)}
    if actuator_serial is not None and actuator_serial.is_open:
        actuator_port = getattr(actuator_serial, "port", None)
        if actuator_port:
            excluded.add(os.path.realpath(actuator_port))
    unique = []
    seen = set()
    for port in candidates:
        if not port or not os.path.exists(port):
            continue
        actual_port = os.path.realpath(port)
        if actual_port in excluded or actual_port in seen:
            continue
        seen.add(actual_port)
        unique.append(port)
    return unique
```

## Process images

![Raspberry Pi and display connection with breadboard wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_3.jpg)

Raspberry Pi and display connection with breadboard wiring.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The standalone Pi workflow removed the laptop and barcode database from the normal single-doser interaction. A simpler user choice was useful only if it still selected the correct profile and device, so process paths, slot contents, and serial discovery became explicit application responsibilities as the machine expanded.

## Sources

- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R17_replace_the_barcode_plan_with_selectable_profiles_and_run_the_doser_from_the_pi.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j18"></a>

# J18 Measure 5 g performance with sugar, salt, cocoa, and cinnamon

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I compared 5 g trials for sugar, salt, cocoa, and cinnamon to check both final mass and the time required to reach it. Sugar and salt fed readily and completed faster in the recorded runs. Cocoa and cinnamon needed longer, and cocoa also escaped near the lid.

The recorded sugar and salt readings both matched the 5 g target at the precision listed. Cocoa finished slightly above target and cinnamon slightly below it, with both still inside the 3% criterion. I kept containment separate from final mass: collecting the desired amount in the cup did not establish that all material stayed inside its intended path.

These were individual recorded results. The sheet does not contain repeated runs at the same target for calculating a standard deviation or demonstrating that every attempt ended at the same mass. The distinction matters especially for the apparently exact sugar and salt readings, which express the recorded scale values rather than an absence of measurement uncertainty.

## Technical detail

For the 5.000 g target, the sheet records sugar at 5.000 g in 1:54, salt at 5.000 g in 1:49, cocoa at 5.006 g in 3:32, and cinnamon at 4.985 g in 3:05. Absolute percentage error is abs(actual - target) / target times 100, giving 0.00%, 0.00%, 0.12%, and 0.30%. All four recorded values meet 3% at this target.

A displayed 5.000 g reading does not mean literally zero physical error. It means the recorded reading equals the requested value at the shown precision. The balance's resolution, calibration, drift, and final settling affect how closely that reading represents the actual delivered mass. Those quantities are not established by the test sheet, so I report the values as recorded rather than adding unsupported measurement certainty.

The behavior notes describe sugar as easy to move but difficult to finish without overshoot because of rapid flow and scale delay. Salt behaved similarly. Cocoa and cinnamon were fine and delivered smaller quantities, leading to longer runs. Cocoa also escaped upward from the lid. That observation matters because material leaving the intended powder path can make the collected mass and total material removed from the hopper differ.

Containment and dosing error described different outcomes. Cocoa escaping near the lid could increase material removed from the hopper without increasing the amount collected by the scale. The record identifies that symptom, but does not preserve a measured escaped-mass result or a confirmed lid change resolving it.

I kept throughput and final error separate. Cocoa took longer than sugar even though both listed results met the criterion. The sheet provides one 5 g result per powder, rather than repeated runs or a matched tuning comparison. That limits the conclusions to the measured trials without discarding their usefulness.

The next comparison used cohesive powders and a much smaller target. That was necessary because success at 5 g provides a comparatively large absolute error allowance and cannot establish that the same mechanism can dispense tens of milligrams to the same percentage error.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 5 | 5 | 0.00% | 1:54 | Yes |
| Table salt | 5 | 5 | 0.00% | 1:49 | Yes |
| Cocoa powder | 5 | 5.006 | 0.12% | 3:32 | Yes |
| Ground cinnamon | 5 | 4.985 | 0.30% | 3:05 | Yes |

## Process images

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

All four recorded 5 g runs met the 3% target, with different durations and powder-handling behavior. The results supported continuing with the feeder, while cocoa's escape at the lid showed that mass accuracy and containment needed separate attention. I then compared the more cohesive powders and the much smaller 0.055 g target.

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R18_measure_5_g_performance_with_sugar_salt_cocoa_and_cinnamon.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j19"></a>

# J19 Test 5 g dispensing with baking soda, cornstarch, powdered sugar, and flour

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I tested baking soda, cornstarch, powdered sugar, and flour after the changes intended to help clumpier materials. The notes describe intermittent release, sometimes in clumps, and agitation helping keep powder moving toward the screw. Those behaviors could make a run slow even when its eventual final mass was close to target.

All four recorded 5 g results were within 3%, but their durations were around five minutes. I treated that as useful performance with an obvious throughput cost, rather than describing the machine as equally fast for every ingredient.

I recalculated percentage error directly from the listed masses. Flour's recorded 4.993 g gives 0.14% absolute error against 5.000 g, while the source sheet lists 0.18%. I retained the original mass and reported the arithmetic discrepancy. I also kept these trials distinct from the later controller with a 120 s timeout, which is shorter than every run in this group.

## Technical detail

The 5.000 g results were baking soda at 4.994 g in 5:01, cornstarch at 4.991 g in 4:55, powdered sugar at 4.996 g in 4:57, and flour at 4.993 g in 4:39. Recalculated absolute errors are 0.12%, 0.18%, 0.08%, and 0.14%. The source's flour percentage is inconsistent with its recorded mass, so the calculation here uses the listed 4.993 g reading.

All four final readings met 3%, while the durations exposed the cost of slower feeding and finishing. Intermittent discharge and clumps could coexist with a close final mass. I treated the time and transport observations as part of performance rather than reducing the result to a pass label.

The earlier mechanical changes addressed different regions: larger flights changed the feeding space, while agitator reach addressed powder outside the screw's active region. These final results do not isolate the contribution of either change because there is no matched one-variable comparison in the available sheet.

The record contains no measured residual-powder mass or post-run coverage series for these trials. I therefore do not interpret successful collection as proof that the hopper fully cleared or that no powder remained around walls and arm roots. Those internal states are distinct from the final cup reading.

The later controller's 120 s maximum dispense duration is shorter than all four of these runs. I kept their original recorded times and did not attribute them to that file. Version matching matters here because a configuration that times out after two minutes could not complete an uninterrupted five-minute test under the same limit.

The outcome supports an individual 5 g dosing result for each tested cohesive powder. It does not establish general flow behavior for other materials, repeatability across refill levels, or an autonomous recipe containing all four. Those are separate tests with separate evidence.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Baking soda | 5 | 4.994 | 0.12% | 5:01 | Yes |
| Cornstarch | 5 | 4.991 | 0.18% | 4:55 | Yes |
| Powdered sugar | 5 | 4.996 | 0.08% | 4:57 | Yes |
| All purpose flour | 5 | 4.993 | 0.14% | 4:39 | Yes |

## Process images

![V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_sketch.jpg)

V5 agitator: Sketch 10 highlights the two arm profiles before Extrude 8, with the earlier screw geometry present.

![V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_agitator_extrude.jpg)

V5 agitator: Extrude 8 adds two sketch faces symmetrically at 0.318 cm depth into tube adapter. The archived tree shows feature warnings, not a fully validated assembly.

![V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v10_auger_agitator.jpg)

V10 Part Studio 1, saved July 10 2026. Later view of the auger and agitator arms.

![Physical auger and hopper component used to illustrate the cornstarch geometry discussion.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_9.jpg)

Physical auger and hopper component used to illustrate the cornstarch geometry discussion.

## Outcome and reflection

The tests supported a successful individual 5 g result for each cohesive powder, with substantially longer dispensing times than sugar or salt. They did not isolate the contribution of each mechanical change or establish repeatability across hopper fill levels. The next challenge was whether the same system could meet the percentage target at only 55 mg.

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [8 POWDER BEHAVIORS](https://docs.google.com/document/d/1Q__JbsCIq_yhuOzKZ_pea87TgvbIUF_zslr8jq5KP8A/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R19_validate_5_g_dispensing_of_the_four_cohesive_powders.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j20"></a>

# J20 Evaluate the 0.055 g limit and separate accuracy from repeatability

*Milestone 3 | Personal retrospective journal*

## Design and iteration

I reduced the requested mass to 0.055 g to examine the difficult end of the dosing range. At 55 mg, the project's 3% criterion permits only 0.00165 g of absolute error. A small clump or a milligram-scale difference therefore matters far more than it does in a 5 g trial.

The results were mixed. Sugar, cocoa, and baking soda met the criterion in their recorded runs; salt, cinnamon, cornstarch, powdered sugar, and flour did not. The worst listed result was flour at 0.047 g, or about 14.55% below target in absolute percentage terms.

My milestone notes also describe consecutive same-target dispenses, but the available eight-powder sheet is not that repeatability series. Its two sections use different target masses. I therefore kept the small-dose accuracy observations separate from any statistical claim about repeated performance, and treated pulse size, clumping, feedback delay, and stopping behavior as possible contributors rather than a proven single cause.

## Technical detail

At a 0.055 g target, the absolute allowance for 3% is 0.00165 g, or 1.65 mg. A 0.001 g difference already represents about 1.82% of the request. The recorded values and recalculated errors are shown in the table below; all error values use the same absolute percentage formula as the 5 g trials.

Only sugar, cocoa, and baking soda met 3% in these individual runs. Salt overshot while several other powders undershot, so the result does not support a single universal correction to the target. Material delivery per motion, scale response, and the stopping logic remained possible interacting factors.

Run times ranged from 54 seconds for salt to 3 minutes 21 seconds for flour. Several finer or more cohesive materials took longer despite the very small target. Long finishing pauses and small additions are consistent with that pattern, but no phase trace identifies the cause of each trial's duration.

The July 24 FINAL-only behavior below 0.100 g addresses the same class of small-target problem. The code snapshots and test sheet do not establish that these specific results were produced before or after that change. I retained the program comparison as a separate documented revision rather than assigning an improvement to unmatched data.

The milestone notes describe consecutive same-target testing, but its raw series is not present in the available test sheet. The two target groups in that sheet are different-dose comparisons, not replicates. They cannot establish a repeated-run standard deviation or a general probability of meeting the criterion.

A useful next experiment would hold the target, powder, feeder, code, baseline method, and fill conditions fixed, then retain each delivered mass and duration. That would distinguish a consistent offset from variation between runs and provide a direct comparison for revised pulse behavior. It remained a proposed next experiment rather than an added result.

## Recorded measurements

| Powder | Target (g) | Recorded mass (g) | Absolute error | Time | Within 3% |
| --- | ---: | ---: | ---: | --- | --- |
| Granulated sugar | 0.055 | 0.056 | 1.82% | 0:57 | Yes |
| Table salt | 0.055 | 0.058 | 5.45% | 0:54 | No |
| Cocoa powder | 0.055 | 0.054 | 1.82% | 1:03 | Yes |
| Ground cinnamon | 0.055 | 0.052 | 5.45% | 1:10 | No |
| Baking soda | 0.055 | 0.054 | 1.82% | 2:43 | Yes |
| Cornstarch | 0.055 | 0.053 | 3.64% | 2:49 | No |
| Powdered sugar | 0.055 | 0.049 | 10.91% | 3:07 | No |
| All purpose flour | 0.055 | 0.047 | 14.55% | 3:21 | No |

## Process images

![Single doser positioned above the balance. This photo provides setup context, not a trial result.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_7.jpg)

Single doser positioned above the balance. This photo provides setup context, not a trial result.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Outcome and reflection

The 55 mg trials established a real limitation: the eight successful 5 g results did not carry over to the smaller target. Three of eight small-dose runs met 3%. The next experimental priority was a matched series at a fixed target and configuration, so I could distinguish occasional accuracy from consistent delivery and evaluate changes such as FINAL-only control.

## Sources

- [8 POWDER TEST](https://docs.google.com/document/d/1DNaEmukRZWxtxSPTQrcbYwlaYKfkptGngnznrOfEVN0/edit)
- [M3: SINGLE DOSER FULL-COVERAGE](https://docs.google.com/document/d/170HU5NltWJAcoOTJfmL8jjjR1hS0Zjfo67U_EM6s5aQ/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j21"></a>

# J21 Build the solid eight-pocket carousel and evolve it into an open two-plate structure

*Milestone 4 | Personal retrospective journal*

## Design and iteration

With a developed single-doser mechanism, I returned to the eight-position carousel. The early design used a substantial solid disk with pockets; the later design used an open supporting arrangement. The archived feature history makes that structural change visible rather than reducing it to a before-and-after assembly photograph.

I kept the relationship among station spacing, pocket diameter, and remaining material explicit. Enlarging a hopper pocket changes both the neighboring clearance and the material near the outside edge. The disk also needed interfaces for support and drive, so it could not be designed only as eight circles around a center.

The later model retained the overall diameter while changing pocket size, plate geometry, lightening, and the repeated plate arrangement. The CAD feature reports a weight reduction, but I have kept that figure as a model result. The source material does not provide a measured printed-weight comparison or a loaded stiffness test establishing every reason for the revision.

## Technical detail

The V5 Rotary Disk studio starts with Sketch 1, a 33 cm diameter circle on the Top plane. Extrude 1 makes a new solid with a 6 cm blind depth, giving a nominal 330 mm diameter and 60 mm thickness. That is the early blank, rather than the later installed open structure.

Sketch 2 is on a face of that blank and lays out the eight pockets. Its displayed dimensions include a 12 cm center-to-pocket radial dimension and a 7 cm pocket diameter. Eight equally spaced pocket centers imply 45-degree spacing. For this geometry, adjacent centers are approximately 91.84 mm apart, calculated as twice the 120 mm radius times sin(22.5 degrees). A 70 mm pocket leaves approximately 21.84 mm between adjacent circular boundaries before any further cuts.

The outer edge also has limited material around each pocket. The disk radius is 165 mm; the station radius plus pocket radius is 120 + 35 = 155 mm. The nominal radial material outside a pocket is therefore about 10 mm at its outermost point. These calculations are geometric interpretations of this archived sketch, not finite-element results or measurements of a printed disk.

Extrude 2 removes the eight regions of Sketch 2 to a blind depth of 3 cm. The sequence shows the solid blank, pocket layout, cut preview, and saved pocketed model. In this revision the pocket feature selects faces from one sketch; the construction is not inferred from the appearance of eight completed recesses.

Rotary Disk V2 is a later open supporting arrangement. I compared its saved state with the earlier solid construction so the two revisions remained distinguishable. The change visibly altered the load-carrying material and access around the hopper stations, while measured stiffness and print-mass comparisons are not preserved in the record.

The V18 Rotary Disk V2 archive gives more specific detail for the open structure. Sketch 1 retains a displayed 33 cm outer diameter but shows an 8.5 cm pocket diameter, larger than the earlier 7 cm pockets. Extrude 1 creates an initial plate at 0.635 cm depth, or 6.35 mm. The custom Part Lightening feature uses Manual mode, selects a face of Extrude 2 and 32 rib lines from Sketch 2, and sets wall and rib thicknesses to 0.5 cm each. Its tool-diameter parameter is 0.67 cm and its blind cut depth is 2.5 cm. The feature reports a 42.4% part-weight reduction in CAD; that is not a measured weight reduction of the printed machine. Plane 1 is offset 3 cm from the selected face of Sketch 1. Mirror 1 uses Part mirror in Add mode, selects Part 2, mirrors about Plane 1, and lists Part 1 as the merge scope. Those references define the repeated plate arrangement. The new views preserve the sketch, initial plate, lightening parameters, mirror reference, mirror operation, and saved disk state separately.

Support, fastening, plate spacing, hopper seating, and the connection to the disk drive are assembly constraints in addition to the modeled pocket geometry. The CAD sequence explains how the saved parts were constructed, while the physical photograph establishes that a carousel assembly was built. Neither alone supplies a loaded deflection or indexing-error measurement.

## Process images

![V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_base_sketch.jpg)

V5 solid carousel: Sketch 1, Top-plane circle with displayed diameter 33 cm, before creating the disk blank.

![V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_blank.jpg)

V5 solid carousel: Extrude 1 creates a 6 cm deep New solid disk blank before pocket removal.

![V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_sketch.jpg)

V5 solid carousel: Sketch 2 on the disk face shows eight pockets, displayed 12 cm radial location and 7 cm diameter.

![V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_pocket_cut.jpg)

V5 solid carousel: Extrude 2 removes the eight pocket regions to 3 cm blind depth. Intermediate feature preview.

![V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v5_disk_complete.jpg)

V5 solid carousel saved model after closing the pocket feature preview. Selected feature edges remain highlighted; later suppressed features remain visible in the tree.

![Earlier solid eight-cavity rotary disk for comparison with the open structure.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_3.jpg)

Earlier solid eight-cavity rotary disk for comparison with the open structure.

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_sketch.jpg)

V18 Rotary Disk V2: Sketch 1 on Top plane. The displayed outer diameter is 33 cm and a pocket diameter is 8.5 cm; the rest of the crowded dimensions need direct CAD inspection.

![V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plate.jpg)

V18 Rotary Disk V2: Extrude 1 creates the initial plate from Sketch 1 regions. Historical construction preview.

![V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_lightening.jpg)

V18 Rotary Disk V2: Part Lightening feature inspected as a construction stage, with its parameters and cut structure shown.

![V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_plane.jpg)

V18 Rotary Disk V2: Plane 1 parameter view defining the reference used by Mirror 1. Read-only historical inspection.

![V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_mirror.jpg)

V18 Rotary Disk V2: Mirror 1 duplicates the selected plate about Plane 1, producing the upper/lower arrangement.

![V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_disk_complete.jpg)

V18 saved Rotary Disk V2 after closing its feature preview. The archive contains feature warnings; this view is geometry evidence, not a rigidity or operation test.

![Later open rotary structure with upper and lower plates and spacers.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_1.jpg)

Later open rotary structure with upper and lower plates and spacers.

## Outcome and reflection

The carousel developed from an early solid pocketed blank into an open plate-and-rib structure. Recovering the sketch, cut, lightening, and mirror stages made the geometry reproducible at the CAD level. The next integration work was to support it in the frame and coordinate its motion with the lift and shared drive.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R21_build_the_solid_eight_pocket_carousel_and_evolve_it_into_an_open_two_plate_structure.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j22"></a>

# J22 Develop the lift mechanism that clears the drive before indexing

*Milestone 4 | Personal retrospective journal*

## Design and iteration

The shared motor could not remain engaged while the carousel moved. I needed a way to lift it clear of the active hopper, rotate the disk, and return the motor to the selected auger. That added a vertical motion stage to a mechanism that previously only needed to feed powder.

I initially considered constructing the lift, then decided to purchase a linear mechanism under the cost constraints recorded in the milestone notes. The CAD includes a servo/lead-screw concept in the B4 branch, while later software controls an actuator through a separate XIAO. These represent different stages of the design, not confirmation that every modeled or listed actuator was installed.

The key mechanical requirement was clearance relative to the coupling overlap and surrounding hoppers. More commanded steps did not automatically mean more known physical travel. The later app also depended on an operator-established UP reference, making position knowledge part of the operating sequence as well as the mechanical layout.

## Technical detail

The shared-motor architecture required a motion sequence the single doser did not need. While a hopper is feeding, the motor must engage its auger. While the carousel indexes, that engagement must be clear of the rotating parts. The lift supplies the missing degree of freedom: raise the drive, index the disk, then lower the drive to the selected hopper.

The B4 branch preserves a servo/lead-screw lift concept. The notes record moving from a plan to construct the lift to purchasing a mechanism, and the later app communicates with a separate actuator controller. I kept these stages distinct because the saved sources do not identify one unchanged lift across the entire project.

The required clearance depends on coupling overlap, the nearby hopper envelope, and how the drive is guided. The motor and its wiring move with the stage, while the carousel passes beneath it. A commanded travel value only becomes a physical stroke after applying the actual microsteps, lead, and gearing; it is not an independent measurement of clearance.

The later app sets a travel constant of 69,000 steps and sends ACTUATOR UP or ACTUATOR DOWN to a separate XIAO over USB serial, with a default actuator port of /dev/ttyACM1 at 115200 baud. That is a commanded step count, not millimetres. The mechanical conversion requires the actuator's steps per revolution, microsteps, and lead or gearing.

The app also starts from an assumption that the actuator is physically at its top reference. It has a SET CURRENT AS UP operation and blocks a recipe if the position is UNKNOWN. The source states there are no actuator limit switches in that operating arrangement. This reference-setting behavior must not be described as automatically sensing the top end of travel.

The next mechanical issue was engagement at the bottom of the stroke. Even with enough clearance to index, the coupler could fail if the auger and motor reached incompatible angular orientations. That motivated the separate coupling redesign rather than increasing actuator travel or motor speed.

## Process images

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

![B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_assembly.jpg)

B4 workspace SuperStructureAssem. The alternate arrangement shows a servo and lead-screw lift structure above the auger drive. This is a CAD revision, not proof of installed final hardware.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Outcome and reflection

The lift supplied the disengagement motion required by the shared-drive architecture. Its control also introduced a distinct position state and serial device. Clearing the disk was only half the problem: after lowering, the coupling still had to engage at the angular position left by the previous dispense, which led to the next redesign.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j23"></a>

# J23 Replace the angle-sensitive drive coupling with serrated mating teeth

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I reached a mechanical roadblock when lowering the motor did not consistently connect it to the auger. The first coupling depended on a particular relative angle. After a hopper change or an auger stop, the mating features could arrive in an orientation that prevented them from seating.

This was different from a coupling slipping under load. Before torque transfer could be assessed, the connection had to form through vertical motion alone. Concentric shaft axes were necessary but did not solve the angular registration problem.

I experimented with the interface and changed it to serrated mating teeth. The milestone notes describe that revision as the practical solution to the engagement problem. I interpret the claim of alignment at any angle as the reported aim and outcome of that redesign, rather than a measured guarantee across every orientation. The archived keyed adapter below documents an earlier geometric stage; it is not substituted for the unrecovered tooth-generating features.

## Technical detail

The first coupling concept had an angular-registration problem. The motor-side feature and auger-side feature could mate only when they arrived at a specific orientation. The carousel selected the correct hopper, but lowering the drive did not guarantee that the coupling features lined up. The notes describe this as a roadblock because unsuccessful engagement prevented further integrated tests.

The failure showed that coincident shaft axes were necessary but insufficient. Angular orientation and engagement depth determined whether the features could lower into place. A model could appear concentric while opposing projections still collided during the approach, explaining why a connection that transmitted torque when assembled could fail during automatic re-engagement.

The V18 auger studio preserves a keyed motor-adapter stage. Sketch 15 is on a face of Extrude 2 with a displayed 2.5 cm circular profile. Extrude 13 adds two selected regions at 0.2 cm depth into Part 4. Sketch 13 lies on a face of that extrusion, displays a 2.3 cm circular boundary, and divides the profile into keyed regions; Onshape marks it not fully defined. Extrude 11 adds two regions at 0.75 cm depth into Part 4. These features explain an angularly registered geometry, but this archive is not matched to the exact failed printed coupler or to the later serrated tooth dimensions.

I changed the interface to repeated serrated teeth. More repeated mating features reduced dependence on one relative orientation, and the milestone notes report that change as the practical solution. No orientation sweep or engagement success-rate series is preserved, so the reported behavior remains distinct from a guarantee for every possible initial angle.

Tooth count, spacing, height, flank shape, lead-in, clearance, and axial overlap govern whether the halves seat or meet tip-to-tip. Both halves also need a secure shaft connection. The notes establish the serrated redesign, but its detailed tooth-generating sketch and dimensions are not available in this source set.

The relevant performance question was repeatable seating after independent auger stops, followed by torque transfer. A single assembled connection could not address the original failure mode. The record does not supply a measured failure rate or a controlled old-versus-new engagement series, so I have not assigned one to the redesign.

The lift, disk, and coupling now had complementary jobs: separate the drive, select a hopper, and reconnect to transmit torque. That relationship dictated the later application's order of operations. It also explained why changing only actuator travel or motor speed would not solve a misregistered engagement face.

## Process images

![V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_sketch.jpg)

V18 auger motor adapter: Sketch 15 on a face of Extrude 2, displayed 2.5 cm circular profile before the adapter base is added.

![V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_base_extrude.jpg)

V18 motor adapter: Extrude 13 adds two selected Sketch 15 regions at 0.2 cm blind depth into Part 4.

![V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_sketch.jpg)

V18 motor adapter: Sketch 13 on a face of Extrude 13 shows a 2.3 cm circular boundary and keyed engagement profile. Onshape reports this sketch is not fully defined.

![V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_key_extrude.jpg)

V18 motor adapter: Extrude 11 adds two Sketch 13 regions at 0.75 cm blind depth into Part 4, forming the keyed wall/engagement geometry.

![V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_adapter_complete.jpg)

V18 saved auger with keyed motor adapter. This is a recovered orientation-dependent design stage; its identity with the exact failed printed coupler has not been established, and it is not the later serrated revision.

![Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_11.jpg)

Earlier CAD screenshot of an auger drive assembly. Original image from the milestone document.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

![B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_b4_lift.jpg)

B4 servo actuator assem. CAD of the lift concept with lead screw, brackets, and motor assembly. Confirm its relationship to the built mechanism.

## Outcome and reflection

The coupling redesign completed the mechanical sequence behind the shared-drive idea: lift to disconnect, rotate to select a hopper, then lower and transfer torque. The important lesson was to design for forming the connection, not just for carrying torque once connected. The source record supports the serrated redesign without supplying a quantified engagement failure rate.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R23_replace_the_angle_sensitive_drive_coupling_with_serrated_mating_teeth.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j24"></a>

# J24 Construct the extrusion frame and integrate the carousel, scale, lift, and screen

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I built an aluminum-extrusion frame to bring the carousel, lift, scale, screen, and electronics into one supported machine. The milestone notes describe cutting the members with an electric saw and assembling them around the intended operating envelope. The BOM identifies 3030 T-slot extrusion and associated connectors.

Integration made the alignment chain much clearer: the lift held the motor, the motor had to meet the selected auger, and the outlet had to remain over the receiving container on the scale. Each subsystem could function on the bench while still interfering with another once mounted.

The CAD sequence below records the frame layout, rails, uprights, and plates before the full assembly. I kept the archived nominal dimensions separate from the manufactured cut list and overall measurements, which are not available in this record. The physical assembly image connects the layout to the built prototype without turning the CAD into a collision or load-validation report.

## Technical detail

The V18 Superstructure studio begins with Sketch 1 on the Top plane, containing the frame layout and repeated rail and attachment geometry. Visible dimensions include 50 and 35 in the centimetre-based studio. Extrude 1 creates the first base rail solids from multiple selected sketch faces at a 3 cm depth.

Subsequent features build the structure upward and add plates. Extrude 3 uses selected Sketch 1 regions at a 0.5 cm depth, with existing uprights and new base plate geometry visible in the preview. Further sketches, extrusions, and mirrors lead to the saved superstructure, preserving the order from layout to rails, uprights, and plates.

Extrude 2 selects four faces of Sketch 1, creates New solids, and uses a 48 cm blind depth for the uprights. That is the archived CAD member height. Attachments and supports can extend the overall machine beyond a nominal rail length, so it does not independently establish the measured assembled envelope.

I used the 3030 extrusion and connectors identified in the BOM, cutting and assembling the frame as described in M4. The saved CAD contains nominal design dimensions; the fabrication record does not preserve a complete measured cut list, kerf allowances, and bracket offsets. Those remain limits on dimensional reproduction from this account alone.

Integration brought several alignment requirements together. The disk axis had to be supported by the frame, the selected hopper outlet had to sit over the receiving container, and the lifted motor's axis had to meet the auger coupling when lowered. The scale also needed access for the cup and a support arrangement that did not mechanically interfere with the powder path.

The frame also carried the screen and electronics. Their placement affected control access, visibility of mass feedback, removal of contact parts, and wiring service. The later full assembly CAD shows one populated hopper and linked or mate warnings. It records packaging, without constituting a resolved simulation of a fully loaded eight-hopper machine.

The physical assembly photograph shows the carousel and drive packaged into the frame. The archived construction views provide the preceding CAD stages, while photographs of every physical installation step are not preserved. I kept those two forms of evidence separate rather than treating a final view as a record of frame squaring and every fitting adjustment.

## Process images

![V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_sketch.jpg)

V18 frame: Sketch 1 on Top plane, including rail/attachment layout and visible 50 and 35 dimensions in the centimetre-based model.

![V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_rails.jpg)

V18 frame: Extrude 1 creates the first base rail solids from selected Sketch 1 faces, blind depth 3 cm.

![V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_baseplates.jpg)

V18 frame: Extrude 3 creates plate geometry at 0.5 cm depth; previously created rails and uprights remain in the construction preview.

![V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_complete.jpg)

V18 saved Superstructure after closing the feature preview. This historical model is distinct from the later Main assembly.

![V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_v18_frame_uprights.jpg)

V18 frame: Extrude 2 creates four upright solids from Sketch 1 faces at 48 cm blind depth.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Outcome and reflection

The frame changed the project from several related mechanisms into one integrated physical arrangement. Alignment, cup access, lifted-drive clearance, and service access became shared constraints. The next work was to express that layout in slot references and ordered motion commands so software could select the correct feeder predictably.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R24_construct_the_extrusion_frame_and_integrate_the_carousel_scale_lift_and_screen.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j25"></a>

# J25 Convert carousel positions to step counts and establish a known reference

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I translated the carousel's eight equal positions into motor commands. Geometrically, adjacent stations are 45 degrees apart. Electrically, the corresponding pulse count depends on full steps, microsteps, and any motor-to-disk transmission ratio.

The saved step-count firmware uses 200 full steps per revolution, 32 microsteps, and direct drive. That gives 6400 pulses per disk revolution and 800 per station. An integral station count avoids rounding accumulation, but it still assumes that the installed driver settings match the program and that the disk follows the commanded motion.

I also separated a known reference from the ability to move between slots. The recovered firmware starts with position unknown and requires the operator to declare an aligned slot. Later application text describes a switch and detent arrangement. Because those are different source states, I documented the manual reference behavior actually present in the step-count code rather than combining them into an automatic homing claim.

## Technical detail

The timer-based disk firmware specifies eight slots, 200 full steps per motor revolution, 32 microsteps, and a 1:1 motor-to-disk ratio. The calibration is therefore 200 times 32 divided by eight, or 800 step pulses per station and 6400 per revolution. This is the configuration actually declared in the saved file; the driver must physically use the matching microstep mode for the calculation to hold.

The geometry gives 45 degrees per slot, while the motor configuration gives electrical pulses per slot. They agree only if the gearing, microstep mode, direction, and physical reference are correct. Changing the driver microstep switch without updating the software would change disk travel even though the slot-number arithmetic remains unchanged.

The step-count firmware starts with position unknown. SET SLOT n validates the requested range 1 through 8, refuses while auger or disk motion is active, stores the current slot, marks position known, and enables the disk driver. It does not rotate to a sensor or discover the physical location; the operator must already align the disk correctly before declaring the slot.

A requested movement is rejected when the reference is unknown. DISK STOP and DISK DISABLE stop motion and invalidate position as appropriate. That state handling prevents the program from continuing to treat an interrupted movement as a completed index. A later open/reset cycle also needs the known slot restored if the physical disk has not moved.

The later app mentions a switch, an indent, and counterclockwise indexing. The recovered disk firmware instead uses bidirectional counted steps and no matching switch-homing implementation. These are different source states. The account therefore describes the SET SLOT reference procedure for the saved firmware, while the final matched switch-based configuration remains unidentified.

The pulse count defines intended travel, while a known physical starting alignment gives slot numbers their meaning. Repeated alignment around all eight stations and recovery after interruption are separate physical checks. No measured home-position error or full station-error series is preserved with this revision.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 59–75

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
const uint8_t DISK_SLOT_COUNT = 8;
const uint32_t DISK_MOTOR_FULL_STEPS_PER_REV = 200UL;
const uint32_t DISK_DRIVER_MICROSTEPS = 32UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR = 1UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR = 1UL;

const uint32_t DISK_STEP_CALCULATION_NUMERATOR =
    DISK_MOTOR_FULL_STEPS_PER_REV * DISK_DRIVER_MICROSTEPS *
    DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR;
const uint32_t DISK_STEP_CALCULATION_DENOMINATOR =
    DISK_SLOT_COUNT * DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR;
const uint32_t DISK_STEPS_PER_SLOT =
    DISK_STEP_CALCULATION_NUMERATOR / DISK_STEP_CALCULATION_DENOMINATOR;

const uint32_t DISK_STEP_FREQUENCY_HZ = 1000UL;
const uint16_t DISK_ENABLE_SETTLE_MS = 20;
const uint16_t DISK_DIRECTION_SETTLE_US = 20;
```

### timer_controller_later.ino · lines 776–795

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
  if (parseSlotArgument("SET SLOT ", requestedSlot)) {
    if (requestedSlot == 0) {
      Serial.println(F("ERR SLOT MUST BE 1..8"));
      return;
    }

    if (augerMode != AUGER_STOPPED || diskMoveActive) {
      Serial.println(F("ERR MOTION ACTIVE"));
      return;
    }

    diskCurrentSlot = requestedSlot;
    diskPositionKnown = true;
    setDiskDriverEnabled(true);
    Serial.print(F("OK DISK SLOT SET "));
    Serial.println(diskCurrentSlot);
    return;
  }

  requestedSlot = 0;
```

## Process images

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

Slot motion became an explicit combination of geometry, pulse calibration, and a known starting reference. The recovered code also invalidates position after interrupted motion instead of trusting an unfinished index. The unresolved switch-based versus step-count revision remains a configuration limitation, while the 800-pulse station calculation is fully specified for the archived direct-drive setup.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j26"></a>

# J26 Choose the shortest carousel route and wait for completed indexing

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I added shortest-route selection so the carousel could reverse rather than make nearly a full revolution to reach a nearby hopper across the slot-number boundary. The step-count firmware compares forward and reverse distances and uses a consistent forward choice for a four-station tie.

Reducing travel did not change the required mechanical order. The drive had to stay clear throughout the index, and the next action had to wait for completion. An accepted command was therefore not enough information for the Pi to lower the actuator.

I used separate command and completion responses, including the destination slot in the completion message. The code-derived examples below explain wraparound and tie behavior. They are calculations of what this revision requests, rather than a substituted set of measured physical alignment trials.

## Technical detail

The step-count firmware calculates forward distance as (requested + 8 - current) modulo 8 and reverse distance as (current + 8 - requested) modulo 8. It chooses the smaller distance, with forward motion for a four-slot tie. This is a concrete implementation of the shortest-route note, rather than simply assuming the motor always turns in one direction.

For example, from slot 1 to slot 8, the forward distance is seven slots and the reverse distance is one, so the firmware requests one reverse slot. From slot 2 to slot 6, both distances are four, so it takes the documented forward tie. Requesting the current slot performs no index and immediately reports that slot while maintaining driver hold. These are derived examples of the code, not recorded physical tests.

startDiskMove() refuses indexing if the auger is moving, the disk is already busy, a disk alarm is latched, or the step calibration is not integral. It sets direction, enables the driver, allows a 20 ms enable-settling interval and a 20 microsecond direction-settling interval, then starts Timer2. The nominal disk frequency is 1000 pulses per second in the recovered configuration.

The number of timer compare events is twice the number of steps because the output toggles once high and once low for each full pulse. The interrupt decrements that count and disconnects the output when the move ends. Completion is then handled in the main loop, which updates the slot reference and emits DONE DISK SLOT n. That response separates an accepted command from a completed move.

The Pi-side recipe worker waits for a motion response and checks that the slot number in DONE DISK SLOT matches the requested target. It does not lower the actuator merely because an OK line says motion started. That distinction matters because the mechanical coupling must stay clear throughout indexing.

These formulas and responses document the bidirectional step-count revision. Later switch and counterclockwise descriptions belong to a different state of the app. The available record contains the routing implementation, but no complete physical trial set for wraparound, ties, same-slot requests, and interruption recovery.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 552–578

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void goToDiskSlot(uint8_t requestedSlot) {
  if (!diskPositionKnown) {
    Serial.println(F("ERR DISK POSITION UNKNOWN - SEND SET SLOT n"));
    return;
  }

  uint8_t forwardDistance =
      (requestedSlot + DISK_SLOT_COUNT - diskCurrentSlot) %
      DISK_SLOT_COUNT;
  uint8_t reverseDistance =
      (diskCurrentSlot + DISK_SLOT_COUNT - requestedSlot) %
      DISK_SLOT_COUNT;

  if (forwardDistance == 0) {
    setDiskDriverEnabled(true);
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
    return;
  }

  // For the four-slot tie, use the forward direction.
  if (forwardDistance <= reverseDistance) {
    startDiskMove(1, forwardDistance, requestedSlot);
  } else {
    startDiskMove(-1, reverseDistance, requestedSlot);
  }
}
```

### timer_controller_later.ino · lines 525–550

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateDiskCompletion() {
  if (!diskMoveFinished) {
    return;
  }

  noInterrupts();
  diskMoveFinished = false;
  interrupts();

  digitalWrite(DISK_STEP_PIN, LOW);

  if (diskPositionKnown && diskPendingTargetSlot >= 1 &&
      diskPendingTargetSlot <= DISK_SLOT_COUNT) {
    diskCurrentSlot = diskPendingTargetSlot;
  }

  diskPendingDirection = 0;
  diskPendingTargetSlot = 0;

  if (diskPositionKnown) {
    Serial.print(F("DONE DISK SLOT "));
    Serial.println(diskCurrentSlot);
  } else {
    Serial.println(F("DONE DISK SLOT UNKNOWN"));
  }
}
```

## Process images

![Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_rotary.jpg)

Current Rotary Disk V2 Part Studio showing eight openings, two plates, spacers, and central indexing features.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The routing logic reduced unnecessary commanded travel while preserving a clear completion boundary. The more significant integration detail was waiting for the correct DONE response before lowering the drive. Shorter rotation helped efficiency, but mechanical endpoint accuracy still depended on the reference, calibration, and installed disk following the motion.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j27"></a>

# J27 Sequence lift, indexing, engagement, and mass feedback for a multi-powder recipe

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I extended the application from a single target into a sequence of selected ingredients. Each active recipe item needed a slot, a powder name, and its own requested mass. The app then had to coordinate positioning before handing that item to the mass controller.

The sequence was raise, index, lower, and dispense. I made the transitions depend on state and completion responses rather than assuming each mechanism finished immediately. The controller for the actuator was separate from the Uno, so cancellation also had to reach more than one device.

A new ingredient used a starting mass reference so earlier ingredients in the receiving container were not counted as newly added powder. The later app also retained per-item result fields for CSV output. That provides a useful structure for integrated trials, but the available record does not include a complete measured recipe series tied to one confirmed final app-and-firmware configuration.

## Technical detail

The later app builds active_run_items from slots with a positive requested amount, preserving each slot's powder name and target. It initializes per-item dispensed, remaining, and status values, computes the total recipe target, clears cancellation events, and begins preparing the first item. That is the data model behind the multi-powder workflow.

The preparation worker first checks cancellation and actuator state. If the actuator is UNKNOWN, it refuses to continue. If it is not UP, it sends ACTUATOR UP and waits for a motion response with a 70 s timeout. If it is already UP, it checks status and handles the source's declared reference procedure. Only then does it request DISK GOTO for the next item.

Disk motion has a 12 s timeout in the recipe worker. The returned line must contain DONE DISK SLOT with the requested slot number. Once that is confirmed, the app records the slot, checks cancellation again, sends ACTUATOR DOWN, waits for completion, and queues a ready result. The main UI then launches mass dispensing for the item. This is an explicit raise/index/lower/feed chain with completion checks between actions.

The actuator has a separate controller, so Uno STOP ALL does not stop every moving mechanism by itself. The app's force-stop route also sends an actuator stop and marks actuator and disk state unknown. Cancellation checks between stages prevent a canceled preparation sequence from proceeding through the remaining actions on its old assumptions.

After all recipe items have dispensed, preparation is called with no next item; the worker raises the actuator and queues completion. The app exports per-item results to CSV, including target, actual mass, error, remaining amount, and status. Those fields can document a real integrated trial, but their presence in source code does not prove that such a trial occurred successfully.

The final paired actuator firmware, disk firmware, and measured recipe transcript are not identified in the available archive. In particular, switch-based app wording differs from the recovered step-count disk code. The state and command flow above describe the saved implementation without asserting that an arbitrary combination of those files is a validated final build.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 959–997

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def _prepare_recipe_item_worker(item):
    global actuator_position, disk_current_slot, disk_position_known
    try:
        _check_recipe_cancelled()
        if actuator_position == "UNKNOWN":
            raise RuntimeError("Linear actuator position is UNKNOWN. Return it to the top "
                               "and use SET CURRENT AS UP before restarting the recipe.")
        if actuator_position != "UP":
            _recipe_status("Raising the linear actuator 69,000 steps before disk movement...")
            _perform_actuator_command("ACTUATOR UP", response_type="motion", timeout=70.0)
            actuator_position = "UP"
        else:
            status = _perform_actuator_command("ACTUATOR STATUS", response_type="status", timeout=3.0)
            if "POSITION=UNKNOWN" in status:
                _perform_actuator_command("SET ACTUATOR UP", response_type="ok", timeout=2.0)
            elif "POSITION=UP" not in status:
                raise RuntimeError(f"XIAO did not confirm the actuator is UP: {status}")
        _check_recipe_cancelled()
        if item is None:
            recipe_result_queue.put(("complete", None))
            return
        target_slot = item["slot"]
        _recipe_status(f"Actuator is UP. Moving disk to slot {target_slot}: {item['name']}...")
        disk_response = _perform_disk_command(f"DISK GOTO {target_slot}", response_type="motion", timeout=12.0)
        match = re.search(r"DONE DISK SLOT\s+(\d+)", disk_response)
        if not match or int(match.group(1)) != target_slot:
            raise RuntimeError(f"Disk did not confirm slot {target_slot}: {disk_response}")
        disk_current_slot = target_slot
        disk_position_known = True
        _check_recipe_cancelled()
        _recipe_status(f"Disk is at slot {target_slot}. Lowering the actuator 69,000 steps before dispensing...")
        _perform_actuator_command("ACTUATOR DOWN", response_type="motion", timeout=70.0)
        actuator_position = "DOWN"
        _check_recipe_cancelled()
        recipe_result_queue.put(("ready", item))
    except RecipeSequenceCancelled as exc:
        recipe_result_queue.put(("cancelled", str(exc)))
    except Exception as exc:
        recipe_result_queue.put(("error", str(exc)))
```

### app_later.py · lines 1035–1047

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def start_recipe_preparation():
    if not recipe_run_active or recipe_cancel_event.is_set():
        return
    if recipe_run_index < len(active_run_items):
        item = active_run_items[recipe_run_index]
        message = (f"Preparing item {recipe_run_index + 1} of {len(active_run_items)}: "
                   f"Slot {item['slot']} — {item['name']}")
    else:
        item = None
        message = "All powders are dispensed. Returning the actuator to UP..."
    recipe_motion_screen(message)
    threading.Thread(target=_prepare_recipe_item_worker, args=(item,), daemon=True).start()
    root.after(100, process_recipe_result_queue)
```

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Outcome and reflection

The application encoded the complete preparation sequence and separated item results from recipe state. That was a substantial step beyond putting eight slots on a screen. The remaining verification boundary was the installed combination of actuator firmware, disk firmware, and app, together with a measured multi-ingredient run; the existing single-powder results cannot substitute for that evidence.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R27_sequence_lift_indexing_engagement_and_mass_feedback_for_a_multi_powder_recipe.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j28"></a>

# J28 Move STEP generation from the software loop to hardware timers

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I revisited motor speed at the pulse-generation level after the mechanical drive upgrade. The early controller toggled STEP through software timing checks. As the main loop handled other work, generating the intended waveform became a separate question from whether the loaded motor could follow it.

I changed the later firmware to use hardware timers for the step outputs. Timer1 generated the auger waveform, while Timer2 handled the disk. This moved repeated output transitions away from ordinary loop timing and still allowed software to count finite motions and report their completion.

The change also affected wiring. Hardware output-compare channels use particular pins, so retaining an old pin map with the new timing code would not produce the intended system. I documented the timer equation, configured rates, pins, and enable behavior together. Those settings describe the program; they are not a measured maximum loaded speed.

## Technical detail

The M5 notes distinguish a basic pulse-generation version from a hardware-timer version. The early July firmware calculates halfPeriodMicros as 500000 divided by the current step rate and toggles STEP in software. That arrangement depends on how often the main loop returns to the timing check. Serial handling, acceleration updates, and other work compete with pulse timing.

The later firmware assigns auger STEP to pin 9, the AVR OC1A output, and uses Timer1 in CTC mode with prescaler 1. The output toggles on each compare match. The source's conversion is frequency = F_CPU divided by twice (OCR1A + 1). On a 16 MHz configuration, 20,000 pulses per second corresponds to OCR1A = 399. This is a calculated timer setting, not a measured maximum loaded motor speed.

Continuous auger motion starts at 2000 Hz and changes by 500 Hz on nominal 10 ms ramp updates. The timer-based settings use 20,000 Hz TURBO for both families, 2400 Hz FREE NORMAL, and 9000 Hz NONFREE NORMAL. These are later parameters and differ from the early July rates; they are not one speed configuration carried unchanged through the project.

Finite auger pulses enable the Timer1 compare interrupt and count two compare matches per requested step. When the count reaches zero, the interrupt disconnects the timer output and sets a completion flag. The main loop reports completion separately. Hardware creates the waveform while software retains a finite-motion boundary and command reporting.

The disk uses Timer2 and pin 11, OC2A, with a prescaler of 64 and its own compare-match count. Timer selection therefore changes the wiring: auger STEP moves from the early pin 2 to pin 9, and disk STEP uses pin 11. The later integrated drive also uses HIGH for enable and LOW for disable. These pin and polarity changes must accompany the firmware change.

Timer configuration establishes the intended electrical timing, while the motor and powder load determine whether the shaft follows it. The record contains no preserved waveform measurement paired with a loaded-speed series. The configured 20 kHz rate is therefore reported as a command setting, without assigning it the meaning of a demonstrated reliable mechanical limit.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 175–192

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
uint16_t frequencyToOcr(uint32_t frequencyHz) {
  if (frequencyHz < 123) {
    frequencyHz = 123;
  }

  // Timer1 CTC, prescaler = 1, OC1A toggles on every compare match.
  // STEP frequency = F_CPU / (2 * (OCR1A + 1)).
  uint32_t ocr = (F_CPU / (2UL * frequencyHz)) - 1UL;

  if (ocr > 65535UL) {
    ocr = 65535UL;
  }
  if (ocr < 1UL) {
    ocr = 1UL;
  }

  return (uint16_t)ocr;
}
```

### timer_controller_later.ino · lines 303–315

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
ISR(TIMER1_COMPA_vect) {
  if (augerMode != AUGER_PULSE || pulseCompareMatchesRemaining == 0) {
    return;
  }

  pulseCompareMatchesRemaining--;

  if (pulseCompareMatchesRemaining == 0) {
    TCCR1A &= ~_BV(COM1A0);
    TIMSK1 &= ~_BV(OCIE1A);
    pulseFinishedFlag = true;
  }
}
```

### timer_controller_later.ino · lines 317–354

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateContinuousRamp() {
  if (augerMode != AUGER_CONTINUOUS) {
    return;
  }

  uint32_t now = millis();
  if ((uint32_t)(now - lastRampUpdateMs) < RAMP_UPDATE_MS) {
    return;
  }
  lastRampUpdateMs = now;

  if (currentContinuousHz == targetContinuousHz) {
    return;
  }

  if (currentContinuousHz < targetContinuousHz) {
    uint32_t next = currentContinuousHz + RAMP_STEP_HZ;
    if (next > targetContinuousHz) {
      next = targetContinuousHz;
    }
    currentContinuousHz = next;
  } else {
    if (currentContinuousHz > RAMP_STEP_HZ) {
      uint32_t next = currentContinuousHz - RAMP_STEP_HZ;
      if (next < targetContinuousHz) {
        next = targetContinuousHz;
      }
      currentContinuousHz = next;
    } else {
      currentContinuousHz = targetContinuousHz;
    }
  }

  noInterrupts();
  setTimerFrequency(currentContinuousHz);
  TCNT1 = 0;
  interrupts();
}
```

## Process images

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

Hardware timers provided a more regular timing source while preserving phase commands and bounded pulses. The optimization addressed how steps were generated, leaving motor torque and powder resistance as separate limits. Keeping the frequency calculation and pin map with the firmware made this revision more reproducible than describing it only as a faster controller.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [steppermotortest.ino](https://github.com/aaravs-s/pharmatech/blob/main/firmware/steppermotortest.ino)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R28_move_step_generation_from_the_software_loop_to_hardware_timers.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j29"></a>

# J29 Add driver-alarm handling and an interactive motor-speed test

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I added an interactive speed-test workflow so I could enter a new requested speed without editing and uploading the program for every setting. The milestone notes describe recording the commanded speed associated with a driver-reported problem. That shortened the experiment cycle and made a fault more informative than an unexplained stop.

The later production firmware also contains explicit alarm handling. A fault can stop motion, latch a state, and produce a serial message. I kept those paths distinct from the communication watchdog and from ordinary status reporting, because each responds to different information.

A generic driver alarm did not identify the underlying cause by itself. I did not turn that signal into a specific overcurrent, temperature, or stall diagnosis without supporting status data. The standalone test transcript is not available in the source record, so this account documents the workflow and implemented fault paths without assigning a numerical failure-speed limit.

## Technical detail

The M5 speed-test workflow accepted a typed speed and recorded the requested rate associated with a driver fault. This reduced recompilation between experiments. The standalone test source and captured output are not preserved in the available set, so no numerical fault-speed threshold is reconstructed from that description.

The later production firmware does contain concrete fault paths. Auger alarm is pin 7 and disk alarm is pin 6. The auger alarm check reads LOW as a fault while the mechanism is running, stops auger motion, latches faulted state, and emits FAULT DRIVER ALARM. The source uses INPUT_PULLUP and notes that an unconnected alarm line reads HIGH, so an unused input does not establish functional driver fault detection.

RESET FAULT clears the latched fault states and stops the auger. STATUS reports the run mode, current frequency, target frequency, and OCR1A. The 2000 ms serial watchdog stops active auger motion if serial contact disappears. These are distinct mechanisms: driver alarm reports the driver signal, status describes configured motion, and watchdog detects lost controller communication.

FAULT DRIVER ALARM identifies the received fault signal, rather than a detailed cause. Without the installed driver's corresponding status information, it does not separately diagnose temperature, current, or position error. The active-LOW interpretation in the saved source is a wiring assumption tied to that revision.

Requested frequency, microsteps, acceleration, supply, and powder load all affect how a speed test is interpreted. An unloaded shaft test and an auger moving cornstarch are different operating conditions. I did not infer a grams-per-second rate or universal speed ceiling from the presence of a regular timer output.

Alarm latching, fault reset, status output, and the watchdog are directly visible in the later firmware. The milestone notes separately describe the interactive test version. Together they document a more observable development process, while the missing raw speed trials limit quantitative conclusions.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### timer_controller_later.ino · lines 662–674

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void checkAlarm() {
  if (augerMode == AUGER_STOPPED || faulted) {
    return;
  }

  // With nothing connected, INPUT_PULLUP reads HIGH and will not fault.
  // Confirm your driver's ALM polarity before wiring this input.
  if (digitalRead(AUGER_ALM_PIN) == LOW) {
    stopAugerImmediate(false);
    faulted = true;
    Serial.println(F("FAULT DRIVER ALARM"));
  }
}
```

### timer_controller_later.ino · lines 635–660

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void printStatus() {
  Serial.print(F("STATUS MODE="));

  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(F("CONTINUOUS"));
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(F("PULSE"));
  } else {
    Serial.print(F("STOPPED"));
  }

  Serial.print(F(" CURRENT_HZ="));
  if (augerMode == AUGER_CONTINUOUS) {
    Serial.print(currentContinuousHz);
  } else if (augerMode == AUGER_PULSE) {
    Serial.print(activePulseHz);
  } else {
    Serial.print(0);
  }

  Serial.print(F(" TARGET_HZ="));
  Serial.print(targetContinuousHz);

  Serial.print(F(" OCR1A="));
  Serial.println(OCR1A);
}
```

### timer_controller_later.ino · lines 676–685

Recovered later Library Uno firmware; uses Timer1 for auger and Timer2 with step counts for disk.

```cpp
void updateWatchdog() {
  if (augerMode == AUGER_STOPPED) {
    return;
  }

  if ((uint32_t)(millis() - lastSerialContactMs) > SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false);
    Serial.println(F("FAULT WATCHDOG"));
  }
}
```

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

## Outcome and reflection

The controller became easier to investigate because requested speed, reported state, and alarm handling had explicit roles. Fault latching and reset behavior are present in the saved firmware. The milestone record supports the interactive test version, while the absence of its raw transcript limits the numerical conclusions I can draw from it.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j30"></a>

# J30 Drop the fixed-board plan, troubleshoot perfboard, and mount a half-size breadboard

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I returned to electronics packaging once the mechanisms were assembled. The PCB plan had not reached a stable layout, and the original full-size breadboard arrangement was bulky and difficult to mount cleanly.

I tried perfboard as a more permanent alternative, but it did not provide the working connections I needed. The notes do not identify a confirmed soldering or mapping fault, so I have kept the failed connection attempt separate from a diagnosis. I returned to a breadboard to keep development moving.

I reduced the footprint with a half-size breadboard and a custom printed mount. That retained access to change the circuit while making it more practical to attach to the machine. The decision prioritized a serviceable prototype over finalizing a permanent board while motor, alarm, and actuator interfaces were still evolving.

## Technical detail

The early PCB plan never reached a finalized design according to M5 notes. As motor control, timers, alarm lines, and the actuator changed, a fixed board layout would have needed repeated revision. The eventual prototype needed an adaptable arrangement that could support continued testing.

A perfboard was tried after the larger breadboard proved bulky and messy. The notes say the perfboard failed to connect, then record returning to a breadboard. That establishes a failed implementation attempt, but does not identify whether the failure came from a solder joint, a trace break, a wrong connection, or another electrical cause. The comparison photo shows both arrangements; it does not diagnose the failure.

The final mounting response was a half-size breadboard and a custom printed mount. The design task shifted from creating a permanent electrical circuit to constraining an interchangeable board mechanically. Relevant CAD details are the board footprint, retaining edges, access to connection rows, mounting-hole positions, standoff height, and clearance around the frame fasteners.

The mount had to hold the breadboard without covering useful connection rows or making routine changes awkward. Wire movement could pull at contacts, while excessive retention could distort the board. These were packaging constraints on the printed part, rather than evidence of a measured vibration or pullout rating.

The comparison imagery records the electrical arrangements, and the notes identify the custom mount. Its detailed retaining geometry and a diagnosed perfboard fault are not preserved. I therefore describe the reported transition and its practical purpose without adding a particular joint failure or an invented mount dimension.

The result was a prototype arrangement that kept the electronics accessible and modifiable. The decision explains why a breadboard remained in the assembled machine despite the earlier PCB proposal. A permanent board could become useful once the circuit stabilized, but it was not a prerequisite for completing this integration stage.

## Process images

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Outcome and reflection

The final packaging choice for this stage was a half-size breadboard in a printed mount. It addressed the immediate mounting problem while keeping the circuit modifiable. The abandoned PCB and failed perfboard were useful parts of that decision: a more permanent construction method only helped if the electrical implementation was ready for it.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j31"></a>

# J31 Design protective covers and consolidate wiring along the frame

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I printed wire covers, an Arduino cover, and mounting parts to organize the electronics on the assembled frame. I secured wiring along the side and concentrated routing around one extrusion rather than leaving the connections spread across the machine.

This was a mechanical integration task as much as a cosmetic one. The carousel, lifted motor, receiving cup, and fixed electronics occupied the same working space. Covers and supports had to fit around real connectors and preserve access for continued debugging.

The moving drive also meant part of the cable route changed with actuator position. That made travel allowance and the locations of restraints relevant to the design. The available notes establish the consolidation work, but do not contain a measured electrical-noise comparison or a complete endpoint inspection record. I have described the physical change without assigning those unrecorded outcomes to it.

## Technical detail

M5 notes describe printed wire covers, an Arduino cover, and a breadboard mount, with wiring secured to the side and consolidated around one extrusion. This was a final integration task because the motor, lift, disk, scale, and screen positions determined where the cable routes could run.

The cable bundle and actual mounting surface constrained the covers. Internal space, wall thickness, connector exits, and attachment positions affected whether the parts could organize wiring without pinching it or blocking board access. The milestone record identifies the printed parts but does not provide all of their feature dimensions.

The lifted drive required a moving cable section, while most electronics stayed on the frame. The moving segment needed enough travel allowance at both UP and DOWN positions. A cable photographed with the actuator in only one position cannot show whether it becomes taut or catches during the other part of the stroke.

The reported change was consolidation and physical support of wiring. The source does not establish final wire gauges, terminal specifications, a quantified strain-relief rating, or a measured noise reduction. Those outcomes cannot be deduced from the cleaner layout alone.

Cable clearance has to be considered over the full index-and-lift sequence. A route could rub at the disk, pull at a driver or breadboard, obstruct coupling, or cross the cup access area. Those are relevant inspection conditions; a recorded full-travel result for each route is not available here.

The assembly views show the wider packaging context, while the notes supply the description of covers and consolidated routing. I retained the actual images without adding a substitute construction sequence for unrecovered channel and enclosure features.

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Outcome and reflection

The covers and consolidated routing made the prototype's electronics more organized around the frame. The main lesson was to judge packaging in the context of motion and service access, rather than only the appearance of a stationary machine. Electrical noise performance and full-travel cable behavior remained separate questions from the reported routing work.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R31_design_protective_covers_and_consolidate_wiring_along_the_frame.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j32"></a>

# J32 Write an operating and cleaning procedure consistent with the actual prototype

*Milestone 5 | Personal retrospective journal*

## Design and iteration

I wrote an operating procedure to make the doser usable without requiring someone to understand the control code first. It covered powder selection, loading, taring, target entry, starting a run, checking the result, stopping, and cleaning the removable powder-contact components.

The procedure also exposed assumptions that were easy to overlook during development. A correct mass command depends on the baseline, and an automatic recipe depends on meaningful disk and actuator references. The later app's unknown-position state therefore mattered to operation, not just to debugging.

I kept the documented household-powder tests as the operating evidence for this account. A capacity target and a written cleaning procedure do not establish performance across every dose or validated sanitation. The practical achievement was recording how to use and recover the prototype, while identifying the limits of the available measurements.

## Technical detail

The written SOP covers selecting powder, entering mass, dispensing, stopping, and cleaning. The original single-doser procedure and the later recipe app have different positioning requirements. I treated the documented procedure and later source behavior as distinct stages so a general START instruction did not conceal the extra references required by the carousel.

The later recipe app requires a known disk position and a meaningful actuator UP reference. UNKNOWN blocks a run. In the saved reference-based arrangement, physical alignment and SET CURRENT operations establish what the software will treat as its position; the app does not automatically sense an actuator top limit.

Force stop marks actuator and disk state unknown. That differs from normal completion and can require the operator to establish references again before continuing. Retaining an old slot number after interrupted motion would assume the disk finished a movement that may have stopped partway through.

Cleaning connects directly to the earlier interface decisions. The contact path includes the hopper interior, agitator, screw, outlet, and receiving area. Combining components removed a joint but left those surfaces to access and inspect. The source procedure calls for disassembly of the hopper and lid and lists an M3 wrench and screwdriver or Allen key among the tools.

The original procedure includes broad performance language and a capacity limit. The measured evidence in this account is narrower: individual household-powder results at 5 g and 0.055 g, including small-dose failures. I have kept that demonstrated range distinct from the hopper capacity target and from any clinical performance claim.

Writing the procedure did not validate a cleaning chemistry or quantify residual powder. No compatibility study, contamination acceptance measurement, or independent usability trial is preserved in this record. The result of this stage was an operating document, with those additional questions left as future validation work.

## Process images

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

## Outcome and reflection

The operating document brought setup, feeding, stopping, and cleaning into one workflow. It also tied usability back to engineering decisions: detachable surfaces, baseline mass, and lost position after interruption all affect the operator. The written procedure did not create new validation results, so its claims remain bounded by the actual powder tests and implemented reference behavior.

## Sources

- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)


---

<a id="j33"></a>

# J33 Bring the prototype together and assess the documented results

*Milestone 5 | Personal retrospective journal*

## Design and iteration

By the final milestone, I had brought the feeder, agitation, rotary selection, lifted drive, scale feedback, and touchscreen interface into an integrated prototype. The remaining work described in the notes concentrated on motor control, fault visibility, mounting, and wiring organization.

Looking back across the iterations, the major decisions were connected. Sharing the motors created the lift-and-coupling problem. Sugar required resistance to passive discharge and careful stopping. Cornstarch required attention to both the screw and the powder outside its active region. Moving to recipes made state, references, and completion messages as important as the motion itself.

The clearest measured outcome is the powder test sheet: all eight recorded 5 g runs met the 3% target, while only three of eight at 0.055 g did. I kept that distinction in the closing account. The available source set does not establish a fully matched final software configuration or an ingredient-by-ingredient autonomous run, so the completed narrative closes the documented development without claiming those missing measurements.

## Technical detail

The integrated system spans feeder and disk CAD, printed interfaces, motor and actuator hardware, driver settings, wiring, the touchscreen app, the mass controller, and separate motion firmware. The archive preserves several real revisions of those elements, but not a confirmed final manifest matching every file to the installed hardware.

Two version boundaries remain especially important. The app describes switch-based indexing while the recovered disk firmware uses counted steps, and the later controller's 120 s timeout is shorter than several recorded powder trials. Those mismatches do not erase the trials; they prevent attributing all earlier results to one assumed final code set.

The intended integrated flow covers reference setup, recipe entry, lift clearance, disk movement, engagement, mass-controlled feeding, and the transition to the next ingredient. The saved app implements that ordering with state and completion checks. The available evidence does not include an uncut run and corresponding ingredient-by-ingredient data that establish the complete sequence's measured performance.

Per-item CSV fields in the app can retain target, actual mass, error, remaining amount, and status. Those fields are part of the logging design; they are not populated test results in this account. Recipe duration, manual interventions, and final mixture measurements are therefore not assigned values that the source does not provide.

The strongest numerical distinction remains the target size: eight of eight recorded 5 g trials met 3%, compared with three of eight at 0.055 g. These are single-powder results. The full assembly CAD shows one populated hopper, so its appearance does not independently establish the hopper count or success of a physical eight-ingredient demonstration.

My next priorities would be to freeze one matched hardware-and-code configuration, retain a complete integrated run, and repeat fixed-target measurements with controlled conditions. Those experiments would build directly on the documented mechanism and expose whether remaining error came from dispensing variability, feedback timing, positioning, or engagement. They are future work rather than additional completed tests.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### controller_later.py · lines 107–108

Recovered later Library controller; its settings are distinct from both July snapshots.

```python
MAX_DISPENSE_TIME_S = 120.0
HEARTBEAT_INTERVAL_S = 0.50
```

### app_later.py · lines 1108–1112

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
                     "limit switch is OPEN in its indent, then press SET CURRENT AS "
                     "SLOT 1. After that one-time setup, START "
                     "will move through the complete recipe automatically.")
        return
    if actuator_position == "UNKNOWN":
```

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Outcome and reflection

The project developed from a printable feeder into a coordinated powder-dispensing prototype with meaningful feedback and integration challenges. Its strongest measured evidence was at 5 g; its clearest remaining performance limitation was small-dose consistency. The next useful work was a version-matched integrated trial and repeated fixed-target measurements, building on the mechanisms and control structure already developed.

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
