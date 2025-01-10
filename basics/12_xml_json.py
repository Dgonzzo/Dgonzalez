'''
1️⃣ Desenvolupa un programa capaç de crear un arxiu XML i JSON que guardi les següents dades (fent ús de la sintaxi correcta en cada cas):

    Nom
    Edat
    Data de naixement
    Llistat de llenguatges de programació

2️⃣ Mostra el contingut dels arxius.
3️⃣ Esborra els arxius.

DIFICULTAT EXTRA (Puntua si el resols totsol):
4️⃣ Utilitzant la lògica de creació dels arxius anteriors, crea un programa capaç de llegir i transformar en una mateixa classe del teu llenguatge les dades emmagatzemades en l'XML i el JSON.
5️⃣ Esborra els arxius.
'''

data = {
    "name" : 'Some name', 
    "age" : 18, 
    "birth_date" : "12-04-2002",
    "programing_languages": ['Python', 'Cpp', 'Javascript']
}

'''
with open('test.txt', 'w') as file:
    for k,v in data.items():
        file.write(f'{k}: {v}\n')
'''

# XML

import xml.etree.ElementTree as xml

root = xml.Element('data')

for k, v in data.items():
    child = xml.SubElement(root, k)
    if isinstance(v, list):
        for item in v:
            xml.SubElement(child, 'item').text = item
    else:
        child.text = str(v)

tree = xml.ElementTree(root)
tree.write('test.xml')

with open('test.xml', 'r') as xml_file:
    root = xml.fromstring(xml_file.read())
    print(root.find('age').text)
    print(root.find('birth_date').text)


# JSON

import json

with open('test.json', 'w') as json_file:
    json.dump(data, json_file)

with open('test.json', 'r') as json_file:
    json_dict = json.load(json_file)
    
    print(json_dict['programing_languages'])