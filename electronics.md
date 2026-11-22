# Electronics

## System overview

- **Voltage supply:** _Nominal and maximum_
- **Power budget:** _Expected and peak current_
- **Primary controller:** _Part number and revision_
- **Sensors and actuators:** _Part names_

## Design files

| Artifact | Location | Revision | Notes |
| --- | --- | --- | --- |
| Schematic |  |  |  |
| PCB layout |  |  |  |
| Bill of materials |  |  |  |
| Assembly drawing |  |  |  |

## Interfaces

| Interface | Direction | Voltage or protocol | Connector | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Component and safety requirements

- Record approved part substitutions and manufacturer lifecycle considerations.
- Identify power, ground, fusing, isolation, ESD, EMC, and thermal requirements.
- Review voltage and current ratings at every interface.
- Include the maximum operating conditions for each subsystem.

## Board bring-up

1. Inspect solder joints and verify polarity and component placement.
2. Measure resistance to ground and rail-to-rail shorts before applying power.
3. Apply current-limited power and verify each supply rail.
4. Verify clocks, resets, communication interfaces, and safety interlocks.
5. Exercise loads within controlled limits and record observations.

## Validation

- [ ] Schematic review completed
- [ ] PCB design rules and manufacturing checks passed
- [ ] BOM approved
- [ ] Power and thermal budgets reviewed
- [ ] Interface voltages and polarities verified
- [ ] Prototype passed functional and safety testing
