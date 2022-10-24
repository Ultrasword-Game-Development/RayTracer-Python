# Welcome to the painful world known as python development
# Today we wil development a ray-tracer at minimal efficiency :)
# I love python!

from typing import List, Union, Tuple

import rtx
from rtx.io import image
from rtx import world, vec3, face, entity, camera

# ------------------------------------------ #
# world tests
rworld = world.World()
re = entity.Entity([10, 10, 10])

# ------------------------------------------ #
# camera test
rcam = camera.Camera(vec3.Vector3([1, 1, 1]), vec3.Vector3([0, 0, 0]), (1.0, 1.0), (100, 100), camera.ORTHO)


# ------------------------------------------ #
# image test
# arr = image.convert_buffer_to_uint32([[(255, 255, 255, 255), (255, 255, 255, 255)] for i in range(30)])
# image.save_to_file("assets/result.png", arr)
# print("saved file")

# ------------------------------------------ #
# math testing
# a = vec3.Vector3([-2, -2, 0])
# b = vec3.Vector3([-2, -1, 0])

# print(a, b)
# print(a + b)
# print(a - b)
# print(a.cross(b))
# print(a.dot(b))



