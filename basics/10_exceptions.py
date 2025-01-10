'''
1️⃣ Explora el concepte de maneig d'excepcions de Python.
2️⃣ Força un error en el teu codi, captura l'error, imprimeix aquest error i evita que el programa es detingui 
de manera inesperada.
3️⃣ Prova de dividir "10/0" o accedir a un índex no existent d'un llistat per a intentar provocar un error.

DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣ Crea una funció que sigui capaç de processar paràmetres, però que també pugui llançar 
3 tipus diferents d'excepcions (una d'elles ha de correspondre's amb una mena d'excepció creada 
per nosaltres de manera personalitzada, i ha de ser llançada de manera manual) en cas d'error.

- Longitud < 3
- Posició [1] no pot ser 0
- [3] == str

5️⃣ Captura totes les excepcions des del lloc on anomenes a la funció.
6️⃣ Imprimeix el tipus d'error.
7️⃣ Imprimeix si no s'ha produït cap error.
8️⃣ Imprimeix que l'execució ha finalitzat.
'''

result = None

my_list = [1, 3, 4]

try:
    print(my_list[4])
    
except Exception as error:
    print(f"Error: {error}:{type(error).__name__}")
    # print(result)

print(result)

# Own errors

class DumbError(Exception):
    pass

'''
while True:
    num_a = int(input('1 Num >'))
    num_b = int(input('2 Num >'))
    try:
        if 10 == (num_a + num_b):
            raise DumbError('Error 201: I am a cup of tea')
    
    except Exception as error:
        print(f"I'm a cup of tea: {error}:({type(error).__name__})")
'''

'''
Extra dificulty
'''



# longitud < 3
def proces_parameters(parameters:list):
    
    if 3 > len(parameters):
        raise IndexError()
    
    elif 0 == parameters[1]:
        raise ZeroDivisionError()
    
    elif str != type(parameters[3]):
        raise DumbError('Element in index 3 has to be a str')

elements = [3, 1, 2, "a"]

try:
    proces_parameters(elements)
    print("Finishing program...")
except IndexError as error:
    print("Error: the numbers of elements has to be greater than 3")
except ZeroDivisionError as error:
    print("Error: element in index 1 cannot be 0")
except DumbError as error:
    print(error)
else:
    print('No errors')

