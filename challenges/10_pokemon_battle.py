'''
10. Batalla Pokémon
Crea un programa que calculi la potència d’un atac durant una batalla Pokémon.
● La fórmula serà la següent: potència = 50 * (atac / defensa) * efectivitat.
● Càlcul de efectivitat: x2 (super efectiu), x1 (neutral), x0.5 (no és molt efectiu).
● Ho simplificarem a 4 tipus de Pokémon: aigua, foc, planta i elèctric

l programa rebrà els següents paràmetres:
○ Tipo atacant.
○ Tipo defensor.
○ Atac: entre 1 i 100.
○ Defensa: entre 1 i 100

Entrada i sortida:
L’entrada consistirà en quatre línies. Les dues primeres representaran el tipus de
l’atacant i el tipus del defensor respectivament. Els únics valors vàlids seran: Aigua, Foc,
Planta i Elèctric.
Les dues darreres línies (la 3 i la 4) representaran el valor de l’atac i el valor de la
defensa. Aquests valors només podran ser entre 1 i 100.
La sortida serà el valor numèric calculat a partir de la fórmula
.𝑝𝑜𝑡è𝑛𝑐𝑖𝑎 = 50 * ( 𝑎𝑡𝑎𝑐
𝑑𝑒𝑓𝑒𝑛𝑠𝑎 ) * 𝑒𝑓𝑒𝑐𝑡𝑖𝑣𝑖𝑡𝑎𝑡
Qualsevol valor no vàlid que s’introdueixi el programa haurà de mostrar el missatge
“error”
'''
ELEMENTS = ('Aigua', 'Foc', 'Planta', 'Elèctric')

def battle(type_atack:str, type_def:str, attack:float, defense:float):
    efective = 1

    if type_atack == type_def: # when both pokemons are of the same element, efective is always 0.5
        efective = 0.5
    
    elif ELEMENTS[0] == type_atack: # For water element attacking
        if ELEMENTS[1] == type_def:
            efective = 2
        elif ELEMENTS[2] == type_def:
            efective = 0.5
    
    elif ELEMENTS[1] == type_atack:
        if ELEMENTS[0] == type_def:
            efective = 0.5
        elif ELEMENTS[2] == type_def:
            efective = 2
    
    elif ELEMENTS[2] == type_atack:
        if ELEMENTS[0] == type_def:
            efective = 2
        elif ELEMENTS[1] == type_def:
            efective = 0.5
    
    elif ELEMENTS[3] == type_atack:
        if ELEMENTS[0] == type_def:
            efective = 2
        if ELEMENTS[2] == type_def:
            efective = 0.5
    
    return (50 * (attack / defense) * efective)

count = 0
in_judge = []

battle_elements = {
    'type_attack': '',
    'type_defense': '',
    'attack': 1,
    'defense': 1
}

# input
for _ in range(4):
    in_judge.append(input().strip())

# conversion
index = 0
for i in in_judge:
    if index > 1:
        in_judge[index] = float(i)
    index += 1

# Insert elements in dict
index = 0
for item in battle_elements:
    battle_elements[item] = in_judge[index]
    index += 1

# prove valid values
# print(battle_elements)
if battle_elements['type_attack'] and battle_elements ['type_defense'] not in ELEMENTS:
    print('Error')
elif battle_elements['attack'] < 1 or battle_elements['defense'] < 1: 
    print('Error')
elif battle_elements['attack'] > 100 or battle_elements['defense'] > 100:
    print('Error')
else:
    print(battle(battle_elements['type_attack'], battle_elements['type_defense'],battle_elements['attack'], battle_elements['defense']))
