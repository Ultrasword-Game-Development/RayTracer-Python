
class Test:
    def __init__(self):
        self.x = 0

    def __mul__(self, o):
        print(self.x* o)

    def __truediv__(self, o):
        print(self.x / o)

t = Test()
t.x = 100

t / 100
t * 12
