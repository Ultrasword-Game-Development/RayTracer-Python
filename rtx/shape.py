"""
shape.py

contains methods and functions for shapes that can be placed within the world

"""

import numpy as np
from collections.abc import Sequence
from typing import List, Union, Any, Tuple, Annotated
from dataclasses import dataclass

from . import vec3, ray, intersect, maths

# ------------------------------------------ #
# shape

@dataclass(init=False)
class Shape:
    """
    Shape
    - base class for different shapes (cubes, spheres, etc)
    """

    pos: vec3.Vector3
    
    # ------------------------------------------ #
    # methods

    def __init__(self, pos: vec3.Vector3) -> None:
        """Init function for a Shape"""
        if not isinstance(pos, vec3.Vector3):
            pos = vec3.Vector3(pos)
        self.pos = pos

    def ray_intersect(self, r: ray.Ray) -> Tuple[bool, intersect.Collision]:
        """Checks if a ray intersects a shape"""
        pass
    
    def handle_intersect(self, r: ray.Ray) -> None:
        """Handles a ray intersection"""
        pass


# ------------------------------------------ #
# sphere

class Sphere(Shape):
    """
    Sphere
    - a sphere object that can be rendered
    """

    def __init__(self, pos: vec3.Vector3, radius: float) -> None:
        """Init function for a sphere"""
        super().__init__(pos)
        self.radius = radius
    
    def ray_intersect(self, r: ray.Ray) -> Tuple[bool, float]:
        """Checks is a ray intersects with the sphere"""
        # equation: (x1 - tx) ^2 + (y1 - ty)^2 + (z1 - tz)^2 = r^2
        # tx = translation of sphere
        # x1, y1, z1 = position
        # r = radius
        a: float = r.direction.x ** 2 + r.direction.y ** 2 + r.direction.z ** 2
        b: float = 2 * (r.direction.x * (r.origin.x - self.pos.x) + r.direction.y * (r.origin.y - self.pos.y) + r.direction.z * (r.origin.z - self.pos.z))
        c: float = self.pos.x ** 2 + self.pos.y ** 2 + self.pos.z ** 2 + r.origin.x ** 2 + r.origin.y ** 2 + r.origin.z ** 2 - 2 * maths.dot(self.pos, r.origin) - self.radius ** 2

        # discriminant
        d: float = b ** 2 - 4 * a * c
        if d < 0:
            # none nonexistent 
            return (False, 0.0)
        # if one or more -- just assume yep cuz we lazy
        # find distance coef (r.direction * t)
        t = (-b - maths.math.sqrt(d)) / (2 * a)
        if t < 0:
            return (False, 0.0)
        # print(r.origin + r.direction * t)
        return (True, t)


