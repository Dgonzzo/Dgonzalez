import core as c

print('Insert books')

author = input('Author: ')
isbn = input('ISBN: ')
name = input('Name: ')
title = input('Title: ')
pages = input('Pages: ')
c.insert_book(author=author, isbn=isbn)
c.print_books()