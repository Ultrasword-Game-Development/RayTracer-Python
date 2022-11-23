"""
ray.py

contains methods and objects for rays

"""

import numpy as np
from dataclasses import dataclass
from typing import List, Union, Any
from collections.abc import Sequence

from . import vec3

# ------------------------------------------ #
# ray

@dataclass(init=False)
class Ray:
    """
    Ray
    - a ray object
    """

    origin: vec3.Vector3
    direction: vec3.Vector3

    def __init__(self, origin: vec3.Vector3, direction: vec3.Vector3) -> None:
        """Init function for Ray"""
        self.origin = origin
        self.direction = direction
    
    def trace(self, world: Any, color: List[float]):
        """Trace the ray in a world - recursive"""
        for eid, ent in world.entities.items():
            col = ent.shape.ray_intersect(self)
            # print(col)
            if not col[0]:
                continue
            # there is a collision
            # for now just set all to white
            # print(col[1])
            for x in range(4):
                color[x] = 1 - 1 / (col[1] - 30)
            color[3] = 1
            # print(color)
            return color
        # garunteed
        return color

