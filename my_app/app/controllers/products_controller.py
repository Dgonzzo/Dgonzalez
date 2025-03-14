from app.models import Product
from app.views import show_menu, show_products, ask_info, show_message, ask_id
from app.services import get_products, insert_product, delete_product

def configure_app():
    Product.all_products = get_products()

def product_manager():
    while True:
        option = show_menu()

        if 1 == option:
            product = Product.get_all()
            show_products(product)
        
        elif 2  == option:
            name, price = ask_info()
            
            product = Product(name, price)

            Product.insert_product(product) # Inserts at the classmethod
            insert_product(product.name, product.price) # Inserts in DB
            
            show_message('Product added')

        elif 3 == option:
            products = Product.get_all()
            show_products(products)
            show_message('Which product do you want to delete?')

            id = ask_id()
            
            Product.delete_product(id)
            
            delete_product(id)

            

            show_message('Product deleted')

        elif 4 == option:
            show_message('Bye!')
            break

        else:
            show_message('Invalid option')
