from coe_6810110510.Staircase import staircase
import unittest

class StaircaseTestCase(unittest.TestCase):
    def test_staircase_input_4_hash_should_be_correct(self):
        expected_output = "   #\n  ##\n ###\n####"
        self.assertEqual(staircase(4, "#"), expected_output)

    def test_staircase_input_5_star_should_be_correct(self):
        expected_output = "    *\n   **\n  ***\n ****\n*****"
        self.assertEqual(staircase(5, "*"), expected_output)

    def test_staircase_input_0_should_raise_assertion_error(self):
        self.assertRaises(AssertionError, staircase, 0, "#")

    def test_staircase_input_31_should_raise_assertion_error(self):
        self.assertRaises(AssertionError, staircase, 31, "#")

    def test_staircase_input_negative_should_raise_assertion_error(self):
        self.assertRaises(AssertionError, staircase, -1, "#")

    def test_staircase_input_4_A_letter_should_be_correct(self):
        expected_output = "   A\n  AA\n AAA\nAAAA"
        self.assertEqual(staircase(4, "A"), expected_output)
