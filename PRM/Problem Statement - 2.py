class Triangle:
    def __init__(self, x, y, z):
        self.sides = [x, y, z]

    def validate_triangle(self):
        self.sides.sort()
        if (self.sides[0] + self.sides[1]) > self.sides[2]:
            print("Valid Triangle")
        else:
            print("Invalid Triangle")


class Rectangle:
    def __init__(self, m, n, o, p):
        self.sides = [m, n, o, p]

    def validate_rectangle(self):
        if self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")


a, b, c = map(int, input().split())
triangle = Triangle(a, b, c)
a, b, c, d = map(int, input().split())
rectangle = Rectangle(a, b, c, d)

triangle.validate_triangle()
rectangle.validate_rectangle()
