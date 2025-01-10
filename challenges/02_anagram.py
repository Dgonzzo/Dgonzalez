'''
Escriu una funció que rebi dues paraules (String) i retorni Vertader o Fals segons siguin
o no anagrames:
● Un anagrama consisteix a formar una paraula reordenant totes les lletres d'una
altra paraula inicial.
● No influeix que siguin majúscules o minúscules.
● No fa falta comprovar que les paraules existeixen.
● Dues paraules exactament igual no són anagrames.

Entrada i sortida:
El programa demanarà dues paraules i la sortida serà vertader o false segons es
compleixin les condicions.
'''

def anagram(word1:str, word2:str):
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return False
    for let in word1:
        if word1.count(let) == word2.count(let):
            pass
        else:
            return False
        return True

print(anagram(input().strip(), input().strip()))
