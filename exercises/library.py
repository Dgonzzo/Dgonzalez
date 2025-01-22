from abc import ABC, abstractmethod

class PhysicalBookInterface(ABC):
    @abstractmethod
    def borrowable(self):
        pass

class EBookInterface(ABC):
    @abstractmethod
    def borrowable(self):
        pass

class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, new_element):
        pass
    
    @abstractmethod
    def eliminate(self, element):
        pass

    @abstractmethod
    def change_status(self, element, status):
        pass

class ReportGeneratorInterface(ABC):
    @abstractmethod
    def print_all(self):
        pass
    
    @abstractmethod
    def print_borrowed(self):
        pass

    @abstractmethod
    def print_available(self):
        pass

    @abstractmethod
    def print_physical(self):
        pass

    @abstractmethod
    def print_ebooks(self):
        pass


class Book():
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

class Library(DatabaseInterface, ReportGeneratorInterface):
    def __init__(self):
        self.inventory = {}
    
    # Database interface
    def save(self, new_element:Book):
        self.inventory[new_element.title] = new_element
    
    def eliminate(self, element:Book):
        del self.inventory[element.title]
    
    def change_status(self, element:Book, status):
        self.inventory[element.title].status = status
    
    # Report Interface
    def print_available(self):
        print('All available books')
        for k,v in self.inventory:
            if 'Available' == v.status:
                print(f'# {k}')
    
    def print_available(self):
        print('All borrowed books')
        for k,v in self.inventory:
            if 'Not Available' == v.status:
                print(f'# {k}')
    
    def print_all(self):
        print('All books')
        for k in self.inventory:
            print(f'# {k}')
    
    def print_ebooks(self):
        pass

    def print_physical(self):
        pass
    