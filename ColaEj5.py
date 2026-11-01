from cola import Queue
from random import randint
from stack import Stack

cola = Queue()
pila = Stack()
pilaAux = Stack()

for i in range(10):
    pila.push(randint(1, 10))

print("Pila original:")
pila.show()

while pila.size()>0:
    num = pila.pop()
    cola.arrive(num)

while cola.size()>0:
    num=cola.attention()
    pilaAux.push(num)

while pilaAux.size()>0:
    num=pilaAux.pop()
    cola.arrive(num)

while cola.size()>0:
    num=cola.attention()
    pila.push(num)

print("Pila invertida:")
pila.show()