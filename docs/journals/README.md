# Pill Compounder: Personal Build Journals

Thirty-three retrospective entries following the feeder, powder tests, controls, carousel, and assembly. The writing follows the problem being worked through, with the saved geometry, code, measurements, and images kept alongside it.

These are AI-assisted reconstructions for personal documentation, not contemporaneous notebook pages, verified session logs, or Forge submissions. The conversational voice is an editorial interpretation, not a transcript of thoughts or a record of additional events. No work dates or hours have been invented. Unresolved results remain unresolved.

CAD construction views were captured from saved models on October 13, 2026. Archive-specific qualifications appear in expandable notes where needed. The original reference drafts and their evidence gaps are unchanged.

- [Read the whole collection](ALL_JOURNALS.md)
- [Original reference drafts](../journal-reference/README.md)
- [Image gallery](../journal-reference/GALLERY.md)
- [Copyable image URLs](../journal-reference/IMAGE_URLS.md)
- [Evidence and version notes](../journal-reference/EVIDENCE.md)
- [Project journal](../../JOURNAL.md)

| Entry | Milestone | Topic |
| --- | --- | --- |
| J01 | 1 | [Eight hoppers, but start with one](J01_define_the_requirements_and_develop_the_shared_eight_hopper_architecture.md) |
| J02 | 1 | [Getting the first powder path into CAD](J02_construct_the_first_hopper_adapter_and_bottom_feeder_cad.md) |
| J03 | 1 | [The auger print had to work first](J03_build_the_auger_from_a_helix_and_flight_profile_then_obtain_a_usable_print.md) |
| J04 | 1 | [The thread looked better in CAD](J04_test_the_removable_threaded_hopper_and_replace_it_with_a_short_locking_interface.md) |
| J05 | 1 | [Sugar was falling out before I started](J05_simplify_the_powder_path_and_reduce_sugar_leaking_during_loading.md) |
| J06 | 1 | [Cornstarch changed the problem](J06_diagnose_cornstarch_jamming_and_the_first_agitator_s_incomplete_coverage.md) |
| J07 | 1 | [Adding arms without losing the screw](J07_model_the_two_arm_agitator_and_compare_uniform_and_tapered_flight_concepts.md) |
| J08 | 2 | [Getting commanded motion out of the feeder](J08_wire_the_first_nema_17_and_tmc2209_drive_and_establish_controlled_motion.md) |
| J09 | 2 | [The scale reading is behind the powder](J09_read_serial_scale_data_and_establish_the_baseline_mass_for_each_dispense.md) |
| J10 | 2 | [Making the screen talk to the controller](J10_build_the_touchscreen_workflow_and_hand_targets_to_a_separate_controller_process.md) |
| J11 | 2 | [Stopping the motor didn't stop the added mass](J11_replace_continuous_feeding_near_the_target_with_stop_settle_and_pulse_phases.md) |
| J12 | 2 | [Sugar settings made cornstarch crawl](J12_separate_powder_behavior_into_configurable_motion_and_settling_profiles.md) |
| J13 | 2 | [The program ended. The motor kept moving.](J13_stop_unwanted_motion_after_program_termination_and_add_layered_shutdown_behavior.md) |
| J14 | 2 | [A PCB sounded like the way out of the wiring](J14_plan_the_electronics_mounting_and_pcb_while_the_control_system_is_still_changing.md) |
| J15 | 3 | [Trying to get more out of the NEMA 17](J15_investigate_loaded_speed_limits_and_upgrade_the_nema_17_drive.md) |
| J16 | 3 | [A 55 mg request shouldn't start like a large dose](J16_make_phase_thresholds_depend_on_dose_size_the_july_21_to_july_24_controller_revision.md) |
| J17 | 3 | [Dropping the scanner and getting off the laptop](J17_replace_the_barcode_plan_with_selectable_profiles_and_run_the_doser_from_the_pi.md) |
| J18 | 3 | [The 5 g results were encouraging, with a lid problem](J18_measure_5_g_performance_with_sugar_salt_cocoa_and_cinnamon.md) |
| J19 | 3 | [Close to 5 g, but it took a while](J19_validate_5_g_dispensing_of_the_four_cohesive_powders.md) |
| J20 | 3 | [The 55 mg tests didn't go nearly as well](J20_evaluate_the_0_055_g_limit_and_separate_accuracy_from_repeatability.md) |
| J21 | 4 | [Back to the carousel, and a lot less solid material](J21_build_the_solid_eight_pocket_carousel_and_evolve_it_into_an_open_two_plate_structure.md) |
| J22 | 4 | [The drive has to get out of the way](J22_develop_the_lift_mechanism_that_clears_the_drive_before_indexing.md) |
| J23 | 4 | [Lowering the motor wasn't enough to connect it](J23_replace_the_angle_sensitive_drive_coupling_with_serrated_mating_teeth.md) |
| J24 | 4 | [Getting the separate mechanisms onto one frame](J24_construct_the_extrusion_frame_and_integrate_the_carousel_scale_lift_and_screen.md) |
| J25 | 4 | [The controller needs to know which hopper is there](J25_convert_carousel_positions_to_step_counts_and_establish_a_known_reference.md) |
| J26 | 4 | [One slot backward instead of seven forward](J26_choose_the_shortest_carousel_route_and_wait_for_completed_indexing.md) |
| J27 | 4 | [Getting the recipe to wait for the mechanisms](J27_sequence_lift_indexing_engagement_and_mass_feedback_for_a_multi_powder_recipe.md) |
| J28 | 5 | [The pulse generator was another speed limit](J28_move_step_generation_from_the_software_loop_to_hardware_timers.md) |
| J29 | 5 | [Changing speed without uploading another sketch](J29_add_driver_alarm_handling_and_an_interactive_motor_speed_test.md) |
| J30 | 5 | [Back to a breadboard, but make it fit](J30_drop_the_fixed_board_plan_troubleshoot_perfboard_and_mount_a_half_size_breadboard.md) |
| J31 | 5 | [The wiring needed somewhere to live](J31_design_protective_covers_and_consolidate_wiring_along_the_frame.md) |
| J32 | 5 | [Writing down the steps I was already taking for granted](J32_write_an_operating_and_cleaning_procedure_consistent_with_the_actual_prototype.md) |
| J33 | 5 | [Putting the build in perspective](J33_document_the_final_integrated_state_and_identify_exactly_what_was_demonstrated.md) |
