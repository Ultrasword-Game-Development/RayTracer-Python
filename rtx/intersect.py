"""
intersect.py

- contains objects specifically for information storage
- stores info about collisions / intersections between ray and shapes
"""

from typing import List, Union, Tuple
from dataclasses import dataclass

from . import vec3
from . import ray

# ------------------------------------------ #
# collisions/interceptions

@dataclass
class Collision:
    """
    Collision

    - stores collision data between rays and shapes/objects/meshes
    """

    has_collision: bool
    iray: ray.Ray
    cpos: vec3.Vector3

    def __init__(self, incident_ray: Union[ray.Ray, None], collision_pos: Union[vec3.Vector3, None]) -> None:
        """Init function for the Collision object"""
        self.iray = incident_ray if incident_ray else ray.Ray(vec3.Vector3([0,0,0]), vec3.Vector3([0,0,0]))
        self.cpos = collision_pos if collision_pos else ray.Ray(vec3.Vector3([0,0,0]), vec3.Vector3([0,0,0]))
        if not incident_ray or not collision_pos:
            self.has_collision = False
    
    @property
    def incident_ray(self) -> ray.Ray:
        """Get the incident ray"""
        return self.iray
    
    @property
    def collision_point(self) -> vec3.Vector3:
        """Get the collision point"""
        return self.cpos
    
    @property
    def collided(self) -> bool:
        """Returns if there was a collision"""
        return self.has_collision


