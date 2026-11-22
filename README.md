# Pharmatech

> Hardware project workspace for the Pharmatech device.

Pharmatech is organized so that design decisions, manufacturing files, electronics, and firmware remain easy to find and reproduce. This repository is currently a project-template scaffold; replace each placeholder with project-specific information as work progresses.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`journals.md`](journals.md) | Chronological engineering log, decisions, experiments, and lessons learned |
| [`cad.md`](cad.md) | CAD workflow, mechanical design notes, tolerances, and release guidance |
| [`electronics.md`](electronics.md) | Schematics, PCB requirements, wiring, BOM, and hardware test notes |
| [`firmware.md`](firmware.md) | Firmware architecture, build instructions, flashing, and validation |

## Project overview

- **Status:** Planning / prototype
- **Purpose:** _Describe the device and its intended use._
- **Target platform:** _Add enclosure, processor family, and operating environment._
- **Maintainers:** _Add maintainer names and contact information._

## Getting started

1. Read the project overview and the relevant discipline document.
2. Record design assumptions and changes in [`journals.md`](journals.md).
3. Use the CAD, electronics, and firmware documents to keep source files and releases synchronized.
4. Before testing, review applicable safety requirements and verify that all hardware is configured as documented.

## Development workflow

```text
Define requirements
  -> Record decisions in the journal
  -> Develop CAD and electronics
  -> Implement and test firmware
  -> Review, release, and document revisions
```

- Commit source files and generated exports together when a revision is released.
- Include a meaningful revision name or issue reference in related commits.
- Record test equipment, test setup, firmware version, and results for reproducible validation.
- Never commit credentials, private keys, personal data, or proprietary exports without approval.

## Hardware safety

> [!WARNING]
> This repository does not establish that the system is safe for a particular use. Perform a risk assessment and all required electrical, mechanical, chemical, and regulatory checks before operating or shipping a prototype.

Disconnect power before changing wiring, inspect for shorts and damaged components, and use appropriately rated tools and personal protective equipment.

## Testing

Document test results in the relevant discipline file and link them to dated journal entries. Include:

- Hardware and firmware revision
- Test configuration and equipment
- Pass/fail criteria
- Observed behavior and measurements
- Known limitations and follow-up actions

## Contributing

1. Create a focused branch for the change.
2. Update the applicable discipline document and journal.
3. Validate CAD exports, PCB files, firmware builds, and hardware tests.
4. Describe the change and any outstanding risks in the pull request.

## License

_Choose a license and add its terms before distributing or releasing the project._