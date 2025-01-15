from abc import ABC, abstractmethod
'''From class'''
# Incorrect 
# class Shape1():
#     def draw(self):
#         print('Drawing a square')

#     def draw_circle(self):
#         print('Drawing a circle')

'''From copilot'''
# Base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class extending Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle class extending Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function to calculate total area of multiple shapes
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

# Example usage
shapes = [Rectangle(2, 3), Circle(5)]
print("Total area:", total_area(shapes))