import math
import re
import sys
import unittest
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SOURCE_DIR))

import motor_scale_control as controller


class WeightParsingTests(unittest.TestCase):
    def test_parses_common_gram_output(self):
        self.assertEqual(controller.parse_weight("ST,GS,+ 1.234 g"), 1.234)

    def test_converts_supported_units_to_grams(self):
        self.assertEqual(controller.parse_weight("250 mg"), 0.25)
        self.assertEqual(controller.parse_weight("0.002 kg"), 2.0)

    def test_rejects_unsupported_explicit_units(self):
        self.assertIsNone(controller.parse_weight("1.25 oz"))
        self.assertIsNone(controller.parse_weight("2.0 lb"))

    def test_keeps_unitless_gram_stream_compatibility(self):
        self.assertEqual(controller.parse_weight("+0.125"), 0.125)


class TargetValidationTests(unittest.TestCase):
    def test_rejects_non_finite_and_non_positive_targets(self):
        for target in (math.nan, math.inf, -math.inf, 0.0, -1.0):
            with self.subTest(target=target):
                self.assertIsNotNone(controller.target_validation_error(target))

    def test_rejects_target_over_configured_maximum(self):
        self.assertIsNotNone(
            controller.target_validation_error(controller.MAX_TARGET_GRAMS + 0.001)
        )

    def test_accepts_target_inside_configured_range(self):
        self.assertIsNone(controller.target_validation_error(1.0))


class MotorProtocolTests(unittest.TestCase):
    def test_nonfree_profile_reaches_smallest_final_pulse(self):
        self.assertEqual(
            controller.select_auger_command(
                0.050,
                0.020,
                controller.NON_FREE_FLOWING,
            ),
            "AUGER PULSE NONFREE FINAL",
        )

    def test_every_generated_motion_command_is_accepted_by_firmware(self):
        arduino_source = (SOURCE_DIR /
            "pill_compounder_arduino/pill_compounder_arduino.ino"
        ).read_text(encoding="utf-8")
        accepted = set(
            re.findall(r'commandEquals\("([^"]+)"\)', arduino_source)
        )

        targets = (0.050, 0.200, 0.500, 1.000, 2.000, 12.000)
        generated = set()
        for mode in (
            controller.FREE_FLOWING,
            controller.NON_FREE_FLOWING,
        ):
            for target in targets:
                remaining_values = {
                    target,
                    target * 0.75,
                    target * 0.50,
                    target * 0.25,
                    0.500,
                    0.220,
                    0.150,
                    0.100,
                    0.050,
                    0.030,
                    0.010,
                    0.001,
                }
                for remaining in remaining_values:
                    if 0 < remaining <= target:
                        generated.add(
                            controller.select_auger_command(
                                target,
                                remaining,
                                mode,
                            )
                        )

        expected = {
            "AUGER CONT FREE TURBO",
            "AUGER CONT FREE NORMAL",
            "AUGER CONT NONFREE TURBO",
            "AUGER CONT NONFREE NORMAL",
            "AUGER PULSE FREE APPROACH",
            "AUGER PULSE FREE FINE",
            "AUGER PULSE FREE FINAL",
            "AUGER PULSE NONFREE FINAL",
        }
        self.assertEqual(generated, expected)
        self.assertTrue(generated.issubset(accepted), generated - accepted)

    def test_nonfree_uses_only_fast_medium_and_super_slow(self):
        for powder in (
            "Powdered sugar",
            "Baking soda",
            "Cornstarch",
            "Ground cinnamon",
            "All-purpose flour",
            "Cocoa powder",
        ):
            with self.subTest(powder=powder):
                mode = controller.powder_mode_for(powder)
                self.assertEqual(mode, controller.NON_FREE_FLOWING)
                self.assertEqual(
                    controller.select_auger_command(12.000, 5.001, mode),
                    "AUGER CONT NONFREE TURBO",
                )
                self.assertEqual(
                    controller.select_auger_command(12.000, 5.000, mode),
                    "AUGER CONT NONFREE NORMAL",
                )
                self.assertEqual(
                    controller.select_auger_command(12.000, 1.000, mode),
                    "AUGER CONT NONFREE NORMAL",
                )
                self.assertEqual(
                    controller.select_auger_command(12.000, 0.999, mode),
                    "AUGER PULSE NONFREE FINAL",
                )
                self.assertEqual(
                    controller.select_auger_command(0.200, 0.200, mode),
                    "AUGER PULSE NONFREE FINAL",
                )

    def test_table_salt_remains_free_flowing(self):
        self.assertEqual(
            controller.powder_mode_for("Table salt"),
            controller.FREE_FLOWING,
        )


class DeviceCommunicationContractTests(unittest.TestCase):
    def test_app_disk_commands_and_uno_responses_match(self):
        app_source = (SOURCE_DIR / "app.py").read_text(encoding="utf-8")
        uno_source = (SOURCE_DIR /
            "pill_compounder_arduino/pill_compounder_arduino.ino"
        ).read_text(encoding="utf-8")

        for command in (
            "PING",
            "DISK STATUS",
            "DISK STOP",
            "DISK DISABLE",
            "DISK NEXT",
            "DISK PREV",
        ):
            self.assertIn(command, app_source)
            self.assertIn(f'commandEquals("{command}")', uno_source)

        self.assertIn('parseSlotArgument("SET SLOT "', uno_source)
        self.assertIn('parseSlotArgument("DISK GOTO "', uno_source)
        self.assertIn("DONE DISK SLOT ", app_source)
        self.assertIn("DONE DISK SLOT ", uno_source)

    def test_app_actuator_commands_and_xiao_responses_match(self):
        app_source = (SOURCE_DIR / "app.py").read_text(encoding="utf-8")
        xiao_source = (SOURCE_DIR / "linearActuator/linearActuator.ino").read_text(
            encoding="utf-8"
        )

        for command in (
            "PING",
            "HEARTBEAT",
            "ACTUATOR STATUS",
            "ACTUATOR STOP",
            "SET ACTUATOR UP",
            "ACTUATOR DOWN",
            "ACTUATOR UP",
        ):
            self.assertIn(command, app_source)
            self.assertIn(f'commandEquals("{command}")', xiao_source)

        for response in (
            "OK ACTUATOR PING",
            "DONE ACTUATOR ",
            "ACTUATOR STATUS ",
            "OK ACTUATOR STOPPED",
        ):
            self.assertIn(response, app_source)
            self.assertIn(response, xiao_source)


if __name__ == "__main__":
    unittest.main()
