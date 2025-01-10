'''
1️⃣ Implementa els mecanismes d'introducció i recuperació d'elements propis de les piles (stacks - LIFO) i les cues (queue - FIFO) utilitzant una estructura de llista.

DIFICULTAT EXTRA (Puntua si el resols totsol):
2️⃣ Utilitzant la implementació de pila i cadenes de text, simula el mecanisme d'avançar i tornar enrere d'un navegador web. Crea un programa en el qual puguis navegar a una pàgina o indicar-li que et vols desplaçar endavant o enrere, mostrant en cada cas el nom de la web.

    Les paraules "endavant", "enrere" desencadenen aquesta acció, la resta s'interpreta com el nom d'una nova web.

3️⃣ Utilitzant la implementació de cua i cadenes de text, simula el mecanisme d'una impressora compartida que rep documents i els imprimeix quan així se li indica.

    La paraula "imprimir" imprimeix un element de la cua, la resta de paraules s'interpreten com a noms de documents.
'''

# Stack (LIFO)

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# pop
pop_item = stack[-1]
del stack[-1]
print(pop_item)
print(stack)

# Queue (FIFO)

queue = []

# enqueue

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# dequeue
dequeue_item = queue[0]
del queue[0]
print(dequeue_item)
print(queue)

'''
Web
'''

stack_navi = []
temp_navi = []

while True:
    action = input('URL or undo/redo [q for exit]:')
    if action.lower() == 'q':
        print('Closing program...')
        break
    
    elif action.lower() == 'undo':
        temp_navi.append(stack_navi[-1])
        del stack_navi[-1]
    
    elif action.lower() == 'redo': 
        stack_navi.append(temp_navi[-1])
        del temp_navi[-1]
    
    else:
        temp_navi = []
        stack_navi.append(action)
    
    print(stack_navi)
    print(temp_navi)


'''
Printer
'''

print_queue = []

while True:
    action = input('Insert doc or select print/exit[q] >')

    if 'q' == action.lower():
        break
    elif 'print' == action.lower():
        if len(print_queue) > 0:
            print(f'Printed document: {print_queue[0]}')
            del print_queue[0]
        else:
            print('Any documents in queue...')
    else:
        print_queue.append(action)
    
    print(print_queue)
