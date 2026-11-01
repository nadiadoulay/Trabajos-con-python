from random import randint
from stack import Stack

pila=Stack()
pilaaux=Stack()

for i in range(10):
    pila.push(randint(1,10))

valor= int (input("Ingrese el valor a reemplazar: "))
valor2= int (input("Ingrese un valor nuevo: "))

while pila.size() > 0:
    value= pila.pop()
    if value == valor:
        pilaaux.push(valor2)
    else:
        pilaaux.push(value)


print("La pila con los valores reemplazados es:")
pilaaux.show()