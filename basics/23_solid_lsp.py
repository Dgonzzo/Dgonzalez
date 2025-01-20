'''From class'''
# Incorrect

# class Bird:
#     def fly(self):
#         print('Flying')

# class Chicken(Bird):
#     def fly(self):
#         raise Exception('No flying')

# bird = Bird()
# bird.fly()

# chicken = Chicken()
# chicken.fly()



'''From copilot'''
# Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of a subclass without affecting the functionality of the program.

# Base class for a Bird
class Bird:
    def fly(self):
        # Base class method for flying
        return "Flying"

# Derived class for a Sparrow, which is a type of Bird
class Sparrow(Bird):
    def fly(self):
        # Sparrow can fly, so we use the base class method
        return super().fly()

# Derived class for an Ostrich, which is a type of Bird but cannot fly
class Ostrich(Bird):
    def fly(self):
        # Ostrich cannot fly, so we override the method to reflect that
        return "Cannot fly"

# Function that makes a bird fly
def make_bird_fly(bird: Bird):
    # Calls the fly method of the bird object
    return bird.fly()

# Create instances of Sparrow and Ostrich
sparrow = Sparrow()
ostrich = Ostrich()

# Test the Liskov Substitution Principle
print(make_bird_fly(sparrow))  # Output: Flying
print(make_bird_fly(ostrich))  # Output: Cannot fly