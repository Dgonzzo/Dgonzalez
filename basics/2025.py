'''
1️⃣ Crea un programa que permeti a l'usuari gestionar una llista de propòsits per al nou any. El programa ha de permetre:

    Afegir nous propòsits.
    Veure els propòsits actuals.
    Marcar propòsits com a complerts.
    Esborrar propòsits complets.
    Sortir del programa.

2️⃣ Requisits tècnics:

    Utilitza estructures condicionals (if, elif, else) per gestionar les opcions del menú.
    Utilitza estructures repetitives (while, for) per mantenir el programa actiu fins que l'usuari decideixi sortir.
    Gestiona una llista per emmagatzemar els propòsits.
'''
import os
import time

def add_objective(items:dict) -> dict:
    items.update({input('Add your objective >'): 'not_done'})
    return items

def show_objectives(items:dict) -> None:
    print('Objective\t Status')
    for key, value in items.items():
        print(f'{key}\t\t {value}')

def set_objective_done(items:dict) -> dict:
    for key, value in items.items():
        if value == 'not_done':
            items[key] = 'done'
    return items

def delete_done_objectives(items:dict) -> dict:
    for key, value in items.items():
        if value == 'done':
            del items[key]
    return items

def main() -> None:
    in_user:str = ''
    user_objectives = {}
    while in_user != '5':
        os.system('clear')
        print('\t---- Menu ----\n',
              '1. Add objective\n',
              '2. Show objectives\n',
              '3. Mark objectives as done\n',
              '4. Delete done objectives\n',
              '5. Close program')
        in_user = input('Introduce your option >')

        if '1' == in_user:
            user_objectives = add_objective(user_objectives)
            print('Objective added')
            time.sleep(1)
        elif '2' == in_user:
            show_objectives(user_objectives)
            time.sleep(5)
        elif '3' == in_user:
            set_objective_done(user_objectives)
            time.sleep(1)
        elif '4' == in_user:
            user_objectives = delete_done_objectives(user_objectives)
            print('Delete done objectives')
            time.sleep(1)
        else:
            pass
        

main()