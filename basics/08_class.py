'''
1️⃣ Explora el concepte de classe i crea un exemple que implementi un inicialitzador, atributs i una funció que els imprimeixi (tenint en compte les possibilitats del llenguatge).
2️⃣ Una vegada implementada, crea-la, estableix els seus paràmetres, modifica'ls i imprimeix-los utilitzant la seva funció.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣Implementa dues classes que representin les estructures de Pila i Cua (estudiades en l'apartat 07 de la ruta d'estudi)

    Han de poder inicialitzar-se i disposar d'operacions per a afegir, eliminar, retornar el nombre d'elements i imprimir tot el seu contingut.
'''

class Programmer:
    
    level: str = 'Junior'
    def __init__(self, name:str, age:int, stack:list) -> None:
        self.name = name
        self.age = age
        self.stack = stack
    
    def __str__(self) -> str:
        return f"Name: {self.name} \nAge: {self.age} \n\tStack: {self.stack} \n\tLevel: {self.level}" # \n newline \t tab


my_programmer = Programmer('Daniel', 17, ['Python', 'Javascript'])
my_programmer.age = 22
my_programmer.level = 'Mid-senior' # Changes default value
# print(my_programmer.age, my_programmer.level)

print(my_programmer)


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)
    
    def pop(self) -> any: 
        pop_item = self.stack[-1]
        del self.stack[-1]
        return pop_item
    
    def print(self) -> None:
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()

my_stack.push('a')
my_stack.push('b')
my_stack.push('c')

my_stack.print()

pop_item = my_stack.pop()
print(f'Eliminated item: {pop_item}')
pop_item = my_stack.pop()
print(f'Eliminated item: {pop_item}')

my_stack.print()


class Queue:
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self) -> any:
        dequeue_item = self.queue[0]
        del self.queue[0]
        return dequeue_item

    def print(self) -> None:
        for item in self.queue:
            print(item)

my_queue = Queue()

my_queue.enqueue('Doc A')
my_queue.enqueue('Doc B')
my_queue.enqueue('Doc C')

my_queue.print()

my_dequeued_item = my_queue.dequeue()
print(f'Dequeued item: {my_dequeued_item}')
my_dequeued_item = my_queue.dequeue()
print(f'Dequeued item: {my_dequeued_item}')

my_queue.print()
