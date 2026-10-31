#!/usr/bin/env python3
"""Dispense one powder using scale feedback. Positioning belongs to app.py.

Usage: python3 motor_scale_controller.py 5.0 "Cornstarch"

The Raspberry Pi now talks to one combined Arduino Uno controller for the
auger, detent-indexed disk, and linear actuator. The app passes ARDUINO_PORT
and DISK_CURRENT_SLOT in the child environment. Opening a classic Uno serial
port may reset it, so SET SLOT restores the disk's logical slot only after D2
confirms that the disk is physically sitting in a detent.

This dispensing process does not move the actuator; app.py owns positioning.
Each powder name selects its matching Arduino auger speed profile (1..8).
"""

from __future__ import annotations

import argparse
import os
import math
import re
import signal
import time
from enum import Enum
from typing import Optional


# ============================================================
# 1) SERIAL SETTINGS - EDIT HERE
# ============================================================

SCALE_PORT = os.environ.get("SCALE_PORT", "/dev/ttyUSB0")
SCALE_BAUD = int(os.environ.get("SCALE_BAUD", "9600"))

CONTROLLER_PORT = os.environ.get("ARDUINO_PORT", "/dev/ttyACM0")
CONTROLLER_BAUD = int(os.environ.get("ARDUINO_BAUD", "115200"))

SERIAL_OPEN_DELAY_S = 2.0
SCALE_TIMEOUT_S = 3.0


# ============================================================
# 2) PER-POWDER THRESHOLDS - EDIT HERE
# ============================================================
# Thresholds are GRAMS REMAINING. Every powder has its own threshold block so
# it can be tuned independently later. The copied values below preserve the
# current behavior exactly: sugar/salt use the existing FREE values and the
# remaining powders use the existing NONFREE values.
#
# These gram settings choose WHEN the phase changes. ``arduino_profile_id``
# links each powder to the same numbered row in AUGER_POWDER_PROFILES in the
# Arduino sketch; the Arduino row controls motor speeds and pulse sizes.
POWDER_PROFILES = {
    "granulated sugar": {
        "category": "FREE",
        "arduino_profile_id": 1,
        "max_to_turbo_g": 10,
        "turbo_to_normal_g": 5,
        "normal_to_fine_g": 1.5,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "table salt": {
        "category": "FREE",
        "arduino_profile_id": 2,
        "max_to_turbo_g": 10,
        "turbo_to_normal_g": 5,
        "normal_to_fine_g": 1.5,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "powdered sugar": {
        "category": "NONFREE",
        "arduino_profile_id": 3,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "baking soda": {
        "category": "NONFREE",
        "arduino_profile_id": 4,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "cornstarch": {
        "category": "NONFREE",
        "arduino_profile_id": 5,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "ground cinnamon": {
        "category": "NONFREE",
        "arduino_profile_id": 6,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "all-purpose flour": {
        "category": "NONFREE",
        "arduino_profile_id": 7,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
    "cocoa powder": {
        "category": "NONFREE",
        "arduino_profile_id": 8,
        "max_to_turbo_g": 4,
        "turbo_to_normal_g": 0.50,
        "normal_to_fine_g": 0.3,
        "fine_to_final_g": 0.05,
        "tolerance_g": 0.005,
    },
}


# Settling times are still shared by category because this requested change is
# only about giving each powder independent gram thresholds.
CATEGORY_TIMING = {
    "FREE": {
        "continuous_settle_s": 0.25,
        "fine_settle_s": 0.20,
        "final_settle_s": 0.30,
    },
    "NONFREE": {
        "continuous_settle_s": 0.25,
        "fine_settle_s": 0.20,
        "final_settle_s": 0.30,
    },
}


def get_profile(powder_name: str) -> tuple[str, dict]:
    key = " ".join(powder_name.lower().split())
    if key not in POWDER_PROFILES:
        raise ValueError(f"Add {powder_name!r} to POWDER_PROFILES before dispensing.")

    powder_profile = POWDER_PROFILES[key]
    category = powder_profile.get("category")
    if category not in ("FREE", "NONFREE"):
        raise ValueError(f"Invalid category for {powder_name!r}: {category}")

    threshold_names = {
        "max_to_turbo_g",
        "turbo_to_normal_g",
        "normal_to_fine_g",
        "fine_to_final_g",
        "tolerance_g",
    }
    unknown = powder_profile.keys() - threshold_names - {
        "category", "arduino_profile_id"
    }
    if unknown:
        raise ValueError(f"Unknown profile settings: {sorted(unknown)}")

    missing = threshold_names - powder_profile.keys()
    if missing:
        raise ValueError(
            f"Missing threshold settings for {powder_name!r}: {sorted(missing)}"
        )

    arduino_profile_id = powder_profile.get("arduino_profile_id")
    if (isinstance(arduino_profile_id, bool) or
            not isinstance(arduino_profile_id, int) or
            not 1 <= arduino_profile_id <= 8):
        raise ValueError(
            f"Invalid arduino_profile_id for {powder_name!r}: "
            f"{arduino_profile_id!r}; expected an integer from 1 to 8."
        )

    settings = CATEGORY_TIMING[category].copy()
    settings.update({name: powder_profile[name] for name in threshold_names})
    settings["arduino_profile_id"] = arduino_profile_id
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0
           for v in settings.values()):
        raise ValueError("Profile values must be finite, nonnegative numbers.")
    if not (settings["tolerance_g"] < settings["fine_to_final_g"] <
            settings["normal_to_fine_g"] < settings["turbo_to_normal_g"] <
            settings["max_to_turbo_g"]):
        raise ValueError(
            "Thresholds must increase: tolerance < final < fine < normal < turbo."
        )
    return category, settings


# ============================================================
# 3) MACHINE SETTINGS - EDIT HERE
# ============================================================

MAX_DISPENSE_TIME_S = 3000
HEARTBEAT_INTERVAL_S = 0.50


# ============================================================
# PHASE LOGIC
# ============================================================

class Phase(str, Enum):
    MAX = "MAX"
    TURBO = "TURBO"
    NORMAL = "NORMAL"
    FINE = "FINE"
    FINAL = "FINAL"
    DONE = "DONE"


def choose_phase(remaining_g: float, profile: Optional[dict] = None) -> Phase:
    """Choose one of the five dispensing phases from grams remaining."""
    if profile is None:
        _, profile = get_profile("cornstarch")
    if remaining_g <= profile["tolerance_g"]:
        return Phase.DONE
    if remaining_g <= profile["fine_to_final_g"]:
        return Phase.FINAL
    if remaining_g <= profile["normal_to_fine_g"]:
        return Phase.FINE
    if remaining_g <= profile["turbo_to_normal_g"]:
        return Phase.NORMAL
    if remaining_g <= profile["max_to_turbo_g"]:
        return Phase.TURBO
    return Phase.MAX


# ============================================================
# SCALE
# ============================================================

NUMBER_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")


def parse_weight(line: str) -> Optional[float]:
    """Extract the first signed number from a scale line."""
    text = line.strip()
    if not text:
        return None

    match = NUMBER_RE.search(text)
    if match is None:
        return None

    value = float(match.group())

    if "kg" in text.lower():
        value *= 1000.0

    return value


class Scale:
    def __init__(self, serial_port) -> None:
        self.serial = serial_port
        self._pending = b""

    def read_grams(self, timeout: float = SCALE_TIMEOUT_S) -> float:
        """Return the newest complete reading, draining any received backlog.

        Settling waits and Arduino replies can let scale messages accumulate.
        Preserve incomplete lines across calls; never parse a partial number.
        Do not reuse a previous call's weight if the scale stops sending data.
        """
        deadline = time.monotonic() + timeout
        latest = None
        while time.monotonic() < deadline:
            waiting = self.serial.in_waiting
            raw = self.serial.read(min(waiting, 4096) if waiting else 1)
            if not raw:
                continue
            self._pending += raw
            while b"\n" in self._pending:
                line, self._pending = self._pending.split(b"\n", 1)
                value = parse_weight(line.decode("ascii", errors="ignore"))
                if value is not None:
                    latest = value
            if len(self._pending) > 4096:
                raise ValueError("Scale message has no line ending; check serial format.")
            if latest is not None and self.serial.in_waiting == 0:
                return latest
        if latest is not None:
            return latest
        raise TimeoutError("No valid scale reading received.")

    def stable_grams(self, samples: int = 5) -> float:
        readings = [self.read_grams() for _ in range(samples)]
        return sum(readings) / len(readings)


# ============================================================
# ARDUINO SERIAL CLIENT
# ============================================================

class ControllerError(RuntimeError):
    pass


class MachineController:
    def __init__(
        self,
        serial_port,
        category: str = "NONFREE",
        powder_profile_id: int = 5,
    ) -> None:
        if category not in ("FREE", "NONFREE"):
            raise ValueError("Category must be FREE or NONFREE.")
        if (isinstance(powder_profile_id, bool) or
                not isinstance(powder_profile_id, int) or
                not 1 <= powder_profile_id <= 8):
            raise ValueError("powder_profile_id must be an integer from 1 to 8.")
        self.serial = serial_port
        self.category = category
        self.powder_profile_id = powder_profile_id

    def _write(self, command: str) -> None:
        self.serial.write((command.strip() + "\n").encode("ascii"))
        self.serial.flush()

    def _wait_for(
        self,
        expected: str,
        timeout: float,
        command: str,
    ) -> str:
        deadline = time.monotonic() + timeout
        last_line = ""

        while time.monotonic() < deadline:
            raw = self.serial.readline()
            if not raw:
                continue

            line = raw.decode("ascii", errors="ignore").strip()
            if not line:
                continue

            last_line = line
            print(f"[ARDUINO] {line}", flush=True)

            if line.startswith("ERR") or line.startswith("FAULT"):
                raise ControllerError(line)

            if line == expected:
                return line

        raise ControllerError(
            f"Timed out after '{command}'. "
            f"Expected '{expected}', last line was '{last_line or '<none>'}'."
        )

    def command(
        self,
        command: str,
        expected: str,
        timeout: float = 5.0,
    ) -> None:
        self._write(command)
        self._wait_for(expected, timeout, command)

    def ping(self) -> None:
        self.command("PING", "OK PING", 2.0)

    def heartbeat(self) -> None:
        self.command("HEARTBEAT", "OK HEARTBEAT", 1.0)

    def verify_disk_at_slot(self, slot: int) -> None:
        """Verify the restored logical slot and the physical D2 detent state.

        The final combined Uno firmware reports fields such as:
            DISK STATUS MOVING=NO ENABLED=YES SLOT=n AT_SLOT=YES SWITCH=OPEN ...

        The switch proves that the disk is physically in a detent. Because all
        eight detents are identical, DISK_CURRENT_SLOT supplied by app.py still
        provides the absolute logical slot reference after an Uno reset.
        """
        if not 1 <= slot <= 8:
            raise ValueError("slot must be between 1 and 8.")

        command = "DISK STATUS"
        self._write(command)
        deadline = time.monotonic() + 2.0
        last_line = ""

        while time.monotonic() < deadline:
            raw = self.serial.readline()
            if not raw:
                continue

            line = raw.decode("ascii", errors="ignore").strip()
            if not line:
                continue

            last_line = line
            print(f"[ARDUINO] {line}", flush=True)

            if line.startswith("ERR") or line.startswith("FAULT"):
                raise ControllerError(line)

            if line.startswith("DISK STATUS "):
                fields = {}
                for token in line[len("DISK STATUS "):].split():
                    if "=" in token:
                        key, value = token.split("=", 1)
                        fields[key] = value

                problems = []
                if fields.get("SLOT") != str(slot):
                    problems.append(f"SLOT={fields.get('SLOT', '<missing>')}")
                if fields.get("AT_SLOT") != "YES":
                    problems.append(f"AT_SLOT={fields.get('AT_SLOT', '<missing>')}")
                if fields.get("SWITCH") != "OPEN":
                    problems.append(f"SWITCH={fields.get('SWITCH', '<missing>')}")
                if fields.get("MOVING") != "NO":
                    problems.append(f"MOVING={fields.get('MOVING', '<missing>')}")

                if problems:
                    raise ControllerError(
                        "Disk position check failed after Uno reset: expected "
                        f"SLOT={slot}, AT_SLOT=YES, SWITCH=OPEN, MOVING=NO; got "
                        + ", ".join(problems)
                        + f" in {line!r}."
                    )
                return

        raise ControllerError(
            "Timed out checking disk detent/slot state. "
            f"Last line was {last_line or '<none>'!r}."
        )

    def restore_disk_hold(self, slot: int) -> None:
        # Reassert the app's logical reference only when the D2 switch
        # confirms that the disk is physically sitting in a detent.
        if not 1 <= slot <= 8:
            raise ValueError("DISK_CURRENT_SLOT must be between 1 and 8.")
        self.command(f"SET SLOT {slot}", f"OK DISK SLOT SET {slot}", 2.0)
        self.verify_disk_at_slot(slot)

    def start_continuous(self, phase: Phase) -> None:
        if phase not in (Phase.MAX, Phase.TURBO, Phase.NORMAL):
            raise ValueError("Only MAX, TURBO, and NORMAL are continuous.")
        self.command(
            f"AUGER CONT {self.powder_profile_id} {phase.value}",
            "OK CONTINUOUS",
            2.0,
        )

    def pulse(self, phase: Phase) -> None:
        if phase not in (Phase.FINE, Phase.FINAL):
            raise ValueError("Only FINE and FINAL are pulse phases.")
        self.command(
            f"AUGER PULSE {self.powder_profile_id} {phase.value}",
            "DONE PULSE",
            5.0,
        )

    def stop_auger(self) -> None:
        self.command("AUGER STOP", "OK AUGER STOP", 2.0)

    def stop_all_best_effort(self) -> None:
        try:
            self._write("STOP ALL")
        except Exception:
            pass


# ============================================================
# DISPENSING LOOP
# ============================================================

def dispense(
    target_g: float,
    powder_name: str,
    scale: Scale,
    controller: MachineController,
) -> float:
    if not math.isfinite(target_g) or target_g <= 0:
        raise ValueError("Target must be greater than zero.")

    category, profile = get_profile(powder_name)
    controller.category = category
    controller.powder_profile_id = profile["arduino_profile_id"]

    print(
        f"START | Powder: {powder_name} | "
        f"Target: {target_g:.3f} g | Category: {category} | "
        f"Arduino profile: {controller.powder_profile_id}",
        flush=True,
    )

    start_weight_g = scale.stable_grams()
    print(f"Start weight: {start_weight_g:.3f} g", flush=True)

    start_time = time.monotonic()
    active_phase: Optional[Phase] = None
    last_heartbeat = 0.0

    while True:
        now = time.monotonic()

        if now - start_time > MAX_DISPENSE_TIME_S:
            raise TimeoutError("Maximum dispense time exceeded.")

        current_weight_g = scale.read_grams()
        dispensed_g = current_weight_g - start_weight_g
        remaining_g = target_g - dispensed_g
        phase = choose_phase(remaining_g, profile)

        # Keep these exact words because app.py already parses them.
        print(
            f"Dispensed: {dispensed_g:.3f} g | "
            f"Remaining: {remaining_g:.3f} g | "
            f"Phase: {phase.value}",
            flush=True,
        )

        if phase is Phase.DONE:
            controller.stop_auger()
            print(f"DONE | Dispensed: {dispensed_g:.3f} g", flush=True)
            return dispensed_g

        # Continuous phases -------------------------------------------------
        if phase in (Phase.MAX, Phase.TURBO, Phase.NORMAL):
            if active_phase is not phase:
                controller.start_continuous(phase)
                active_phase = phase
                print(f"MODE -> {phase.value}", flush=True)

            if now - last_heartbeat >= HEARTBEAT_INTERVAL_S:
                controller.heartbeat()
                last_heartbeat = time.monotonic()

            continue

        # First transition out of continuous movement -----------------------
        if active_phase in (Phase.MAX, Phase.TURBO, Phase.NORMAL):
            controller.stop_auger()
            active_phase = None
            print(
                f"Continuous movement stopped; "
                f"settling {profile['continuous_settle_s']:.2f} s",
                flush=True,
            )
            time.sleep(profile["continuous_settle_s"])
            continue

        # Pulse phases ------------------------------------------------------
        controller.pulse(phase)
        active_phase = None

        if phase is Phase.FINE:
            time.sleep(profile["fine_settle_s"])
        else:
            time.sleep(profile["final_settle_s"])


# ============================================================
# PROGRAM ENTRY
# ============================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pill Compounder motor + scale controller"
    )
    parser.add_argument("target", type=float, help="Target grams")
    parser.add_argument("powder", help="Powder name")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not math.isfinite(args.target) or args.target <= 0:
        print("TARGET MUST BE A FINITE NUMBER GREATER THAN ZERO", flush=True)
        return 2

    try:
        get_profile(args.powder)  # Validate edits before opening USB devices.
    except (ValueError, KeyError, TypeError) as exc:
        print(f"INVALID POWDER PROFILE: {exc}", flush=True)
        return 2

    # Require the app's position reference before opening/resetting the Arduino.
    try:
        slot = int(os.environ["DISK_CURRENT_SLOT"])
        if not 1 <= slot <= 8:
            raise ValueError("slot outside 1..8")
    except (KeyError, ValueError):
        print("DISK_CURRENT_SLOT must contain the known physical slot (1..8).", flush=True)
        return 2

    try:
        import serial
    except ImportError:
        print("Install pyserial with: pip3 install pyserial", flush=True)
        return 3

    scale_serial = controller_serial = controller = None
    previous_sigterm = signal.signal(signal.SIGTERM, request_stop)
    try:
        scale_serial = serial.Serial(SCALE_PORT, SCALE_BAUD, timeout=0.10)
        controller_serial = serial.Serial(
            CONTROLLER_PORT, CONTROLLER_BAUD, timeout=0.10, write_timeout=0.50
        )
        time.sleep(SERIAL_OPEN_DELAY_S)
        controller_serial.reset_input_buffer()
        controller = MachineController(controller_serial)
        controller.ping()
        controller.restore_disk_hold(slot)
        scale_serial.reset_input_buffer()
        dispense(args.target, args.powder, Scale(scale_serial), controller)
        return 0
    except KeyboardInterrupt:
        print("STOP REQUESTED", flush=True)
        if controller is not None:
            controller.stop_all_best_effort()
        return 130
    except Exception as exc:
        print(f"FATAL ERROR: {exc}", flush=True)
        if controller is not None:
            controller.stop_all_best_effort()
        return 10
    finally:
        for connection in (controller_serial, scale_serial):
            if connection is not None:
                try:
                    connection.close()
                except Exception:
                    pass
        signal.signal(signal.SIGTERM, previous_sigterm)


def request_stop(signum, frame):
    """Route subprocess terminate() through the same cleanup as Ctrl-C."""
    raise KeyboardInterrupt


if __name__ == "__main__":
    raise SystemExit(main())
