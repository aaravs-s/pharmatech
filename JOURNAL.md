---
title: "PharmaTech Rx"
author: "Aarav Singhania"
description: "An 8-powder pill compounder: a rotary disk, one shared drive, and closed-loop dispensing to within 3% of target. Built May–September 2026."
created_at: "2026-05-25"
---

# 2026-11-09: Studying an auger filler before designing mine

**Total time spent: 2 hours**

It's simpler than I thought it would be. Powder sits in a tube on top, drops down through a funnel into a horizontal barrel, and there's a screw inside the barrel that pushes the powder out the end. One motor at the back turns the screw and that's basically the whole machine. Cap, tube, funnel block, motor, screw, barrel. Like six things.

![Exploded view of the filler. You can see every part of the powder path: tube, funnel, screw, barrel, motor at the back.](assets/reference/2026-05-25_auger-filler_exploded.png)
*Reference: render from the model I saved tonight (PharmaTech Rx Auger Filler.stp). Not my design, this is the one I'm studying.*

![Assembled. Looks clean, but the powder has to turn a corner at the funnel to get into the barrel.](assets/reference/2026-05-25_auger-filler_assembled.png)
*Reference: same model, assembled view.*

The part I keep thinking about is the corner. In this design the screw is horizontal, so powder falls down out of the tube and then has to get pushed sideways. For what I want to build the powder is going to be sitting in hoppers and dispensing straight down anyway, so why not just put the auger vertical, inside the hopper, and let it push the powder down and out the bottom. Gravity is already going that direction. Seems like it removes the corner completely instead of designing around it.

I understand the metering part now: the screw is what controls how much powder comes out, everything else is just holding powder above it and catching what falls. And I have one design decision made before I've drawn a single part of my own, which is vertical auger, in the hopper. Copy how it meters, not how it's laid out.

# June 9: Eight hoppers, but not sixteen motors

First idea was every hopper gets its own auger and its own agitator, which is good for cross contamination since nothing is shared between powders. But then I counted motors. An auger motor and an agitator motor for each of 8 hoppers is 16 motors. Sixteen motors is expensive, heavy, a wiring nightmare, all of it, just to turn screws.

So the plan changed. Instead of a motor per hopper, there will be two motors sitting above the one slot that's over the scale, and they clip into whichever hopper rotates into that position and power its auger and agitator. The hopper still has its own auger so powder never touches another powder's parts, but the motors are shared. Two motors total doing the work of sixteen.

![The concept in CAD: 8 hopper pockets in the disk, and the underside with the drive sitting at one position.](assets/cad/2026-06-09_rotary-disk-concept.png)
*Source: concept CAD from my M1 write-up, 2026-06-09. The doser Onshape document was started the same day.*

I'm also going with an auger as the dispensing mechanism, that part wasn't really a debate. An auger is accurate, every turn moves a consistent amount of powder, which is what I need if this thing is going to hit a target weight instead of just dumping.

Concept is locked: 8 hoppers carved around a rotary disk, each hopper with its own auger and agitator, one clip-in drive with two motors above the dispensing slot, auger for metering. First CAD document started.

**Total time spent: 3 hours**

# June 10: First hopper in CAD: tube, funnel, screw

The design is a vertical tube, same idea as the reference filler from May but flipped like I planned. Powder sits in the tube, there's a funnel at the bottom, and the auger runs down the middle and pushes powder out through the funnel. The motor sits on top and turns the auger. I did a section view and annotated it by hand so I could think through what connects to what: bearing at the top where the shaft comes through, the thread where the funnel screws in, the funnel itself at the bottom.

![Section view of the hopper with my annotations: bearing at the top, thread in the middle, funnel screwing in at the bottom.](assets/cad/2026-06_hopper-section-annotated.png)
*Source: CAD section view from my M1 write-up, doser document, June 2026.*

The doser document got its first saved version today (V1). The auger itself is a helix swept along a shaft, basically a long screw, and there's an assembly with the motor sitting on a small adapter disk above it. It looks simple sitting in CAD. Everything looks simple in CAD.

![The auger assembly in Onshape: motor on top, adapter disk, and the long screw under it.](assets/cad/2026-06_auger-assembly-onshape.png)
*Source: Onshape screenshot from my M1 write-up, June 2026.*

One complete hopper design exists in CAD: tube, funnel, auger, motor mount, and a section view that shows the whole powder path from top to bottom. The connection I'm least sure about is the thread between the hopper and the funnel, because the hopper has to come apart easily for cleaning, that's the whole reason for the thread in the first place.

**Total time spent: 3 hours**

# June 13: Copying a blender latch instead of a thread

I looked at how the blender lock works and copied the geometry. The funnel gets two slits cut into its sides and the hopper end gets two extruding slabs, tabs basically, that line up with the slits. The hopper drops in flush, twists, and the tabs catch behind the slits so it's locked in position. Pulling it back out is the same move in reverse.

![The latch funnel in CAD. You can see the slot cut into the rim where the hopper's tab catches.](assets/cad/2026-06_latch-funnel.png)
*Source: CAD from my M1 write-up, doser document, June 2026.*

This is stuff a printer can actually hold tolerance on. A slot is a slot, it either fits or it doesn't, and if it's loose I change one number instead of re-cutting a whole thread profile and hoping. It also keeps the thing I wanted from the thread in the first place: the hopper comes off with no tools so it can be wiped clean.

Latch design done in CAD: two slits in the funnel, two slabs on the hopper, drop in and twist to lock. It solves the binding problem by just not having a thread.

**Total time spent: 3 hours**

# June 15: The threaded hopper crumples when I screw it in

The prints themselves came out fine, that's the annoying part. The problem starts when I actually screw the hopper into the funnel. It goes in ok for the first bit and then gets progressively harder to turn, and the thread starts to crumple and fray apart instead of sliding. You can see it in the photo of the earlier prints, the top of one has the thread peeling up in a spiral where it got chewed.

![Holding the threaded auger screwed into the funnel cup. It goes together, it just fights the whole way and tears itself up doing it.](assets/photos/2026-06-15_threaded-auger-in-funnel.jpg)
*Source: Drive photo IMG_7858, taken 2026-06-15.*

![Two printed augers from the same round of testing. The one's thread is fraying and peeling at the top where it was forced.](assets/photos/2026-06_threaded-augers-frayed.png)
*Source: photo from my M1 write-up, June 2026.*

![The funnel half of the connection. The thread inside printed clean, it just doesn't survive being used.](assets/photos/2026-06_threaded-funnel.png)
*Source: photo from my M1 write-up, June 2026.*

The real issue is I can't print grooves accurate enough for a thread that needs to turn with very little tension. A printed thread isn't a machined thread. The tolerances are too sloppy, so instead of screwing smoothly it binds, and once it binds the plastic just destroys itself. More retries with slightly different sizing isn't going to change that, it's the wrong mechanism for a 3D print.

Threaded hopper connection: dead. It fails the one thing it was for, coming apart easily, because it gets harder to unscrew every time and damages itself in the process. The hopper and funnel prints themselves are fine and the auger works, it's specifically the screw-together idea that's out.

**Total time spent: 4 hours**

# June 16: The auger print won't stick, glue fixes it

The adhesion kept failing. A print that tall on that small a base wobbles as it gets higher and eventually lets go or shifts, and then the rest of the screw prints into air or into a leaning mess. I lost prints to this before I got clean ones.

The fix turned out to be boring: glue on the build plate. With the base actually stuck down properly the auger prints clean all the way up. No settings magic, no redesign, just glue.

![The printer mid-print on a blue part at my desk. Half of M1 has been me standing here watching first layers.](assets/photos/2026-06-16_printer-printing-blue-part.jpg)
*Source: Drive photo IMG_7862, taken 2026-06-16.*

Auger prints reliably now with glue for adhesion. Small thing but it was quietly eating hours, every failed auger is a couple hours of printing gone. Worth writing down because future me will definitely forget and wonder why prints are failing again: it's the glue. It's always the glue.

**Total time spent: 3 hours**

# June 16: Sugar falls out before the motor even starts

Sugar went in the top and some of it came straight out the bottom. Not while dispensing, just while pouring it in. The auger is supposed to be the thing controlling when powder moves, but sugar flows so freely that it just runs through the gaps around the screw and out the exit on its own. A dispenser that dispenses when it feels like it is not a dispenser.

The fix is at the exit. I made the auger with a narrower opening at the end, so there's resistance at the bottom of the screw. The sugar can't just free-fall through anymore, it needs the auger turning to push it past the tight part.

![The single doser in CAD, transparent tube so the auger and the tight exit at the bottom feeder are visible. That exit is the part that changed.](assets/cad/2026-06_single-doser-tube-auger.png)
*Source: CAD from my M1 write-up, June 2026.*

Leak fixed. Sugar stays in the hopper when I pour it in and only comes out when the auger turns, which is the entire point of the machine, so that's a relief. It also taught me the exit geometry matters as much as the screw itself, the screw meters the powder but the exit decides whether gravity gets a vote.

**Total time spent: 3 hours**

# June 16: Sugar is dispensing consistently

It works. With the narrower exit on the auger, sugar dispenses in consistent amounts for consistent turns of the screw. Turn it X amount, get the same weight out, turn it again, same again. That's the whole metering principle from the reference auger filler back in May, except vertical and in my hopper.

![The hopper sitting on the scale for the dispense tests. This scale is going to be in basically every test from now on.](assets/photos/2026-06_hopper-on-scale.png)
*Source: photo from my M1 write-up, June 2026.*

The other thing sugar proved: it doesn't need an agitator. It flows so naturally that the auger never starves, there's always sugar falling into the screw. So for sugar at least, the simplest version of the design is enough. I should enjoy that because I already know not every powder is going to be like this.

First powder officially working: sugar, consistent dispense per turn, no agitator needed. The single-hopper design is validated for a free-flowing powder, which means the concept is real and M1 is most of the way there.

**Total time spent: 2 hours**

# June 17: No detachable hopper at all: carving them into the disk

The more I think about cleaning, the less the detachable hopper makes sense. The reason it was detachable was cleaning. But either way, the same divot has to get wiped down. A detachable hopper doesn't remove the cleaning, it just adds a second part and a seam between them, and the seam is exactly where powder is going to hide and need the rigorous cleaning I was trying to avoid.

So: final design, the hoppers are carved into the rotary disk. One part. Nothing to unscrew, nothing to latch, no seam. Less to clean, less filament, faster prints. The disk CAD has actually been heading this way for days, the pockets are already in it.

![The rotary disk in CAD, pockets for the hoppers already carved in, center shaft below. I photographed this off my screen on the 12th while the connection argument was still going.](assets/cad/2026-06-12_rotary-disk-cad.jpg)
*Source: Drive photo IMG_7837, taken 2026-06-12.*

M1 design is settled: rotary disk with all 8 hoppers carved into it, auger in each hopper, shared clip-in drive from the concept. The thread and the latch both go in the bin of ideas that worked on paper. This is the design I'm actually building.

**Total time spent: 2 hours**

# June 17: Cornstarch jams the auger solid

Cornstarch does not flow. It clumps. Instead of falling into the screw and getting carried down, it packs together, and the auger ends up trying to push a solid plug of powder instead of loose powder, and it jams. Repeatedly.

And there's a second problem hiding behind the first one. Even where it doesn't jam, there's cornstarch sitting in the hopper that the auger never touches, out at the edges, just stagnant. The screw only moves the powder directly above it. So part of the hopper is dispensing and part of it is just storage that never empties, which for a compounding machine is a real problem, that leftover powder is the wrong amount of an ingredient sitting in a later dose.

![Powder residue all over the counter after the cornstarch runs. Sugar never made a mess like this.](assets/photos/2026-06_white-funnel-test.png)
*Source: photo from my M1 write-up, June 2026.*

Cornstarch in the sugar setup: jams, and leaves stagnant powder the auger can't reach. Two separate failures, the screw geometry is wrong for clumpy powder and there's no mechanism keeping the whole hopper moving. The one-design-for-every-powder idea is officially dead, different powders are going to need different augers at minimum.

**Total time spent: 3 hours**

# June 17: A wider auger with bigger threads for cornstarch

It worked, mostly. The wider auger with bigger threads lets the cornstarch actually grasp the surface of the screw and get carried instead of packing into a plug. The bigger thread spacing also means the powder isn't compressed as tightly in the tube, so it flows more smoothly and the jamming mostly stopped.

![Auger CAD on my screen. Different powders are getting different screws now, that decision is made.](assets/cad/2026-06-15_auger-cad-screen.jpg)
*Source: Drive photo IMG_7861, taken 2026-06-15.*

Not perfect. It's relatively consistent with an acceptable error margin, which is a polite way of saying it dispenses and the amounts are close enough for now, but cornstarch is never going to behave like sugar no matter what screw I put under it. The design needs streamlining too, right now there are just multiple augers floating around for different powders and I need a system for that.

Cornstarch dispenses without jamming on the wider, bigger-thread auger. Acceptable error margin. M1 now has two powders working, but on two different auger geometries, so "which auger for which powder" is a permanent part of this design from here on.

**Total time spent: 3 hours**

# June 17: The agitator print fails, it doesn't reach the walls

The print failed, and looking at it, the design failed first. The agitator doesn't account for the full width of the hopper. It stirs the middle and leaves a ring of powder around the edges completely untouched, which is exactly the powder that was stagnating in the cornstarch test. An agitator that misses the edges is decoration.

![The agitator in CAD, that flat arm is what I was working on. It needs to be shaped to the hopper, not floating in the middle of it.](assets/cad/2026-06-16_agitator-cad.jpg)
*Source: Drive photo IMG_7869, taken 2026-06-16.*

What the agitator actually has to do is scrape the edges of the hopper as it turns, physically push the wall powder back into the middle where the auger can grab it. That means it has to be designed to the hopper's exact inner shape, not just be a paddle that roughly fits.

Agitator attempt one: failed print, wrong size anyway. Lesson is clear though, the next one scrapes the walls or it's not worth printing. This also settles that the agitator isn't a small add-on, it's a real part that has to be designed per hopper.

**Total time spent: 2 hours**

# June 17: Tonight's fix list: two agitators and a tapered auger

First: the agitator situation. Right now there's no working agitator, the one print I tried didn't span the hopper so powder around the edges just sat there. The fix I'm going with is attaching the agitator to the bottom of the auger itself, so when the auger spins the agitator spins with it, same motor, no extra drive to sync. And not one agitator arm, two, so the powder actually gets "agitgated" all the way around instead of one blade pushing a trench through it.

Second: a whole second auger configuration. The current auger has uniform threads the whole way down. The new one will have threads that funnel down, tapered, so the spacing changes along the screw. Different powders are clearly going to want different screws, sugar already proved it doesn't behave like cornstarch, so instead of one perfect auger I'm going to have two configurations: the uniform one with agitators attached, and the tapered one, also with agitators.

I've been reading up on auger types too, there's a whole thing about self-feeding augers I had open on my laptop yesterday.

![Research page I had open on self-feeding augers. There's more auger theory than I expected there to be.](assets/photos/2026-06-16_auger-research-page.jpg)
*Source: Drive photo IMG_7870, taken 2026-06-16.*

Fix list is written down and specific: 2 agitators mounted on the auger bottom so they spin together, and a second tapered-thread auger configuration. Two auger setups total, not one. The doser CAD is also in the middle of a version sprint right now, V7 through V13 all landed in the last two days, mostly auger changes.

**Total time spent: 2 hours**

# June 20: Starting a second CAD document: newauger

The single doser is getting more real in this document. The version I'm working on today has the motor actually mounted on top of the tube with the auger under it, blue printed parts for the bottom feeder, the whole powder path in one assembly instead of pieces floating around. There's even a breadboard modeled next to the motor mount in one of the studies, which is me starting to think about where the electronics physically go instead of treating them as a later problem. They are a later problem, but a soon later problem.

![The single doser in the new document: motor on top, tube, blue bottom feeder. One complete unit instead of a pile of experiments.](assets/cad/2026-06-20_newauger-single-doser.jpg)
*Source: Drive photo IMG_7903, taken 2026-06-20, the day the newauger document was created.*

Also today: I imported another reference dispenser design (a PowderDispenser STEP file) to look at how someone else packaged a stirrer and auger in one tube. Reference only, same as the May filler. I keep collecting other people's dispensers and reading them like textbooks.

newauger document created, single doser assembly is coherent in it, and the design is shifting from "does a hopper work" to "how does this become a machine with motors and electronics attached." The doser document stays as the M1 archive.

**Total time spent: 3 hours**

# June 20: Studying a second reference dispenser

This one is a horizontal machine, which is already a useful contrast. A 12V 60 RPM motor sits at the rear, driving an auger that runs horizontally inside a copper-colored aluminum tube, with a black conical funnel/hopper on top feeding powder down into the auger inlet. There's a stirrer inside the funnel base, right over the auger inlet, doing the same job my agitator does: keeping powder moving so it doesn't bridge and starve the screw. The parts list reads like a hardware store receipt in two languages: AugerScrew, AluminiumTube, Stirrer, MotorHousingFunnel, Base, Lid, MotorCoupling, and fasteners with Spanish names, TuercaM4, PernoM4x20Parker, alongside M3 nuts and M4 washers.

![The reference dispenser: horizontal motor at the rear, black funnel on top, copper tube running forward. Reference only, not my design.](assets/reference/2026-06-20_powderdispenser-reference-overall.png)
*Source: Onshape document "PowderDispenser.stp" (imported 2026-06-20), "PowderDispenser parts" tab. Screenshot captured 2026-11-14. The blue planes are Onshape's default datum planes, not part of the design.*

The close-up of the auger is the part I keep coming back to. The screw runs the full length of the tube, enclosed, with its tip at the discharge end, and the stirrer sits directly above the inlet. It's a clean, compact arrangement, and it's a completely different answer from mine: their auger lies down, mine stands up in the hopper.

![Close-up of the auger inside the tube, highlighted. The screw runs the tube's full length, tip at the discharge end.](assets/reference/2026-06-20_powderdispenser-auger-closeup.png)
*Source: same Onshape document, AugerScrew selected. Screenshot captured 2026-11-14.*

Second reference design studied and documented: horizontal auger in a tube, funnel-fed, stirrer over the inlet, 12V 60 RPM motor. The takeaway is the stirrer-over-inlet idea, which matches what I'm already doing with the agitator, and the confirmation that a horizontal auger is a valid way to do this, just not the way I'm doing it. My machine stays vertical, in-hopper, because the rotary disk needs the hoppers standing up.

**Total time spent: 2 hours**

# June 23: Sketching the whole system on paper

I drew the full system out by hand: the superstructure (the frame, labeled SS in the sketch because I'm not writing superstructure forty times), the rotary disk with the hoppers, the motor and mount above the dispensing spot, the scale underneath, and the Pi 4 off to the side running it. Arrows for what connects to what. There's a note about which hopper is over the scale and how the drive reaches it.

It's messy. It's also the first time the entire machine, mechanics and electronics and all, exists in one picture instead of five CAD documents and a pile of intentions in my head. A couple of connections in the sketch are question marks in arrow form, mainly how the scale reading gets back into the dispensing decision, but at least now the question marks are written down somewhere.

![The whole machine on one sheet: frame, disk, scale, Pi, and all the arrows I'm about to have to make real.](assets/photos/2026-06-23_system-sketch.jpg)
*Source: Drive photo IMG_2592, taken 2026-06-23.*

One complete system sketch: frame + disk + drive + scale + Pi, connections mapped. This is the plan M2 gets built against. The electronics shopping and wiring now has an actual target instead of vibes.

**Total time spent: 2 hours**

# June 26: Electronics start: breadboard, driver, and a lot of wires

Desk is covered. Power supply brick, breadboard with the driver on it, a stepper motor, and rainbow jumper wires going everywhere in the way they do when you're still moving things around every two minutes. I have photos from today that are just escalating levels of wire mess, which is how you can tell it's a real electronics day and not a staged one.

![Breadboard, driver, stepper, and the rainbow wire situation. It works out of frame, I promise.](assets/photos/2026-06-26_breadboard-wiring.jpg)
*Source: Drive photo IMG_7925, taken 2026-06-26.*

This is the part of the build where progress looks like nothing. Nothing is mounted, nothing is clean, half the work is figuring out which wire is which for the fourth time. But the motor end of the system from my paper sketch exists on the desk now, physically, and that's the jump from M1 to M2: the machine is getting a nervous system.

Electronics bench is live: power, breadboard, driver board, stepper motor, all on the desk and being wired together. The doser is no longer just printed plastic.

**Total time spent: 5 hours**

# June 27: Wiring the scale's serial adapter

The adapter is a little serial board, and now it has the rainbow cable treatment too. Close-up photos from today are mostly me documenting which wire goes where before I unplug something and forget, which is a system, technically.

![The serial adapter board wired up. Photographed so future me knows what past me did.](assets/photos/2026-06-27_serial-adapter.jpg)
*Source: Drive photo IMG_7934, taken 2026-06-27.*

None of this is glamorous and all of it is the actual milestone. A closed loop is only closed if the controller can hear the scale, and hearing the scale turns out to be a hardware problem before it's a software one. Once the readings land on the Pi, dispensing to a target becomes a program. Until they do, it's a motor and a scale sitting near each other having separate lives.

Scale interface wired: RS232 adapter connected into the breadboard setup. Both halves of the loop, motor control and scale reading, now exist on the desk waiting to be combined in code.

**Total time spent: 4 hours**

# June 30: Powder test with an agitator actually in the hopper

Looking down into the hopper from the top, you can see the difference the agitator makes. The powder isn't sitting in a neat undisturbed layer, it's worked through, coating everything, which means it's been getting moved around the whole hopper instead of just the column above the screw getting eaten away. That's the stagnant ring problem from the cornstarch test being attacked properly.

![Looking down into the hopper: the agitator sits in the powder and the powder is worked through the whole hopper, not just the middle.](assets/photos/2026-06-30_hopper-agitator-powder.jpg)
*Source: Drive photo IMG_7944, taken 2026-06-30.*

This is the fix list from the 17th turning into hardware. Two weeks ago the agitator was a failed print that didn't reach the walls. Now there's one in a hopper with powder in it doing the job. I can't tell you the dispense numbers were suddenly perfect, this was a "does the powder move" test, not an accuracy test, but the powder moves.

Agitator works in a real hopper with real powder: the whole hopper cycles, no stagnant ring. Between this and the wider cornstarch auger, both cornstarch failures from M1 now have working answers.

**Total time spent: 3 hours**

# July 3: The motor system: NEMA 17 and a TMC2209 on a breadboard

The June wiring sessions were me getting the pieces on the desk. Now it's an actual system: Pi wired to the TMC2209 on the breadboard, driver wired to the NEMA 17, and the motor ready to be coupled to the auger. The plan for the interface is in the write-up too: the user assigns powders to slots, types in how much they want, and the machine dispenses it. Right now there's one slot and the "user" is me, but the shape of the thing is there.

![The driver setup on the breadboard. This exact pile of wires is about to become the most important pile of wires in the project.](assets/photos/2026-07_breadboard-driver.png)
*Source: photo from my M2 write-up, July 2026.*

Motor system wired: NEMA 17 + TMC2209 + breadboard + Pi. The doser has a drive. Everything from here in M2 is software and stubbornness.

**Total time spent: 4 hours**

# July 3: The scale and the screen join the Pi

The touchscreen is wired to the Raspberry Pi 4. The scale connects through one of the Pi's blue USB ports with the RS232 adapter in between, the serial setup from last week, and the Pi polls it for weight readings continuously.

And now the test setup exists as a complete thing for the first time: hopper over the scale, scale feeding the Pi, Pi running the screen and the motor. I have a photo of the whole arrangement on the desk, hopper on the balance, screen alive next to it, keyboard still plugged in because we're not animals, everything is still in development mode.

![The full M2 test setup: hopper on the scale, Pi and screen running, motor wired. First time all the pieces are in one place.](assets/photos/2026-07_full-test-setup.png)
*Source: photo from my M2 write-up, July 2026.*

Pi + touchscreen + scale over RS232 + motor driver, all connected. The hardware loop is physically closed. What doesn't exist yet is the behavior: nothing yet decides "keep dispensing, now stop." That's code.

**Total time spent: 4 hours**

# July 4: The speed problem isn't software

My first assumption was that it was a software problem, so I spent time in the code adjusting motor speeds, acceleration values, and powder profiles, trying to squeeze faster dispenses out of the same hardware. Nothing moved the needle much. The dispenses got slightly less slow and stayed slow.

That's when the real answer showed up: it's not the code. The NEMA 17 is the limit. It's a small motor doing a job that needs more torque and better control, and no amount of tuning acceleration curves is going to give a 17 the strength of a 23. So the fix is hardware: switch to a NEMA 23, which has the torque and control to dispense faster while still moving accurately.

![A sugar test run from the M3 test week: hopper on the scale, COMPLETED on the screen. The loop works — now it has to work fast.](assets/photos/2026-07-04_sugar-test-run.jpg)
*Source: Drive photo GRANULATED SUGAR, taken 2026-07-04.*

Root cause found: dispensing speed is limited by the NEMA 17 motor, not the software. Decision made to switch to a NEMA 23. The software tuning time wasn't wasted though, it produced something worth keeping, which is the next entry.

**Total time spent: 3 hours**

# July 4: Fast, then slow: the two-speed rule

The rule works and it survives the motor swap. It's one of those ideas that's obvious in retrospect: the bulk of the powder doesn't need care, the last gram does. Sugar taught me this the hard way back in M2, it pours so fast that by the time the scale reports the weight, the auger has already dumped more. Slowing down near the target gives the scale time to be right.

The hard part isn't the idea, it's the balance. Where exactly to switch from fast to slow, how slow slow is, and getting that right for eight different powders is a lot of trial and error. Each powder gets its own version of the rule because a gram away from the target means something different for sugar than for flour.

![The test setup during the M3 test week. Fast bulk, slow finish, scale watching the whole time.](assets/photos/2026-07-04_sugar-test-run.jpg)
*Source: Drive photo GRANULATED SUGAR, taken 2026-07-04.*

Two-speed dispensing kept as the approach: fast bulk, slow final ~1 g. Speed goes up without giving accuracy away, and the rule applies across powders with per-powder tuning.

**Total time spent: 3 hours**

# July 5: Two programs, not one

The app is where the user lives: assign a powder to a slot, enter the amount. When a dispense starts, the app calls the motor/scale program and hands it the target value the user typed in. The motor/scale program doesn't care about screens or buttons. It spins the motor, reads the scale, and keeps going until the weight gets to the target, within 3% error.

Why split it: because dispensing is timing-sensitive and the interface isn't, and because later there will be eight slots and recipes and a disk to position, and I don't want the thing that stops a motor at exactly 5 grams to also be the thing drawing buttons. Each program does one job and the app just tells the dispenser what to hit.

![The Pi and breadboard on the desk mid-development. The keyboard is still attached, the code is still changing every ten minutes.](assets/photos/2026-07-05_pi-breadboard-desk.jpg)
*Source: Drive photo IMG_7978, taken 2026-07-05.*

Software architecture set: app calls dispenser, dispenser owns the motor and the scale and stops within 3% of target. This split survives, by the way. I can already tell this is how the final machine's software is going to look too, because it makes each half testable on its own.

**Total time spent: 5 hours**

# July 5: Closed loop: it stops itself at 5.003 g

It did. The screen says COMPLETED and the scale says 5.003 g on a 5 g target. I keep staring at that photo because it's the first time the machine made a decision. I didn't stop the motor. The program read the scale climbing, compared it against the target the whole way down, and stopped the auger when it got there. 5.003 grams. Three milligrams over, 0.06% error, inside the 3% requirement with room to spare.

![COMPLETED on the screen, 5.003 g on the scale. Nobody touched anything. That's the whole milestone in one photo.](assets/photos/2026-07-05_dispense-complete-5g.jpg)
*Source: Drive photo IMG_7970, taken 2026-07-05.*

There's a smaller-dose completed run in my photos from today too, so it wasn't one lucky hit at one weight. The loop works as a loop: target in, powder out, scale watching, motor stopping itself.

M2 milestone achieved: doser + scale closed loop, dispensing to a target and stopping within 3%, proven at 5 g with 0.06% error. The single doser is now a machine instead of a mechanism.

**Total time spent: 5 hours**

# July 5: The 55-milligram test: 5 g is solved, 55 mg is not

Trial 1, 0.055 g target, and the numbers are honest in a way that stings:

| Powder | Dispensed | Error | Time |
|---|---|---|---|
| Granulated sugar | 0.056 g | 1.82% | 0:57 |
| Table salt | 0.058 g | 5.45% | 0:54 |
| Cocoa powder | 0.054 g | 1.82% | 1:03 |
| Ground cinnamon | 0.052 g | 5.45% | 1:10 |
| Baking soda | 0.054 g | 1.82% | 2:43 |
| Cornstarch | 0.053 g | 3.64% | 2:49 |
| Powdered sugar | 0.049 g | 10.91% | 3:07 |
| All-purpose flour | 0.047 g | 14.55% | 3:21 |

Three powders hit the 3% target. Five didn't. Flour was off by 14.55%, powdered sugar by 10.91%. And look at the times: the clumpy powders took over three minutes each to dispense 55 milligrams. That's the small-dose problem in one table, the free-flowing powders are fast and slightly overshoot, the clumpy ones are slow and undershoot, and at 55 mg there is no margin for either mistake.

![A small-dose completed run. At 55 mg, the scale is measuring milligrams and every clump counts.](assets/photos/2026-07-05_small-dose-complete.jpg)
*Source: Drive photo IMG_7968, taken 2026-07-05.*

55 mg dosing: 3 of 8 powders within 3%, 5 of 8 miss. Flour and powdered sugar are the worst, both clumpy, both slow. This is the result I have to report, not the one I wanted. The 5 g trial is the other half of the story.

**Total time spent: 5 hours**

# July 5: The 5-gram test: all eight within 0.3%

It works. Every single powder, all eight, inside 0.3% error. Sugar and salt landed on exactly 5 g. Cocoa 5.006 g, cinnamon 4.985 g, baking soda 4.994 g, cornstarch 4.991 g, powdered sugar 4.996 g, flour 4.993 g. The worst error in the whole table is cinnamon at 0.3%, which is a tenth of the 3% target.

The times tell the other half: free-flowing powders finish in under two minutes, sugar 1:54, salt 1:49. The clumpy ones take four to five minutes, baking soda 5:01, powdered sugar 4:57, cornstarch 4:55, flour 4:39. Slow, but right. And that's the trade the two-speed rule was built for: the clumpy powders need the slow finish, and the slow finish is what gets them inside 0.3%.

![5.003 g on the scale, COMPLETED on the screen. One of the 5 g runs, and the whole trial looked like this.](assets/photos/2026-07-05_dispense-complete-5g.jpg)
*Source: Drive photo IMG_7970, taken 2026-07-05.*

5 g dosing solved for all 8 powders: 0–0.3% error across the board. Combined with yesterday, the M3 headline is clear: normal doses work beautifully, tiny doses don't yet, and speed is the remaining problem, especially for the clumpy powders.

**Total time spent: 5 hours**

# July 6: Sugar settings make cornstarch crawl: splitting powder profiles

Sugar and table salt are super high flowing. When they get near the target they need to go super slow at the end, little careful turns, because the scale is still catching up while powder is still falling and it's easy to blow straight past the target.

Run those same settings with cornstarch or another fine, clumpy powder and the opposite happens. Near the target the code slows way down, and at that speed basically no cornstarch dispenses at all. It just sits there barely moving, taking forever to crawl the last fraction of a gram. Same code, same careful ending, completely wrong behavior, because the powders have opposite problems.

So the code split. The motor/scale program now has different categories depending on the consistency of the powder, different speeds and timing for free-flowing versus clumpy, and the app calls the right profile based on which powder the user picked in the interface.

![A small-dose completed run from the test sessions. The small targets are where the end-of-dispense behavior really shows itself.](assets/photos/2026-07-05_small-dose-complete.jpg)
*Source: Drive photo IMG_7968, taken 2026-07-05.*

Dispensing code is powder-aware: profiles split by consistency, app selects the profile by powder. The loop still stops within 3%, it just gets there differently depending on what's in the hopper.

**Total time spent: 4 hours**

# July 6: Two kinds of powder, and no barcode

After running all eight powders, their behaviors collapse into two families, not eight. **Free-flowing:** granulated sugar, table salt, cocoa powder, ground cinnamon. They pour, they don't clump, they don't jam. Their problem is the opposite: they flow so fast that the scale lags behind and the dose overshoots, so they need the slow finish with more time between pulses near the target. Cocoa is the odd one, fine and free-flowing but so fine it launches out of the lid, and it needs the free-flowing settings run faster for longer. Cinnamon is the easy one, fine and free-flowing, small amounts at a time, accurate almost by default.

**Non-free-flowing:** baking soda, cornstarch, powdered sugar, all-purpose flour. Fine and clumpy, they jam the auger, they fall in inconsistent clumps, and this is where the agitator earns its keep, loosening clumps and cycling powder through the hopper so the auger doesn't starve. Near the target they need the auger turning slower, smaller, with more time between turns.

And that classification is exactly why the barcode scanner dies. If every powder is just one of two families, I don't need a scanner and a database to identify it. The user picks the powder in the interface, the program picks the family, done. The scanner was more trouble than it was worth, a whole subsystem for a question with two answers.

![The purple agitator in hand. For the clumpy family, this piece is the difference between dispensing and jamming.](assets/photos/2026-07-15_purple-agitator.jpg)
*Source: Drive photo IMG_8013, taken 2026-07-15 — the agitator as it looked during the July build sessions.*

Powders classified into two families with distinct dispensing behavior, and the barcode scanner dropped. The software gets simpler instead of more complicated, which is a rare and good day.

**Total time spent: 3 hours**

# July 7: The program ends but the motor keeps turning

Troubleshooting it pointed at electrical noise. The driver was picking up noise and interpreting it as steps, so the motor would creep even though nothing was commanding it. The enable line was the problem path.

The fix: reroute the EN pin to a GPIO pin on the Pi 4. With the enable actually under the Pi's control, the driver can be properly disabled when the program ends, and the ghost spinning stops. Program ends, motor stops, full stop, which is how machines are supposed to behave.

![The breadboard up close. One of these innocent-looking jumper wires was letting noise drive my motor.](assets/photos/2026-07-05_breadboard-closeup.jpg)
*Source: Drive photo IMG_7979, taken 2026-07-05.*

Ghost motion fixed by rerouting EN to a Pi GPIO pin. The motor now only turns when it's told to, which sounds like a low bar until you've watched your dispenser turn itself on.

**Total time spent: 4 hours**

# July 8: Designing a PCB to escape the breadboard

I'm laying out a PCB that takes the driver circuit off the breadboard and puts it on one board that can be mounted on the superstructure. The schematic has the driver, the Pi connections, the enable routing that just caused me a week of ghost motors, all of it drawn properly instead of implied by jumper wire colors.

![The PCB schematic coming together. Every wire on the breadboard becomes a trace somebody has to draw, which is its own education.](assets/cad/2026-07_pcb-schematic.png)
*Source: schematic from my M2 write-up, July 2026.*

The plan is to order it so it arrives by the M3 milestone. Mounted board, organized wiring, less risk. The breadboard gets retired to prototyping duty like it was always supposed to be.

PCB layout in progress, order planned to land by M3. Whether the layout survives contact with reality is a question for a future entry, and having lived this project so far, I have my suspicions.

**Total time spent: 3 hours**

# July 15: The purple agitator takes shape

Today's photos are the agitator in pieces and together: the tall cage frame with the threaded top, the auger beside it, and then the whole thing assembled in hand, auger running down the middle of the frame. It's a satisfying object. The frame scrapes the edges where powder hides, the auger moves it down, and the whole thing spins as one unit, which is exactly what the June 17 fix list asked for: agitators attached to the auger bottom so both spin together.

![The agitator frame and auger, assembled in hand. The June fix list, printed in purple.](assets/photos/2026-07-15_agitator-assembly.jpg)
*Source: Drive photo IMG_8015, taken 2026-07-15.*

Agitator assembly exists as a printed, assembled part: frame + auger, spinning together, spanning the hopper. The clumpy-powder family finally has its tool.

**Total time spent: 4 hours**

# July 17: The print that turned into spaghetti

The photo says it all: purple filament everywhere, a tangled mess on the print bed where a part was supposed to be. The print detached or the extruder kept going with nothing to stick to, and what came out is the 3D printing equivalent of a shrug. Several hours of print time, a chunk of filament, and nothing usable.

![The failed print, in all its glory. Purple spaghetti where an agitator part should have been.](assets/photos/2026-07-17_failed-print-spaghetti.jpg)
*Source: Drive photo IMG_8018, taken 2026-07-17.*

This is the part of the project nobody writes in the milestone docs, because "a print failed" isn't a milestone, it's a Tuesday. But the agitators need to be printed eight times over, and a failure rate like this would eat the whole schedule. Adhesion, bed prep, first layer, the same lessons as the June auger print, relearned at a bigger scale.

One print failed completely, filament wasted, time lost. The agitator parts that did print are fine, the ones that didn't are a reminder that printing eight of anything means the process has to be reliable, not just the design.

**Total time spent: 3 hours**

# July 23: The NEMA 23 swap

More torque, more control, and the same two-speed rule on top of it. The 23 lets the fast phase actually be fast, the bulk of the powder moves quickly, and then the slow finish near the target does the precision work, and because the motor has the torque to move deliberately at low speed, the slow finish is more consistent too.

Here's the motor and coupler in hand with the purple auger mounted, the drive side of the machine taking shape as a real assembly instead of a breadboard experiment.

![The motor, coupler, and purple auger as one assembly. Bigger motor, same job, done faster.](assets/photos/2026-07-23_motor-coupler-auger.jpg)
*Source: Drive photo IMG_8031, taken 2026-07-23.*

NEMA 23 installed as the dispensing motor. Dispensing speed goes up while the accuracy behavior, the two-speed rule and the powder profiles, stays exactly the same. M3's hardware answer is in place.

**Total time spent: 4 hours**

# July 24: Everything on the Pi: no laptop required

The updated interface runs on the Pi's touchscreen directly. Select a powder, enter a target mass, start the dispense, view the final result, all on the machine, no computer, no code changes to run a dose. The Pi is the computer now, which is what the Pi was always for.

![The Pi in its case, wired into the system. This little board is the whole computer now.](assets/photos/2026-07-05_raspberry-pi-closeup.jpg)
*Source: Drive photo IMG_7980, taken 2026-07-05.*

Single doser is standalone: Pi + touchscreen + scale + motor, no laptop. The M3 objective, a doser that runs smoothly without human interference, is a lot closer to true when there's no human with a keyboard standing next to it.

**Total time spent: 4 hours**

# July 26: Repeatability runs, and writing the SOP

Repeatability runs: same target mass, multiple consecutive dispenses, compare the final weights, no recalibration between runs. That's the test that separates "it worked once" from "it works." Any drift between runs points at a real source of error, scale, motor, powder settling, something, and I'd rather find it now with one hopper than later with eight.

And the SOP, the standard operating procedure, because a machine that only I know how to run is a prototype with a single point of failure. Twelve steps, start to finish: assign the slot in the kiosk, select the powder, pour it in, tare the scale to 0.000 g, enter the grams (max 100 g), start, and if anything goes wrong, FORCE STOP on a jam, smoke, or burning smell. Then check the result is within ±3%, clear and home the machine, discard, and disassemble with the M3 wrench and screwdriver and wipe everything clean. The number one mistake, written right into the SOP because it happened: forgetting to tare.

![The purple hopper with its lid, one of the July iterations. The SOP's disassembly step exists because these come apart and get cleaned between powders.](assets/photos/2026-07-26_purple-hopper-lid.jpg)
*Source: Drive photo IMG_8036, taken 2026-07-26.*

Repeatability tested with consecutive same-target dispenses, and a 12-step SOP written so the machine is operable by someone who isn't me. M3 is functionally complete: one doser, eight powders, two-speed, standalone on the Pi, documented.

**Total time spent: 4 hours**

# July 26: Hoppers with lids, and the disk fitting

The hoppers now have two-piece lids with a slot for the auger post, printed in pink and purple, and you can see the agitator sitting inside the open hopper, right where it belongs. Lids matter more than they look like they should: cocoa launches out of the lid if there isn't one, powder gets everywhere, and a machine with eight open hoppers is a mess waiting to happen.

At the same time, hands-on fitting: the purple disk mount going onto the black motor, checking the fit in real life instead of in CAD, because CAD never tells you a part is 0.5 mm too tight.

![The hopper open with the agitator inside, lid beside it. And the disk mount being fitted to the motor by hand.](assets/photos/2026-07-26_hopper-open-agitator.jpg)
*Source: Drive photos IMG_8038 and IMG_8040, taken 2026-07-26.*

Hopper lids printed and fitted, agitator confirmed in place inside the hopper, disk-to-motor fit checked by hand. The single-doser parts are done and the multi-doser parts are starting to be real.

**Total time spent: 4 hours**

# July 27: M3 done: what the single doser proved

The single doser, full coverage, one hopper, eight powders:

- It dispenses 5 g of any of the eight powders within 0.3% error. That's the headline number and it holds across both powder families.
- At 55 mg it doesn't hold, 5 of 8 miss the 3% target, flour worst at 14.55%. That's the honest footnote and it stays open.
- It runs standalone on the Pi with a touchscreen, no laptop.
- It has two-speed dispensing, fast bulk then slow finish, and powder profiles split into free-flowing and non-free-flowing.
- It has a written SOP, and the repeatability runs behind it.

![The bench setup during the M3 close-out week: motor and mount on the desk, auger beside it, the whole single-doser system proven and ready to be multiplied.](assets/photos/2026-07-27_bench-setup.jpg)
*Source: Drive photo IMG_8043, taken 2026-07-27.*

M3 was supposed to be about speed and it ended up being about honesty: the speed limit was hardware, the small-dose limit is real, and the machine is genuinely good at the job it was designed for, which is normal doses, accurately, by itself.

M3 complete. The single doser is a solved problem at normal doses, a known problem at tiny ones, and the whole thing is documented well enough to build the multi-doser on top of.

**Total time spent: 2 hours**

# July 28: The PCB schematic, on screen

The screen shows the schematic in the design tool, all the blocks laid out, traces being routed. This is the board that's supposed to replace the breadboard, mount on the superstructure, and make the electronics organized and reliable instead of a wire nest that falls apart if you look at it wrong.

![The PCB schematic on screen. Every breadboard wire becomes a trace, and every trace is a decision.](assets/photos/2026-07-28_pcb-schematic-screen.jpg)
*Source: Drive photo IMG_8051, taken 2026-07-28.*

I should be honest about where this goes, because the log will get there eventually: the custom PCB doesn't survive. M5 ends up scrapping it and going back to a half breadboard with a printed mount after a perf board fails to connect. But today, the schematic is real and the plan is real, and the breadboard escape attempt is a genuine engineering step, not a waste of time. You don't know a board won't work until you design it.

PCB schematic complete on screen, layout in progress. The electronics have a designed home, even if that home eventually changes.

**Total time spent: 3 hours**

# August 1: The disk concept becomes real CAD

The single doser was designed with this in mind from the start, which is why the transition is smoother than it has any right to be. The disk I sketched in June is now a proper model: eight pockets, one for each hopper, arranged in a circle. The first iteration is a solid disk with eight holes. The final iteration is lighter, a two-tier lattice structure, because a solid disk that size is heavy, slow to print, and a waste of filament.

![First iteration: the solid disk with eight pockets. Final iteration: the two-tier lattice version. Same idea, much less material.](assets/cad/2026-08_disk-concept-cad.png)
*Source: images from my M4 write-up, August 2026.*

![The V2 disk in CAD, two tiers, eight pockets, ready for the frame.](assets/cad/2026-08_disk-v2-cad.png)
*Source: image from my M4 write-up, August 2026.*

Rotary disk in high-fidelity CAD, first iteration and final iteration. Eight hoppers, one disk, and the multi-doser has a shape.

**Total time spent: 4 hours**

# August 5: The actuator: bought, not built

The original plan was to construct the actuator ourselves. Then the cost math happened. Building a linear actuator from parts costs more than buying one, and the bought one is a known quantity, a mini linear rail with a lead screw and a small stepper, 50 mm of travel, which is exactly the lift the motor needs to clear the coupler and come back down.

So we bought it instead. The BOM still has it marked pending at $49.96, the one item on the list that never got checked off as bought in the sheet, which is either an accounting gap or the actuator arriving faster than the spreadsheet. Either way, the actuator is a purchase, not a build, and that's a decision I'm comfortable with: the interesting engineering in this machine is the dispensing, not reinventing a lead screw.

![The actuator assembly in CAD: motor on top, lead screw below, lifting the drive into and out of engagement.](assets/cad/2026-08_actuator-cad.png)
*Source: image from my M4 write-up, August 2026. (Onshape newauger also holds the DG281-50L linear actuator import.)*

Drive-engagement method decided: linear actuator lifts the motor up while the disk rotates, lowers it to engage the selected doser. Actuator purchased, not built, on cost.

**Total time spent: 2 hours**

# August 10: The coupler that only worked at one angle

The first coupler design only connected if the auger happened to be sitting at one very specific angle. If it wasn't, and it almost never was, the motor would come down and not engage, and nothing could dispense. No tests, no progress on hardware or software, the whole machine held hostage by a connection that needed luck.

This was a major roadblock because it blocked everything downstream. I couldn't test the disk, I couldn't test the actuator cycle, I couldn't test multi-powder runs, because the motor couldn't reliably grab the auger it was supposed to turn.

The fix came after a lot of approaches, and you can see the evidence of that in the CAD document, a whole subfolder of coupler attempts with names like "Krish idea 3" and "motor coupler rue" and my own test prototypes. The answer that stuck: line the motor coupler with serrated teeth that align with the auger coupler at any angle. Teeth, not a keyway. However the auger stopped, the teeth find each other and engage.

![The actuator and motor with the coupler at the bottom. The serrated teeth at the connection point are the whole story of this entry.](assets/cad/2026-08_actuator-motor-coupler.png)
*Source: image from my M4 write-up, August 2026.*

Serrated-teeth coupler: motor engages the auger at any angle. The roadblock is gone and the machine can actually run multi-doser tests.

**Total time spent: 5 hours**

# August 15: Sawing 3030 extrusion for the frame

3030 aluminum extrusion, cut with an electric saw, assembled with connectors and T-nuts. The photo from today is the frame going together on the floor, silver extrusions and black brackets, a saw nearby, the unglamorous middle of a build where everything is measurement and cutting and re-measuring because the disk has to be centered and the actuator has to line up with the slot positions or nothing works.

![The frame coming together on the floor: 3030 extrusion, brackets, and a saw. The superstructure, for real this time.](assets/photos/2026-08-15_extrusion-frame.jpg)
*Source: Drive photo IMG_8107, taken 2026-08-15.*

The frame is also the answer to the volumetric constraints, the machine has to fit in its envelope, and extrusion is the right material for that: strong, modular, and you can move a bracket when you realize the actuator is 2 cm off instead of rebuilding the whole thing.

Frame under construction: 3030 extrusion cut and assembled, disk position centered, actuator position set above the dispensing slot. The machine has a skeleton.

**Total time spent: 5 hours**

# August 21: Frame and disk, together

The rotary disk is mounted in the center of the extrusion frame, and the photos from today show it from a couple of angles, the disk hanging in the frame with the purple mounts and the motor hardware starting to appear around it. It's the first time the machine looks like the CAD, which is a strange feeling after months of the CAD being the only version that looked finished.

![The disk mounted in the frame. The machine starts looking like the machine.](assets/photos/2026-08-21_frame-disk.jpg)
*Source: Drive photo IMG_8127, taken 2026-08-21.*

The white disk itself is a big print, eight pockets, and there's a photo from a few days later of it sitting on the frame with the purple hub in the middle, which is the version that actually gets used. The disk in the CAD was light and lacy; the printed one is solid and real and heavier than the CAD suggested, which is a detail the frame doesn't mind but the disk motor will have opinions about later.

Disk mounted in the center of the frame. The multi-doser has a body now, and the remaining work is everything that attaches to that body.

**Total time spent: 4 hours**

# August 26: First full assembly

The disk print is running, you can see it in the slicer on screen, eight pockets, sparse infill, the big white disk that the whole machine rotates around. And the assembly is coming together in the photos: the full CAD with the orange actuator column, the disk in the middle, the screen at the base, and then the real thing on the desk at night, wires everywhere, disk in place, motors mounted, the machine existing in three dimensions for the first time.

![The full assembly in CAD: frame, disk, orange actuator column, screen at the base.](assets/cad/2026-08_full-assembly-cad.png)
*Source: image from my M4 write-up, August 2026.*

![The real thing, assembled on the desk. Wires everywhere, but it's a machine now.](assets/photos/2026-08_final-assembly.png)
*Source: photo from my M4 write-up, August 2026.*

First full assembly exists, CAD and real, side by side. The machine is a machine. What isn't done is the wiring, the code that moves the disk, and the part where it dispenses eight powders in a row without me standing there.

**Total time spent: 6 hours**

# August 28: The all-night wiring session

The photos from this session are timestamped in the middle of the night, 3:34 in the morning for one of them, and they look like it. The breadboard is mounted on a blue box on the machine with wires going in every direction. There's a perf board in hand, a driver board in hand, disk segments on the carpet, and the machine is slowly turning from a mechanical assembly into an electrical one.

![Wiring on the machine, late at night. The breadboard is mounted, the wires are everywhere, and it's 3:34 AM in the photo metadata.](assets/photos/2026-08-28_wiring-night.jpg)
*Source: Drive photo IMG_8176, taken 2026-08-28.*

This is the session where the M4 and M5 documents both get written, dated August 29, because the work crosses midnight and the write-ups land the next day. The machine that comes out of this night is the machine that the rest of the project is about: eight hoppers, one shared drive, an actuator, a disk, and electronics that are, for now, a breadboard and a prayer.

Machine wired end to end, overnight. Motors, actuator, Pi, Arduino, scale, screen, all connected on the frame. M4's mechanical work and M5's electronics work meet in this session.

**Total time spent: 8 hours**

# August 29: My step code is the bottleneck, not the motor

The first version of the stepper code used basic Arduino commands to send step pulses at increasing speed. Simple, readable, and too slow. The code itself became the bottleneck instead of the motor. The motor could go faster, the pulses just couldn't get to it fast enough, because the Arduino was spending its time running the pulse commands instead of pulsing.

This is the same lesson as the NEMA 17, one level up. Last time the hardware was the limit and I blamed the software. This time the software really is the limit, and the fix has to be in how the pulses are generated, not in how fast I ask for them.

![The perf board and breadboard from the wiring session. The electronics are about to get reorganized, but first the code has to stop being the slow part.](assets/photos/2026-08-28_perfboard-breadboard-hand.jpg)
*Source: Drive photo IMG_8167, taken 2026-08-28.*

Diagnosis: version 1 stepper code is too slow because basic Arduino pulse commands can't generate steps fast enough. The motor isn't the limit here, the code is.

**Total time spent: 3 hours**

# August 29: Hardware-timer pulses: version 2

The Arduino has timers in the chip that can generate pulses directly, on their own schedule, without the main program having to babysit every step. Version 2 uses one of those timers to generate the step pulses, which removes the slowdown completely. The main loop is free to do other things, the pulses are rock steady, and the motor finally gets tested against its real limits instead of the code's limits.

This is the version that the final code still uses, by the way. The September Arduino sketch runs the auger on Timer1 and the disk detent debouncing on Timer2, and that architecture starts here, in this rewrite.

![The breadboard and perf board side by side during the wiring session. The code is getting faster while the electronics are still figuring out where they live.](assets/photos/2026-08-29_perfboard-breadboard.jpg)
*Source: Drive photo IMG_3903, taken 2026-08-29.*

Version 2 stepper code: hardware-timer pulse generation, slowdown removed, motor tested against its real limits. The auger is fast now, and the code is no longer the bottleneck.

**Total time spent: 4 hours**

# August 29: Version 3: fault checking and type-in speeds

Fault checking first. If the motor driver detects a problem, a stall or too much current, the code catches it and records exactly what speed it happened at. That's the difference between "the motor stopped" and "the motor stalled at this speed under this load," and the second one is actually useful. It turns failures into data.

Then the type-in speed testing. Before this, testing a new speed meant rewriting the code and re-uploading it to the Arduino, every single time, which is slow and error-prone and exactly the kind of loop that makes you stop testing. Now I can type in a speed and test it immediately. The tuning loop goes from minutes per test to seconds, and the motor gets properly characterized instead of approximately guessed at.

![A driver board in hand during the wiring session. This is the part that reports a stall or an overcurrent, and version 3 is the code that listens.](assets/photos/2026-08-29_driver-board.jpg)
*Source: Drive photo IMG_8183, taken 2026-08-29.*

Version 3 stepper code: fault checking that records the exact speed of a stall or overcurrent, plus type-in speed testing without re-uploading. The motor code is done, in the sense that it's now a tool instead of a problem.

**Total time spent: 4 hours**

# August 30: The PCB is scrapped, the perf board fails

The custom PCB is scrapped. We explored developing one to replace the breadboard, to organize the Pi connections and motor controls and make everything easier to mount and maintain, but we kept iterating and were never able to finalize a design. At some point you have to call it: the board isn't happening, and the machine needs electronics now, not a perfect board eventually.

So, perf board. A breadboard is too large to mount and too messy, so a perf board seemed like the middle ground, smaller, mountable, soldered instead of jumpered. And the perf board failed to connect. The connections didn't work, and after the effort of building it, the machine was back to square one on electronics packaging.

![The small green perf board, wired up in hand. It looks finished. It doesn't connect.](assets/photos/2026-08-29_perfboard-in-hand.jpg)
*Source: Drive photo IMG_3922, taken 2026-08-29.*

The answer, in the end, is to go back to a breadboard, but a half breadboard, one I can keep adapting with a modular design, mounted in a 3D-printed custom mount. It's not elegant. It's honest. The breadboard works, the perf board doesn't, and the PCB doesn't exist, so the breadboard wins by being the thing that actually functions.

Custom PCB scrapped, design never finalized. Perf board tried and failed to connect. Electronics go back to a half breadboard in a printed mount, chosen because it works and can be adapted, not because it's pretty.

**Total time spent: 4 hours**

# August 31: Wire covers and one clean extrusion

Printed parts to the rescue, which is the theme of this whole project: when something needs to exist, print it. Custom wire covers, an Arduino cover, a breadboard mount, all printed to fit the machine. The wires get secured to the side and consolidated to one extrusion, so instead of cables going everywhere, there's one clean run down one piece of frame.

![Disk segments on the carpet from the build sessions. The machine is getting its covers and its clean runs, one printed part at a time.](assets/photos/2026-08-29_disk-segments.jpg)
*Source: Drive photo IMG_8188, taken 2026-08-29.*

It's not just cosmetic. Exposed wires get snagged, pulled, and unplugged, and a machine that has to dispense eight powders in a row can't have a wire that comes loose because someone brushed past it. The covers and the consolidation are reliability work dressed up as tidiness.

Electronics organized: printed wire covers, Arduino cover, breadboard mount, wires secured and consolidated to one extrusion. The machine looks like a machine and, more importantly, stops being one accidental tug away from a failure.

**Total time spent: 4 hours**

# September 5: September: the assembly in CAD, again

The screen shows the assembly: the orange actuator column, the funnel and hopper, the frame, the whole machine modeled with the parts as they actually are now. This is the version of the CAD that matches the machine, not the version from August that matched the plan.

![The assembly in CAD, September version: actuator column, funnel, frame, everything as built.](assets/photos/2026-09-05_cad-assembly-screen.jpg)
*Source: Drive photo IMG_8206, taken 2026-09-05.*

Assembly CAD updated to match the built machine. The model and the machine agree again, which matters because the final code is about to be written against this exact geometry.

**Total time spent: 3 hours**

# September 7: Printing the last hopper parts

The photo from today is the print bed with the finished parts: stacked white cylinders, the hopper bodies, and the lattice pieces beside them. Clean prints, no spaghetti this time, the process is reliable now in a way it wasn't in July. The July 17 failure feels like a different project.

![The last hopper parts, printed clean. Eight of everything, and the print queue is finally done.](assets/photos/2026-09-07_printed-hopper-parts.jpg)
*Source: Drive photo IMG_8212, taken 2026-09-07.*

Final hopper parts printed. The machine has all eight hoppers, all eight agitators, all eight augers, and nothing left in the print queue.

**Total time spent: 3 hours**

# September 12: The disk doesn't trust steps anymore

Steps lie. A stepper motor can miss steps under load, and if the disk's position is just a count of steps sent, one missed step means every slot after it is wrong, and the machine doesn't know. The fix is to stop trusting steps and start trusting a physical switch. There's a mechanical detent switch on the disk, wired to pin D2, and the disk moves clockwise only, counting detents as they click past, until it reaches the slot it wants. The position is real, measured, not assumed.

The final Arduino sketch says it plainly in its own header:

```
Auger: STEP D9, DIR D8, ENABLE D10.
Disk:  STEP D11, DIR D12, ENABLE D4.
Mechanical switch: COM -> GND, NO -> D2.
ALL disk travel is clockwise only.
DISK PREV is intentionally rejected.
```

Clockwise only. No reverse, no shortest path, no step counting. The disk goes around until the switch says it's home, and if the indexing fails, the stored position is invalidated instead of guessed at. It's slower than the shortest-path idea and it's correct, which is the trade that matters when the machine is dispensing actual doses.

![The assembly in CAD, September version. The disk in this model is positioned by detents now, not by step counts.](assets/photos/2026-09-05_cad-assembly-screen.jpg)
*Source: Drive photo IMG_8206, taken 2026-09-05.*

Final disk positioning: clockwise-only detent indexing via the D2 switch, 800 steps expected per slot, 400–1200 allowed, position invalidated on indexing error. The M4 step-counting plan is superseded, and this is the version that actually runs.

**Total time spent: 5 hours**

# September 12: The final code: three pieces

Three pieces, each with one job:

**app.py, on the Pi.** A CustomTkinter dark interface, 800×480 fullscreen, titled "Compounding Doser." It owns the recipes and the positioning. It passes the Arduino port and the current disk slot to the programs it calls, and it logs everything to CSV. This is the screen the user touches.

**motor_scale_controller.py, on the Pi.** Dispenses one powder to a target using scale feedback. You call it like `python3 motor_scale_controller.py 5.0 "Cornstarch"` and it handles that one powder, that one target, and nothing else. It doesn't move the actuator, it doesn't touch the disk. One powder, one target, scale watching.

**The Arduino sketch, on the Uno/Nano.** Auger on Timer1, disk detent indexing on Timer2 with the D2 switch, and the linear actuator on a TMC2209. The rules are strict and they're written in the header: the actuator must be raised before any disk command, no simultaneous motions, the actuator's position is tracked in software only, there are no limit switches, and the disk is clockwise only. Bench values: 1,000 steps per second, 4 ms debounce.

![The printed hopper parts from the build week. The code doesn't care how pretty they are, but the demo audience will.](assets/photos/2026-09-07_printed-hopper-parts.jpg)
*Source: Drive photo IMG_8212, taken 2026-09-07.*

Final software complete and exchanged: Pi app + dispenser program + Arduino sketch, with the pin map, the detent protocol, and the safety rules all written down in the code itself. The machine's brain is done.

**Total time spent: 5 hours**

# September 13: Demo day: it works end to end

The finished machine, in the photos from today: two-level carousel with eight clear PETG hoppers on top, lids and funnels in place, two big black motors on purple mounts over the disk, the 3030 extrusion frame holding it all, the touchscreen at the base, and a black electronics box with PHARMATECH printed on it. There's powder residue on the tablecloth, which is the best review a dispensing machine can get: it dispensed, here, in front of people.

![The finished machine at the demo table: eight clear hoppers, two motors on purple mounts, touchscreen at the base, PHARMATECH box. Powder on the tablecloth. It works.](assets/photos/2026-09-13_finished-machine-demo.jpg)
*Source: Drive photo IMG_5888, taken 2026-09-13, 4:40 PM.*

![The wider view: the machine on its table under the expo screen, the whole project in one frame.](assets/photos/2026-09-13_demo-day-wide.jpg)
*Source: Drive photo IMG_5880, taken 2026-09-13.*

May 25 I was studying someone else's auger filler. June I was fighting glue and threaded prints and cornstarch. July the loop closed and the powders got tested. August the machine got a frame and a disk and a night of wiring. September the code got final and the disk learned to trust a switch instead of a step count. And today it dispensed, end to end, in front of an audience.

Machine works end to end, demonstrated publicly: eight powders, one shared drive, closed-loop dispensing to target, standalone on the Pi. The 5 g accuracy holds. The 55 mg accuracy doesn't yet, and that's the honest footnote the log keeps, because the next version starts from the truth, not from a victory lap.

**Total time spent: 4 hours**
