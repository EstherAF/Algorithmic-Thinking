import unittest

from testing.module2.dataTest import *
from modules.module2 import bfs_visited, cc_visited, largest_cc_size, compute_resilience


class TestProject2(unittest.TestCase):
    def test_bfs_visited(self):
        self.assertEqual(bfs_visited(GRAPH0, 0), set([0, 1, 2, 3]))

    def test_cc_visited(self):
        self.assertEqual(cc_visited(GRAPH0), [set([0, 1, 2, 3])])

    def test_compute_resilience(self):
        # self.assertEqual(compute_resilience(GRAPH0, [1, 2]), [4, 2, 1])
        self.assertEqual(compute_resilience(GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8]), [8, 7, 6, 5, 1, 1, 1, 1, 0])

    def test_largest_cc_size(self):
        self.assertEqual(largest_cc_size(GRAPH0), 4)


#Execute only when executor is this module
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:  # raised by sys.exit(True) when tests failed
            raise