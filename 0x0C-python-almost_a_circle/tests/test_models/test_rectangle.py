#!/usr/bin/python3
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):

    def test_positive_id(self):
        r = Rectangle(2, 3, 2, 2, 10)
        self.assertEqual(10, r.id)

        r = Rectangle(4, 2, 3, 1, 5)
        self.assertEqual(5, r.id)

        r = Rectangle(1, 2, 4, 3, 2)
        self.assertEqual(2, r.id)

    def test_zero_id(self):
        r = Rectangle(2, 4, 5, 6, 0)
        self.assertEqual(0, r.id)

    def test_width(self):
        r = Rectangle(2, 5)
        r.width = 5
        self.assertEqual(5, r.width)

        r.width = 9
        self.assertEqual(9, r.width)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(-3, 1)

        with self.assertRaises(TypeError):
            r = Rectangle("string", 1)

        with self.assertRaises(TypeError):
            r = Rectangle(None, 4)

        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height(self):
        r = Rectangle(4, 8)
        r.height = 3
        self.assertEqual(3, r.height)

        r.height = 15
        self.assertEqual(15, r.height)

        with self.assertRaises(ValueError):
            r = Rectangle(3, -5)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "string")

        with self.assertRaises(TypeError):
            r = Rectangle(1, None)

        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_x(self):
        r = Rectangle(3, 6)
        r.x = 7
        self.assertEqual(7, r.x)

        r.x = 4
        self.assertEqual(4, r.x)

        r.x = 0
        self.assertEqual(0, r.x)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, -1, 9)

        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "string", 9)

    def test_y(self):
        r = Rectangle(3, 3)
        r.y = 4
        self.assertEqual(4, r.y)

        r.y = 15
        self.assertEqual(15, r.y)

        r.y = 0
        self.assertEqual(0, r.y)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, 3, -5)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 3, 3, "string")

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(6, r.area())

        r = Rectangle(4, 5)
        self.assertEqual(20, r.area())

        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r.area())

    def test_display(self):
        r = Rectangle(4, 6)
        expected = "####\n####\n####\n####\n####\n####\n"

        captured = StringIO()
        sys.stdout = captured

        r.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected)

        r = Rectangle(3, 2)
        expected = "###\n###\n"

        captured = StringIO()
        sys.stdout = captured

        r.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected)

    def test_display_1(self):
        r = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"

        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", r.__str__())

        r = Rectangle(5, 5, 1, 0, 3)
        self.assertEqual("[Rectangle] (3) 1/0 - 5/5", r.__str__())

    def test_update(self):
        r = Rectangle(4, 3, 2, 1)
        r.update(92)
        self.assertEqual(92, r.id)

        r.update(92, 20, 15)
        self.assertEqual(20, r.width)
        self.assertEqual(15, r.height)

        r.update(4, 2, 6, 9, 1)
        self.assertEqual(4, r.id)
        self.assertEqual(2, r.width)
        self.assertEqual(6, r.height)
        self.assertEqual(9, r.x)
        self.assertEqual(1, r.y)

        r.update(height=4)
        self.assertEqual(4, r.height)

        r.update(height=6, x=1, y=0, id=22)
        self.assertEqual(6, r.height)
        self.assertEqual(1, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual(22, r.id)

        with self.assertRaises(ValueError):
            r.update(height=0)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), expected)

        r = Rectangle(4, 5, id=3)
        expected = {'x': 0, 'y': 0, 'width': 4, 'height': 5, 'id': 3}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
