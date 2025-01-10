'''
Escriu una funció que calculi l'enèsim factor de la successió de Fibonacci.
Entrada i sortida:
L'entrada consistirà en un nombre positiu major a 0 que representarà l'enèsima posició
de la successió de Fibonacci.
La sortida serà l'enèsim valor de la successió.
'''

def fibonacci(num):
    if 1 == num:
        return 1
    if 2 == num: 
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num - 2)

print(fibonacci(int(input())))    
