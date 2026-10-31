import customtkinter as ctk

import subprocess

import os

import sys

import signal

import threading

import queue

import re

import time

import csv

from datetime import datetime

from tkinter import filedialog



# ============================================================

# UI SETUP

# ============================================================


ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")


root = ctk.CTk()

root.geometry("800x480")

root.title("Compounding Doser")

root.attributes("-fullscreen", True)


# ============================================================

# UI STYLE CONSTANTS

# ============================================================


APP_BG = "#101114"

CARD_BG = "#1A1C20"

CARD_BG_2 = "#20232A"

BORDER = "#30343D"


PRIMARY = "#2563EB"

PRIMARY_HOVER = "#1D4ED8"


DANGER = "#B91C1C"

DANGER_HOVER = "#7F1D1D"


SUCCESS = "#16A34A"

WARNING = "#F59E0B"


TEXT_MUTED = "#A1A1AA"


BUTTON_WIDTH = 360

SMALL_BUTTON_WIDTH = 250


root.configure(fg_color=APP_BG)


# ============================================================

# CONSTANTS

# ============================================================


POWDERS = [

    "EMPTY",

    "Granulated sugar",

    "Powdered sugar",

    "Table salt",

    "Baking soda",

    "Cornstarch",

    "Ground cinnamon",

    "All-purpose flour",

    "Cocoa powder"

]


NON_FREE_FLOWING_POWDERS = [

    "Powdered sugar",

    "Baking soda",

    "Cornstarch",

    "Ground cinnamon",

    "All-purpose flour",

    "Cocoa powder"

]




# ============================================================

# PROCESS / RUN STATE

# ============================================================


motor_process = None

output_queue = queue.Queue()


original_target = 0.0

current_run_target = 0.0

remaining_to_dispense = 0.0

dispensed_this_run = 0.0


stopped_by_user = False


progress_var = None

remaining_var = None

script_var = None


# This stores the recipe summary at the moment START is pressed.

# That way, the completed screen can show what was actually run.

active_run_items = []

active_run_script_name = ""


current_run_id = ""


# ============================================================
# COMBINED ARDUINO SERIAL STATE
# ============================================================

# One Arduino Uno now owns the auger, disk, and linear actuator.
ARDUINO_PORT = os.environ.get("ARDUINO_PORT", "/dev/ttyACM0")
ARDUINO_BAUD = int(os.environ.get("ARDUINO_BAUD", "115200"))
SCALE_PORT = os.environ.get("SCALE_PORT", "/dev/ttyUSB0")
LINEAR_ACTUATOR_TRAVEL_STEPS = 69000

controller_serial = None
controller_serial_lock = threading.RLock()
controller_port_in_use = ARDUINO_PORT

# Disk state tracked by the app. The Uno loses this software reference when
# its USB serial port resets, so a known slot is reasserted after reconnect.
disk_command_active = False
disk_result_queue = queue.Queue()
disk_current_slot = 1
disk_position_known = False
disk_position_var = None
disk_status_var = None

# Actuator state tracked by the app. The physical machine is placed at its
# top reference before app startup. Known UP/DOWN state is reasserted to the
# Uno after a USB reset using SET ACTUATOR UP/DOWN (no physical movement).
actuator_command_active = False
actuator_result_queue = queue.Queue()
actuator_cancel_event = threading.Event()
actuator_position = "UP"
actuator_position_var = None
actuator_status_var = None


# ============================================================
# AUTOMATIC RECIPE SEQUENCE STATE
# ============================================================


recipe_run_active = False

recipe_run_index = 0

recipe_total_dispensed = 0.0

recipe_status_var = None

recipe_result_queue = queue.Queue()

recipe_cancel_event = threading.Event()

recipe_interrupted = False


# ============================================================

# CSV LOGGING

# ============================================================


CSV_FILE = os.path.join(

    os.path.dirname(__file__),

    "dispensing_history.csv"

)


csv_headers = [

    "Run ID",

    "Date",

    "Time",

    "Slot",

    "Powder Name",

    "Target Amount (g)",

    "Motor Mode",

    "Total Recipe Target (g)",

    "Actual Dispensed (g)",

    "Error (g)",

    "Percent Error (%)",

    "Remaining (g)",

    "Status"

]



def create_csv_if_needed():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(csv_headers)



def export_run_to_csv(status="COMPLETED"):

    global current_run_id


    create_csv_if_needed()


    if current_run_id == "":

        current_run_id = datetime.now().strftime("%Y%m%d_%H%M%S")


    now = datetime.now()


    total_actual = sum(

        item.get("dispensed", 0.0)

        for item in active_run_items

    )

    total_target = original_target




    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)


        for item in active_run_items:


            powder_target = item["amount"]


            powder_actual = item.get("dispensed", 0.0)


            powder_error = powder_actual - powder_target


            if powder_target > 0:

                powder_percent_error = (

                    abs(powder_error) / powder_target

                ) * 100

            else:

                powder_percent_error = 0


            writer.writerow([

                current_run_id,

                now.strftime("%Y-%m-%d"),

                now.strftime("%H:%M:%S"),

                f"Slot {item['slot']}",

                item["name"],

                f"{powder_target:.3f}",

                active_run_script_name,

                f"{total_target:.3f}",

                f"{powder_actual:.3f}",

                f"{powder_error:.3f}",

                f"{powder_percent_error:.2f}",

                f"{item.get('remaining', max(0.0, powder_target - powder_actual)):.3f}",

                status

            ])





def view_csv():

    create_csv_if_needed()

    csv_viewer_page()


def export_csv():

    create_csv_if_needed()


    save_location = filedialog.asksaveasfilename(

        title="Export Dispensing History",

        defaultextension=".csv",

        filetypes=[

            ("CSV Files", "*.csv"),

            ("All Files", "*.*")

        ],

        initialfile="dispensing_history.csv"

    )


    if save_location:

        try:

            with open(CSV_FILE, "r") as source:

                data = source.read()


            with open(save_location, "w") as destination:

                destination.write(data)


        except Exception as e:

            print("CSV export error:", e)




# ============================================================

# DATA

# ============================================================


def reset_data():

    """

    Resets all slot powder names and recipe weights.

    """

    global slots, recipe


    slots = {i: {"name": "EMPTY"} for i in range(1, 9)}

    recipe = {i: 0.0 for i in range(1, 9)}



def reset_run_state():

    """

    Resets saved run/progress values.

    """

    global original_target

    global current_run_target

    global remaining_to_dispense

    global dispensed_this_run

    global stopped_by_user

    global active_run_items

    global active_run_script_name

    global current_run_id

    global recipe_run_active, recipe_run_index, recipe_total_dispensed

    global recipe_interrupted


    original_target = 0.0

    current_run_target = 0.0

    remaining_to_dispense = 0.0

    dispensed_this_run = 0.0

    stopped_by_user = False

    active_run_items = []

    active_run_script_name = ""

    current_run_id = ""

    recipe_run_active = False

    recipe_run_index = 0

    recipe_total_dispensed = 0.0

    recipe_interrupted = False

    recipe_cancel_event.clear()


def clear_all_data():

    """

    Clears:

    - slot powder names

    - recipe weights

    - saved progress/run values

    """

    if motor_process is not None and motor_process.poll() is None:

        error_screen(

            "Cannot clear while dispensing is active.\n\n"

            "Use FORCE STOP first, then clear from the home page."

        )

        return


    if recipe_run_active:

        error_screen(

            "Cannot clear while an automatic recipe is active.\n\n"

            "Use FORCE STOP RECIPE first."

        )

        return


    if actuator_command_active:

        error_screen(

            "Cannot clear while the linear actuator is moving.\n\n"

            "Use EMERGENCY ACTUATOR STOP first."

        )

        return


    reset_data()

    reset_run_state()

    home()



def get_active_recipe_items():

    """

    Returns a list of active recipe entries:

    [

        {"slot": 1, "name": "Granulated sugar", "amount": 2.0},

        ...

    ]

    """

    items = []


    for i in range(1, 9):

        name = slots[i]["name"]

        amount = recipe[i]


        if amount > 0:

            items.append({

                "slot": i,

                "name": name,

                "amount": amount

            })


    return items



def get_recipe_total():

    return sum(recipe.values())



def get_powder_type_label():

    return "Automatic 8-slot recipe mode"




reset_data()


# ============================================================

# UI HELPERS

# ============================================================


def clear():

    for w in root.winfo_children():

        w.destroy()



def make_page(title, subtitle=None):

    """

    Creates a consistent page layout:

    - header

    - content card

    - footer

    """

    clear()


    page = ctk.CTkFrame(root, fg_color=APP_BG)

    page.pack(fill="both", expand=True, padx=18, pady=12)


    header = ctk.CTkFrame(page, fg_color="transparent")

    header.pack(fill="x", pady=(0, 8))


    ctk.CTkLabel(

        header,

        text=title,

        font=("Arial", 28, "bold")

    ).pack(anchor="w")


    if subtitle:

        ctk.CTkLabel(

            header,

            text=subtitle,

            font=("Arial", 14),

            text_color=TEXT_MUTED

        ).pack(anchor="w", pady=(2, 0))


    content = ctk.CTkFrame(

        page,

        fg_color=CARD_BG,

        corner_radius=18,

        border_width=1,

        border_color=BORDER

    )

    content.pack(fill="both", expand=True, pady=(4, 8))


    footer = ctk.CTkFrame(page, fg_color="transparent")

    footer.pack(fill="x")


    return page, content, footer



def make_footer_button(parent, text, command, color=PRIMARY, hover=PRIMARY_HOVER, width=SMALL_BUTTON_WIDTH):

    return ctk.CTkButton(

        parent,

        text=text,

        width=width,

        height=42,

        fg_color=color,

        hover_color=hover,

        font=("Arial", 15, "bold"),

        command=command

    )



def make_secondary_button(parent, text, command, width=SMALL_BUTTON_WIDTH):

    return ctk.CTkButton(

        parent,

        text=text,

        width=width,

        height=42,

        fg_color=CARD_BG_2,

        hover_color=BORDER,

        font=("Arial", 15, "bold"),

        command=command

    )



def make_danger_button(parent, text, command, width=SMALL_BUTTON_WIDTH, height=42):

    return ctk.CTkButton(

        parent,

        text=text,

        width=width,

        height=height,

        fg_color=DANGER,

        hover_color=DANGER_HOVER,

        font=("Arial", 15, "bold"),

        command=command

    )



def add_clear_button(parent):

    make_danger_button(

        parent,

        text="CLEAR ALL",

        command=clear_all_data,

        width=130

    ).pack(side="right", padx=6)


# ============================================================

# KEYBOARD

# ============================================================


def keyboard(callback, mode="text"):

    win = ctk.CTkToplevel(root)

    win.geometry("420x420")

    win.title("Keyboard")

    win.configure(fg_color=APP_BG)


    entry = ctk.CTkEntry(win, width=300, height=42, font=("Arial", 18))

    entry.pack(pady=12)


    def press(x):

        entry.insert("end", x)


    def back():

        t = entry.get()

        entry.delete(0, "end")

        entry.insert(0, t[:-1])


    def save():

        callback(entry.get())

        win.destroy()


    if mode == "number":

        keys = [

            "123",

            "456",

            "789",

            "0."

        ]

    else:

        keys = [

            "qwertyuiop",

            "asdfghjkl",

            "zxcvbnm"

        ]


    for row in keys:

        f = ctk.CTkFrame(win, fg_color="transparent")

        f.pack(pady=2)


        for c in row:

            ctk.CTkButton(

                f,

                text=c,

                width=42,

                height=38,

                command=lambda v=c: press(v)

            ).pack(side="left", padx=2)


    ctk.CTkButton(

        win,

        text="BACKSPACE",

        width=260,

        height=38,

        fg_color=CARD_BG_2,

        hover_color=BORDER,

        command=back

    ).pack(pady=6)


    ctk.CTkButton(

        win,

        text="SAVE",

        width=260,

        height=42,

        fg_color=SUCCESS,

        hover_color="#15803D",

        command=save

    ).pack(pady=4)


# ============================================================
# EIGHT-SLOT DISK CONTROL
# ============================================================


def disk_arduino_candidates():
    candidates = [
        ARDUINO_PORT,
        "/dev/ttyACM0",
        "/dev/ttyACM1",
        "/dev/ttyUSB1",
        "/dev/ttyUSB0",
    ]

    unique = []
    for port in candidates:
        if port == SCALE_PORT:
            continue
        if port not in unique:
            unique.append(port)

    return unique


def _disk_exchange_locked(command, response_type="ok", timeout=5.0):

    if controller_serial is None or not controller_serial.is_open:

        raise RuntimeError("Arduino serial port is not open.")


    controller_serial.write((command.strip() + "\n").encode("ascii"))

    controller_serial.flush()


    deadline = time.monotonic() + timeout

    last_line = ""


    while time.monotonic() < deadline:

        raw = controller_serial.readline()

        if not raw:

            continue


        line = raw.decode("ascii", errors="ignore").strip()

        if not line:

            continue


        last_line = line

        print("[DISK]", line)


        if line.startswith(("ERR", "FAULT")):

            raise RuntimeError(line)


        if response_type == "motion" and line.startswith("DONE DISK SLOT "):

            return line

        if response_type == "motion" and line.startswith("OK DISK STOPPED"):

            raise RuntimeError("Disk movement was stopped; position is unknown.")

        if response_type == "motion" and line == "OK STOP ALL":

            raise RuntimeError("Disk movement was stopped; position is unknown.")

        if response_type == "status" and line.startswith("DISK STATUS "):

            return line

        if response_type == "ok" and line.startswith("OK"):

            return line


    raise RuntimeError(

        f"Timed out waiting for Arduino after '{command}'. "

        f"Last response: {last_line or '<none>'}"

    )


def _restore_controller_state_after_reset_locked():
    """Restore software-only references lost when opening/resetting the Uno.

    These commands do NOT move either mechanism. They only tell the freshly
    reset firmware which physical detent/actuator endpoint the app already
    knows the machine is sitting at.
    """
    if actuator_position in ("UP", "DOWN"):
        _actuator_exchange_locked(
            f"SET ACTUATOR {actuator_position}",
            response_type="ok",
            timeout=2.0,
        )

    if disk_position_known:
        _disk_exchange_locked(
            f"SET SLOT {disk_current_slot}",
            response_type="ok",
            timeout=2.0,
        )


def _open_controller_serial_locked():
    global controller_serial, controller_port_in_use

    if controller_serial is not None and controller_serial.is_open:
        return False

    try:
        import serial
    except ImportError as exc:
        raise RuntimeError(
            "pyserial is required. Install it with: pip3 install pyserial"
        ) from exc

    errors = []

    for port in disk_arduino_candidates():
        if not os.path.exists(port):
            continue

        connection = None
        try:
            connection = serial.Serial(
                port,
                ARDUINO_BAUD,
                timeout=0.10,
                write_timeout=0.50,
            )
            controller_serial = connection

            # A classic Uno normally resets when USB serial opens.
            time.sleep(2.0)
            connection.reset_input_buffer()

            ping_response = _disk_exchange_locked("PING", timeout=2.0)
            if ping_response != "OK PING":
                raise RuntimeError(
                    f"Unexpected controller identity: {ping_response}"
                )

            controller_port_in_use = port
            _restore_controller_state_after_reset_locked()

            print(f"Combined Uno controller connected on {port}")
            return True

        except Exception as exc:
            errors.append(f"{port}: {exc}")
            if connection is not None:
                try:
                    connection.close()
                except Exception:
                    pass
            controller_serial = None

    detail = "; ".join(errors) if errors else "no candidate serial device exists"
    raise RuntimeError(
        f"Could not connect to combined Arduino Uno. "
        f"Checked {disk_arduino_candidates()}. Details: {detail}"
    )


def close_controller_serial():
    global controller_serial

    with controller_serial_lock:
        if controller_serial is None:
            return

        try:
            controller_serial.close()
        except Exception:
            pass

        controller_serial = None


def _perform_disk_command(command, response_type, timeout):
    with controller_serial_lock:
        _open_controller_serial_locked()
        return _disk_exchange_locked(command, response_type, timeout)


def _update_disk_page_labels(message=None):

    if disk_position_var is not None:

        if disk_position_known:

            disk_position_var.set(f"Current disk position: Slot {disk_current_slot}")

        else:

            disk_position_var.set("Current disk position: UNKNOWN")


    if message is not None and disk_status_var is not None:

        disk_status_var.set(message)


def _finish_disk_command(command, response, requested_slot):

    global disk_command_active, disk_current_slot, disk_position_known


    disk_command_active = False


    if command.startswith("SET SLOT "):

        disk_current_slot = requested_slot

        disk_position_known = True


    elif command.startswith(("DISK GOTO ", "DISK NEXT")):

        match = re.search(r"DONE DISK SLOT\s+(\d+)", response)

        if match:

            disk_current_slot = int(match.group(1))

            disk_position_known = True


    elif command in ("DISK STOP", "DISK DISABLE"):

        disk_position_known = False


    _update_disk_page_labels(response)


def _fail_disk_command(command, message):

    global disk_command_active, disk_position_known


    disk_command_active = False


    # A timeout during movement can leave the disk between positions.

    if command.startswith(("DISK GOTO ", "DISK NEXT")):

        disk_position_known = False


    _update_disk_page_labels(f"ERROR: {message}")


def process_disk_result_queue():

    try:

        result_type, command, payload, requested_slot = (

            disk_result_queue.get_nowait()

        )

    except queue.Empty:

        if disk_command_active:

            root.after(100, process_disk_result_queue)

        return


    if result_type == "success":

        _finish_disk_command(command, payload, requested_slot)

    else:

        _fail_disk_command(command, payload)


def run_disk_command(command, response_type="ok", timeout=5.0, requested_slot=0):

    global disk_command_active


    if recipe_run_active:

        _update_disk_page_labels(

            "Manual disk control is unavailable during an automatic recipe."

        )

        return


    if motor_process is not None and motor_process.poll() is None:

        _update_disk_page_labels("Cannot move disk while dispensing is active.")

        return


    if actuator_command_active:

        _update_disk_page_labels(

            "Wait for the linear actuator movement to finish."

        )

        return


    if disk_command_active:

        _update_disk_page_labels("A disk command is already running.")

        return


    if (

        command.startswith(("DISK GOTO ", "DISK NEXT"))

        and not disk_position_known

    ):

        _update_disk_page_labels(

            "Align the disk at slot 1 with the switch OPEN, then press "
            "SET CURRENT AS SLOT 1."

        )

        return


    disk_command_active = True

    _update_disk_page_labels(f"Sending: {command}")


    def worker():

        try:

            response = _perform_disk_command(command, response_type, timeout)

        except Exception as exc:

            disk_result_queue.put(

                ("error", command, str(exc), requested_slot)

            )

            return


        disk_result_queue.put(

            ("success", command, response, requested_slot)

        )


    threading.Thread(target=worker, daemon=True).start()

    root.after(100, process_disk_result_queue)


def emergency_disk_stop():

    global disk_position_known


    disk_position_known = False

    _update_disk_page_labels("Sending emergency disk stop...")


    # During a move, the worker owns the read side of the serial connection.

    # PySerial supports a concurrent write, allowing STOP to interrupt the

    # Timer2 move instead of waiting for the command timeout.

    if disk_command_active and controller_serial is not None and controller_serial.is_open:

        try:

            controller_serial.write(b"DISK STOP\n")

            controller_serial.flush()

            _update_disk_page_labels(

                "Emergency stop sent. Disk position is now UNKNOWN."

            )

        except Exception as exc:

            _update_disk_page_labels(f"ERROR sending stop: {exc}")

        return


    run_disk_command("DISK STOP")


def disk_control_page():

    global disk_position_var, disk_status_var


    page, content, footer = make_page(

        "Powder Disk Position",

        "Clockwise-only indexing. RELEASE, align slot 1 in an indent, then set it."

    )


    disk_position_var = ctk.StringVar()

    disk_status_var = ctk.StringVar(

        value=(
            "Initial setup: RELEASE → align slot 1 so the limit switch OPENS "
            "in the indent → SET CURRENT AS SLOT 1"
        )

    )

    _update_disk_page_labels()


    ctk.CTkLabel(

        content,

        textvariable=disk_position_var,

        font=("Arial", 22, "bold")

    ).pack(pady=(14, 4))


    ctk.CTkLabel(

        content,

        textvariable=disk_status_var,

        font=("Arial", 14),

        text_color=TEXT_MUTED,

        wraplength=700

    ).pack(pady=(0, 8))


    slot_grid = ctk.CTkFrame(content, fg_color="transparent")

    slot_grid.pack(pady=5)


    for slot in range(1, 9):

        ctk.CTkButton(

            slot_grid,

            text=f"GO TO {slot}",

            width=145,

            height=40,

            font=("Arial", 15, "bold"),

            command=lambda target=slot: run_disk_command(

                f"DISK GOTO {target}",

                response_type="motion",

                timeout=7.0,

                requested_slot=target

            )

        ).grid(row=(slot - 1) // 4, column=(slot - 1) % 4, padx=5, pady=5)


    controls = ctk.CTkFrame(content, fg_color="transparent")

    controls.pack(pady=8)


    make_footer_button(

        controls,

        text="SET CURRENT AS SLOT 1",

        command=lambda: run_disk_command(

            "SET SLOT 1",

            requested_slot=1

        ),

        width=210

    ).pack(side="left", padx=4)


    make_secondary_button(

        controls,

        text="NEXT",

        command=lambda: run_disk_command(

            "DISK NEXT",

            response_type="motion",

            timeout=4.0

        ),

        width=125

    ).pack(side="left", padx=4)


    make_danger_button(

        controls,

        text="RELEASE",

        command=lambda: run_disk_command("DISK DISABLE"),

        width=115

    ).pack(side="left", padx=4)


    make_secondary_button(

        footer,

        text="BACK HOME",

        command=home,

        width=180

    ).pack(side="left", padx=6)


    make_danger_button(

        footer,

        text="EMERGENCY DISK STOP",

        command=emergency_disk_stop,

        width=240

    ).pack(side="left", padx=6)


# ============================================================
# LINEAR ACTUATOR CONTROL
# ============================================================


def _actuator_exchange_locked(command, response_type="ok", timeout=5.0):
    if controller_serial is None or not controller_serial.is_open:
        raise RuntimeError("Combined Arduino serial port is not open.")

    controller_serial.write((command.strip() + "\n").encode("ascii"))
    controller_serial.flush()

    deadline = time.monotonic() + timeout
    last_line = ""

    while time.monotonic() < deadline:
        raw = controller_serial.readline()
        if not raw:
            continue

        line = raw.decode("ascii", errors="ignore").strip()
        if not line:
            continue

        last_line = line
        print("[ACTUATOR]", line)

        if line.startswith(("ERR", "FAULT")):
            raise RuntimeError(line)

        if response_type == "identity" and line == "OK ACTUATOR PING":
            return line

        if response_type == "motion" and line.startswith("DONE ACTUATOR "):
            return line

        if response_type == "motion" and line == "OK ACTUATOR STOPPED":
            raise RuntimeError(
                "Actuator movement was stopped; position is unknown."
            )

        if response_type == "status" and line.startswith("ACTUATOR STATUS "):
            return line

        if response_type == "ok" and line.startswith("OK ACTUATOR"):
            return line

    raise RuntimeError(
        f"Timed out waiting for the linear actuator after '{command}'. "
        f"Last response: {last_line or '<none>'}"
    )


def _perform_actuator_command(command, response_type, timeout):
    with controller_serial_lock:
        _open_controller_serial_locked()

        if (
            command in ("ACTUATOR UP", "ACTUATOR DOWN")
            and actuator_cancel_event.is_set()
        ):
            _actuator_exchange_locked("ACTUATOR STOP", timeout=2.0)
            raise RuntimeError(
                "Actuator movement was cancelled before it started."
            )

        return _actuator_exchange_locked(command, response_type, timeout)


def _update_actuator_page_labels(message=None):

    if actuator_position_var is not None:

        actuator_position_var.set(

            f"Actuator position: {actuator_position}"

        )


    if message is not None and actuator_status_var is not None:

        actuator_status_var.set(message)


def _finish_actuator_command(command, response):

    global actuator_command_active, actuator_position


    actuator_command_active = False

    actuator_cancel_event.clear()


    if command == "ACTUATOR UP" and response.startswith("DONE ACTUATOR UP "):

        actuator_position = "UP"

    elif command == "ACTUATOR DOWN" and response.startswith("DONE ACTUATOR DOWN "):

        actuator_position = "DOWN"

    elif command == "ACTUATOR STOP":

        actuator_position = "UNKNOWN"

    elif command == "SET ACTUATOR UP":

        actuator_position = "UP"

    elif command == "ACTUATOR STATUS":

        match = re.search(r"POSITION=(UP|DOWN|UNKNOWN)", response)

        if match:

            actuator_position = match.group(1)


    _update_actuator_page_labels(response)


def _fail_actuator_command(command, message):

    global actuator_command_active, actuator_position


    actuator_command_active = False

    actuator_cancel_event.clear()


    if command in ("ACTUATOR UP", "ACTUATOR DOWN"):

        actuator_position = "UNKNOWN"


    _update_actuator_page_labels(f"ERROR: {message}")


def process_actuator_result_queue():

    try:

        result_type, command, payload = actuator_result_queue.get_nowait()

    except queue.Empty:

        if actuator_command_active:

            root.after(100, process_actuator_result_queue)

        return


    if result_type == "success":

        _finish_actuator_command(command, payload)

    else:

        _fail_actuator_command(command, payload)


def run_actuator_command(command, response_type="ok", timeout=5.0):

    global actuator_command_active


    if recipe_run_active:

        _update_actuator_page_labels(

            "Manual actuator control is unavailable during an automatic recipe."

        )

        return


    if motor_process is not None and motor_process.poll() is None:

        _update_actuator_page_labels(

            "Cannot move the actuator while dispensing is active."

        )

        return


    if disk_command_active:

        _update_actuator_page_labels(

            "Wait for the current disk movement to finish."

        )

        return


    if actuator_command_active:

        _update_actuator_page_labels(

            "A linear actuator command is already running."

        )

        return


    if command == "ACTUATOR UP" and actuator_position == "UP":

        _update_actuator_page_labels("Actuator is already at the UP reference.")

        return


    if command == "ACTUATOR DOWN" and actuator_position == "DOWN":

        _update_actuator_page_labels("Actuator is already at the DOWN reference.")

        return


    actuator_command_active = True

    actuator_cancel_event.clear()


    if command in ("ACTUATOR UP", "ACTUATOR DOWN"):

        direction = command.rsplit(" ", 1)[-1]

        _update_actuator_page_labels(

            f"Moving {direction}: {LINEAR_ACTUATOR_TRAVEL_STEPS:,} steps "

            "(approximately 55 seconds)..."

        )

    else:

        _update_actuator_page_labels(f"Sending: {command}")


    def worker():

        try:

            response = _perform_actuator_command(command, response_type, timeout)

        except Exception as exc:

            actuator_result_queue.put(("error", command, str(exc)))

            return


        actuator_result_queue.put(("success", command, response))


    threading.Thread(target=worker, daemon=True).start()

    root.after(100, process_actuator_result_queue)


def emergency_actuator_stop():

    global actuator_position


    actuator_position = "UNKNOWN"

    actuator_cancel_event.set()

    _update_actuator_page_labels("Sending emergency actuator stop...")


    # The worker owns serial reads during motion, but a concurrent write lets
    # the non-blocking Uno firmware stop before the 69,000-step move finishes.
    if (

        actuator_command_active

        and controller_serial is not None

        and controller_serial.is_open

    ):

        try:

            controller_serial.write(b"ACTUATOR STOP\n")

            controller_serial.flush()

            _update_actuator_page_labels(

                "Emergency stop sent. Actuator position is now UNKNOWN."

            )

        except Exception as exc:

            _update_actuator_page_labels(f"ERROR sending stop: {exc}")

        return


    run_actuator_command("ACTUATOR STOP")


def linear_actuator_control_page():

    global actuator_position_var, actuator_status_var


    page, content, footer = make_page(

        "Linear Actuator",

        "Each UP or DOWN command moves exactly 69,000 steps."

    )


    actuator_position_var = ctk.StringVar()

    actuator_status_var = ctk.StringVar(

        value=(

            "No limit switches are installed. Confirm the actuator has enough "

            "travel before pressing UP or DOWN."

        )

    )

    _update_actuator_page_labels()


    ctk.CTkLabel(

        content,

        textvariable=actuator_position_var,

        font=("Arial", 22, "bold")

    ).pack(pady=(24, 8))


    ctk.CTkLabel(

        content,

        textvariable=actuator_status_var,

        font=("Arial", 14),

        text_color=WARNING,

        wraplength=680

    ).pack(pady=(0, 20))


    make_footer_button(

        content,

        text=f"MOVE UP — {LINEAR_ACTUATOR_TRAVEL_STEPS:,} STEPS",

        command=lambda: run_actuator_command(

            "ACTUATOR UP",

            response_type="motion",

            timeout=70.0

        ),

        width=330

    ).pack(pady=6)


    make_footer_button(

        content,

        text=f"MOVE DOWN — {LINEAR_ACTUATOR_TRAVEL_STEPS:,} STEPS",

        command=lambda: run_actuator_command(

            "ACTUATOR DOWN",

            response_type="motion",

            timeout=70.0

        ),

        width=330

    ).pack(pady=6)


    make_secondary_button(

        content,

        text="SET CURRENT AS UP (NO MOVEMENT)",

        command=lambda: run_actuator_command(

            "SET ACTUATOR UP",

            response_type="ok",

            timeout=2.0

        ),

        width=330

    ).pack(pady=6)


    make_secondary_button(

        content,

        text="CHECK CONNECTION / STATUS",

        command=lambda: run_actuator_command(

            "ACTUATOR STATUS",

            response_type="status",

            timeout=3.0

        ),

        width=330

    ).pack(pady=6)


    make_secondary_button(

        footer,

        text="BACK HOME",

        command=home,

        width=180

    ).pack(side="left", padx=6)


    make_danger_button(

        footer,

        text="EMERGENCY ACTUATOR STOP",

        command=emergency_actuator_stop,

        width=270

    ).pack(side="left", padx=6)


# ============================================================

# HOME PAGE

# ============================================================


def home():

    page, content, footer = make_page(

        "Compounding Doser",

        "Assign powders to slots, set a recipe, then start dispensing."

    )


    slot_frame = ctk.CTkScrollableFrame(

        content,

        fg_color="transparent",

        corner_radius=12

    )

    slot_frame.pack(fill="both", expand=True, padx=14, pady=14)


    for i in range(1, 9):

        name = slots[i]["name"]


        row = ctk.CTkFrame(

            slot_frame,

            fg_color=CARD_BG_2,

            corner_radius=14

        )

        row.pack(fill="x", pady=4)


        ctk.CTkLabel(

            row,

            text=f"Slot {i}",

            font=("Arial", 17, "bold"),

            width=90,

            anchor="w"

        ).pack(side="left", padx=(14, 4), pady=10)


        ctk.CTkLabel(

            row,

            text=name,

            font=("Arial", 16),

            text_color=TEXT_MUTED,

            anchor="w"

        ).pack(side="left", fill="x", expand=True, padx=4)


        ctk.CTkButton(

            row,

            text="Edit",

            width=82,

            height=34,

            command=lambda x=i: slot_page(x)

        ).pack(side="right", padx=10)


    make_footer_button(
        footer,
        text="CONTINUE",
        command=recipe_page,
        width=105
    ).pack(side="left", padx=4)

    make_footer_button(
        footer,
        text="MOVE DISK",
        command=disk_control_page,
        width=110
    ).pack(side="left", padx=4)

    make_footer_button(
        footer,
        text="ACTUATOR",
        command=linear_actuator_control_page,
        width=115
    ).pack(side="left", padx=4)

    make_secondary_button(
        footer,
        text="VIEW CSV",
        command=view_csv,
        width=95
    ).pack(side="left", padx=4)

    make_footer_button(
        footer,
        text="EXPORT CSV",
         command=export_csv,
        width=105
    ).pack(side="left", padx=4)

    add_clear_button(footer)



# ============================================================

# SLOT PAGE

# ============================================================


def slot_page(i):

    page, content, footer = make_page(

        f"Edit Slot {i}",

        "Choose which powder is loaded into this doser slot."

    )


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    ctk.CTkLabel(

        center,

        text=f"Current Slot {i} Powder",

        font=("Arial", 18, "bold")

    ).pack(pady=(0, 12))


    var = ctk.StringVar(value=slots[i]["name"])


    def save_powder(choice):

        slots[i]["name"] = choice


    ctk.CTkOptionMenu(

        center,

        values=POWDERS,

        variable=var,

        command=save_powder,

        width=330,

        height=46,

        font=("Arial", 16)

    ).pack(pady=10)


    if slots[i]["name"] in NON_FREE_FLOWING_POWDERS:

        mode_text = "This powder will use non-free-flowing mode."

    else:

        mode_text = "This powder will use free-flowing mode."


    ctk.CTkLabel(

        center,

        text=mode_text,

        font=("Arial", 14),

        text_color=TEXT_MUTED

    ).pack(pady=8)


    make_secondary_button(

        footer,

        text="BACK",

        command=home,

        width=180

    ).pack(side="left", padx=6)


    add_clear_button(footer)


# ============================================================

# RECIPE PAGE

# ============================================================


def recipe_page():

    page, content, footer = make_page(

        "Set Recipe",

        "Tap a powder row to enter the amount to dispense."

    )


    top_info = ctk.CTkFrame(content, fg_color="transparent")

    top_info.pack(fill="x", padx=14, pady=(12, 4))


    total_var = ctk.StringVar()


    def update_total():

        total = get_recipe_total()

        total_var.set(f"Total: {total:.3f} g")


    update_total()


    ctk.CTkLabel(

        top_info,

        textvariable=total_var,

        font=("Arial", 22, "bold")

    ).pack(side="left")


    ctk.CTkLabel(

        top_info,

        text=get_powder_type_label(),

        font=("Arial", 14),

        text_color=TEXT_MUTED

    ).pack(side="right")


    recipe_frame = ctk.CTkScrollableFrame(

        content,

        fg_color="transparent"

    )

    recipe_frame.pack(fill="both", expand=True, padx=14, pady=8)


    def set_weight(slot):

        def save(val):

            try:

                recipe[slot] = max(0.0, float(val))

                update_total()

                recipe_page()

            except:

                pass


        keyboard(save, "number")


    for i in range(1, 9):

        name = slots[i]["name"]

        amount = recipe[i]


        row = ctk.CTkFrame(

            recipe_frame,

            fg_color=CARD_BG_2,

            corner_radius=14

        )

        row.pack(fill="x", pady=4)


        powder_label = f"Slot {i}: {name}"


        ctk.CTkLabel(

            row,

            text=powder_label,

            font=("Arial", 15, "bold"),

            anchor="w"

        ).pack(side="left", padx=14, pady=10, fill="x", expand=True)


        ctk.CTkButton(

            row,

            text=f"{amount:.3f} g",

            width=120,

            height=36,

            command=lambda x=i: set_weight(x)

        ).pack(side="right", padx=10)


    make_footer_button(

        footer,

        text="START",

        command=start_motor,

        width=180

    ).pack(side="left", padx=6)


    make_secondary_button(

        footer,

        text="BACK HOME",

        command=home,

        width=180

    ).pack(side="left", padx=6)


    add_clear_button(footer)


# ============================================================

# MOTOR SCRIPT SELECTION

# ============================================================





# ============================================================

# MOTOR SCRIPT SELECTION

# ============================================================



def choose_motor_script(amount_to_dispense):

    """

    Uses the main motor controller.

    Powder behavior is passed separately.

    """

    return "motor_scale_control.py"



# ============================================================

# MOTOR OUTPUT PARSING

# ============================================================


def read_motor_output(process):

    try:

        for line in process.stdout:

            output_queue.put(line.strip())

    except:

        pass



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

            except:

                pass


        if remaining_match:

            try:

                remaining_to_dispense = max(0.0, float(remaining_match.group(1)))

            except:

                pass

        else:

            remaining_to_dispense = max(0.0, current_run_target - dispensed_this_run)


        update_progress_labels()


    if motor_process is not None:

        root.after(100, process_output_queue)



def update_progress_labels():

    if progress_var is not None:

        progress_var.set(f"Dispensed this run: {dispensed_this_run:.3f} g")


    if remaining_var is not None:

        remaining_var.set(f"Remaining: {remaining_to_dispense:.3f} g")


# ============================================================

# MOTOR PROCESS HELPERS

# ============================================================


class RecipeSequenceCancelled(RuntimeError):

    pass


def _check_recipe_cancelled():

    if recipe_cancel_event.is_set():

        raise RecipeSequenceCancelled("Recipe sequence was stopped by the user.")


def _recipe_status(message):

    recipe_result_queue.put(("status", message))


def recipe_motion_screen(message):

    global recipe_status_var


    page, content, footer = make_page(

        "Preparing Recipe",

        "The actuator stays UP while the clockwise disk indexes by its slot switch."

    )


    recipe_status_var = ctk.StringVar(value=message)


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    ctk.CTkLabel(

        center,

        text="AUTOMATIC POSITIONING",

        font=("Arial", 26, "bold")

    ).pack(pady=(0, 14))


    ctk.CTkLabel(

        center,

        textvariable=recipe_status_var,

        font=("Arial", 19),

        text_color=TEXT_MUTED,

        justify="center",

        wraplength=680

    ).pack(pady=8)


    make_danger_button(

        footer,

        text="FORCE STOP RECIPE",

        command=force_stop,

        width=280,

        height=54

    ).pack(side="left", padx=6)


def _prepare_recipe_item_worker(item):

    global actuator_position, disk_current_slot, disk_position_known


    try:

        _check_recipe_cancelled()


        if actuator_position == "UNKNOWN":

            raise RuntimeError(

                "Linear actuator position is UNKNOWN. Return it to the top "

                "and use SET CURRENT AS UP before restarting the recipe."

            )


        if actuator_position != "UP":

            _recipe_status(

                "Raising the linear actuator 69,000 steps before disk movement..."

            )

            _perform_actuator_command(

                "ACTUATOR UP",

                response_type="motion",

                timeout=70.0

            )

            actuator_position = "UP"

        else:

            # This opens the combined Uno and verifies its restored actuator state.
            status = _perform_actuator_command(

                "ACTUATOR STATUS",

                response_type="status",

                timeout=3.0

            )

            if "POSITION=UNKNOWN" in status:

                _perform_actuator_command(

                    "SET ACTUATOR UP",

                    response_type="ok",

                    timeout=2.0

                )

            elif "POSITION=UP" not in status:

                raise RuntimeError(

                    f"Uno did not confirm the actuator is UP: {status}"

                )


        _check_recipe_cancelled()


        if item is None:

            recipe_result_queue.put(("complete", None))

            return


        target_slot = item["slot"]

        _recipe_status(

            f"Actuator is UP. Moving disk to slot {target_slot}: "

            f"{item['name']}..."

        )

        disk_response = _perform_disk_command(

            f"DISK GOTO {target_slot}",

            response_type="motion",

            timeout=12.0

        )


        match = re.search(r"DONE DISK SLOT\s+(\d+)", disk_response)

        if not match or int(match.group(1)) != target_slot:

            raise RuntimeError(

                f"Disk did not confirm slot {target_slot}: {disk_response}"

            )


        disk_current_slot = target_slot

        disk_position_known = True


        _check_recipe_cancelled()


        _recipe_status(

            f"Disk is at slot {target_slot}. Lowering the actuator "

            "69,000 steps before dispensing..."

        )

        _perform_actuator_command(

            "ACTUATOR DOWN",

            response_type="motion",

            timeout=70.0

        )

        actuator_position = "DOWN"


        _check_recipe_cancelled()

        recipe_result_queue.put(("ready", item))


    except RecipeSequenceCancelled as exc:

        recipe_result_queue.put(("cancelled", str(exc)))

    except Exception as exc:

        recipe_result_queue.put(("error", str(exc)))


def process_recipe_result_queue():

    global recipe_run_active, remaining_to_dispense


    terminal_result = None


    while True:

        try:

            result_type, payload = recipe_result_queue.get_nowait()

        except queue.Empty:

            break


        if result_type == "status":

            if recipe_status_var is not None:

                recipe_status_var.set(payload)

            continue


        terminal_result = (result_type, payload)


    if terminal_result is None:

        if recipe_run_active and motor_process is None:

            root.after(100, process_recipe_result_queue)

        return


    result_type, payload = terminal_result


    if result_type == "ready" and recipe_run_active:

        item = payload

        remaining_to_dispense = item["remaining"]

        launch_motor(item["remaining"], item["name"])

        return


    if result_type == "complete" and recipe_run_active:

        recipe_run_active = False

        remaining_to_dispense = 0.0

        completed_screen()

        return


    if result_type == "cancelled" or recipe_cancel_event.is_set():

        return


    recipe_run_active = False

    error_screen(

        "Automatic recipe positioning stopped.\n\n"

        f"{payload}\n\n"

        "The disk will not move again until a new recipe is started."

    )


def start_recipe_preparation():

    if not recipe_run_active or recipe_cancel_event.is_set():

        return


    if recipe_run_index < len(active_run_items):

        item = active_run_items[recipe_run_index]

        message = (

            f"Preparing item {recipe_run_index + 1} of {len(active_run_items)}: "

            f"Slot {item['slot']} — {item['name']}"

        )

    else:

        item = None

        message = "All powders are dispensed. Returning the actuator to UP..."


    recipe_motion_screen(message)


    threading.Thread(

        target=_prepare_recipe_item_worker,

        args=(item,),

        daemon=True

    ).start()


    root.after(100, process_recipe_result_queue)


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


    # The app and dispensing subprocess share ONE Uno USB port. Close the app's

    # handle before launching the child. Opening the Uno resets its software

    # references; the child restores the known disk slot, and this app restores

    # disk + actuator references the next time it reconnects.

    close_controller_serial()


    child_environment = os.environ.copy()

    child_environment["ARDUINO_PORT"] = controller_port_in_use or ARDUINO_PORT

    if disk_position_known:

        child_environment["DISK_CURRENT_SLOT"] = str(disk_current_slot)

    else:

        child_environment.pop("DISK_CURRENT_SLOT", None)


    motor_process = subprocess.Popen(

        [

            sys.executable,

            "-u",

            script_path,

            str(current_run_target),

            powder_type

        ],

        stdout=subprocess.PIPE,

        stderr=subprocess.STDOUT,

            text=True,

            bufsize=1,

            env=child_environment

    )



    threading.Thread(

        target=read_motor_output,

        args=(motor_process,),

        daemon=True

    ).start()


    running_screen(script_name)

    process_output_queue()

    check_motor_process()



def start_motor():

    global original_target, remaining_to_dispense, active_run_items

    global recipe_run_active, recipe_run_index, recipe_total_dispensed

    global recipe_interrupted, stopped_by_user, current_run_id


    active_items = get_active_recipe_items()


    if disk_command_active:

        error_screen(

            "Wait for the current disk movement to finish before dispensing."

        )

        return


    if actuator_command_active:

        error_screen(

            "Wait for the linear actuator movement to finish before dispensing."

        )

        return


    if not active_items:

        error_screen(
            "No powder amount entered.\n"
            "Please enter one powder amount before starting."
        )

        return


    empty_items = [item for item in active_items if item["name"] == "EMPTY"]

    if empty_items:

        error_screen(
            "A recipe amount is assigned to an EMPTY slot.\n"
            "Choose a powder for every active recipe slot before starting."
        )

        return


    if not disk_position_known:

        error_screen(

            "The disk's starting position is unknown.\n\n"

            "Open MOVE DISK, press RELEASE, physically align slot 1 so the "

            "limit switch is OPEN in its indent, then press SET CURRENT AS "

            "SLOT 1. After that one-time setup, START "

            "will move through the complete recipe automatically."

        )

        return


    if actuator_position == "UNKNOWN":

        error_screen(

            "The linear actuator position is unknown.\n\n"

            "Return it to the physical top position and use the ACTUATOR "

            "page to SET CURRENT AS UP before starting."

        )

        return


    active_run_items = [

        {

            **item,

            "dispensed": 0.0,

            "remaining": item["amount"],

            "status": "PENDING"

        }

        for item in active_items

    ]


    original_target = sum(item["amount"] for item in active_run_items)

    remaining_to_dispense = active_run_items[0]["amount"]

    recipe_run_index = 0

    recipe_total_dispensed = 0.0

    recipe_run_active = True

    recipe_interrupted = False

    stopped_by_user = False

    current_run_id = ""

    recipe_cancel_event.clear()

    actuator_cancel_event.clear()


    while not recipe_result_queue.empty():

        try:

            recipe_result_queue.get_nowait()

        except queue.Empty:

            break


    start_recipe_preparation()



def check_motor_process():

    global motor_process

    global recipe_run_active, recipe_run_index, recipe_total_dispensed


    if motor_process is None:

        return


    return_code = motor_process.poll()


    if return_code is None:

        root.after(500, check_motor_process)

        return


    process_output_queue()


    motor_process = None


    if stopped_by_user:

        if recipe_run_index < len(active_run_items):

            item = active_run_items[recipe_run_index]

            item["dispensed"] += dispensed_this_run

            item["remaining"] = remaining_to_dispense

            item["status"] = "STOPPED"

        stopped_screen()

    elif return_code == 0:

        if recipe_run_active and recipe_run_index < len(active_run_items):

            item = active_run_items[recipe_run_index]

            item["dispensed"] += dispensed_this_run

            item["remaining"] = 0.0

            item["status"] = "COMPLETED"

            recipe_total_dispensed = sum(

                run_item["dispensed"]

                for run_item in active_run_items

            )

            recipe_run_index += 1

            start_recipe_preparation()

        else:

            completed_screen()

    else:

        recipe_run_active = False

        if recipe_run_index < len(active_run_items):

            item = active_run_items[recipe_run_index]

            item["dispensed"] += dispensed_this_run

            item["remaining"] = remaining_to_dispense

            item["status"] = "ERROR"

        error_screen(

            f"Dispensing program stopped unexpectedly.\n"

            f"Return code: {return_code}\n\n"

            f"Remaining amount was estimated as {remaining_to_dispense:.3f} g."

        )



def force_stop():
    global stopped_by_user
    global recipe_run_active, recipe_interrupted
    global actuator_position, disk_position_known

    stopped_by_user = True
    recipe_interrupted = recipe_run_active or recipe_interrupted
    recipe_run_active = False
    recipe_cancel_event.set()
    actuator_cancel_event.set()

    motor_was_running = motor_process is not None and motor_process.poll() is None

    # If the app currently owns the Uno (positioning/manual control), one STOP
    # ALL command stops auger + disk + actuator. During dispensing the child
    # process owns the port, so SIGINT below makes it send STOP ALL itself.
    if (
        not motor_was_running
        and controller_serial is not None
        and controller_serial.is_open
    ):
        try:
            controller_serial.write(b"STOP ALL\n")
            controller_serial.flush()
        except Exception:
            pass

    actuator_position = "UNKNOWN"
    disk_position_known = False

    if motor_was_running:
        try:
            motor_process.send_signal(signal.SIGINT)
        except Exception:
            try:
                motor_process.terminate()
            except Exception:
                pass

    stopping_screen()
    root.after(1500, force_kill_if_needed)

    if not motor_was_running:
        root.after(750, stopped_screen)


def force_kill_if_needed():

    if motor_process is not None and motor_process.poll() is None:

        try:

            motor_process.kill()

        except:

            pass



def resume_motor():

    """

    Continues only the missing amount.

    """

    if remaining_to_dispense <= 0.001:

        completed_screen()

        return


    launch_motor(remaining_to_dispense)


# ============================================================

# RUNNING SCREEN

# ============================================================


def running_screen(script_name):

    global progress_var, remaining_var, script_var


    page, content, footer = make_page(

        "Running Recipe",

        "Dispensing is active. Use FORCE STOP immediately if anything looks unsafe."

    )


    progress_var = ctk.StringVar(value=f"Dispensed this run: {dispensed_this_run:.3f} g")

    remaining_var = ctk.StringVar(value=f"Remaining: {remaining_to_dispense:.3f} g")

    script_var = ctk.StringVar(value=f"Mode: {script_name}")


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    current_item = (

        active_run_items[recipe_run_index]

        if recipe_run_index < len(active_run_items)

        else None

    )


    ctk.CTkLabel(

        center,

        text="DISPENSING IN PROGRESS",

        font=("Arial", 24, "bold")

    ).pack(pady=(0, 10))


    if current_item is not None:

        ctk.CTkLabel(

            center,

            text=(

                f"Item {recipe_run_index + 1} of {len(active_run_items)} — "

                f"Slot {current_item['slot']}: {current_item['name']}"

            ),

            font=("Arial", 18, "bold")

        ).pack(pady=4)


    ctk.CTkLabel(

        center,

        text=f"Current run target: {current_run_target:.3f} g",

        font=("Arial", 20)

    ).pack(pady=4)


    ctk.CTkLabel(

        center,

        textvariable=script_var,

        font=("Arial", 15),

        text_color=TEXT_MUTED

    ).pack(pady=4)


    progress_card = ctk.CTkFrame(

        center,

        fg_color=CARD_BG_2,

        corner_radius=14

    )

    progress_card.pack(pady=14, padx=20)


    ctk.CTkLabel(

        progress_card,

        textvariable=progress_var,

        font=("Arial", 20)

    ).pack(padx=28, pady=(16, 6))


    ctk.CTkLabel(

        progress_card,

        textvariable=remaining_var,

        font=("Arial", 20)

    ).pack(padx=28, pady=(6, 16))


    make_danger_button(

        footer,

        text="FORCE STOP",

        command=force_stop,

        width=260,

        height=54

    ).pack(side="left", padx=6)


# ============================================================

# STOPPING SCREEN

# ============================================================


def stopping_screen():

    page, content, footer = make_page(

        "Stopping",

        "Motor shutdown signal has been sent."

    )


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    ctk.CTkLabel(

        center,

        text="STOPPING...",

        font=("Arial", 30, "bold"),

        text_color=WARNING

    ).pack(pady=12)


    ctk.CTkLabel(

        center,

        text="Wait for the system to fully stop before touching the doser.",

        font=("Arial", 18),

        text_color=TEXT_MUTED,

        justify="center"

    ).pack(pady=10)


# ============================================================

# STOPPED SCREEN

# ============================================================


def stopped_screen():

    page, content, footer = make_page(

        "Dispensing Stopped",

        "The run was force stopped before completion."

    )


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    ctk.CTkLabel(

        center,

        text=f"Remaining amount: {remaining_to_dispense:.3f} g",

        font=("Arial", 24, "bold")

    ).pack(pady=10)


    ctk.CTkLabel(

        center,

        text=(

            "Check the doser, scale, container, and powder path "

            "before continuing."

        ),

        font=("Arial", 17),

        text_color=TEXT_MUTED,

        justify="center",

        wraplength=650

    ).pack(pady=12)


    if not recipe_interrupted:

        make_footer_button(

            footer,

            text=f"CONTINUE {remaining_to_dispense:.3f} g",

            command=resume_motor,

            width=260

        ).pack(side="left", padx=6)


    make_secondary_button(

        footer,

        text="EXIT TO HOME",

        command=home,

        width=190

    ).pack(side="left", padx=6)


# ============================================================

# COMPLETED SCREEN

# ============================================================


def completed_screen():

    export_run_to_csv("COMPLETED")


    page, content, footer = make_page(

        "Completed",

        "Dispensing finished. Wipe down contact surfaces before the next run."

    )



    top = ctk.CTkFrame(content, fg_color="transparent")

    top.pack(fill="x", padx=18, pady=(16, 8))


    ctk.CTkLabel(

        top,

        text="COMPLETED",

        font=("Arial", 30, "bold"),

        text_color=SUCCESS

    ).pack(anchor="w")


    ctk.CTkLabel(

        top,

        text=f"Total target: {original_target:.3f} g",

        font=("Arial", 20)

    ).pack(anchor="w", pady=(6, 0))


    ctk.CTkLabel(

        top,

        text=(

            "Total measured dispense: "

            f"{sum(item.get('dispensed', 0.0) for item in active_run_items):.3f} g"

        ),

        font=("Arial", 17)

    ).pack(anchor="w", pady=(2, 0))


    if active_run_script_name:

        ctk.CTkLabel(

            top,

            text=f"Completed using: {active_run_script_name}",

            font=("Arial", 14),

            text_color=TEXT_MUTED

        ).pack(anchor="w", pady=(2, 0))


    summary_frame = ctk.CTkFrame(

        content,

        fg_color=CARD_BG_2,

        corner_radius=14

    )

    summary_frame.pack(fill="both", expand=True, padx=18, pady=8)


    ctk.CTkLabel(

        summary_frame,

        text="Completed Powder Summary",

        font=("Arial", 18, "bold")

    ).pack(anchor="w", padx=16, pady=(12, 6))


    if active_run_items:

        for item in active_run_items:

            row = ctk.CTkFrame(summary_frame, fg_color="transparent")

            row.pack(fill="x", padx=16, pady=2)


            ctk.CTkLabel(

                row,

                text=f"Slot {item['slot']}: {item['name']}",

                font=("Arial", 15),

                anchor="w"

            ).pack(side="left", fill="x", expand=True)


            ctk.CTkLabel(

                row,

                text=(

                    f"Target {item['amount']:.3f} g  |  "

                    f"Measured {item.get('dispensed', 0.0):.3f} g"

                ),

                font=("Arial", 15, "bold"),

                anchor="e"

            ).pack(side="right")

    else:

        ctk.CTkLabel(

            summary_frame,

            text="No powder summary was recorded for this run.",

            font=("Arial", 15),

            text_color=TEXT_MUTED

        ).pack(anchor="w", padx=16, pady=8)


    ctk.CTkLabel(

        content,

        text=(

            "Reminder: wipe down the dispensing area, scale surface, chute area, "

            "and all contact surfaces before starting another run."

        ),

        font=("Arial", 15),

        text_color=TEXT_MUTED,

        justify="center",

        wraplength=700

    ).pack(padx=18, pady=(4, 12))


    make_footer_button(

        footer,

        text="BACK TO HOME",

        command=home,

        width=150

    ).pack(side="left", padx=4)


    make_secondary_button(

        footer,

        text="VIEW CSV",

        command=view_csv,

        width=150

    ).pack(side="left", padx=4)


    make_footer_button(

        footer,

        text="EXPORT CSV",

        command=export_csv,

        width=150

    ).pack(side="left", padx=4)


    make_danger_button(

        footer,

        text="CLEAR ALL + HOME",

        command=clear_all_data,

        width=170

    ).pack(side="left", padx=4)




# ============================================================

# ERROR SCREEN

# ============================================================


def error_screen(message):

    page, content, footer = make_page(

        "Error",

        "Something needs attention before continuing."

    )


    center = ctk.CTkFrame(content, fg_color="transparent")

    center.pack(expand=True)


    ctk.CTkLabel(

        center,

        text="ERROR",

        font=("Arial", 30, "bold"),

        text_color=DANGER

    ).pack(pady=10)


    ctk.CTkLabel(

        center,

        text=message,

        font=("Arial", 18),

        justify="center",

        wraplength=700

    ).pack(pady=12)


    make_secondary_button(

        footer,

        text="BACK TO RECIPE",

        command=recipe_page,

        width=220

    ).pack(side="left", padx=6)


    make_secondary_button(

        footer,

        text="BACK TO HOME",

        command=home,

        width=220

    ).pack(side="left", padx=6)


def csv_viewer_page():


    page, content, footer = make_page(

        "Dispensing History",

        "Previous dispensing runs"

    )


    table_frame = ctk.CTkScrollableFrame(

        content,

        fg_color="transparent"

    )

    table_frame.pack(

        fill="both",

        expand=True,

        padx=10,

        pady=10

    )


    try:

        with open(CSV_FILE, "r") as f:

            reader = csv.reader(f)

            rows = list(reader)


    except Exception as e:

        ctk.CTkLabel(

            table_frame,

            text=f"Could not load CSV:\n{e}",

            font=("Arial", 18)

        ).pack(pady=20)


        return



    if not rows:

        ctk.CTkLabel(

            table_frame,

            text="No dispensing history yet.",

            font=("Arial", 18)

        ).pack(pady=20)


        return



    for row_index, row in enumerate(rows):


        row_frame = ctk.CTkFrame(

            table_frame,

            fg_color=CARD_BG_2,

            corner_radius=8

        )


        row_frame.pack(

            fill="x",

            pady=2

        )



        for col_index, value in enumerate(row):


            label = ctk.CTkLabel(

                row_frame,

                text=value,

                font=(

                    "Arial",

                    12,

                    "bold" if row_index == 0 else "normal"

                ),

                width=100,

                anchor="w"

            )


            label.pack(

                side="left",

                padx=4,

                pady=5

            )



    make_secondary_button(

        footer,

        text="BACK",

        command=completed_screen,

        width=200

    ).pack(

        side="left",

        padx=6

    )


# ============================================================

# START APP

# ============================================================



home()

root.mainloop()