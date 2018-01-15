# -*- coding: utf-8 -*-

import unittest
from .context import shapes
#from shapes import Square, Triangle

"""
test_hello_shapes
"""
class HelloShapesTests(unittest.TestCase):
    """
    HelloShapeTests
    """
    def test_square(self):
        """Test square."""
        expected = 4.0
        shape = shapes.Square("square1", 2.0)
        size = shape.get_area()
        assert (size == expected)

    def test_triangle(self):
        """Test triangle."""
        expected = 2.0
        shape = shapes.Triangle("triangle1", 2.0, 2.0)
        size = shape.get_area()
        assert (size == expected)

if __name__ == '__main__':
    unittest.main()
