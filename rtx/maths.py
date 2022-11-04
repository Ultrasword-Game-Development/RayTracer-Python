"""
Maths library for random stuff
"""

import math
from typing import List, Union, Tuple

from . import vec3


def solve_quadratic(a: float, b: float, c: float) -> Tuple[int, List[float]]:
    """Solve the quadratic equation"""
    # find discrim
    discrim = b * b - 4 * a * c
    # print(discrim)
    # return no answers
    if discrim < 0:
        return (0, [])
    elif discrim == 0:
        # one answer
        return (1, [-b / 2 / a])
    else:
        # two answers
        return (2, [(-b + discrim) / 2 / a, (-b - discrim) / 2 / a])


def copy_vector(vec: vec3.Vector3) -> vec3.Vector3:
    """Copy a vector"""
    return vec3.Vector3(vec.arr.copy())
