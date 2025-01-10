'''
1️⃣ Crea una funció que s'encarregui de sumar dos números i retornar el seu resultat.
2️⃣ Crea un test, utilitzant les eines de Python, que sigui capaç de determinar si aquesta funció s'executa correctament.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣ Crea un diccionari amb les següents claus i valors:

    "name": "El teu nom"
    "age": "La teva edat"
    "birth_date": "La teva data de naixement"
     "programming_languages": ["Llistat de llenguatges de programació"]

4️⃣ Crea dos test:

    Un primer que determini que existeixen tots els camps.
    Un segon que determini que les dades introduïdes són correctes.
'''

import unittest
from datetime import datetime, date

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 1), 2)
        
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum('a', 4)
        with self.assertRaises(ValueError):
            sum('a', 'v')
        with self.assertRaises(ValueError):
            sum(None, None)


def sum(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("ValueError: insert a int or float type")
    return num1 + num2 + 1



# sum('a', 3)

class TestDict(unittest.TestCase):
    
    def test_key_exists(self):
        self.assertIn('name', person)
        self.assertIn('age', person)
        self.assertIn('birth_date', person)
        self.assertIn('programming_languages', person)

    def test_key_type(self):
        self.assertIsInstance(person['name'], str)
        self.assertIsInstance(person['age'], int)
        self.assertIsInstance(person['birth_date'], date)
        self.assertIsInstance(person['programming_languages'], list)

person = {
    "name": 'Dani',
    "age": 17,
    "birth_date": datetime.strptime("28-06-07", "%d-%m-%y").date(),
    "programming_languages": ["Python", "Javascript", "Rust"]
}



unittest.main()
