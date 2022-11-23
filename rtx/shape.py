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
    
    def ray_intersect(self, r: ray.Ray) -> Tuple[bool, Union[None, intersect.Collision]]:
        """Checks is a ray intersects with the sphere"""
        # first calculations - distance between ray origin and sphere center
        i: List[float] = [
            r.origin.x - self.pos.x,
            r.origin.y - self.pos.y,
            r.origin.z - self.pos.z
        ]
        # equation: (x1 - tx) ^2 + (y1 - ty)^2 + (z1 - tz)^2 = r^2
        # tx = translation of sphere
        # x1, y1, z1 = position
        # r = radius
        a: float = r.direction.x ** 2 + r.direction.y ** 2 + r.direction.z ** 2
        b: float = 2 * (r.direction.x * (r.origin.x - self.pos.x) + r.direction.y * (r.origin.y - self.pos.y) + r.direction.z * (r.origin.z - self.pos.z))
        
        c: float = self.pos.x ** 2 + self.pos.y ** 2 + self.pos.z ** 2 + r.origin.x ** 2 + r.origin.y ** 2 + r.origin.z ** 2 - 2 + dot

        one_variable: float = 

        # this is the [t^2]
        no_variables: float = self.pos[0] * self.pos[0] + self.pos[1] * self.pos[1] + self.pos[2] * self.pos[2]

        # non variable values - finding x^2, y^2, and z^2
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
        f: List[float] = [sum(tvv), sum(ovv), sum(nvv) - self.radius*self.radius] # all this equals = 0
        quad: Tuple[int, List[float]] = maths.solve_quadratic(f[0], f[1], f[2])
        # find closest value
        if not quad[0] or not len(quad[1]):
            return (False, None)
        if len(quad[1]) == 1:
            if quad[1][0] < 0: return (False, None)
            rr = r.origin + r.direction * quad[1][0]
            return (True, intersect.Collision(r, vec3.Vector3(rr.arr)))
        # return closer value
        # print(quad)
        rr = r.origin + r.direction
        dis = max(quad[1])
        if dis < 0: return (False, None)
        rr *= dis
        # print(rr)
        return (True, intersect.Collision(r, vec3.Vector3(rr.arr)))


