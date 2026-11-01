from random import randint
from stack import Stack

pila= Stack()

for i in range(10):
    pila.push(randint(1,10))


pila_aux = Stack()

while pila.size() > 0:
    value = pila.pop()
    if value % 2 == 0:
        pila_aux.push(value)

print("PARES:")
pila_aux.show()