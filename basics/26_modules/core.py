import models as m


list_books = []

def insert_book(isbn, author):
    list_books.append(m.Book
                      (isbn = isbn, 
                       author = author))

def print_books():
    for book in list_books:
        print(book)