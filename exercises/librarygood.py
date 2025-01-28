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

class BorrowableInterface(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

class BorrowablePrintedBook(PrintedBook, BorrowableInterface):
    def borrow(self):
        if self.status == 'Available':
            self.status = 'Borrowed'
            print(f'{self.title} borrowed successfully')
        else:
            print(f'{self.title} is already borrowed')
    
    def return_book(self):
        self.status = 'Available'
        print(f'{self.title} returned successfully')

class ReportInterface(ABC):
    @abstractmethod
    def generate(self, books):
        pass        

class Library():
    def __init__(self, report_generator):
        self.books = []
        self.report_generator = {}
    
    def add_generator(self, name, reportGenerator):
        self.report_generator[name] = reportGenerator
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            book.print_info()
    
    def borrow_book(self, book):
        if isinstance(book, BorrowableInterface):
            book.borrow()
        else:
            print(f'{book.title} is not borrowable')
        
        # for b in self.books:
        #     if b.title == book.title and b.status == 'Available':
        #         if b.status:
        #             b.status = 'Borrowed'
        #             print(f'{b.title} borrowed successfully')
        #             break
        # else: # Only executes when entire loop is completed without break
        #     print(f'{book.title} is already borrowed or is not in the library')

    def return_book(self, book):
        if isinstance(book, BorrowableInterface):
            book.return_book()
        else:
            print(f'{book.title} can not be returned')

    def generate_report(self, name):
        self.report_generator[name].generate(self.books)    
        
class TextReport(ReportInterface):
    def generate(self, books):
        print("Book's report:")
        for book in books:
            book.print_info()

book_1 = BorrowablePrintedBook('The Hobbit', 'J.R.R. Tolkien', 'Available')
book_2 = DigitalBook('The Lord of Rings', 'J.R.R. Tolkien')
book_3 = BorrowablePrintedBook('The Silmarillion', 'J.R.R. Tolkien', 'Available')


my_library = Library(TextReport())

my_library.add_book(book_1)
my_library.add_book(book_2)
my_library.add_book(book_3)

my_library.generate_report('CSV')

my_library.borrow_book(book_1)
my_library.borrow_book(book_2)

my_library.generate_report('JSON')
