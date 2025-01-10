'''
4. De decimal a binari
Crea un programa que s’encarregui de transformar un nombre decimal a binari sense
utilitzar funcions pròpies del llenguatge que ho resolguin automàticament.

Entrada i sortida:
L’entrada consistirà en diversos casos de prova. El primer número indica la quantitat de
casos a provar. A continuació es llegiran tants de nombres com s’hagi indicat.
Per cada cas de prova s’ha de mostrar el mateix número però passat a binari
'''

def binary(decimal_num):
    temp_bin = ''
    while True:
        if decimal_num < 2: #!! This was the error
            temp_bin = str(int(decimal_num % 2)) + temp_bin
            return temp_bin
        else:
            temp_bin = str(int(decimal_num % 2)) + temp_bin
            decimal_num = (decimal_num / 2)


count = int(input())
i = 0
in_numbers = []

while i < count:
    in_numbers.append(int(input()))
    i += 1

for decimal_num in in_numbers:
    print(binary(decimal_num))
    