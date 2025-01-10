'''
1️⃣Mostra exemples de creació de totes les estructures suportades per defecte a Python.

    Utilitza operacions d'inserció, esborrament, actualització i ordenació.

DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣Crea una agenda de contactes per terminal.

    Has d'implementar funcionalitats de cerca, inserció, actualització i eliminació de contactes.
    Cada contacte ha de tenir un nom i un número de telèfon.
    
    El programa sol·licita, en primer lloc, quina és l'operació que es vol realitzar, 
    i a continuació les dades necessàries per a dur-la a terme.
    
    El programa no pot deixar introduir números de telèfon no numèrics 
    i amb més d'11 dígits (o el nombre de dígits que vulguis).
    
    També s'ha de proposar una operació de finalització del programa.
'''

def search (agenda:dict, search_element:str) -> dict:

   if search_element in agenda:
      return agenda[search_element]
   else:
      print("No s'ha encontrat el contacte")
      return False

def insert_update (agenda:dict, insert_element) -> dict:
   name:str = input('Insertar nombre >')
   phone_num:str = input('Insertar el telèfon >')
   
   if len(phone_num) > 0 and len(phone_num) <= 11 and phone_num.isdigit():
      agenda[name] = phone_num
   else:
      print('Inserta un nombre de teléfon vàlid')
   return agenda

def agenda() -> None:
   agenda:dict = {} # key = name, value = telephone_num

   while True:
      user_in:str = input('Cerca [c], Inserta [i], Actualitza [a], Elimina [d], salir [q] >')

      if 'c' == user_in:
        user_in:str = input('Contacte que vols cercar>')
        print(f'El contacte: {user_in} amb telèfon: {search(agenda, user_in)}')
    
      elif 'i' == user_in:
         insert_update(agenda, user_in)
      
      elif 'a' == user_in:
         insert_update(agenda, user_in)
      
      elif 'd' == user_in:
         try:
            del agenda[input('Contacte que vols eliminar >')]
         except:
            print('No existeix el contacte')
      
      elif 'q' == user_in:
         break
   
if __name__ == '__main__':
   my_list:list[str] = ['Hahahah', 'Daniel', 'Guillem'] 
   print(my_list)

   my_list.append('Damian')

   my_list.remove('Hahahah')

   print(my_list[-1]) # List's last item
   my_list[1] = 'Iker'

   # Sort method
   my_list.sort(reverse=False)
   print(my_list)

   # Insert in an especific index
   my_list.insert(2, 'Carlos')
   print(my_list)

   '''
   Tuples
   '''
   my_tuple:tuple = ('hi', 'ludwig')
   print(my_tuple[0])

   my_tuple = tuple(sorted(my_tuple))


   '''
   Set
   '''

   my_set:set = {"Guillem", "Mas", "@iessarenal.net"}
   
   print(my_set)
   my_set.add('dgonzalez@iessarenal.net')
   print(my_set)
   my_set.add('dgonzalez@iessarenal.net')
   print(my_set)

   my_set.remove('Guillem')
   print(my_set)

   '''
   Dict
   '''

   my_dict:dict ={
      'name': 'Ludwig',
      'nachname': 'von Johannes',
      'geburstag': '28-04-98'
   }
   print(my_dict)
   my_dict['e-mail'] = 'dgonzalez@iessarenal.net'
   print(my_dict)

   my_dict['nachname'] = 'Holl'
   print(my_dict)

   del my_dict['geburstag']
   print(my_dict)

   '''
   Extra
   '''
   agenda()