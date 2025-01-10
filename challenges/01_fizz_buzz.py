'''
Escriu un programa que mostri per consola els nombres de 
l'1 al 100 (ambdós inclosos i amb un bot de línia entre cada nombre), substituint 
els nombres per “FIZZ” o “BUZZ” segons les següents regles:
- Múltiples de 3 per la paraula “FIZZ”.
- Múltiples de 5 per la paraula “BUZZ”.
- Múltiples de 3 i de 5 per la paraula “FIZZ BUZZ”.

Entrada i sortida:
Aquest programa no tendrà cap entrada. 
El programa mostrarà directament els
nombres d'1 a 100 seguint les instruccions de l'enunciat.
'''

for count in range(1, 101):
    if (0 == count % 3) and (0 == count % 5): 
        print('FIZZ BUZZ')
    elif 0 == count % 3:
        print('FIZZ')
    elif 0 == count % 5:
        print('BUZZ')
    else:
        print(count)

