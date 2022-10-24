"""
shape.py

contains methods and functions for shapes that can be placed within the world

"""

import numpy as np
from collections.abc import Sequence
from typing import List, Union, Any
from dataclasses import dataclass

from . import vec3
from . import ray

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
        self.pos = pos

    def ray_intersect(self, r: ray.Ray) -> bool:
        """Checks if a ray intersects a shape"""
        return False
    
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
    
    def ray_intersect(self, r: ray.Ray) -> bool:
        """Checks is a ray intersects with the sphere"""
        # first calculations
        i: List[float] = [
            r.origin.x - self.pos.x,
            r.origin.y - self.pos.y,
            r.origin.z - self.pos.z
        ]
        # non variable values
        nvv: List[float] = [
            i[0] * i[0],
            i[1] * i[1],
            i[2] * i[2]
        ]

        # one variable values
        ovv: List[float] = [
            -2 * i[0] * r.direction.x,
            -2 * i[1] * r.direction.y,
            -2 * i[2] * r.direction.z
        ]

        # variable squared
        tvv: List[float] = [
            r.direction.x * r.direction.x,
            r.direction.y * r.direction.y,
            r.direction.z * r.direction.z
        ]

        # find final equation - 0 = t^2, 1 = t, 2 = 0
        final: List[float] = [sum(tvv), sum(ovv), sum(nvv) - self.radius] # all this equals = 0

