import xml.etree.ElementTree as xml
import os
import time
import datetime
from abc import ABC, abstractmethod

file_name = 'inventory.xml'

class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, books):
        pass

class Book():
    def __init__(self, title, author, released_date:datetime, genre, age_clasification, language, isbn, price):
        self.title = title
        self.author = author
        self.released_date = released_date
        self.genre = genre
        self.age_clasification = age_clasification
        self.language = language
        self.isbn = isbn
        self.price = price

    def change_author(self, new_author):
        self.author = new_author
    
    def release_date(self, new_date:datetime):
        self.released_date = new_date

    def change_genre(self, new_genre):
        self.genre = new_genre
    
    def change_age_clasification(self, new_age_clasification):
        self.age_clasification = new_age_clasification
    
    def change_language(self, new_language):
        self.language = new_language
    
    def change_isbn(self, new_isbn):
        self.isbn = new_isbn

    def change_price(self, new_price):
        self.price = new_price

class Library():
    def __init__(self, report_generator):
        self.books = []
        self.report_generator = report_generator

    def add_book(self, book):
        self.books.append(book)
    
    def delete_book(self, book):
        self.books.remove(book)
    
    def update_book(self, book):
        for item in self.books:
            if book.title == item.title:
                # print('Book updated')
                break
        else:
            print('Book not found')
    
    def get_elements(self):
        tree = xml.parse(file_name)

        for book in tree.getroot():
            book = Book(book.find('title').text, book.find('author').text, datetime.datetime.strptime(book.find('released_date').text, '%d-%m-%Y'), book.find('genre').text, book.find('age_clasification').text, book.find('language').text, book.find('isbn').text, float(book.find('price').text))
            self.add_book(book)
        

    # def generate(self, books):
    #     return super().generate(books)

class TerminalReportGenerator(ReportGeneratorInterface):
    def generate(self, books):
        print('Books in inventory: ')
        for book in books:
            print(f'Title: {book.title}')

class XMLReportGenerator(ReportGeneratorInterface):
    def generate(self, books, root):
        # root = xml.Element('books')
        
        for book in books:
            book_element = xml.Element('book')
            root.append(book_element)

            title = xml.SubElement(book_element, 'title')
            title.text = book.title

            author = xml.SubElement(book_element, 'author')
            author.text = book.author

            released_date = xml.SubElement(book_element, 'released_date')
            released_date.text = book.released_date.strftime(f'%d-%m-%Y')

            genre = xml.SubElement(book_element, 'genre')
            genre.text = book.genre

            age_clasification = xml.SubElement(book_element, 'age_clasification')
            age_clasification.text = book.age_clasification

            language = xml.SubElement(book_element, 'language')
            language.text = book.language

            isbn = xml.SubElement(book_element, 'isbn')
            isbn.text = book.isbn
            
            price = xml.SubElement(book_element, 'price')
            price.text = str(book.price)
    
        tree = xml.ElementTree(root)
        tree.write(file_name)
    
    def delete(self, title_book_to_delete):
        tree = xml.parse(file_name)

        temp_file = xml.Element('Inventory')

        for book in tree.getroot():
            if book.tag == title_book_to_delete:
                print(f'Book {title_book_to_delete} deleted')
            else:
                temp_file.append(book)
        
        tree = xml.ElementTree(temp_file)
        tree.write(file_name)

def main():
    try:
        tree = xml.parse(file_name)
        root = tree.getroot()
        my_library = Library(XMLReportGenerator()).get_elements()
    
    except:
        root = xml.Element('Inventory')
    my_library = Library(XMLReportGenerator())

    XMLReportGenerator().generate(my_library.books, root)

    while True:
        print('1. Add book')
        print('2. Delete book')
        print('3. Update book')
        print('4. Generate report')
        print('[q] for quit\n')
        user_input = input('Choose an option: ')
        
        if '1' == user_input:
            try:
                add_book = Book(input('Title: '), input('Author: '), datetime.datetime.strptime(input('Release date (dd-mm-yyyy): ').strip(), '%d-%m-%Y'), input('Genre: '), input('Age clasification: '), input('Language: '), input('ISBN: '), float(input('Price: ')))
                my_library.add_book(add_book)
            except ValueError as e:
                print(f'Invalid input: {e} \n')

        elif '2' == user_input:
            title_book_to_delete = input('Title of the book to delete: ')
            # XMLReportGenerator().delete(title_book_to_delete, root)

        elif '3' == user_input:
            pass

        elif '4' == user_input:
            pass

        elif 'q' == user_input.lower():
            break
        
        else:
            print('Invalid option\n')
        
        XMLReportGenerator().generate(my_library.books, root)

my_library = Library('xml')

my_book = Book('The Hobbit', 'J.R.R. Tolkien', datetime.date(day=27, month=6, year=1937), 'Fantasy', 'PG-13', 'English', '978-3-16-148410-0', 10.99)
# not_my_book = Book('The Pillars of the Earth', 'Ken Follet', datetime.datetime(2, 10, 1987), 'Historical Fiction', 'R', 'English', '978-0-451-16002-6', 9.99)

my_library.add_book(my_book)
my_library.update_book(my_book)

if __name__ == '__main__':
    main()
