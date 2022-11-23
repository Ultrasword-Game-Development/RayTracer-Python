"""
camera.py

contains functions and objects for the camera (basically the renderer but not really)

"""

from collections.abc import Sequence
from typing import List, Union, Tuple

from . import vec3, ray, world, maths, intersect


# ------------------------------------------ #
# view types

ORTHO: int = 0
PERSP: int = 1

# ------------------------------------------ #
# camera

class Camera:
    """
    Camera
    - is what allows the user to see the world :)
    """

    def __init__(self, pos: vec3.Vector3, target: vec3.Vector3, viewport: Tuple[float, float], resolution: Tuple[int, int], view_type: int) -> None:
        """Init function for a camera"""
        self.pos = pos
        self.target = target
        self.viewport = viewport
        self.res = resolution
        self.view_type = view_type
        # calculate vector from position to target
        print("camera.py | when testing, if camera is inverted or objects do not appear, try reversing lookat vector")
        la = [self.target.x - self.pos.x, self.target.y - self.pos.y, self.target.z - self.pos.z]
        self.lookat = vec3.Vector3(la) * -1
        self.lookat.normalize()
        # print(maths.copy_vector(self.lookat))
        # calculate view vectors
        self.rays: List[List[ray.Ray]] = self.generate_orthographic_rays() if self.view_type == ORTHO else self.generate_perspective_rays()
        # ray collision events
        self.collision_events: List[intersect.Collision] = []

    def generate_orthographic_rays(self) -> List[List[ray.Ray]]:
        """Generate rays for orthographic viewport"""
        result: List[List[ray.Ray]] = []
        half: Tuple[float, float] = (self.viewport[0] / 2, self.viewport[1] / 2)
        ww: Tuple[float, float] = (self.viewport[0]/self.res[0], self.viewport[1]/self.res[1])
        # generate vectors
        for y in range(self.res[1]):
            result.append([])
            for x in range(self.res[0]):
                # generate ray
                pos: List[float] = [self.pos.x - half[0] + ww[0] * x, self.pos.y - half[1] + ww[1] * y, self.pos.z]
                result[y].append(ray.Ray(vec3.Vector3(pos), maths.copy_vector(self.lookat)))
        print(result[0][0].direction)
        return result

    def generate_perspective_rays(self) -> List[List[ray.Ray]]:
        """Generate rays for perspective viewport"""
        pass

    def compute_rays(self, rworld: world.World) -> List[List[Tuple[int, int, int, int]]]:
        """Compute all the rays and calculate an image"""
        result: List[List[Tuple[int, int, int, int]]] = []
        for y in range(self.res[1]):
            result.append([])
            for x in range(self.res[0]):
                pix: List[float] = [0, 0, 0, 0]
                # calculate pixel values
                rgba: List[float] = rworld.handle_ray(self.rays[y][x])
                # collisions!!!
                # append to buf
                result[y].append((int(rgba[0]*255), int(rgba[1]*255), int(rgba[2]*255), int(rgba[3]*255)))
                # print(result[y][x])
        print("we need collisions ln 73 camera.py")
        return result
