import math

class AreaCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius**2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return sides[0]**2 + sides[1]**2 == sides[2]**2

    @staticmethod
    def calculate_area(shape_type, *args):
        if shape_type == 'circle':
            return AreaCalculator.circle_area(*args)
        elif shape_type == 'triangle':
            return AreaCalculator.triangle_area(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args).area()
        elif shape_type == 'square':
            return Square(*args).area()
        else:
            raise ValueError("Unsupported shape type")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return super().area()