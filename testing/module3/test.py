import unittest

from testing.module3.dataTest import *
from modules.module3 import slow_closest_pairs, fast_closest_pair, hierarchical_clustering


class TestProject3(unittest.TestCase):
    def test_slow_closest_pairs_1(self):
        self.assertEqual(slow_closest_pairs(TEST_SLOW_1), set([(10.574516674876683, 0, 7)]))

    def test_slow_closest_pairs_2(self):
        self.assertEqual(slow_closest_pairs(TEST_SLOW_2), set([(1.0, 0, 1), (1.0, 1, 2)]))

    def test_fast_closest_pair_1(self):
        self.assertIn(fast_closest_pair(TEST_FAST_1), set([(1.0, 0, 1)]))

    def test_fast_closest_pair_2(self):
        expected_result = [(1.0, 9, 10), (1.0, 2, 3), (1.0, 15, 16), (1.0, 11, 12), (1.0, 13, 14), (1.0, 16, 17),
                           (1.0, 14, 15),
                           (1.0, 12, 13), (1.0, 4, 5), (1.0, 18, 19), (1.0, 3, 4), (1.0, 8, 9), (1.0, 17, 18),
                           (1.0, 6, 7),
                           (1.0, 7, 8), (1.0, 5, 6), (1.0, 10, 11), (1.0, 0, 1), (1.0, 1, 2)]
        self.assertIn(fast_closest_pair(TEST_FAST_2), expected_result)

    def test_fast_closest_pair_3(self):
        expected_result = set([(10.5745166749, 0, 7)])
        self.assertIn(fast_closest_pair(TEST_FAST_3), expected_result)

    def test_fast_closest_pair_4(self):
        expected_result = set([(92.95273653175754, 3, 12)])
        self.assertIn(fast_closest_pair(TEST_FAST_4), expected_result)

    def test_fast_closest_pair_5(self):
        self.assertEqual(fast_closest_pair(TEST_FAST_5), (5.131309436742058, 158, 167))

    def test_hierarchical_clustering(self):
        hierarchical_clustering(TEST_FAST_3, 5)
        self.assertTrue()

# Execute only when executor is this module
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit(True) when tests failed
            raise