effective: dict = {
    'Aigua': {
        'effective': ['Foc'], # ('Foc') also valid
        'non_effective': ['Aigua', 'Planta']
    },
    'Foc': {
        'effective': ['Planta'],
        'non_effective': ['Foc', 'Aigua']
    },
    'Planta': {
        'effective': ['Aigua'],
        'non_effective': ['Planta', 'Foc']
    },
    'Elèctric': {
        'effective': ['Aigua'],
        'non_effective': ['Elèctric', 'Planta']
    },
}

def potency(attack, defense, v_attack, v_def):
    
    def efectivity(typeA, typeB):
        if typeA in effective[typeA]['effective']:
            return 2
        elif typeB in effective[typeA]['non_effective']:
            return 0.5
        else:
            return 1

    if v_attack < 0 or v_def < 0 or v_attack > 100 or v_def > 100:
        return 'error'
    
    efectivity = efectivity(attack, defense)
    return 50 * (v_attack / v_def) * efectivity

attack = input().strip()
defense = input().strip()

v_attack = int(input())
v_def = int(input())

print(potency(attack, defense, v_attack, v_def))