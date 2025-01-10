
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
'''
    def __init__(self):
        pass
'''
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1, singleton2)

class UserSession:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, id, name):
        self.id = id
        self.name = name
    
    def clear_user(self):
        self.id = None
        self.name = None
    
    def get_user(self):
        print(f'{self.id} - {self.name}')

session1 = UserSession()
session1.set_user('1', 'Z0KEER')

session1.get_user() 

session2 = UserSession()
session2.get_user()
session2.set_user('1', 'FoxSpectrum')

session1.get_user()

# Extra

class Shop_basket():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
    