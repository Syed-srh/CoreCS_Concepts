# 3: Shape Area Calculator (Polymorphism)
# Complete the  Shape, Circle, and Rectangle classes.

# Shape class:
# Add method:
# area() : Prints generic message
# Circle class:
# Inherits from Shape.

# Add attribute:
# radius
# Override:
# area() : Calculate and print area
# Rectangle class:
# Inherits from Shape.

# Add attributes:
# length
# breadth
# Override:
# area() : Calculate and print area


class Shape:
    def area(self):
        print("Area of the shape")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of the circle: {3.14 * self.radius ** 2}")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of the rectangle: {self.length * self.width}")

# Create a list of shape objects
shapes = [Circle(5), Rectangle(4, 6)]
# Call area() using a loop
for shape in shapes:
    shape.area()