'''
5. Conversor de temps
Crea una funció que rebrà 4 paràmetres de tipus numèric que 
seran: dies, hores,
minuts i segons. La funció retornarà la data en miŀlisegons.
Entrada i sortida:
El programa demanarà quatre nombres que 
representaran: dies, hores, minuts i
segons en aquest ordre.
La sortida serà el valor que representen però en segons
'''



# Input
i = 0
num_in = [] # days, hours, minuts, seconds
count = 4

while i < count:
    num_in.append(int(input()))
    i += 1

# Output
i = 0
result = 0
for item in num_in:
    if 0 == i:
        result += item * 24 * 3600 * (10 ** 3)
    elif 1 == i:
        result += item * 3600 * (10 ** 3)
    elif 2 == i:
        result += item * 60 * (10 ** 3)
    elif 3 == i:
        result += item * (10 ** 3)
    
    i += 1

print(result)
