class Product:
    all_products = []
    product_counter = 1

    def __init__(self, name, price):
        self.id = self.product_counter + 1
        self.name = name
        self.price = price
    
    @classmethod
    def get_all(cls):
        return cls.all_products
    
    @classmethod
    def insert_product(cls, product):
        cls.all_products.append(product)
        cls.product_counter += 1

    def __str__(self):
        return self.name