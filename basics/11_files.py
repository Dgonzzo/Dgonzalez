'''
1️⃣ Desenvolupa un programa capaç de crear un arxiu amb el teu nom i tingui l'extensió .txt.
2️⃣ Afegeix diverses línies en aquest fitxer:

    El teu nom.
    Edat.
    Llenguatge de programació favorit.

3️⃣ Imprimeix el contingut.
4️⃣ Esborra el fitxer.

DIFICULTAT EXTRA (Puntua si el resols totsol):

5️⃣ Desenvolupa un programa de gestió de vendes que emmagatzema les seves dades en un arxiu .txt.
6️⃣ Cada producte es guarda en una línia de l'arxiu de la manera següent:

    [nom_producte], [quantitat_venuda], [preu].
    Seguint aquest format, i mitjançant terminal, ha de permetre afegir, 
    consultar, actualitzar, eliminar productes i sortir.
    També ha d'haver-hi opcions per a calcular la venda total i per producte.
    L'opció sortir esborra el .txt.
'''

import os

# open("test.txt", "w")
# os.remove("test.txt")
'''
with open("test.txt", "a") as file: # Save environment
    file.write("Dani\n")
    file.write("17\n")
    file.write("Python\n")

with open("test.txt", "r") as file:
    print(file.read())

with open("test.txt", "r") as file:
    print(file.readline())

with open("test.txt", "r") as file:
    for line in file.readlines():
        print(line)

os.remove("test.txt")
'''

'''
Extra
'''

file_name = "shop_list.txt"

open(file_name, 'a')
while True:
    os.system('clear')
    print("1. Add product\n"+
        "2. Consult product\n"+
        "3. Update product\n"+
        "4. Delete product\n"+
        "5. Show all products\n"+
        "6. Calculate total sell\n"+
        "7. Calculate total income per product\n"+
        "8. Exit")
    
    in_user = input('>')

    if '1' == in_user: # Add
        with open(file_name, 'a') as file:
            in_user = input('Insert name_product quantity price >').split(' ')
            # print(in_user)
            for item in in_user:
                if in_user[-1] == item:
                    file.write(item)
                else:
                    file.write(item + ", ")
            file.write('\n')

    elif '2' == in_user: # Consult
        name = input("Insert product's name >")
        with open(file_name, 'r') as file:
            for line in file.readlines():
                if name == line.split(', ')[0]:
                    print(line)
                    input('Continue >')
                    break

    elif '3' == in_user: # Update
        in_user = input('Which product would you like to update >')
        with open(file_name, 'r') as file:
            temp_file = file.readlines() # Guillem's method to store the temp_file
        
        with open(file_name, 'w') as file:
            for line in temp_file:
                if line.split(', ')[0] == in_user:
                    in_user_add = input('Insert name_product quantity price >').split(' ')
                for item in in_user_add:
                    if in_user_add[-1] == item:
                        file.write(item)
                    else:
                        file.write(item + ", ")
                file.write('\n')


    elif '4' == in_user: # Delete
        with open(file_name, 'r') as file:
            temp_file = []
        
            for line in file.readlines():
                temp_file.append(line)         
        
        with open(file_name, 'w') as file:
            in_user = input('Which product would you like to delete >')
            
            i = 0
            for line in temp_file:
                if in_user in line:
                    del temp_file[i] 
                    break
                else:
                    i += 1
            
            for line in temp_file:
                file.write(f'{line}\n')

    elif '5' == in_user: # Show all the products
        with open(file_name, "r") as file:
            print('These are the products:')
            products = []
            for line in file.readlines():
                products.append(line.split(', ')[0])
            for i in products:
                print(f'\t - {i}')
            input('Continue >')

    elif '6' == in_user: # Calculate total sell
        total = 0
        with open(file_name, 'r') as file:
            for product in file.readlines():
                components = product.split(', ')
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
            print(total)
            input('continue >')

    elif '7' == in_user: # Calculate total revenue per products
        name = input("Insert product's name >")
        with open(file_name, 'r') as file:
            for line in file.readlines():
                components = line.split(', ')
                if name == components[0]:
                    print(int(components[1]) * float(components[2]))
                    input('Continue >')
                    break
    elif '8' == in_user:
        os.remove(file_name)
        break
