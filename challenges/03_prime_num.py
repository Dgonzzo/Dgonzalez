'''
3. És un nombre primer?
Crea un programa que s’encarregui de comprovar si un nombre és o no primer.

Entrada i sortida:
L’entrada consistirà en diversos casos de prova. El primer número indica la quantitat de
casos a provar. A continuació es llegiran tants de nombres com s’hagi indicat.
Per cada cas de prova s’ha de mostrar si és un nombre primer o no.
'''

# Input
i = 0
num_in = []
count = int(input())

while i < count:
    num_in.append(int(input()))
    i += 1

# Output
for num in num_in:
    for divisor in range(num):
        if 1 == divisor or 0 == divisor or num == divisor:
            prime = True
        elif 0 == (num % divisor):
            prime = False
    print(prime)
