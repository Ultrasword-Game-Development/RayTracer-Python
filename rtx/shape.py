"""
shape.py

contains methods and functions for shapes that can be placed within the world

"""

import numpy as np
from collections.abc import Sequence
from typing import List, Union, Any, Tuple
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

    def ray_intersect(self, r: ray.Ray) -> intersect.Collision:
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
    
    def ray_intersect(self, r: ray.Ray) -> Tuple[bool, intersect.Collision]:
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
        f: List[float] = [sum(tvv), sum(ovv), sum(nvv) - self.radius] # all this equals = 0
        quad: Tuple[int, List[float]] = maths.solve_quadratic(f[0], f[1], f[2])
        # find closest value
        if not quad[0] or not len(quad[1]):
            return (False, intersect.Collision(r, vec3.Vector3([0, 0, 0])))
        if len(quad[1]) == 1:
            rr = r.origin + r.direction * quad[0]
            return (True, intersect.Collision(r, vec3.Vector3(rr.arr)))
        # return closer value
        # print(quad)
        rr = r.origin + r.direction * (quad[1][0] if abs(quad[1][0]) < abs(quad[1][1]) else quad[1][1])
        return (True, intersect.Collision(r, vec3.Vector3(rr.arr)))


