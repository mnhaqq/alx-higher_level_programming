#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_valid_nums(self):
        b = Base(4)
        self.assertEqual(4, b.id)

        b = Base(63)
        self.assertEqual(63, b.id)

        b = Base(2)
        self.assertEqual(2, b.id)

    def test_negatives(self):
        b = Base(-10)
        self.assertEqual(-10, b.id)

        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_none(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_to_json_dictionary_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 53)

        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_dicts)), 106)

    def test_to_json_dictionary_square(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 39)
        self.assertEqual("[]", Base.to_json_string([]))


if __name__ == "__main__":
    unittest.main()
