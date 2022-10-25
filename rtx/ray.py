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
        self.direction = direction.normalize()


