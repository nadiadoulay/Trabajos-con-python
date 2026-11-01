from cola import Queue
from random import randint
from stack import Stack

cola = Queue()
pila = Stack()

for i in range(10):
    cola.arrive(randint(1, 10))

print("Cola original:")
cola.show()

while cola.size() >0:
    pila.push(cola.attention())

while pila.size() >0:
    cola.arrive(pila.pop())

print("Cola invertida:")
cola.show()
    
