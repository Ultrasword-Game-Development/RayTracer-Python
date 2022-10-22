"""
shape.py

contains methods and functions for shapes that can be placed within the world

"""

import numpy as np
from collections.abc import Sequence
from typing import List, Union, Any
from dataclasses import dataclass

from . import ray

# ------------------------------------------ #
# shape

@dataclass(init=False)
class Shape:
    """
    Shape
    - base class for different shapes (cubes, spheres, etc)
    """
    
    # ------------------------------------------ #
    # methods

    def ray_intersect(self, r: ray.Ray) -> bool:
        """Checks if a ray intersects a shape"""
        return False


