'''
1️⃣ Explora el concepte d'herència segons Python. Crea un exemple que implementi una superclasse Animal i un parell de subclasses Ca i Moix, juntament amb una funció que serveixi per a imprimir el so que emet cada Animal.

DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣ Implementa la jerarquia d'una empresa de desenvolupament formada per Empleats que poden ser Gerents, Gerents de Projectes o Programadors.
3️⃣ Cada empleat té un identificador i un nom.
4️⃣ Depenent de la seva labor, tenen propietats i funcions exclusives de la seva activitat, i emmagatzemen els empleats a càrrec seu.
'''

# Main class

class Animal:
    def __init__(self, name:str, color:str) -> None:
        self.name = name
        self.color = color
        # self.type_animal = type_animal
    
    def sound(self):
        print('Not especified sound')


# Subclasses
class Dog(Animal):
    def sound(self):
        print('Woof')

class Cat(Animal):
    def sound(self): 
        print('Meow')

class Bird(Animal):
    def sound(self):
        print('Pio')

def print_sound(animal:Animal):
    animal.sound()


dog = Dog('Dog', 'Black')
cat = Cat('Cat', 'White')
bird = Bird('Bird', 'Yellow')

dog.sound()
cat.sound()

print_sound(dog)
print_sound(cat)
print_sound(bird)


class Employee:
    def __init__(self, name:str, id:str) -> None:
        self.name = name
        self.id = id
    
    def coordinate_project(self):
        return None
    

class Manager(Employee):
    def coordinate_project(self):
        return f"{self.name} coordinates all the projects"
    

class ProjectManager(Employee):
    def __init__(self, name: str, id: str, projects:list) -> None:
        super().__init__(name, id)
        self.projects = projects
    
    def coordinate_project(self):
        return f"{self.name} coordinates the projects: {self.projects}"
    

class Programer(Employee):
    def __init__(self, name: str, id: str, stack:list) -> None:
        super().__init__(name, id)
        self.stack = stack
    
    def code(self):
        return f"{self.name} is programming on {self.stack}"
        

my_programers = [Programer('Lara', 'TZ983', ['Python']), Programer('Charles', 'BD384',['Cpp', 'C']), Programer('Alba', 'GB234', ['Haskell', 'Rust'])]
my_project_managers = [ProjectManager('Michael', 'DA883', ['App', 'Shopify']), ProjectManager('David', 'OC234', ['App'])]
my_managers = [Manager('John', 'AB001')]

for per in my_project_managers:
    print(per.coordinate_project())