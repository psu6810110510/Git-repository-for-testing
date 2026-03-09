from coe_6810110510.Hackerrank4twochar import alternate
import unittest

class AlternateTestCase(unittest.TestCase):
    
    def test_example_from_hackerrank(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_already_alternating(self):
        self.assertEqual(alternate("abab"), 4)
        self.assertEqual(alternate("aba"), 3)
        self.assertEqual(alternate("ab"), 2)

    def test_invalid_strings(self):
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("aa"), 0)
        self.assertEqual(alternate("aaaaa"), 0)

    def test_adjacent_duplicates_after_filter(self):
        self.assertEqual(alternate("aab"), 0)
        self.assertEqual(alternate("ababb"), 0)

    def test_multiple_valid_pairs(self):
        self.assertEqual(alternate("abacaba"), 3)

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)