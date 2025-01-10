'''
1️⃣Mostra exemples d'assignació de variables "per valor" i "per referència", segons el seu tipus de dada.
2️⃣Mostra exemples de funcions amb variables que passen "per valor" i "per referència", 
i com es comporten en cada cas en el moment de ser modificades.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣Crea dues funcions que rebin dos paràmetres (cada una). 
En un cas paràmetres per valor, i en un altre cas, per referència.

4️⃣La funció ha d'intercanviar el valor de les dues variables en l'interior, 
i retornar-ho en dues variables diferents de les originals.

5️⃣Imprimeix el valor de les variables originals i les noves, 
comprovant que s'ha invertit el seu valor en les segones.

6️⃣Comprova també que s'ha conservat el valor original en les primeres.
'''

def change_value(value_a, value_b):
    temp = value_a
    value_a = value_b
    value_b = temp

    return value_a, value_b


'''
def change_ref(list_a, list_b):
    temp = list_a
    list_a = list_b
    list_a = temp
    return list_a, list_b
'''

if __name__ == '__main__':
    
    v_a = 10
    v_b = 20
    v_c, v_d = change_value(v_a, v_b)
    print(f'Originals:{v_a}, {v_b}. Modificat: {v_c, v_d}')
    
    l_a = [10, 20]
    l_b = [30, 40]
    l_c, l_d = change_value(l_a, l_b)
    print(f'Originals:{l_a}, {l_b}. Modificat: {l_c, l_d}')

    '''
    # Type of data via value
    my_int_a = 10
    my_int_b = my_int_a
    my_int_a = 30

    print(my_int_a)
    print(my_int_b)

    # Type of data via refererence
    my_list_a = [20, 30]
    my_list_b = my_list_a.copy()
    my_list_b.append(30)
    print(my_list_a)
    print(my_list_b)

    # Functions with data per value
    
    def my_int_func(my_int):
        my_int = 20
        print(my_int)
    
    my_int_c = 10s
    my_int_func(my_int_c)
    print(my_int_c)

    # Functions with data per reference
    def my_list_func(my_list:list):
        my_list.append(30)
        my_list_d = my_list
        my_list.append(40)
        print(my_list)
        print(my_list_d)
    
    my_list_c = [10, 20]
    my_list_func(my_list_c) # Similar to my_list_c = my_list
    '''
