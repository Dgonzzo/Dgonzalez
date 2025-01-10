"""
1️⃣Crea exemples utilitzant tots els tipus d'operadors de Python:

    Aritmètics, lògics, de comparació, assignació, identitat, pertinença, bits...

2️⃣Utilitzant les operacions amb operadors que tu vulguis, crea exemples que representin tots els tipus d'estructures de control que existeixen a Python:

    Condicionals, iteratives, excepcions...

3️⃣Has de fer print per consola del resultat de tots els exemples.

DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣Crea un programa que imprimeixi per consola tots els números compresos 
entre 10 i 55 (inclosos), parells, i que no són ni el 16 ni múltiples de 3.

"""

def arithmetic_operators() -> None:
    print(f"Suma: 10 + 3 = {10 + 3}")
    print(f"Resta: 10 + 3 = {10 - 3}")
    print(f"Multiplicació: 10 x 3 = {10 * 3}")
    print(f"Divisió: 10 / 3 = {10 / 3}")
    print(f"Exponent: 10^3 = {10 ** 3}")
    print(f"Módul(resto) = 10 % 3 = {10 % 3}")
    print(f"Divisió entera: 10 // 3 = {10 // 3}")

def comparative_operators() -> None:
    print(f"Igualtat: 10 = 3 -> {10 == 3}")
    print(f"Desigualtat: 10 = 3 -> {10 != 3}")
    print(f"Major que: 10 > 3 -> {10 > 3}")
    print(f"Menor que: 10 < 3 -> {10 < 3}")
    print(f"Major o igual que: 10 >= 3 -> {10 >= 3}")
    print(f"Menor o igual que: 10 <= 3 -> {10 <= 3}")

def logic_operators() -> None:
    print(f"AND: 10 + 3 == 13 and 5 - 1 = 4 és {10 + 3 == 13 and 5 - 1 == 4}")
    print(f"OR: 10 + 3 == 13 or 5 - 1 = 1 és {10 + 3 == 13 or 5 - 1 == 1}")
    print(f"NOT: NOT 10 + 3 == 13 és {not 10 + 3 == 13}")

def assignment_operators() -> int:
    my_number = 11
    print(my_number)

    my_number += 1
    print(my_number)

    my_number -= 1
    print(my_number)

    my_number *= 1
    print(my_number)

    my_number /= 1
    print(my_number)

    my_number %= 1
    print(my_number)

    my_number **= 1
    print(my_number)
    
    my_number //= 1
    print(my_number)

    return my_number

def indentitiy_operators(par_in:any) -> None:
    new_number = par_in
    
    # Identity operators
    print(f"my_number is new_number és {par_in is new_number}")
    print(f"my_number is not new_number és {par_in is not new_number}")
    
    # Belonging operators
    print(f"'u' in 'Guillem' {'u' in 'Guillem'}")
    print(f"'Gui' in 'Guillem' {'Gui' in 'Guillem'}")
    print(f"'u' not in 'Guillem' {'u' not in 'Guillem'}")

    # Bit operators
    a = 10  # 1010
    b = 3   # 0011
            # 0010 -> 2 {0 - False 1 - True}

    print(f'AND: 10 & 3 = {10 & 3}')    # 0010 -> 2
    print(f'OR: 10 | 3 = {10 | 3}')     # 1011 -> 11
    print(f'XOR: 10 ^ 3 = {10 ^ 3}')    # 1001 -> 9
    print(f'NOT: ~10 = {~10}')          # 0101

def flow_execution() -> None:    
    # Conditionals 
    my_str:str = "Guillem"
    if my_str == 'Guillem':
        print("my_string és 'Guillem'")
    elif my_str == 'GMA':
        print("my_string és 'GMA'")
    else:
        print("my_string no és ni 'Guillem' ni 'GMA'")
    
    # Iterative
    i = 0
    while i < 10:
        print(i)
        i += 1
    
    for let in my_str:
        print(let)

    # Exception management
    try:
        print(10/0)
    except:
        print('Error: 201 I am a cup of tee')
    finally:
        print('The control management has been succesfully ended')


def extra_exercise() -> None:
    '''
    Dificultat extra: ponme buena nota guillem pls
    '''

    print('Extra')

    for i in range(10, 56): 
        if i % 2 == 0:
            if i == 16:
                pass
            else:
                print(i)
    '''
    # Best solution
    
    for i in range(10, 56, 2):
        if i != 16 and not i % 3 == 0:
            print(i)
    '''

if __name__ == "__main__":
    arithmetic_operators()
    comparative_operators()
    logic_operators()
    assignment_operators()
    indentitiy_operators(assignment_operators())
    flow_execution()
    extra_exercise()