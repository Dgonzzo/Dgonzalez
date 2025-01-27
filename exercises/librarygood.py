from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @abstractmethod
    def print_info(self):
        # available = 'Available' if self.status else 'Borrowed'
        # print(f'Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}')
        pass

class PrintedBook(Book):
    def __init__(self, title, author, status):
        super().__init__(title, author)
        # self.title = title
        # self.author = author
        self.status = status
    
    def print_info(self):
        # available = 'Available' if self.status else 'Borrowed'
        print(f'[Physical] Title: {self.title}\nAuthor: {self.author}\nStatus: {self.status}')

class DigitalBook(Book):    
    def print_info(self):
        # available = 'Available' if self.status else 'Borrowed'
        print(f'[Digital] Title: {self.title}\nAuthor: {self.author}\nStatus: always available')

class Library():
    def __init__(self, report_generator):
        self.books = []
        self.report_generator = report_generator
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            book.print_info()
    
    def borrow_book(self, book):
        for b in self.books:
            if b.title == book.title and b.status == 'Available':
                if b.status:
                    b.status = 'Borrowed'
                    print(f'{b.title} borrowed successfully')
                    break
        else: # Only executes when entire loop is completed without break
            print(f'{book.title} is already borrowed or is not in the library')

    def generate_report(self):
        self.report_generator.generate(self.books)    

class ReportInterface(ABC):
    @abstractmethod
    def generate(self, books):
        pass

class TextReport(ReportInterface):
    def generate(self, books):
        print("Book's report:")
        for book in books:
            book.print_info()

book_1 = PrintedBook('The Hobbit', 'J.R.R. Tolkien', 'Available')
book_2 = DigitalBook('The Lord of Rings', 'J.R.R. Tolkien')

my_library = Library(TextReport())

my_library.add_book(book_1)
my_library.add_book(book_2)
my_library.generate_report()