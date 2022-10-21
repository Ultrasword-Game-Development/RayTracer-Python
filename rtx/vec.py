"""
vec.py

contains functions and objects that store data for vector2/vector3

"""

from typing import Union, List, overload

from dataclasses import dataclass
from math import sqrt, atan, pi


@dataclass(init=False)
class Vector2:
    """
    Vector2
    - stores positional data in 2 dimensions
    """

    x: float
    y: float

    mag: float
    angle: float

    def __init__(self, x: float, y: float):
        """Init function for Vector2"""
        self.x = x
        self.y = y
        self.mag = self.get_magnitude()
        self.angle = self.get_angle()

    # ------------------------------------------ #
    # data related funcs
    
    def get_magnitude(self) -> float:
        """Get the magnitude of a vector2"""
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_angle(self) -> float:
        """Get the angle of a vector2"""
        return atan(self.y / self.x) / pi * 180


    # ------------------------------------------ #
    # math related funcs

    def __eq__(self, o: object) -> bool:
        """Checks if one vector is equal to another"""
        if not isinstance(o, Vector2):
            return False
        return self.x == o.x and self.y == o.y
    
    def __add__(self, o: object) -> object:
        """Adds two vectors together"""
        if not isinstance(o, Vector2):
            return False
        return Vector2(self.x + o.x, self.y + o.y)

    def __sub__(self, o: object) -> object:
        """Subtract two vectors together"""
        if not isinstance(o, Vector2):
            return False
        return Vector2(self.x - o.x, self.y - o.y)
    
    def __mul__(self, o: object) -> object:
        """Multiply two vectors together"""
        if not isinstance(o, Vector2):
            return False
        return Vector2(self.x * o.x, self.y * o.y)
