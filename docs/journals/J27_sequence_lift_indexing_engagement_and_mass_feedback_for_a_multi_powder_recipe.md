# J27 Sequence lift, indexing, engagement, and mass feedback for a multi-powder recipe

*Milestone 4 | Personal retrospective journal*

## Design and iteration

I extended the application from a single target into a sequence of selected ingredients. Each active recipe item needed a slot, a powder name, and its own requested mass. The app then had to coordinate positioning before handing that item to the mass controller.

The sequence was raise, index, lower, and dispense. I made the transitions depend on state and completion responses rather than assuming each mechanism finished immediately. The controller for the actuator was separate from the Uno, so cancellation also had to reach more than one device.

A new ingredient used a starting mass reference so earlier ingredients in the receiving container were not counted as newly added powder. The later app also retained per-item result fields for CSV output. That provides a useful structure for integrated trials, but the available record does not include a complete measured recipe series tied to one confirmed final app-and-firmware configuration.

## Technical detail

The later app builds active_run_items from slots with a positive requested amount, preserving each slot's powder name and target. It initializes per-item dispensed, remaining, and status values, computes the total recipe target, clears cancellation events, and begins preparing the first item. That is the data model behind the multi-powder workflow.

The preparation worker first checks cancellation and actuator state. If the actuator is UNKNOWN, it refuses to continue. If it is not UP, it sends ACTUATOR UP and waits for a motion response with a 70 s timeout. If it is already UP, it checks status and handles the source's declared reference procedure. Only then does it request DISK GOTO for the next item.

Disk motion has a 12 s timeout in the recipe worker. The returned line must contain DONE DISK SLOT with the requested slot number. Once that is confirmed, the app records the slot, checks cancellation again, sends ACTUATOR DOWN, waits for completion, and queues a ready result. The main UI then launches mass dispensing for the item. This is an explicit raise/index/lower/feed chain with completion checks between actions.

The actuator has a separate controller, so Uno STOP ALL does not stop every moving mechanism by itself. The app's force-stop route also sends an actuator stop and marks actuator and disk state unknown. Cancellation checks between stages prevent a canceled preparation sequence from proceeding through the remaining actions on its old assumptions.

After all recipe items have dispensed, preparation is called with no next item; the worker raises the actuator and queues completion. The app exports per-item results to CSV, including target, actual mass, error, remaining amount, and status. Those fields can document a real integrated trial, but their presence in source code does not prove that such a trial occurred successfully.

The final paired actuator firmware, disk firmware, and measured recipe transcript are not identified in the available archive. In particular, switch-based app wording differs from the recovered step-count disk code. The state and command flow above describe the saved implementation without asserting that an arbitrary combination of those files is a validated final build.

## Archived implementation

Exact archived source excerpts. The file labels identify their revisions.

### app_later.py · lines 959–997

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def _prepare_recipe_item_worker(item):
    global actuator_position, disk_current_slot, disk_position_known
    try:
        _check_recipe_cancelled()
        if actuator_position == "UNKNOWN":
            raise RuntimeError("Linear actuator position is UNKNOWN. Return it to the top "
                               "and use SET CURRENT AS UP before restarting the recipe.")
        if actuator_position != "UP":
            _recipe_status("Raising the linear actuator 69,000 steps before disk movement...")
            _perform_actuator_command("ACTUATOR UP", response_type="motion", timeout=70.0)
            actuator_position = "UP"
        else:
            status = _perform_actuator_command("ACTUATOR STATUS", response_type="status", timeout=3.0)
            if "POSITION=UNKNOWN" in status:
                _perform_actuator_command("SET ACTUATOR UP", response_type="ok", timeout=2.0)
            elif "POSITION=UP" not in status:
                raise RuntimeError(f"XIAO did not confirm the actuator is UP: {status}")
        _check_recipe_cancelled()
        if item is None:
            recipe_result_queue.put(("complete", None))
            return
        target_slot = item["slot"]
        _recipe_status(f"Actuator is UP. Moving disk to slot {target_slot}: {item['name']}...")
        disk_response = _perform_disk_command(f"DISK GOTO {target_slot}", response_type="motion", timeout=12.0)
        match = re.search(r"DONE DISK SLOT\s+(\d+)", disk_response)
        if not match or int(match.group(1)) != target_slot:
            raise RuntimeError(f"Disk did not confirm slot {target_slot}: {disk_response}")
        disk_current_slot = target_slot
        disk_position_known = True
        _check_recipe_cancelled()
        _recipe_status(f"Disk is at slot {target_slot}. Lowering the actuator 69,000 steps before dispensing...")
        _perform_actuator_command("ACTUATOR DOWN", response_type="motion", timeout=70.0)
        actuator_position = "DOWN"
        _check_recipe_cancelled()
        recipe_result_queue.put(("ready", item))
    except RecipeSequenceCancelled as exc:
        recipe_result_queue.put(("cancelled", str(exc)))
    except Exception as exc:
        recipe_result_queue.put(("error", str(exc)))
```

### app_later.py · lines 1035–1047

Recovered full later Library app; contains automatic recipes, serial discovery, and switch-indexing wording.

```python
def start_recipe_preparation():
    if not recipe_run_active or recipe_cancel_event.is_set():
        return
    if recipe_run_index < len(active_run_items):
        item = active_run_items[recipe_run_index]
        message = (f"Preparing item {recipe_run_index + 1} of {len(active_run_items)}: "
                   f"Slot {item['slot']} — {item['name']}")
    else:
        item = None
        message = "All powders are dispensed. Returning the actuator to UP..."
    recipe_motion_screen(message)
    threading.Thread(target=_prepare_recipe_item_worker, args=(item,), daemon=True).start()
    root.after(100, process_recipe_result_queue)
```

## Process images

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Outcome and reflection

The application encoded the complete preparation sequence and separated item results from recipe state. That was a substantial step beyond putting eight slots on a screen. The remaining verification boundary was the installed combination of actuator firmware, disk firmware, and app, together with a measured multi-ingredient run; the existing single-powder results cannot substitute for that evidence.

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)

[Corresponding reference and evidence gaps](https://github.com/aaravs-s/pharmatech/blob/main/docs/journal-reference/entries/R27_sequence_lift_indexing_engagement_and_mass_feedback_for_a_multi_powder_recipe.md)

CAD construction captures are retrospective inspections of saved models, captured on October 13, 2026. They are not contemporaneous design-session screenshots.

[Journal collection](README.md) | [Original references](../journal-reference/README.md) | [Project journal](../../JOURNAL.md)
