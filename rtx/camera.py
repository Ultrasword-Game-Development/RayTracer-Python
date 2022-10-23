"""
camera.py

contains functions and objects for the camera (basically the renderer but not really)

"""

from collections.abc import Sequence
from typing import List, Union, Tuple

from . import vec3
from . import ray


# ------------------------------------------ #
# camera

class Camera:
    """
    Camera
    - is what allows the user to see the world :)
    """

    def __init__(self, pos: vec3.Vector3) -> None:
        """Init function for a camera"""
        self.pos = pos

