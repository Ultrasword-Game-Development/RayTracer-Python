# Welcome to the painful world known as python development
# Today we wil development a ray-tracer at minimal efficiency :)
# I love python!

from typing import List, Union, Tuple

import rtx
from rtx.io import image
from rtx import world


rworld = world.World()

# arr = [[0xff3ffac3 for i in range(10)] for j in range(10)]

arr = image.convert_buffer_to_uint32([[(255, 255, 255, 255), (255, 255, 255, 255)] for i in range(30)])

image.save_to_file("assets/result.png", arr)
print("saved file")


