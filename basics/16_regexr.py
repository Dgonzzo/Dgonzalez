'''
1️⃣ Explora el concepte d'expressions regulars, creant una funció capaç de trobar i extreure tots els nombres d'un text.

DIFICULTAT EXTRA (Puntua si el resols tot sol):

2️⃣ Crea 3 expressions regulars capaces de:
    - Validar un email.
    - Validar un número de telèfon.
    - Validar un URL.
'''
import re

regexr = r'^\w+@+.[a-zA-Z]{2,5}$'

phone_num_regexr = r'^\+?[\d\s]{2,}$'

def find_nums(text):
    return re.findall(regexr, text)

def proto_validate_email(text):
    return bool(re.match(regexr, text))

def validate_phone(text):
    return bool(re.match(phone_num_regexr, text))

print(find_nums('Hola soc 2n batxillerat del curs 2024'))

print(proto_validate_email('dgonzalez@iessarenal.net'))

print(validate_phone('+49 395 293 04 35'))

regexr = r'^http[s]?://(www.)?[\w.]+\.[a-z]{2,}(/[\S]+)?$'

def validate_url(url):
    return bool(re.match(regexr, url))

print(validate_url('https://www.reddit.com/r/pchelp/comments/15vxg27/dumb_question_but_how_do_i_type_a_question_mark/?rdt=34157'))