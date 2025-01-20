from abc import ABC, abstractmethod

# Incorrect

# class WorkerInterface():
#     @abstractmethod
#     def work(self):
#         pass

#     @abstractmethod
#     def eat(self):
#         pass

# class Human(WorkerInterface):
#     def work(self):
#         return super().work()
    
#     def eat(self):
#         return super().eat()

# class Robot(WorkerInterface):
#     def work(self):
#         return super().work()
    
#     def eat(self):
#         pass

class WorkInterface(ABC):
    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(WorkInterface):
    def work(self):
        print('Robot working')


class Human(WorkInterface, EatInterface):
    def eat(self):
        print('Human eating')
    
    def work(self):
        print('Human working')

'''
Exercici:
Crear un gestor d'impressores

Requisits:
    - Tenim impressores en blanc i negre 
    - Impresores en color.
    - Impresores multifunció (imprimir, escanejar i enviar correus)

Instruccions:
    - Implementar un sistema, amb els diferents tipos d'impressores i funcions.
    - Aplicar el principi ISP
    - Comprovar que es compleix el principi
'''

class PrintBlackAndWhiteInterface(ABC):
    @abstractmethod
    def print(self, document):
        pass

class PrintColorInterface(ABC):
    @abstractmethod
    def print(self, document):
        pass

class ScanInterface(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class SendEmailInterface(ABC):
    @abstractmethod
    def send_email(self, document):
        pass

class BlackAndWhitePrinter(PrintBlackAndWhiteInterface):
    def print(self, document):
        print(f'Printing {document} on black and white')
    
class ColorPrinter(PrintColorInterface):
    def print(self, document):
        print(f'Printing {document} on color')

class MultifunctionPrinter(PrintColorInterface, ScanInterface, SendEmailInterface):
    def print(self, document):
        print(f'Printing {document} on color')
    
    def scan(self, document):
        print(f'Scanning {document}')
    
    def send_email(self, document):
        print(f'Sending {document} as an email')
