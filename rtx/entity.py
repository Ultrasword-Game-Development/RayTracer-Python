"""
entity.py

contains functions and objects that can be placed within the world

"""

import numpy as np

from collections.abc import Sequence
from typing import Union, List, Type
from dataclasses import dataclass


from . import vec3


# ------------------------------------------ #
# entity
@dataclass(init=False)
class Entity:
    """
    Entity
    - different types of entities
    """
    pos: vec3.Vector3

    def __init__(self, pos: vec3.Vector3):
        """Init function for Entity"""
        self.pos = pos



