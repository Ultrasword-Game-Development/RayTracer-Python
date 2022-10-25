"""
The WORLD

ZAAAA WAAAAAAAAAAAAARRRUUUULLLLDDOOOOOOOOO

# ------------------------------------------ #

world.py

contains functions and objects that store the world (the thing that renderer renders) :D
"""

from typing import Union, List, Tuple, Dict

from . import entity, camera, ray


class World:
    """
    World
    - stores world data
    - objects, etc
    """

    def __init__(self) -> None:
        """Init function for World"""
        print("World was created!")
        self.entities: Dict[int, entity.Entity] = {}
    
    def handle_ray(self, r: ray.Ray) -> List[float]:
        """Handles the ray intersection in a world"""
        return [0, 0, 0, 0]




