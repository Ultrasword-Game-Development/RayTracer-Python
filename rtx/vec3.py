"""
vec.py

contains functions and objects that store data for vector2/vector3

"""

import numpy as np

from collections.abc import Sequence
from typing import Union, List, Any, Annotated
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
    arr: Any
    mag: float
    
    def __init__(self, arr: Annotated[List[VECTOR_TYPES], 3]):
        """Init function for Vector3"""
        self.arr = np.array(arr, dtype=np.float32)
        self.mag = self.get_magnitude()
    
    @property
    def x(self) -> float:
        """The x property"""
        return self.arr[0]
    
    @x.setter
    def x(self, n: float) -> None:
        """Set x"""
        self.arr[0] = n

    @property
    def y(self) -> float:
        """The y property"""
        return self.arr[1]
    
    @y.setter
    def y(self, n: float) -> None:
        """Set y"""
        self.arr[1] = n

    @property
    def z(self) -> float:
        """The z property"""
        return self.arr[2]
    
    @z.setter
    def z(self, n: float) -> None:
        """Set z"""
        self.arr[2] = n
    
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
        return Vector3(list(np.cross(self.arr, o.arr)))

    def to_array(self) -> Annotated[List[VECTOR_TYPES], 3]:
        """Return a vector array"""
        return [self.arr[0], self.arr[1], self.arr[2]]

    def normalize(self) -> None:
        """Normalize a vector"""
        if not self.mag: return
        self.x /= self.mag
        self.y /= self.mag
        self.z /= self.mag
        self.mag = 1
        # print(self.x, self.y, self.z, self.mag)
        # print("Implement Normalizing Vectors")

    # ------------------------------------------ #
    # math related funcs

    def __eq__(self, o: object) -> bool:
        """Checks if one vector is equal to another"""
        if not isinstance(o, Vector3):
            return False
        return self.arr[0] == o.arr[0] and self.arr[1] == o.arr[1] and self.arr[2] == o.arr[2]
    
    def __add__(self, o: object) -> object:
        """Adds two vectors together"""
        if isinstance(o, (list, tuple)):
            # calcualte with list
            return Vector3([self.arr[0] + o[0], self.arr[1] + o[1], self.arr[2] + o[2]])
        if not isinstance(o, Vector3):
            raise NotImplementedError(f"What vector is that? | {o}")
        return Vector3([self.arr[0] + o.arr[0], self.arr[1] + o.arr[1], self.arr[2] + o.arr[2]])

    def __sub__(self, o: object) -> object:
        """Subtract two vectors together"""
        if isinstance(o, (list, tuple)):
            # calculate with list
            return Vector3([self.arr[0] - o[0], self.arr[1] - o[1], self.arr[2] - o[2]]) 
        if not isinstance(o, Vector3):
            raise NotImplementedError(f"What vector is that? | {o}")
        return Vector3([self.arr[0] - o.arr[0], self.arr[1] - o.arr[1], self.arr[2] - o.arr[2]])
    
    def __mul__(self, o: Union[int, float]) -> object:
        """Multiply a vector with a scalar"""
        return Vector3([self.arr[0] * o, self.arr[1] * o, self.arr[2] * o])
    
    def __truediv__(self, o: Union[int,float]) -> object:
        """Divide a vector with a scalar"""
        return Vector3([self.arr[0] / o, self.arr[1] / o, self.arr[2] / o])
