from random import randint
from stack import Stack

pila = Stack()
pilaAux = Stack()

for i in range(15):
    numero = randint(1, 10)
    print("Número generado:", numero)

   
    while pila.size() > 0 and pila.on_top() > numero:
        pilaAux.push(pila.pop())

    pila.push(numero)

    while pilaAux.size() > 0:
        pila.push(pilaAux.pop())

print("Pila ordenada (de menor a mayor):")
pila.show()