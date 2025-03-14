def show_message(message):
    print(message)

def show_products(products):
    print('Products:')
    for product in products:
        print(f' - {product[0]} {product[1]}')

def ask_info():
    name = input('Product name: ')
    price = float(input('Product price: '))
    return name, price 

def ask_id():
    return input('Product id: ')

def show_menu():
    print('---- MENU ----')
    print('1. Show products')
    print('2. Add product')
    print('3. Delete product')
    print('4. Exit')
    return int(input('Option: '))

