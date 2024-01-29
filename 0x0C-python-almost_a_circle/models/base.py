#!/usr/bin/python3
"""
Module which contains the base class
"""
import json


class Base:
    """
    Class describing the base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function initializing base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation of a list of dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that writes json string representation of a list of
        instances to a file
        """
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
                return
            list_objs = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of json string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
