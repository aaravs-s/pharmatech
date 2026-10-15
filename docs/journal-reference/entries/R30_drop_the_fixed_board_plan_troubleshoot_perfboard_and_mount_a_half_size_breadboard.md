# R30 Drop the fixed-board plan, troubleshoot perfboard, and mount a half-size breadboard

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 5 · Previous topics J44, J45

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Make the changing electronics practical to assemble and service without claiming an unfinished PCB was installed.

## Design process

I returned to the electronics packaging problem after the mechanical components were working together. The PCB I had planned earlier was no longer a straightforward next step because the design continued to change and I had not finalized a stable board layout.

I tried a perfboard as an alternative to the larger breadboard. The notes say that it failed to connect as needed, but do not identify the exact electrical fault. That detail matters: a solder bridge, missing connection, wrong pin mapping, or broken joint would each lead to a different debugging story. I would describe the symptom and actual checks before naming the cause.

I ultimately returned to a breadboard so I could continue modifying the electronics. This was a practical development decision rather than proof that breadboards were the final best packaging method. Keeping the PCB proposal, perfboard attempt, and return to a modular prototype in the journal preserves the real sequence of decisions.

I reduced the electronics footprint by using a half-size breadboard and designing a custom printed mount. The earlier full-size arrangement was too large and messy to mount conveniently on the frame.

The smaller board retained the flexibility needed for continued changes while making it easier to package the working circuit. The mount needed to locate the board securely and provide a way to attach it to the structure. The notes establish that a custom mount was printed, but the hole spacing, fastening method, and any cable access need to be added from the actual CAD or built part.

This was a small update, but it affected how the machine could be assembled and maintained. A working circuit laid on the bench is different from one mounted where moving parts and wiring must coexist. I would show the old footprint next to the new mount and explain any changes needed to keep the connections accessible.

## Construction and implementation detail

The early PCB plan never reached a finalized design according to M5 notes. As motor control, timers, alarm lines, and the actuator changed, a fixed board layout would have needed repeated revision. The eventual prototype needed an adaptable arrangement that could support continued testing.

A perfboard was tried after the larger breadboard proved bulky and messy. The notes say the perfboard failed to connect, then record returning to a breadboard. That establishes a failed implementation attempt, but does not identify whether the failure came from a solder joint, a trace break, a wrong connection, or another electrical cause. The comparison photo shows both arrangements; it does not diagnose the failure.

The final mounting response was a half-size breadboard and a custom printed mount. The design task shifted from creating a permanent electrical circuit to constraining an interchangeable board mechanically. Relevant CAD details are the board footprint, retaining edges, access to connection rows, mounting-hole positions, standoff height, and clearance around the frame fasteners.

The print also needed to keep connections accessible while making the board stable enough that wire motion would not repeatedly pull on breadboard contacts. A mount that grips the board too tightly can distort it; a mount that covers edge rows makes changes harder. The exact retention and fastening geometry needs the actual mount CAD rather than an unrelated electronics-cover image.

For a useful process sequence, the journal should show the perfboard before installation, the actual connection test that failed, the half-board footprint sketch, retaining/mounting features in progress, and the board installed on the frame. The available photos and notes support the overall sequence, while the original board-mount construction views remain placeholders.

The outcome was a working-prototype organization choice that kept the electronics modifiable. It does not erase the failed perfboard attempt or prove production reliability. Recording that tradeoff helps another builder understand why the final photographed machine still uses a breadboard despite the earlier PCB proposal.

## Image sequence

![IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/photo_perfboard_comparison.jpg)

IMG_8167.HEIC Drive preview: breadboard wiring beside an unsoldered perfboard. Supports the board-packaging discussion; does not show a completed failed perfboard circuit.

![Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_1.jpg)

Electronics schematic proposal from M2. It is not evidence that a PCB was manufactured.

![Breadboard motor-control wiring in the early prototype.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_2.jpg)

Breadboard motor-control wiring in the early prototype.

![Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_superstructure.jpg)

Current Main workspace Superstructure Part Studio. CAD geometry capture, not a validated structural test.

## Result and handoff

The source records abandoning the PCB, an unsuccessful perfboard attempt, and returning to a half-size breadboard with a printed mount.

## Complete from your records

Identify the perfboard fault and test, actual mount revision/dimensions, board retention, fasteners, and final wiring map.

[IMAGE PLACEHOLDER: Perfboard continuity/connection test with the actual fault marked.]

[IMAGE PLACEHOLDER: Half-board footprint sketch, mounting/retention features in progress, final CAD, and installed board.]

## Sources

- [M5: Autonomous compounding](https://docs.google.com/document/d/1qJvuvPlFe_6ilBBHeEVFkOWMDnufg_hk30H74qPh1nc/edit)
- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
