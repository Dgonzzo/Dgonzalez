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
        for product in cls.all_products:
            # print(type(product.id),type(id_product))
            if product.id == int(id_product):
                cls.all_products.remove(product)
                break
    
    @classmethod
    def update_new_ident(cls, last_id):
        if None == type(last_id):
            cls.new_ident = 0
        else:
            cls.new_ident = int(last_id)
            # cls.new_ident = 0
            # print(last_id)

    @classmethod
    def get_new_ident(cls):
        print(cls.new_ident)
        cls.new_ident += 1
        return cls.new_ident

    # Debugging function
    @classmethod
    def print_x(cls):
        print(cls.new_ident)


    def __str__(self):
        return f'{self.id} {self.name} {self.price}$'