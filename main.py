# Welcome to the painful world known as python development
# Today we wil development a ray-tracer at minimal efficiency :)
# I love python!

from typing import List, Union, Tuple

import rtx
from rtx.io import image
from rtx import world, vec, face

# ------------------------------------------ #
# world tests
# rworld = world.World()

# ------------------------------------------ #
# image test
# arr = image.convert_buffer_to_uint32([[(255, 255, 255, 255), (255, 255, 255, 255)] for i in range(30)])
# image.save_to_file("assets/result.png", arr)
# print("saved file")


# ------------------------------------------ #
# math testing
a = vec.Vector3(-2, -2, 0)
b = vec.Vector3(-2, -1, 0)

print(a)
print(b)

# add
print(a + b)
print(a - b)
print(a.dot(b))
