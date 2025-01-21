from abc import ABC, abstractmethod

class DatabaseInterface():
    @abstractmethod
    def save(self, new_element):
        pass
    
    @abstractmethod
    def eliminate(self, element):
        pass


class Book():
    def __init__(self, title, author, state):
        self.title = title
        self.author = author
        self.state = state
