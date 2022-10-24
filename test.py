from rtx import ray, vec3, maths

from typing import List


pos = vec3.Vector3([0, 0, 0])
radius = 3
r = ray.Ray(vec3.Vector3([3, 3, 0]), vec3.Vector3([-1, 0, 0]))

# first calculation
i: List[float] = [
    r.origin.x - pos.x,
    r.origin.y - pos.y,
    r.origin.z - pos.z
]
# non variable values
nvv: List[float] = [
    i[0] * i[0],
    i[1] * i[1],
    i[2] * i[2]
]

# one variable values
ovv: List[float] = [
    -2 * i[0] * r.direction.x,
    -2 * i[1] * r.direction.y,
    -2 * i[2] * r.direction.z
]

# variable squared
tvv: List[float] = [
    r.direction.x * r.direction.x,
    r.direction.y * r.direction.y,
    r.direction.z * r.direction.z
]

# find final equation - 0 = t^2, 1 = t, 2 = 0
final: List[float] = [sum(tvv), sum(ovv), sum(nvv) - radius] # all this equals = 0

print(final)

print(maths.solve_quadratic(final[0], final[1], final[2]))