from coe_6810110510.Hackerrank2alternating_characters import alternatingCharacters
import unittest

class AlternatingCharactersTestCase(unittest.TestCase):
    def test_alternating_characters_input_AABA_should_return_1(self):
        self.assertEqual(alternatingCharacters("AABA"), 1)

    def test_alternating_characters_input_AAAA_should_return_3(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_alternating_characters_input_ABABABAB_should_return_0(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_alternating_characters_input_AAABBB_should_return_4(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_alternating_characters_input_empty_should_return_0(self):
        self.assertEqual(alternatingCharacters(""), 0)