from app.models import Product
from app.views import show_menu, show_products, ask_info, show_message
from app.services import get_products, insert_product

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
            Product.insert_product(product)
            insert_product(product.name, product.price)
            
            show_message('Product added')

        elif 3 == option:
            pass

        elif 4 == option:
            show_message('Bye!')
            break

        else:
            show_message('Invalid option')
