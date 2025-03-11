class Product:
    all_products = []

    def __init__(self, name, price):
        self.id = -1
        self.name = name
        self.price = price
    
    @classmethod
    def get_all(cls):
        return cls.all_products
    
    @classmethod
    def insert_product(cls, product):
        cls.all_products.append(product)

    def __str__(self):
        return self.name