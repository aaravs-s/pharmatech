# Recreate PharmaTech Rx from scratch

The journals tell the story in the order it happened. This page is the straight-line build: everything someone needs to rebuild the same machine, with journal numbers pointing back to where each step was figured out.

## What the machine is

An 8-powder pill compounder. A rotary disk carries 8 hoppers; the selected hopper is rotated over a 0.001 g analytical balance, a shared drive engages that hopper's auger, and a scale-feedback loop dispenses to the target mass within ±3%. Controlled from a touchscreen on a Raspberry Pi — no laptop needed.

Design targets set at the start (Journal 002): 8 hopper positions · up to 100 g per hopper · machine fits a 50 × 50 × 50 cm envelope · final mass within 3% of target · 8 test powders: granulated sugar, table salt, cocoa, ground cinnamon, baking soda, cornstarch, powdered sugar, all-purpose flour.

## Bill of materials (from the project BOM sheet — 22 items, $732.06; $49.96 was still pending)

| Part | Used for | Milestone |
|---|---|---|
| Bonvoisin analytical balance, 500 g × 0.001 g | Scale feedback | M2 |
| Raspberry Pi 4 kit (4 GB) | Controller | M2 |
| Hosyond 7" 800×480 DSI touchscreen | Kiosk UI | M2 |
| USB→RS232 serial adapter (PL2303) | Balance → Pi | M2 |
| NEMA 17 stepper, 2 A, 59 Ncm + TMC2209 | First auger drive | M2–M3 |
| 8×8 mm plum flexible coupler | Auger shaft coupling | M3 |
| NEMA 23 closed-loop integrated steppers ×2 | Disk + upgraded drive | M4 |
| 3030 T-slot aluminium extrusion + connectors + T-nuts | Frame | M4 |
| 24 V 15 A 360 W power supply | Main power | M4 |
| LM2596 buck module; 24 V→5 V bucks | Power regulation | M4 |
| Mini linear rail, T6×1 lead screw + NEMA 11, 50 mm travel | Drive lift/engage actuator (was the pending item) | M4 |
| Barcode scanner | Dropped after powder classification (Journal 031) | M4 |
| Food-safe PETG filament ×2 | Hoppers and printed parts | M4 |
| Acetone | Vapor smoothing printed parts | M4 |
| M2.5 screw assortment | Assembly | — |

Full links, quantities and prices live in the PharmaTech Bill of Materials sheet in Drive.

## Electronics map (final state, from the Sep 12, 2026 code)

- **Arduino Uno / classic Nano (ATmega328P)** runs the real-time motion:
  - Auger: STEP D9, DIR D8, ENABLE D10 — pulses from Timer1 hardware (OC1A)
  - Disk: STEP D11, DIR D12, ENABLE D4 — pulses from Timer2; indexes by counting detents on a mechanical switch at **D2** (INPUT_PULLUP, pressed on rim = LOW, released in detent = HIGH), clockwise only; `SET SLOT n` / replies `DONE DISK SLOT n`; an indexing error invalidates the stored position
  - Linear actuator (TMC2209): STEP D6, DIR D7 — raises the drive before any disk move; actuator + disk + auger never move at the same time; actuator position is software-tracked (no limit switches)
- **Raspberry Pi 4** runs the app and talks to the Arduino over serial and to the balance over RS232.

## Software (three pieces, all from the Sep 12, 2026 code exchange)

1. `app.py` (Pi) — CustomTkinter touchscreen app, 800×480 fullscreen, "Compounding Doser." Owns recipes and positioning; starts dispensing runs and passes `ARDUINO_PORT` and `DISK_CURRENT_SLOT` to them.
2. `motor_scale_controller.py` (Pi) — dispenses ONE powder to a target using scale feedback, e.g. `python3 motor_scale_controller.py 5.0 "Cornstarch"`. Profiles differ for free-flowing vs non-free-flowing powders; it does not move the actuator.
3. Arduino sketch — see Electronics map. Full code belongs in `assets/code/` with each journal that changed it linking the version it used.

## Build order (mirrors the journals)

1. Study the auger reference; set targets (Journals 001–002)
2. Build ONE doser: hopper + auger + outlet (M1 journals)
3. Close the loop with the balance (M2 journals)
4. Prove all 8 powders; fix speed (M3 journals)
5. Multiply to 8: disk, drive lift, coupler, frame (M4 journals)
6. Integrate, organise wiring, final code (M5 + September journals)
7. Operate it with the SOP (final journal)

## Known limits (do not claim these are solved)

- **Small doses are not solved.** At a 5 g target every powder lands within 0.3% error, but at a 0.055 g target, 5 of 8 powders miss the 3% target (flour 14.55%, powdered sugar 10.91%). If you rebuild this machine, treat 55 mg accuracy as open work, not a finished result (Journals 029–030, 035, 056).
- **The actuator line in the BOM was still marked pending ($49.96)** even though the actuator was bought and installed (Journal 041). Check the purchase record before re-ordering.
- **The M4 notes' fixed-step disk plan (6,400 steps ÷ 8, shortest path) was superseded** by clockwise-only detent indexing in the final code (Journal 054). Build the detent version.

## Operating it

The full 12-step operating procedure is the project SOP (Drive, Milestone 3 folder): assign the powder to a slot in the kiosk, pour into the hopper, tare the balance to 0.000 g, enter grams (max 100 g), start, FORCE STOP on any jam/smoke/smell, confirm the result is within ±3%, then disassemble with M3 tools and wipe the auger and hopper clean. Forgetting to tare is the documented #1 mistake.
