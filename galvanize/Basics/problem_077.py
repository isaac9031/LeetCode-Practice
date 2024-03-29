# Write a class that meets these requirements.
#
# Name:       Circle
#
# Required state:
#    * radius, a non-negative value
#
# Behavior:
#    * calculate_perimeter()  # Returns the length of the perimater of the circle
#    * calculate_area()       # Returns the area of the circle
#
# Example:
#    circle = Circle(10)
#
#    print(circle.calculate_perimeter())  # Prints 62.83185307179586
#    print(circle.calculate_area())       # Prints 314.1592653589793
#
# There is pseudocode for you to guide you.
import math

class Circle:
    def __init__(self, radius):
        self.radius = abs(radius)

    def calculate_perimeter(self):
        return  2*math.pi*self.radius

    def calculate_area(self):
        return math.pi * self.radius**2

circle = Circle(20)
print(circle.calculate_perimeter())
print(circle.calculate_area())







# class Circle
    # method initializer with radius
        # if radius is less than 0
            # raise ValueError
        # self.radius = radius

    # method calculate_perimeter(self)
        # returns 2 * math.pi * self.radius

    # method calculate_area(self)
        # returns math.pi * (self.radius squared)
