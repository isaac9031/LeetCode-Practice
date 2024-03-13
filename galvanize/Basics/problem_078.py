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
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi*self.radius

    def calculate_area(self):
        return math.pi * self.radius**2

circle = Circle(10)
print(circle.calculate_perimeter())
print(circle.calculate_area()) 
