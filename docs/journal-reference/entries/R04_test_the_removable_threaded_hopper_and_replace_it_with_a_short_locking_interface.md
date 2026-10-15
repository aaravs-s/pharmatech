# R04 Test the removable threaded hopper and replace it with a short locking interface

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 1 · Previous topics J06, J07

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Develop a removable hopper interface that seats securely without damaging the printed connection.

## Design process

I first tried a threaded connection between the removable hopper and its funnel. The idea was to let the hopper screw into place securely while remaining easy to remove for cleaning. This also appeared to be a convenient way to constrain the two parts without adding separate latches or many fasteners.

The printed prototypes exposed a problem that was not obvious from the CAD alone. As I screwed the parts together, the connection progressively became harder to turn. The material started to fray or deform rather than seating smoothly. The notes describe the fit problem, but they do not isolate whether the main cause was clearance, surface roughness, thread geometry, print distortion, or a combination of those factors.

I decided the threaded interface needed reconsideration. A connection intended to simplify cleaning was not useful if assembling it damaged the part or required excessive force. This failure pushed me toward a locking approach with less sliding contact along a long printed thread.

After the threaded connection failed, I looked at the way a blender container locks into its base. I adapted that general idea into a connection using slots and projecting tabs. The goal was to let the hopper seat into place with a short locking movement instead of forcing a long printed thread through repeated contact.

This was a change in how the interface carried load and constrained motion. The hopper still needed to sit flush and resist unintended movement, but assembly could rely on a few engagement features. That made the location and size of the tabs important, as well as the clearance needed to insert them without damaging the printed surfaces.

The notes establish that I created this alternative, but do not provide its exact dimensions or a measured durability result. I would use the CAD view to explain the locking principle and add the real observations from inserting and removing the prototype. The next question was whether a detachable interface was needed at all once I considered the cleaning burden of the whole assembly.

## Construction and implementation detail

The connection was supposed to satisfy two requirements at once: constrain the hopper during operation and allow removal for cleaning. A thread looked attractive because it combined retention and alignment in one printed interface. The physical trial showed why nominal mating geometry was not enough. The parts printed, but resistance increased as they were screwed together, and the surfaces crumpled or frayed rather than seating cleanly.

I separated the observed failure from its possible causes. Increasing turning resistance is evidence of a fit problem; it does not identify the exact root cause. Insufficient clearance, accumulated pitch mismatch, first-layer distortion, rough thread flanks, and misalignment could each contribute. The available notes do not contain a clearance series or measurements that isolate one of those factors, so the entry should record the progressive binding and damage without claiming a proved tolerance diagnosis.

The alternative changed the engagement path. Instead of sliding along several turns of printed thread, the hopper would insert into an interface with slots and projecting tabs, then lock through a short movement. The blender mechanism supplied the general reference. The important design variables became tab thickness, slot width, the insertion clearance, the locking stop, and the supporting surface that made the hopper sit flush.

I needed the seating surface to carry the hopper consistently so that retention features did not become the only alignment features. A tab that can be forced into a slot does not establish that the powder outlet remains centered. Similarly, enough clearance to make insertion easy can leave unwanted rotation or lift. The journal should therefore distinguish successful insertion, full seating, retention, and removal as separate observations rather than reducing the whole fit trial to 'it worked.'

This update led to a second design question: even if the locking connection was easier to use, did it actually simplify cleaning? The interface still created extra surfaces and joints in the powder path. The later decision to combine components came from revisiting that assumption. I keep the thread failure and tab/slot redesign together here because the latter is the direct response to the former, while the integration decision belongs to the next update.

## Image sequence

![Printed blue threaded hopper components from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_1.jpg)

Printed blue threaded hopper components from the M1 notes.

![Printed cylindrical hopper or receiver component from the M1 notes.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_6.jpg)

Printed cylindrical hopper or receiver component from the M1 notes.

![Annotated hopper section showing the screw-in funnel concept and internal drive.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_5.jpg)

Annotated hopper section showing the screw-in funnel concept and internal drive.

![CAD of a hopper interface with locking features. Confirm its exact revision before identifying tabs and slots.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m1_3.jpg)

CAD of a hopper interface with locking features. Confirm its exact revision before identifying tabs and slots.

## Result and handoff

The threaded interface was rejected after progressive binding and material damage. A blender-inspired tab-and-slot alternative was designed; exact fit-test results for it still need the original record.

## Complete from your records

Add thread diameter/pitch and revision, clearance changes attempted, tab and slot dimensions, locking angle, and actual insertion/removal observations.

[IMAGE PLACEHOLDER: Thread sketch and helix/thread feature from the exact failed CAD revision, then the damaged printed interface.]

[IMAGE PLACEHOLDER: Tab and slot sketches, intermediate cuts, and locked/unlocked final views; those stages have not yet been recovered.]

## Sources

- [M1 - MECHANICAL DOSER](https://docs.google.com/document/d/1VJVmuO_Wsarp4JEZYmcffV4hj5R7lj_xGEI08EhueAM/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
