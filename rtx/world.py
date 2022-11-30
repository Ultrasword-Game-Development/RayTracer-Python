"""
The WORLD

ZAAAA WAAAAAAAAAAAAARRRUUUULLLLDDOOOOOOOOO

# ------------------------------------------ #

world.py

contains functions and objects that store the world (the thing that renderer renders) :D
"""

from typing import Union, List, Tuple, Dict

from . import entity, ray, vec3

UP: vec3.Vector3 = vec3.Vector3([0, 1, 0])


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
        return r.trace(self, [0.0, 0.0, 0.0, 0.0])
    
    def add_entity(self, ent: entity.Entity) -> None:
        """Add an entity to a world"""
        self.entities[ent.eid] = ent
    
    def remove_entity(self, eid: int) -> None:
        """Remove an entity from a world"""
        self.entities.pop(eid)




