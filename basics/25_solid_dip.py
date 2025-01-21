from abc import ABC, abstractmethod

'''From class'''
# Incorrect
# class Switch:
#     def turn_on(self):
#         print('Turning on the lamp')
    
#     def turn_off(self):
#         print('Turning off the lamp')

# class Lamp:
#     def __init__(self):
#         self.switch = Switch()
    
#     def operate(self, command):
#         if 'on' == command:
#             self.switch.turn_on()
#         else:
#             self.switch.turn_off()

class SwitchInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ClassicSwitch(SwitchInterface):
    def turn_on(self):
        print('Turn on the lamp')
   
    def turn_off(self):
        print('Turn off the lamp')


class AutomaticSwitch(SwitchInterface):
    def turn_on(self):
        print('Movemente detected, turning on')
    
    def turn_off(self):
        print('Turning off automatically')

class Lamp:
    def __init__(self, switch:SwitchInterface):
        self.switch = switch
    
    def operate(self, command):
        if 'on' == command:
            self.switch.turn_on()
        
        else:
            self.switch.turn_off()
        
# lamp_1 = Lamp(ClassicSwitch())
# lamp_1.operate('on')

# lamp_2 = Lamp(AutomaticSwitch())
# lamp_2.operate('on')

'''
Exercise: Create a notification system

Requirements:
    - Send Email, Push & SMS (specific implementations)
    - The system can not depend of the specific implementations

Instructions:
    - Create the interface or abstract class
    - Make the specific implementations
    - Create a notifications system using DIP
'''

class NotificationInterface(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Email(NotificationInterface):
    def send(self, message):
        print(f'The email with the message:{message} was sent')

class PUSH(NotificationInterface):
    def send(self, message):
        print(f'The email with the PUSH:{message} was sent')

class SMS(NotificationInterface):
    def send(self, message):
        print(f'The email with the SMS:{message} was sent')

class NotificationService:
    def __init__(self, notification:NotificationInterface):
        self.notification = notification
    
    def notify(self, message):
        self.notification.send(message)

noti_1 = NotificationService(Email())
noti_1.notify('Hii')

noti_2 = NotificationService(SMS())
noti_2.notify(':)')


'''From copilot'''

"""
This module demonstrates the Dependency Inversion Principle (DIP) from the SOLID principles of object-oriented design.

The Dependency Inversion Principle states that:
1. High-level modules should not depend on low-level modules.
Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

In this context, high-level modules are the components that contain complex logic and low-level modules are the components that perform basic operations. By depending on abstractions (interfaces or abstract classes), we can change the low-level modules without affecting the high-level modules, promoting flexibility and maintainability in the codebase.
"""

# Abstraction
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

# Low-level module
class FileDataSource(DataSource):
    def get_data(self):
        return "Data from file"

# Low-level module
class APIDataSource(DataSource):
    def get_data(self):
        return "Data from API"

# High-level module
class DataProcessor:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def process_data(self):
        data = self.data_source.get_data()
        return f"Processed {data}"

# Client code
file_data_source = FileDataSource()
api_data_source = APIDataSource()

file_processor = DataProcessor(file_data_source)
api_processor = DataProcessor(api_data_source)

# print(file_processor.process_data())
# print(api_processor.process_data())