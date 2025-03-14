class Product:
    all_products = []
    new_ident = -1

    def __init__(self, id, name, price):
        self.id = id
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
    
    @classmethod
    def update_new_ident(cls, last_id):
        cls.new_ident = last_id

    @classmethod
    def get_new_ident(cls):
        cls.new_ident += 1
        return cls.new_ident


    def __str__(self):
        return f'{self.id} {self.name} {self.price}$'