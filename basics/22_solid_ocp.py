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


''' ** Prompt
Develop a a calculator that enables to make diferent operations
First part: sum, sub, multiplication and division
Second part: potencies
'''

# Base class for operations
class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# Addition operation
class Addition(Operation):
    def execute(self, a, b):
        return a + b

# Subtraction operation
class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

# Multiplication operation
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

# Division operation
class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError() # ValueError("Cannot divide by zero")
        return a / b

# Potency operation
class Potency(Operation):
    def execute(self, a, b):
        return a ** b

# Calculator class
class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.execute(a, b)

# Example usage
add = Calculator(Addition())
print("Addition:", add.calculate(5, 3))

sub = Calculator(Subtraction())
print("Subtraction:", sub.calculate(5, 3))

mul = Calculator(Multiplication())
print("Multiplication:", mul.calculate(5, 1))

div = Calculator(Division())
print("Division:", div.calculate(5, 1))

pot = Calculator(Potency())
print("Potency:", pot.calculate(5, 3))