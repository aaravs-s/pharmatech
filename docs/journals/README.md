# Pill Compounder: Finished Journal Collection

These 33 finished narratives describe the documented design and development of my powder-compounding prototype. Each follows the decisions, failures, changes, and outcomes of a design topic, with technical detail, archived code excerpts, process images, and sources.

This is an AI-assisted retrospective collection for personal documentation, prepared from the existing reference drafts. It is not a Forge submission or a record of verified work sessions. Dates and active hours have not been assigned. A finished narrative does not imply that the prototype met every design target: unresolved performance and configuration limits remain stated in the relevant entries.

The original reference drafts, prompts, and missing-image lists remain available separately. These finished journals contain no fill-in fields or missing-image boxes. Images use the existing public GitHub raw URLs. CAD construction captures were made retrospectively from archived models on October 13, 2026; individual captions identify their saved versions where known.

- [Read all journals in one document](ALL_JOURNALS.md)
- [Original reference collection](../journal-reference/README.md)
- [Image gallery](../journal-reference/GALLERY.md)
- [Copyable image URLs](../journal-reference/IMAGE_URLS.md)
- [Underlying evidence and version notes](../journal-reference/EVIDENCE.md)
- [Project journal](../../JOURNAL.md)

## Individual journals

| Journal | Milestone | Topic |
| --- | --- | --- |
| J01 | 1 | [Define the requirements and develop the shared eight-hopper architecture](J01_define_the_requirements_and_develop_the_shared_eight_hopper_architecture.md) |
| J02 | 1 | [Construct the first hopper, adapter, and bottom-feeder CAD](J02_construct_the_first_hopper_adapter_and_bottom_feeder_cad.md) |
| J03 | 1 | [Build the auger from a helix and flight profile, then obtain a usable print](J03_build_the_auger_from_a_helix_and_flight_profile_then_obtain_a_usable_print.md) |
| J04 | 1 | [Test the removable threaded hopper and replace it with a short locking interface](J04_test_the_removable_threaded_hopper_and_replace_it_with_a_short_locking_interface.md) |
| J05 | 1 | [Simplify the powder path and reduce sugar leaking during loading](J05_simplify_the_powder_path_and_reduce_sugar_leaking_during_loading.md) |
| J06 | 1 | [Diagnose cornstarch jamming and the first agitator's incomplete coverage](J06_diagnose_cornstarch_jamming_and_the_first_agitator_s_incomplete_coverage.md) |
| J07 | 1 | [Model the two-arm agitator and compare uniform and tapered-flight concepts](J07_model_the_two_arm_agitator_and_compare_uniform_and_tapered_flight_concepts.md) |
| J08 | 2 | [Wire the first NEMA 17 and TMC2209 drive and establish controlled motion](J08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md) |
| J09 | 2 | [Read serial scale data and establish the baseline mass for each dispense](J09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md) |
| J10 | 2 | [Build the touchscreen workflow and hand targets to a separate controller process](J10_build_the_touchscreen_workflow_and_hand_targets_to_a_separate_controller_process.md) |
| J11 | 2 | [Replace continuous feeding near the target with stop, settle, and pulse phases](J11_replace_continuous_feeding_near_the_target_with_stop_settle_and_pulse_phases.md) |
| J12 | 2 | [Separate powder behavior into configurable motion and settling profiles](J12_separate_powder_behavior_into_configurable_motion_and_settling_profiles.md) |
| J13 | 2 | [Stop unwanted motion after program termination and add layered shutdown behavior](J13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md) |
| J14 | 2 | [Plan the electronics mounting and PCB while the control system is still changing](J14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md) |
| J15 | 3 | [Investigate loaded speed limits and upgrade the NEMA 17 drive](J15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md) |
| J16 | 3 | [Make phase thresholds depend on dose size: the July 21 to July 24 controller revision](J16_make_phase_thresholds_depend_on_dose_size_the_july_21_to_july_24_controller_revision.md) |
| J17 | 3 | [Replace the barcode plan with selectable profiles and run the doser from the Pi](J17_replace_the_barcode_plan_with_selectable_profiles_and_run_the_doser_from_the_pi.md) |
| J18 | 3 | [Measure 5 g performance with sugar, salt, cocoa, and cinnamon](J18_measure_5_g_performance_with_sugar_salt_cocoa_and_cinnamon.md) |
| J19 | 3 | [Test 5 g dispensing with baking soda, cornstarch, powdered sugar, and flour](J19_validate_5_g_dispensing_of_the_four_cohesive_powders.md) |
| J20 | 3 | [Evaluate the 0.055 g limit and separate accuracy from repeatability](J20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md) |
| J21 | 4 | [Build the solid eight-pocket carousel and evolve it into an open two-plate structure](J21_build_the_solid_eight_pocket_carousel_and_evolve_it_into_an_open_two_plate_structure.md) |
| J22 | 4 | [Develop the lift mechanism that clears the drive before indexing](J22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md) |
| J23 | 4 | [Replace the angle-sensitive drive coupling with serrated mating teeth](J23_replace_the_angle_sensitive_drive_coupling_with_serrated_mating_teeth.md) |
| J24 | 4 | [Construct the extrusion frame and integrate the carousel, scale, lift, and screen](J24_construct_the_extrusion_frame_and_integrate_the_carousel_scale_lift_and_screen.md) |
| J25 | 4 | [Convert carousel positions to step counts and establish a known reference](J25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md) |
| J26 | 4 | [Choose the shortest carousel route and wait for completed indexing](J26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md) |
| J27 | 4 | [Sequence lift, indexing, engagement, and mass feedback for a multi-powder recipe](J27_sequence_lift_indexing_engagement_and_mass_feedback_for_a_multi_powder_recipe.md) |
| J28 | 5 | [Move STEP generation from the software loop to hardware timers](J28_move_step_generation_from_the_software_loop_to_hardware_timers.md) |
| J29 | 5 | [Add driver-alarm handling and an interactive motor-speed test](J29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md) |
| J30 | 5 | [Drop the fixed-board plan, troubleshoot perfboard, and mount a half-size breadboard](J30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md) |
| J31 | 5 | [Design protective covers and consolidate wiring along the frame](J31_design_protective_covers_and_consolidate_wiring_along_the_frame.md) |
| J32 | 5 | [Write an operating and cleaning procedure consistent with the actual prototype](J32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md) |
| J33 | 5 | [Bring the prototype together and assess the documented results](J33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md) |
