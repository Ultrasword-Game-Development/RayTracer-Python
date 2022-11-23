"""
intersect.py

- contains objects specifically for information storage
- stores info about collisions / intersections between ray and shapes
"""

from typing import List, Union, Tuple
from dataclasses import dataclass

from . import vec3, ray

# ------------------------------------------ #
# collisions/interceptions

@dataclass
class Collision:
    """
    Collision

    - stores collision data between rays and shapes/objects/meshes
    """

    iray: ray.Ray
    cpos: vec3.Vector3

    def __init__(self, incident_ray: ray.Ray, collision_pos: vec3.Vector3) -> None:
        """Init function for the Collision object"""
        self.iray = incident_ray
        self.cpos = collision_pos
    
    @property
    def incident_ray(self) -> ray.Ray:
        """Get the incident ray"""
        return self.iray
    
    @property
    def collision_point(self) -> vec3.Vector3:
        """Get the collision point"""
        return self.cpos
    
    def __repr__(self) -> str:
        """Represent the collision"""
        return f"Collision with ray at: {self.cpos}"


