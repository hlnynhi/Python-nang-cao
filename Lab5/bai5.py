import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def slope(self):
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

segment = LineSegment(Point(1, 1), Point(3, 2))
print(segment.slope())
print(segment.length())