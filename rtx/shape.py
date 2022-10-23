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
        return False


