'''
1️⃣ Crea un programa capaç d'executar de manera asíncrona una funció que simularà la petició del temps en determinades ciutats.

2️⃣ La funció imprimeix el nom, quan comença, el temps que durarà l'execució i quan finalitza.

DIFICULTAT EXTRA (Puntua si el resols tot sol):
3️⃣ Utilitzant el concepte d'asincronia i la funció anterior, crea la següent seqüència de funcions:
    - Una funció C que dura 3 segons.
    - Una funció B que dura 2 segons.
    - Una funció A que dura 1 segons.
    - Una funció D que dura 1 segons.
    - Les funcions C, B i A s'executen en paral·lel.
    - La funció D comença la seva execució quan les 3 anteriors han acabat.
'''
import random
import time
import datetime
import asyncio

async def get_time_weather(city):
    print(f'Petition of data for {city} at: {datetime.datetime.now()}')
    temp = random.randint(-5, 20)
    await asyncio.sleep(random.randint(1,5))
    # time.sleep(random.randint(1,5))
    info = {
        'city_name': city,
        'temp': temp
    }
    print(f'Data received for {city} at {datetime.datetime.now()}')
    return info

async def late_func(name, names):
    # names = ['a', 'b', 'c']
    
    time = 1
    print(f'Started execution of func:{name} at {datetime.datetime.now()}')
    for i in names:
        if name == i or name == 'd':
            await asyncio.sleep(time)
        else:
            time += 1
    print(f'Finished execution of func:{name} at {datetime.datetime.now()}')

async def main():
    cities = ['Palma', 'Llucmajor', 'Barcelona', 'Berlin', 'Arenal']
    
    tasks = [get_time_weather(city) for city in cities] # Saves the pointers to the functions calls

    '''
    tasks = list()
    for city in cities:
        tasks.append(get_time_weather(city))
    '''

    info = await asyncio.gather(*tasks)
    
    for i in info:
        print(i)

    '''
    Extra
    '''

    names = ['a', 'b', 'c']

    tasks = [late_func(name, names) for name in names]
    info = await asyncio.gather(*tasks)
    
    info.append(await late_func('d', names))
    

asyncio.run(main())


