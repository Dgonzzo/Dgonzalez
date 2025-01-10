'''
6. Els nombres perduts
Crea una funció que rebrà una llista de nombres positius ordenats i no repetits i que
retorni una llista amb tots els nombres que falten entre el major i el menor.
Si la llista no està ordenada ha de donar un error.


Entrada i sortida:
L’entrada serà una seqüència de nombres positius ordenats de major a menor i
acabada amb el nombre 0.
La sortida serà una seqüència dels nombres que falten.
Si la llista no està ordenada mostrarà el missatge “error”.
'''

in_list_num = []
in_judge = None

while 0 != in_judge:
    in_judge = int(input())
    if 0 != in_judge:
        in_list_num.append(in_judge)
    else:
        pass

if in_list_num == sorted(in_list_num):
    # print(in_list_num)
    for num in range(in_list_num[0], in_list_num[-1]):
        if num not in in_list_num:
            print(num)
else:
    print('error')

