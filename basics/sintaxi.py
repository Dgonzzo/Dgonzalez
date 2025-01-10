'''
1️⃣ Crea un comentari en el codi i col·loca l'URL del lloc web oficial del llenguatge de programació Python.
2️⃣ Representa les diferents sintaxis que existeixen de crear comentaris en el llenguatge (en una línia, vàries...).
3️⃣ Crea una variable (i una constant).
4️⃣ Crea variables representant tots els tipus de dades primitives (simples) del llenguatge (cadenes de text, enters, booleans...).
5️⃣ Imprimeix per terminal (consola) el text: "Hola, Python!"
'''

# https://www.python.org/
"""
Comment with multiple lines
1
2
2
3
"""

def main() -> None:
    CONSTANT_PI_NUM:float = 3.14
    hello_python:str = "Hola, Python" # Python's standard: snake_case
    natural_num:int = 3
    fractional_num:float = 3.12
    bool_value:bool = False

    print(hello_python)

if __name__ == "__main__":
    main()
