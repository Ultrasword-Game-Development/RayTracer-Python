# Welcome to the painful world known as python development
# Today we wil development a ray-tracer at minimal efficiency :)
# I love python!

from typing import List, Union, Tuple

import rtx
from rtx.io import image
from rtx import world, vec3, face, entity, camera, shape

# ------------------------------------------ #
# world tests
rworld = world.World()
re = entity.Entity([0, 0, 0], shape.Sphere([0, 0, 0], 1))
rworld.add_entity(re)
rworld.add_entity(entity.Entity([0, 0, 0], shape.Sphere([-3, 0, 0], 1)))
rworld.add_entity(entity.Entity([0, 0, 0], shape.Sphere([-3, 1, -1], 0.2)))
rworld.add_entity(entity.Entity([0, 0, 0], shape.Sphere([3, 0, 0], 2)))

# ------------------------------------------ #
# camera test
rcam = camera.Camera(vec3.Vector3([10, 0, 0]), vec3.Vector3([0, 0, 0]), (30.0, 30.0), 
                    (100,100), camera.ORTHO)

# test image save
buff = rcam.compute_rays(rworld)

# print(buff)
save = image.convert_buffer_to_uint32(buff)

# print(save)
image.save_to_file("assets/result.png", save)

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



