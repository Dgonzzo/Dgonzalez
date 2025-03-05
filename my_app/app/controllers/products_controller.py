from app.models import Product
from app.views import show_menu, show_products, ask_info, show_message

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

        elif 3 == option:
            show_message('Bye!')
            break

        else:
            show_message('Invalid option')
