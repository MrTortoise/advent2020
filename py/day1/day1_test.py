import unittest
from day1.solver import Solver


class Day1SolverWill(unittest.TestCase):

    def test_returnProductOf2NumbersThatSum2020(self):
        numbers = [1000, 1020]
        solver = Solver()
        result = solver.solve2(numbers)
        self.assertEqual(1_020_000, result)

    def test_returnProductOf3NumbersThatSum2020(self):
        numbers = [1721,
                   979,
                   366,
                   299,
                   675,
                   1456]
        solver = Solver()
        result = solver.solve3(numbers)
        self.assertEqual(241861950, result)
