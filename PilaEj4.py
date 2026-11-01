from random import randint
from stack import Stack

pila=Stack()
pilaaux=Stack()

for i in range(10):
    pila.push(randint(1,10))

print("Pila original:")
pila.show()

while pila.size()>0:
    value=pila.pop()
    pilaaux.push(value)

print("Pila invertida:")
pilaaux.show()