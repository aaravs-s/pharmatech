# R10 Build the touchscreen workflow and hand targets to a separate controller process

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 2 · Previous topics J15, J16

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Let the user assign powders and request a mass without entering the motor-control code, while keeping the interface responsive.

## Design process

I added a touchscreen interface so a user could choose a powder and enter the desired mass without editing the control program. The BOM identifies a seven-inch DSI touchscreen, and the milestone notes describe connecting it to a Raspberry Pi 4.

The interface was designed with the future multi-hopper machine in mind. Even while I was using one physical hopper, the workflow included assigning a powder to a slot and entering a quantity. That made the single-doser test a first version of the interaction the full machine would need later.

The operating procedure gives a more concrete sequence: edit slot 1, select the powder, load the hopper, tare the scale, enter a mass, save, and start. Keeping that sequence visible on the device reduced the amount of setup that depended on remembering code details. The journal should show the actual screens for this revision, including how invalid values, cancellation, and the displayed result were handled if those behaviors were implemented.

I separated the visible app from the motor-and-scale controller. The app collected the requested powder and mass, then called a second program responsible for reading the scale and driving the motor. This let the interface remain focused on the user's recipe while the controller handled the dispensing behavior.

The important information crossing that boundary was the target mass and the powder selection or profile. Inside the controller, the measured mass had to be interpreted consistently: a tare or starting baseline establishes what counts as newly dispensed powder, and the remaining mass is the target minus the amount added. The source notes explain the two-program arrangement but do not include the exact process arguments or final source code.

This separation also made stopping behavior important. Closing or finishing the controller must leave the motor in the intended state, and the interface must know whether the operation completed, failed, or was interrupted. I would include the real mechanism used to communicate those states rather than assuming a particular subprocess or serial protocol from the high-level description.

## Construction and implementation detail

The interface and mass controller have different responsibilities. The interface gathers a powder name and requested grams, displays progress, and exposes stop controls. The controller owns scale feedback and auger phase decisions. M2 notes describe that split explicitly. Keeping it visible in the journal explains why there are two Python programs rather than one screenshot of a touchscreen.

The later app archive gives a detailed implementation of that design: CustomTkinter creates a fullscreen 800 by 480 interface, maintains slot and recipe data separately, and includes an on-screen keyboard. The powder list contains EMPTY plus the eight tested household powders. A recipe item contains the slot, powder name, and requested amount. This is later implementation evidence, not a claim that all recipe features were present in the first M2 interface.

The launch function chooses motor_scale_control.py, builds its path relative to the app file, and starts it with sys.executable, unbuffered output, a target argument, and a powder-name argument. Standard error is merged into standard output. A background reader places each received line into a queue, and the Tk event loop checks that queue through after() callbacks. That avoids blocking the touchscreen while serial feedback and motor control continue.

The words 'Dispensed:' and 'Remaining:' are an interface contract. The app uses regular expressions to extract numbers following those labels and updates progress text. The controller explicitly retains those labels in its output. Changing a label in one program without the matching parser change could make the interface appear frozen even while the auger continues, so the journals need to identify both ends of this connection.

A complete record should show the input page, the validated target, the command/process arguments, live progress, and the completion or error page for the same trial. The final app also checks for empty recipe slots, unknown disk position, and active motion before starting. Those later safeguards should be introduced when they were added rather than retrospectively assigned to the first UI.

The files establish how the process handoff works, but they do not record a screenshot of each original editing stage. I leave targeted placeholders for the early selection page and first working progress parser, alongside the actual source excerpts. This makes the missing evidence precise and avoids treating a final touchscreen photograph as proof of the entire UI development process.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

## Result and handoff

The app/controller separation became a concrete subprocess and output-parser interface. Later recipe, serial-discovery, and interlock code is tracked as subsequent development.

## Complete from your records

Supply the first UI version, target-validation behavior, example launch arguments/output, and an actual start/progress/stop/completion screen sequence.

[IMAGE PLACEHOLDER: Early powder/target page during implementation and its first successful controller launch.]

[IMAGE PLACEHOLDER: Progress parser before/after edit, then a live running page showing output from the same trial.]

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
