class Vehicle:
    def __init__(self, brand:str, color:str) -> None:
        self.brand = brand
        self.color = color

    def num_wheels(self):
        return None
    
class Car(Vehicle):
    def num_wheels(self):
        return 4

class Motorbike(Vehicle):
    def num_wheels(self):
        return 2

class Boat(Vehicle): 
    def num_wheels(self):
        return 0
    

my_car1 = Car("Mercedes-Benz", "White")
my_car2 = Car("Volkswagen", "Black")

my_motorbycicle = Motorbike("BMW", "Red")

my_boat = Boat("Balearia", "White")

print(my_boat.num_wheels())