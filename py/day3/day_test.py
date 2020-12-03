import unittest

from day3.slope import Slope

data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


class PasswordWill(unittest.TestCase):
    def test_day31_test_data_passes(self):
        slope = Slope(data)
        no_trees = slope.get_number_of_trees(3,1)
        self.assertEqual(7, no_trees)
