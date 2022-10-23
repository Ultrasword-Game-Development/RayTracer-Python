"""
The WORLD

ZAAAA WAAAAAAAAAAAAARRRUUUULLLLDDOOOOOOOOO

# ------------------------------------------ #

world.py

contains functions and objects that store the world (the thing that renderer renders) :D
"""

from typing import Union, List, Tuple, Dict

from . import entity
from . import camera


class World:
    """
    World
    - stores world data
    - objects, etc
    """

    def __init__(self) -> None:
        print("World was created!")
        self.entities: Dict[int, entity.Entity] = {}




