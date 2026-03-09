from coe_6810110510.Hackerrank5Grid import gridChallenge
import unittest

class GridChallengeTestCase(unittest.TestCase):
    
    def test_hackerrank_example_yes(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_hackerrank_example_no(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_element_grid(self):
        grid = ['a']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_single_row_grid(self):
        grid = ['qwerty']
        self.assertEqual(gridChallenge(grid), "YES")

    def test_already_sorted_grid(self):
        grid = ['abc', 'def', 'ghi']
        self.assertEqual(gridChallenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()