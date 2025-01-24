from abc import ABC, abstractmethod

# class Borrowable(ABC):
#     @abstractmethod
#     def borrow(self):
#         pass

class FormatBookInterface(ABC):
    @abstractmethod
    def borrow(self):
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

    @abstractmethod
    def borrow(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

class Book(FormatBookInterface):
    def __init__(self, title, author, status, book_type):
        self.title = title
        self.author = author
        self.status = status
        self.book_type = book_type
    
    # def format(self):
    #     if 'Ebook' == self.book_type:
    #         return False
    #     else:
    #         return True 
    
    def borrow(self):
        if self.book_type == 'Physical':
            return True
        return False

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
        for book in self.inventory.values():
            if 'Available' == book.status:
                print(f'# {book.title}')
    
    def print_borrowed(self):
        print('All borrowed books')
        for book in self.inventory.values():
            if 'Not Available' == book.status:
                print(f'# {book.title}')
    
    def print_all(self):
        print('All books')
        for book in self.inventory.values():
            print(f'# {book.title}')
    
    def print_ebooks(self):
        print('All ebooks')
        for book in self.inventory.values():
            if 'Ebook' == book.book_type:
                print(f'# {book.title}')

    def print_physical(self):
        print('All physical books')
        for book in self.inventory.values():
            if 'Physical' == book.book_type:
                print(f'# {book.title}')

    def borrow(self, book:Book):
        if book.borrow() and 'Available' == book.status:
            self.change_status(book, 'Not Available')
        else:
            print(f'{book.title} is not borrowable')
    
    def return_book(self, book:Book):
        if 'Not Available' == book.status and book.borrow():
            self.change_status(book, 'Available')
        if 'Available' == book.status and book.borrow():
            print(f'{book.title} was already returned')
        else:
            print(f'{book.title} is not borrowable')

my_library = Library()

book1 = Book('The Hobbit', 'J.R.R. Tolkien', 'Available', 'Physical')
my_library.save(book1)

my_library.print_all()

my_library.print_physical()

my_library.print_available()

my_library.borrow(book1)

my_library.print_available()
my_library.print_borrowed()

book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien', 'Available', 'Ebook')
my_library.save(book2)

my_library.print_all()
