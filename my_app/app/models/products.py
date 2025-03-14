class Product:
    all_products = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def get_all(cls):
        return cls.all_products
    
    @classmethod
    def insert_product(cls, product):
        cls.all_products.append(product)

    @classmethod
    def delete_product(cls, id_product):
        cls.all_products.remove(id_product)

    def __str__(self):
        return self.name