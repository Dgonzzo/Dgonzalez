class Book:
    def __init__(self, isbn='-1', name='', author='' , pages=0):
        self.isbn = isbn
        self.name = name 
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.isbn} - {self.name} - {self.author} - {self.pages}'