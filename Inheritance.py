#@Author Prathamesh More
"""
Instead of starting from a scratch, you can create a class by deriving it from a pre-existing
class by listing the parent class in parentheses after the new class name.
The child class inherits the attributes of its parent class, and you can use those attributes
as if they were defined in the child class. A child class can also override data members and
methods from the parent
"""


class Area:

    height = 0
    width = 0

    def __init__(self, height, width):

        Area.width = width
        Area.height = height
        print("Calling from Parent Constructor")


class Rectangle(Area):

    areaRectangle = 0

    def __init__(self, w, h):
        print("Printing from Rectangle Class")
        Rectangle.height = h
        Rectangle.width = w

    def calculateAreaOfRectangle(self):

        Rectangle.areaRectangle = Rectangle.width * Rectangle.height

        print("Area of Rectangle ", Rectangle.areaRectangle)


class Triangle(Area):

    areaTriangle = 0
    base = 0

    def __init__(self, height, base):

        print("Printing from Triangle Class")
        Triangle.height = height
        Triangle.base = base

    def calculateAreaOfTriangle(self):

        Triangle.areaTriangle = Triangle.base * Triangle.height
        print("Area of Triangle ", Triangle.areaTriangle)


class Square(Area):

    areaSquare = 0

    def __init__(self, height):

        print("Printing from Square Class")
        Square.height = height

    def calculateAreaOfSquare(self):

        Square.areaSquare = Square.height * Square.height
        print("Area of Square ", Square.areaSquare)


r = Rectangle(20, 20)
r.calculateAreaOfRectangle()

t = Triangle(10, 20)
t.calculateAreaOfTriangle()

q = Square(10)
q.calculateAreaOfSquare()