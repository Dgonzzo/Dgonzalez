'''
1️⃣ Utilitza 3 mecanismes diferents per imprimir números de l'1 al 10 mitjançant iteració.

DIFICULTAT EXTRA (Puntua si el resols tot sol):

2️⃣ Utilitza el màxim de mecanismes que puguis per iterar valors (no només nombre).
'''

# For
for n in range(1, 11):
    print(n)

# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursivity
def count_ten(i=1): 
    if i <= 10:
        print(i)
        count_ten(i+1)
count_ten()

# Extra

for n in [1,2,3,4,5,6,7,8,9,10]:
    print(n)

for k, v in {'a':1,'b': 2,'c': 3,'d':4,'e': 5 }.items():
    print(k, v)

for n in (1,2,3,4,5,6,7,8,9,10):
    print(n)

for n in {1,2,3,4,5,6,7,8,9,10}:
    print(n)

# List comprehension
print([i for i in range(1,11)])

print(*[i for i in range(1,11)], sep='\n')