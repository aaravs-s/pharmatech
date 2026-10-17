# J10 Making the screen talk to the controller

*Milestone 2 | Retrospective build notes*

I wanted the doser to be operable without changing a number in the Python file for every run. The Pi's seven-inch touchscreen became the place to choose the powder and enter the requested mass. Even with one working hopper, I was already thinking in slots because the carousel would need that later.

I split the app from the motor-and-scale controller. The screen handled the request; the other program dealt with the balance and feeding phases. That sounded tidy, but it also meant the two programs needed to agree on what they sent each other.

![Single-doser test arrangement with scale, screen, and controller wiring.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m2_4.jpg)

Single-doser test arrangement with scale, screen, and controller wiring.

The later implementation launches the controller as a subprocess and reads its output in the background. I didn't want waiting on serial data to freeze the interface. The progress labels also mattered more than they looked like they should: the app searches for 'Dispensed:' and 'Remaining:', so changing that text in only one file would break the display connection.

The early SOP is the simpler workflow: select slot 1, choose and load powder, tare, enter mass, save, start. The full recipe checks in the later app came afterward. I'm keeping those stages distinct instead of making the first touchscreen version sound like it already did everything.

## The handoff between programs

The later app archive gives a detailed implementation of that design: CustomTkinter creates a fullscreen 800 by 480 interface, maintains slot and recipe data separately, and includes an on-screen keyboard. The powder list contains EMPTY plus the eight tested household powders. A recipe item contains the slot, powder name, and requested amount. This is later implementation evidence, not a claim that all recipe features were present in the first M2 interface.

The launch function chooses motor_scale_control.py, builds its path relative to the app file, and starts it with sys.executable, unbuffered output, a target argument, and a powder-name argument. Standard error is merged into standard output. A background reader places each received line into a queue, and the Tk event loop checks that queue through after() callbacks. That avoids blocking the touchscreen while serial feedback and motor control continue.

The output labels 'Dispensed:' and 'Remaining:' form a contract between the programs. The app extracts their following numbers with regular expressions, and the controller retains those labels in its output. Changing one side alone could leave the display stale while feeding continued, making the text protocol part of the implemented interface.

## Code for this revision

Exact archived source excerpts. The file labels identify their revisions.

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

The useful result was a request going from the screen to a separate controller and progress coming back. Still two programs to keep in agreement, though. Once positioning was added, that handoff would carry state and device choices as well as the powder and target.

<details>
<summary>Notes added while reconstructing this entry</summary>

The interface gathers the powder and requested grams, displays progress, and exposes stop controls. The separate controller owns scale feedback and auger phase decisions. This division let the application describe the user's request while the controller translated measured mass into motion.

The later app adds startup checks for empty recipe slots, unknown disk position, and active motion. Those safeguards belong to the later integrated source. The initial single-doser workflow and the complete recipe app share the process boundary, but they aren't presented as one unchanged version.

The source excerpts preserve the launch arguments and progress-parsing mechanism even where original development screenshots are unavailable. They explain how a target entered in the interface becomes a controller process and how its reported progress returns to the screen.

</details>

## Sources

- [M2: DOSER + SCALE CLOSED LOOP](https://docs.google.com/document/d/1T77pfLAAVP4tJ4OaOJhaz1ho2cAGb-1LFiVUrzH-hzI/edit)
- [Standard Operating Procedure: Safely Utilizing and Operating PharmaTech Rx's Doser](https://docs.google.com/document/d/1p1OGP37uR5EISkR5pwSQ_23Vjzx4Qd3G_bUwq5q5h0U/edit)
- [PharmaTech Bill of Materials](https://docs.google.com/spreadsheets/d/1ZitIb3FPBRPiebtTJnv18M2zcrYkR5fdOwQJR3Rg8Lo/edit)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R10_build_the_touchscreen_workflow_and_hand_targets_to_a_separate_controller_process.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
