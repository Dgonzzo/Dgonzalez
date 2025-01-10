'''
1️⃣Crea exemples de funcions bàsiques que representin les diferents possibilitats del llenguatge:

    Sense paràmetres ni retorn, amb un o diversos paràmetres, amb retorn...
    Comprova si pots crear funcions dins de funcions.

2️⃣Utilitza algun exemple de funcions ja creades en el llenguatge.
3️⃣Posa a prova el concepte de variable LOCAL i GLOBAL.
4️⃣Has de fer print per consola del resultat de tots els exemples.

DIFICULTAT EXTRA (Puntua si el resols tot sol):
5️⃣Crea una funció que rebi dos paràmetres de tipus cadena de text 
i retorni un número. La funció imprimeix tots els números de l'1 al 100. Tenint en compte que:

    Si el número és múltiple de 3, mostra la cadena de text del primer paràmetre.
    Si el número és múltiple de 5, mostra la cadena de text del segon paràmetre.
    Si el número és múltiple de 3 i de 5, mostra les dues cadenes de text concatenades.
    La funció retorna el nombre de vegades que s'ha imprès el número en lloc dels textos.
'''

# Simple

def greet() -> None:
    print('Hola')

# With return
def return_greet() -> str:
    return 'Hola'

# With parameters
def parameter_greet(name:str) -> None:
    print(f'Hola, {name}')

def more_par_greet(greet:str, name:str) -> None:
    print(f'{greet}, {name}')

# Optional parameters

def optional_greet(name:str='Helicoptero Apache') -> None:
    if 'Helicoptero Apache' != name:
        print(f'Hola, {name}')
    else:
        print(f'Como no se pueden asumir tus pronombres: Hola, {name}')

def optional_greet2(greet:str,name:str='Helicoptero Apache') -> None:
    if 'Helicoptero Apache' != name:
        print(f'{greet}, {name}')
    else:
        print(f'Como no se pueden asumir tus pronombres: {greet}, {name}')

# Multiple returns

def multiple_return_greet():
    return 'Hola', 'Bumpump'

# With an undefined number of parameters

def undifined_parameters_greet(*nums:int) -> None:
    sum = 0
    for num in nums:
        sum += num
    print(f'La suma és: {sum}')

# With an undefined number of key parameters

def undefined_key_parameters_func(**kargs:dict) -> None:
    for key, value in kargs.items():
        print(f'{key}: {value}')

# Functions inside other functions

def outer_function() -> None:
    def inner_function() -> None:
        print('I am an inner function inside outer_function()')
    inner_function()

# Built-in functions
def built_in_functions() -> None:
    print(len('Guillem'))
    a:str = input()
    print(type(a))

    print('ahsdf'.upper())

# Local and global variables

global_var:str = 'Python'

def hello_python () -> None:
    local_var:str = 'Hi'
    print(local_var, global_var)


# Dificultad extra

def extra_function (arg_1:str, arg_2: str) -> int:
    cont:int = 0

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(arg_1, arg_2)
        
        elif num % 3 == 0:
            print(arg_1)

        elif num % 5 == 0:
            print(arg_2)
        
        else:
            print(num)
            cont += 1
    
    return cont



if __name__ == "__main__":

    # print(return_greet) -> without parametres returns the direction to the memory
    print(return_greet())
    parameter_greet('Daniel')
    more_par_greet(name='Daniel', greet='Hallo')
    optional_greet()
    optional_greet2('Hallo')

    my_greet, my_name = multiple_return_greet()
    print(my_greet, my_name)

    undifined_parameters_greet(5, 6, 23, 62, 86886)
    undefined_key_parameters_func(
        name='Otto', 
        surname='Von Bismarck', 
        age=54
    )

    outer_function()
    
    hello_python()
    print(global_var)

    # Dificultad extra
    results:tuple = extra_function(input('Primer text>'), input('Segon text>'))
    print(f"S'ha imprimit els nombres {results} vegades")
