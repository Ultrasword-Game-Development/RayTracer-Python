"""
vec.py

contains functions and objects that store data for vector2/vector3

"""

import numpy as np

from collections.abc import Sequence
from typing import Union, List
from dataclasses import dataclass
from math import sqrt


VECTOR_TYPES = Union[int, float]

# ------------------------------------------ #
# vector 3

@dataclass(init=False)
class Vector3:
    """
    Vector3
    - stores positional data in 3 dimensions
    """
    arr: np.array
    mag: float
    
    def __init__(self, arr: Sequence[VECTOR_TYPES, VECTOR_TYPES, VECTOR_TYPES]):
        """Init function for Vector3"""
        self.arr = np.array(arr)
        self.mag = self.get_magnitude()
    
    # ------------------------------------------ #
    # data related funcs
    
    def get_magnitude(self) -> VECTOR_TYPES:
        """Get the magnitude of a vector3"""
        return sqrt(self.arr[0] ** 2 + self.arr[1] ** 2 + self.arr[2] ** 2)

    def dot(self, o: object) -> VECTOR_TYPES:
        """Find dot product"""
        if not isinstance(o, Vector3):
            raise NotImplementedError(f"{type(o)} is not an instance of Vector3")
        return np.dot(self.arr, o.arr)

    def cross(self, o: object) -> object:
        """Find the cross product"""
        if not isinstance(o, Vector3):
            raise NotImplementedError(f"{type(o)} is not an instance of Vector3")
        return Vector3(np.cross(self.arr, o.arr))


    # ------------------------------------------ #
    # math related funcs

    def __eq__(self, o: object) -> bool:
        """Checks if one vector is equal to another"""
        if not isinstance(o, Vector3):
            return False
        return self.arr[0] == o.arr[0] and self.arr[1] == o.arr[1] and self.arr[2] == o.arr[2]
    
    def __add__(self, o: object) -> object:
        """Adds two vectors together"""
        if not isinstance(o, Vector3):
            return False
        return Vector3([self.arr[0] + o.arr[0], self.arr[1] + o.arr[1], self.arr[2] + o.arr[2]])

    def __sub__(self, o: object) -> object:
        """Subtract two vectors together"""
        if not isinstance(o, Vector3):
            return False
        return Vector3([self.arr[0] - o.arr[0], self.arr[1] - o.arr[1], self.arr[2] - o.arr[2]])
    
