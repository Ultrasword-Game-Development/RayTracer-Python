"""
entity.py

contains functions and objects that can be placed within the world

"""

import numpy as np

from collections.abc import Sequence
from typing import Union, List, Type
from dataclasses import dataclass


from . import vec3, shape as s


# ------------------------------------------ #
# methods

ENTITY_COUNT = 0

def get_entity_id() -> int:
    """Get an entity id"""
    global ENTITY_COUNT
    ENTITY_COUNT += 1
    return ENTITY_COUNT


# ------------------------------------------ #
# entity

@dataclass(init=False)
class Entity:
    """
    Entity
    - different types of entities
    """
    pos: vec3.Vector3
    eid: int
    shape: s.Shape

    def __init__(self, pos: Union[vec3.Vector3, List[Union[int, float]]], shape: s.Shape, eid: int = get_entity_id()):
        """Init function for Entity"""
        self.pos = pos if isinstance(pos, vec3.Vector3) else vec3.Vector3(pos)
        self.shape = shape
        self.eid = eid
        print(self)

    def __repr__(self) -> str:
        """Represent this value in console"""
        return f"eid: {self.eid}, pos: {self.pos}"    



