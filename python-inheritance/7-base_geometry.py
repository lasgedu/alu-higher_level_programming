#!/usr/bin/python3
# 6-base_geometry.py
"""A python module
that creates an empty
class
"""


class BaseGeometry():
    """An empty class
    called BaseGeometry
    """
    def __init__(self, do_print=False):
        if do_print:
            self.count = 1

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not type(value) == int:
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        else:
            self.value = value
