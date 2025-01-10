'''
1️⃣Mostra exemples de totes les operacions que pots realitzar amb cadenes de caràcters a Python. 
Algunes d'aquestes operacions podrien ser:

    Accés a caràcters específics, subcadenes, longitud, concatenació, repetició, recorregut, conversió a 
    majúscules i minúscules, reemplaçament, divisió, unió, interpolació, verificació...

DIFICULTAT EXTRA (Puntua si el resols totsol):

2️⃣Crea un programa que analitzi dues paraules diferents i realitzi comprovacions per a descobrir si són:

    - Palíndroms: és una paraula, frase o grup de paraules les lletres de les quals 
    es repeteixen en el mateix ordre quan són llegides en la direcció inversa. Ex: Radar -> radaR
    
    - Anagrames: és una paraula o una frase formada per la transposició de les lletres d'una altra paraula 
    o una altra frase. Ex: Roma -> amoR
    
    - Isogrames: és una paraula o frase en la qual cada lletra apareix el mateix nombre de vegades. 
    Ex: Paperera -> P*2, a*2, e*2, r*2
'''

def extra(word1:str, word2:str) -> None:
    
    def palindrome (word:str) -> None:
        if reversed(word.lower()) == word.lower():
            print(f'{word} es un palindrome de {word}')
        else:
            print(f'{word} no es un palindrome de {word}')
    
    def anagram (word1:str, word2:str) -> None:
        while True:
            for let in  word1:
                if word1.count(let.lower()) == word2.count(let.lower()):
                    pass
                else:
                    print(f'{word1} no és anagrama de {word2}')
                    return None
            
            print(f'{word1} és anagrama de {word2}')
            return None
    
    def isogram (word:str) -> None:
        word_dict:dict = {}

        for char in word:
            word_dict[char.lower()] = word_dict.get(char.lower(), 0) + 1

        is_isogram = True
        v_init = list(word_dict.values())[0] # Gets the number of times that the first number appears
        
        for k, v in word_dict.items():
            if v != v_init:
                is_isogram = False
                break
            
        print(f'{word} es isograma = {is_isogram}')

    palindrome(word1)
    palindrome(word2)
    anagram(word1, word2)
    
    isogram(word1)
    isogram(word2)


if __name__ == '__main__':
    extra(input('Palabra 1>'), input('Palabra 2>'))
    s1:str = 'Hello'
    s2:str = 'Word'

'''
    # Concatenation
    print(s1 + '' + s2)

    # Repetition
    print(s1 *4)

    # Access
    print(s1[0], s2[0])

    # Length
    print(len(s1))

    # Substring
    print(s1[0:3]) # == s1[:3]
    print(s1[1:])

    # Search
    print('o' in s1)
    print('i' in s1)
    
    # Substitution
    print(s1.replace('e', 'a'))

    # Split
    print(s2.split('r'))
    print('hi mana fahrkarte'.split(' '))

    # Uppercase, lowercase, capitalize
    print(s1.upper())
    print(s2.lower())
    print('un perror que iba caminando'.title())
    print('lorem ipsum algo random'.capitalize())

    # Delete spacebars at the beginning and the end
    print('                           hiiiiiii 234234 ses                  '.strip())

    # Search at the beginning and the end
    print(s1.startswith('Ha'))
    print(s1.startswith('Ho'))
    print(s1.endswith('a'))

    print(s2.endswith('ld'))

    s3:str = 'ha in of kdkdkdkdk'
    print(s3.find('in'))
    print(s3.find('jajajajajaj')) # -1 means not found 

    # Count method
    print(s3.count('k'))

    # Interpolation
    name:str = input('name >')
    age:str = input('age>')
    print(f'Greetings {name}, du bist {age} Jahre alt')

    # Format
    print('Greetings {}, du bist {} Jahre alt'.format(name, age))

    # Conversion str to list
    print(list(s3))

    # Conversion list to str
    my_list:list[str] = ['Alba', 'Carlos', 'El prime']
    my_str:str = ' - '.join(my_list)
    print(my_str)

    # Num transformations
    s4 = '123123123123'
    s5 = '123.523'

    print(int(s4))
    print(float(s5))

    # Prove str
    s6 = '234234234'
    s7 = 'sdfsdfsdfsdfsdf'
    s8 = 'sdfsdfsdfsgsgsdf'
    s9 = '342324.25325234'

    print(s6.isalnum())
    print(s6.isalpha())
    print(s6.isnumeric())
    print(s6.isdecimal())
    
    print(s7.isalnum())
    print(s7.isalpha())
    print(s7.isnumeric())
    print(s7.isdecimal())
    
    print(s8.isalnum())
    print(s8.isalpha())
    print(s8.isnumeric())
    print(s8.isdecimal())
    
    print(s9.isalnum())
    print(s9.isalpha())
    print(s9.isnumeric())
    print(s9.isdecimal())
'''
