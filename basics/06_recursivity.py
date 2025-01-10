'''
1️⃣Entén el concepte de recursivitat creant una funció recursiva que imprimeixi els números del 100 al 0.

DIFICULTAT EXTRA (Puntua si el resols totsol):

2️⃣Utilitza el concepte de recursivitat per a:

    Calcular el factorial d'un número concret (la funció rep aquest número).
    Calcular el valor d'un element concret (segons la seva posició) en 
    la successió de Fibonacci (la funció rep la posició).
'''

def countdown(number) -> None:
    
    if number >= 0:
        print(number)
        countdown(number-1)
    
    '''
    for i in range(100,-1, -1):
        print(i)
    '''

def factorial(num:int) -> int:
    if num  == 1:
        return 1
    else:
        return(num * factorial(num - 1))

def fibonacci(num) -> int:
    if num == 1:
        return 1 
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

if __name__ == '__main__':
    # countdown(100)
    # print(factorial(5))
    # print(factorial(3))
    print(fibonacci(6))
    