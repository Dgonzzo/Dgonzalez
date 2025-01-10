'''
7. La vocal més comuna
Crea una funció que rebrà un text i retornarà la vocal que més pics es repeteixi.
● Si una vocal no hi és no ha de sortir.
● Anar amb compte amb les vocals amb accent.
Entrada i sortida:
L’entrada consistirà en una cadena de text.
La sortida serà un parell de valors per línia on el primer element serà la vocal i el segon
element el nombre de repeticions.
Si una vocal no apareix no ha de sortir
'''
VOCALS_ACCENTS = (('à', 'á'),('è', 'é'), ('í', 'ï'), ('ò', 'ó'), ('ú', 'ü'))
VOCALS = ('a', 'e', 'i', 'o', 'u')

vocals_count = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0,
    }

def common_vocal(in_str:str):
    in_str = in_str.lower()
    i = 0
    # Iterates the both constant tuples simultaneosly
    for vocal in VOCALS:
        for accent in VOCALS_ACCENTS[i]:
            in_str = in_str.replace(accent, vocal)
        i +=1
    
    # Counts all the leters
    for let in in_str:
        if let in VOCALS:
            vocals_count[let] += 1
    
    # Shows all the leters
    for let in vocals_count:
        if vocals_count[let] > 0:
            print(f'{let} {vocals_count[let]}')

common_vocal(input().strip())