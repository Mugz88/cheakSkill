import unittest
from SearchArea import Square, Rectangle, AreaCalculator
from math import pi

class TestAreaCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(AreaCalculator.calculate_area('circle', 5), pi * 25)
    def test_triangle_area(self):
        self.assertAlmostEqual(AreaCalculator.calculate_area('triangle', 3, 4, 5), 6)
    def test_rectangle_area(self):
        self.assertAlmostEqual(AreaCalculator.calculate_area('rectangle', 3, 4), 12)
    def test_square_area(self):
        self.assertAlmostEqual(AreaCalculator.calculate_area('square', 5), 25)
    def test_is_right_triangle(self):
        self.assertTrue(AreaCalculator.is_right_triangle(3, 4, 5))