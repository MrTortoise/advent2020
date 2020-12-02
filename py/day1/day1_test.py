import unittest
from day1.solver import Solver


class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        numbers = [1000, 1020]
        solver = Solver()
        result = solver.solve(numbers)
        self.assertEqual(1_020_000, result)
