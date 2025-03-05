def show_message(message):
    print(message)

def show_products(products):
    print('Products:')
    for product in products:
        print(f' - {product.name}')

def ask_info():
    name = input('Product name: ')
    price = float(input('Product price: '))
    return name, price

def show_menu():
    print('---- MENU ----')
    print('1. Show products')
    print('2. Add product')
    print('3. Exit')
    return int(input('Option: '))

