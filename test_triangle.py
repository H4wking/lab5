import unittest
from triangle import Triangle
from point import Point


triangle = Triangle(Point(1, 1), Point(3, 1), Point(2, 3))


class ClassroomTest(unittest.TestCase):
    def test_is_triangle(self):
        self.assertEqual(Triangle.is_triangle(triangle), True)

    def test_perimeter(self):
        self.assertEqual(Triangle.perimeter(triangle), 6.47213595499958)

    def test_area(self):
        self.assertEqual(Triangle.area(triangle), 2.0)


if __name__ == "__main__":
    unittest.main()