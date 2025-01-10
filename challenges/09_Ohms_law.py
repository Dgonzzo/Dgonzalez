'''
. La llei d’Ohm
Escriu una funció que calculi el valor del paràmetre que falta corresponent a la llei
d’Ohm.
● Enviarem a la funció 2 dels 3 paràmetres (V, R, I) i retornarà el valor del tercer
(arrodonir a 2 decimals).
● Si els paràmetres són incorrectes o insuficients, la funció retornarà la cadena de
text: “Invalid values”.
Entrada i sortida:
L’entrada consistirà en una, dues o tres línies amb un parell de valors. El primer valor
serà “V”, “R” o “I” i representaran el voltatge, la resistència o la intensitat
respectivament. El segon valor serà el valor d’aquest paràmetre.
Finalment, introduirem un 0 per indicar que hem acabat de llegir.
La sortida serà un parell de valors on el primer valor serà “V”, “R” o “I” resultant i el
segon valor serà el valor calculat per aquest paràmetre.
Si s’han introduït zero o un paràmetre o més de 2, es mostrarà el text “Invalid values
'''
count = 0
ohm_var = {'V': 0, 'I': 0, 'R': 0}
in_judge = None

def ohms_law(v, i, r):
    if 0 == v:
        v = i * r
        print(f'V {v}')
    elif 0 == i:
        i = v / r
        print(f'I {i}')
    elif 0 == r:
        r = v / i
        print(f'R {r}')

while True:
    in_judge = list((input().strip()).split(' '))
    # print(in_judge)
    if '0' in in_judge: # When this check is made, 0 is a str
        break  
    else:
        in_judge[1] = float(in_judge[1])
        ohm_var[in_judge[0]] = in_judge[1]
        count += 1
    
if 2 != count:
    print('Invalid values')

else:
    ohms_law(ohm_var['V'], ohm_var['I'], ohm_var['R'])
    
