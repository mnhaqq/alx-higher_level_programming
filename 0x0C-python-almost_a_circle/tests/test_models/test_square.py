#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_positive_id(self):
        r = Square(2, 2, 2, 10)
        self.assertEqual(10, r.id)

        r = Square(4, 3, 1, 5)
        self.assertEqual(5, r.id)

        r = Square(1, 4, 3, 2)
        self.assertEqual(2, r.id)

    def test_zero_id(self):
        r = Square(2, 5, 6, 0)
        self.assertEqual(0, r.id)

    def test_size(self):
        r = Square(2)
        r.size = 5
        self.assertEqual(5, r.size)

        r.size = 9
        self.assertEqual(9, r.size)

        with self.assertRaises(ValueError):
            r = Square(0)

        with self.assertRaises(ValueError):
            r = Square(-3)

        with self.assertRaises(TypeError):
            r = Square("string")

        with self.assertRaises(TypeError):
            r = Square(None)

        with self.assertRaises(TypeError):
            r = Square()

    def test_update(self):
        r = Square(4, 2, 1)
        r.update(92)
        self.assertEqual(92, r.id)

        r.update(92, 20, 15)
        self.assertEqual(20, r.size)
        self.assertEqual(15, r.x)

        r.update(4, 2, 6, 9)
        self.assertEqual(4, r.id)
        self.assertEqual(2, r.size)
        self.assertEqual(6, r.x)
        self.assertEqual(9, r.y)

        r.update(size=4)
        self.assertEqual(4, r.size)

        r.update(size=6, x=1, y=0, id=22)
        self.assertEqual(6, r.size)
        self.assertEqual(1, r.x)
        self.assertEqual(0, r.y)
        self.assertEqual(22, r.id)

        with self.assertRaises(ValueError):
            r.update(size=0)

    def test_to_dictionary(self):
        r = Square(2, 1, 9, 5)
        expected = {'x': 1, 'y': 9, 'id': 5, 'size': 2}
        self.assertEqual(r.to_dictionary(), expected)

        r = Square(4, id=3)
        expected = {'x': 0, 'y': 0, 'size': 4, 'id': 3}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
