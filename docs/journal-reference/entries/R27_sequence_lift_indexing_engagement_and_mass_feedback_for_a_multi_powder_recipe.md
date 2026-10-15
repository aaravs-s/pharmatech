# R27 Sequence lift, indexing, engagement, and mass feedback for a multi-powder recipe

> **AI-assisted reference draft — not a submitted work log.** This reconstruction is for writing your own journal from your actual work. Work dates, active hours, missing measurements, and test claims must be completed from your records. Archived CAD screenshots were captured retrospectively on October 13, 2026; they are not original screenshots from the design session.


Milestone 4 · Previous topics J40

Work date: [your actual date]
Active work time: [your actual hours; group/split by real sessions]

## Objective

Combine individually working mechanisms into an ordered recipe that advances only after each action completes.

## Design process

I extended the single-powder workflow toward selecting several ingredients in one run. The interface needed to know which powder was in each hopper and the requested amount for each ingredient, then coordinate positioning and dispensing.

Earlier project discussion describes the intended sequence as raising the actuator, rotating to the selected slot, lowering the drive, and launching the motor-and-scale controller. That is the structure to compare with the final program. For a multi-ingredient recipe, the mass measurement also needs a clear baseline or cumulative-target convention so powder already in the receiving container is not counted as a new ingredient.

This entry should include the actual recipe demonstration rather than treating the presence of eight slots as proof of autonomous compounding. The source notes establish the integration objective and mechanical arrangement, but do not give a complete ingredient-by-ingredient final test record. I need to add the real targets, final increments, and behavior when a step is interrupted.

## Construction and implementation detail

The later app builds active_run_items from slots with a positive requested amount, preserving each slot's powder name and target. It initializes per-item dispensed, remaining, and status values, computes the total recipe target, clears cancellation events, and begins preparing the first item. That is the data model behind the multi-powder workflow.

The preparation worker first checks cancellation and actuator state. If the actuator is UNKNOWN, it refuses to continue. If it is not UP, it sends ACTUATOR UP and waits for a motion response with a 70 s timeout. If it is already UP, it checks status and handles the source's declared reference procedure. Only then does it request DISK GOTO for the next item.

Disk motion has a 12 s timeout in the recipe worker. The returned line must contain DONE DISK SLOT with the requested slot number. Once that is confirmed, the app records the slot, checks cancellation again, sends ACTUATOR DOWN, waits for completion, and queues a ready result. The main UI then launches mass dispensing for the item. This is an explicit raise/index/lower/feed chain with completion checks between actions.

The actuator is controlled separately from the Uno, so STOP ALL on the Uno cannot by itself stop that mechanism. The app's force-stop route also sends an actuator stop and marks both actuator and disk state unknown. Recipe cancellation is checked between the stages. The journals should show these separate stop paths rather than calling one command a universal machine emergency stop.

After all recipe items have dispensed, preparation is called with no next item; the worker raises the actuator and queues completion. The app exports per-item results to CSV, including target, actual mass, error, remaining amount, and status. Those fields can document a real integrated trial, but their presence in source code does not prove that such a trial occurred successfully.

The key missing reproduction evidence is the paired actuator firmware and final disk firmware, plus a complete recipe run showing command/response order and final masses. The available app contains switch-based wording, while the recovered disk firmware uses step counts. I leave that compatibility issue explicit so the reader does not copy mismatched files and assume the machine will index correctly.

## Archived source excerpts

Exact recovered source text; not original editing-session screenshots.

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

## Image sequence

![Physical multi-doser assembly photograph included in M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_2.jpg)

Physical multi-doser assembly photograph included in M4.

![Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/cad_main_assembly.jpg)

Current Main workspace SuperStructureAssem. Only one hopper is visible in this assembly view. CAD includes mate or linked-reference warnings; the image is not proof of a fully populated or validated mechanism.

![Full frame, carousel, drive, and screen CAD from M4.](https://raw.githubusercontent.com/aaravs-s/pharmatech/main/docs/journal-reference/assets/m4_4.jpg)

Full frame, carousel, drive, and screen CAD from M4.

## Result and handoff

The app contains an ordered recipe worker with completion checks and cancellation handling. A final matching controller set and an end-to-end measured recipe run still need to be identified.

## Complete from your records

Match app, motor/scale, Uno, and XIAO revisions; add complete serial trace and per-ingredient measured masses for a real recipe.

[IMAGE PLACEHOLDER: Recipe worker during implementation, raise/index/lower completion responses, and the final completed ingredient summary.]

[IMAGE PLACEHOLDER: Uncut physical recipe video showing each mechanism transition and the CSV from the same run.]

## Sources

- [M4: Multi-doser compounding](https://docs.google.com/document/d/1j8LOm5HRvMM-VXsni-38hi5GsA0yg5A1A_3LY9DY1Is/edit)
- [Existing Forge journals](https://forge.hackclub.com/projects/763)


[All reference drafts](../README.md) · [Image URLs](../IMAGE_URLS.md) · [Project journal](../../../JOURNAL.md)
