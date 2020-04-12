class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

    def get_x(self):
        return self.x

point = Point(10, 20)
print(point.x)

point.x = 20
print(point.get_x())