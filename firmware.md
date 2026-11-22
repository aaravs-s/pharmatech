# Firmware

## Overview

- **Target board:** _Board and revision_
- **Microcontroller:** _Part number_
- **Toolchain:** _Compiler, IDE, and SDK versions_
- **Current revision:** _Tag or commit_

## Architecture

Describe the firmware modules and their responsibilities. Include startup, configuration, peripheral drivers, communications, state management, logging, and error handling.

```text
app/
  boot/
  drivers/
  services/
  state/
  tests/
```

## Build

Document exact prerequisites and repeatable commands here, for example:

```sh
# Add the project-specific toolchain setup and build commands.
```

Pin dependency versions and record required environment variables or configuration files.

## Flashing

1. Disconnect loads and confirm that the target is powered safely.
2. Select the correct board and firmware image.
3. Erase or preserve existing configuration as appropriate.
4. Flash the bootloader and application, if required.
5. Verify the firmware version and run basic communication checks.

## Configuration

| Setting | Default | Range or options | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Testing

- Unit tests:
- Hardware-in-the-loop tests:
- Peripheral bring-up:
- Fault-injection cases:
- Release acceptance criteria:

## Validation checklist

- [ ] Firmware builds reproducibly from a clean environment
- [ ] Pin assignments match the electronics revision
- [ ] Boot, reset, and recovery behavior tested
- [ ] Communication and sensor paths verified
- [ ] Safety-critical faults produce a safe state
- [ ] Version, logs, and test results recorded
