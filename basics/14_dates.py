# Explaining library dates
'''
1️⃣ Crea dues variables de tipus data (datetime):
    - Una primera que representi la data (dia, mes, any, hora, minut, segons) actual.
    - Una segona que representi la teva data de naixement (pots inventar l'hora).
 2️⃣ Calcula quants d'anys han passat entre els dues.

DIFICULTAT EXTRA (Puntua si el resols totsol):
3️⃣ Utilitzant la data del teu aniversari, formatéjala i mostra el resultat de 10 formes diferents.

Per exemple:
    - Dia, mes i any.
    - Hora, minut i segons.
    - Dia de l'any.
    - Dia de la setmana.
    - Nom del mes.
    - ...
'''
import locale
from datetime import datetime

now = datetime.now()
print(now)


geburstag = datetime(2007,6,28,6,30,0,0)
print(geburstag)

diff = now - geburstag
print(type(diff))
print(diff.days)
print(f'You are {diff.days // 365} years old')
print(f'Du bist {diff.days // 365} Jahre alt')

'''
Extra
'''

print(geburstag.strftime('%d/%m/%Y'))
print(geburstag.strftime('%I%p:%d/%m/%Y'))
print(geburstag.strftime('%j/%Y'))
print(geburstag.strftime('%I:%M:%S %p - %d/%m/%Y'))
print(geburstag.strftime('%I:%M:%S %p'))
print(geburstag.strftime('%d, %A - %m, %b - %Y'))

# Locale time 
locale.setlocale(locale.LC_ALL, '')
print(geburstag.strftime('%c'))
print(geburstag.strftime('%X'))
print(geburstag.strftime('%d, %A - %m, %b - %Y'))
