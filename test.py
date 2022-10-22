from rtx import vec


a = vec.Vector3([1, 1, 1])
b = vec.Vector3([2, -2, 2])

print(a, b)
print(a + b)
print(a - b)
print(a == b)
print(a.cross(b))
print(a.dot(b))



