from stack import Stack
from random import randint

pila = Stack()
pila_oro = Stack()
pila_espada = Stack()
pila_basto = Stack()
pila_copa = Stack()
pila_ordenada = Stack()


for i in range (12):
    palos= ["espada","copa","oro","basto"]
    numero= randint(1,12)
    palo = palos[randint(0,3)]
    cartas= (numero,palo)

    pila.push(cartas)


while pila.size() > 0:
    carta= pila.pop()

    if carta[1]== "oro": 
        pila_oro.push(carta)
    elif carta[1]== "espada": 
        pila_espada.push(carta)
    elif carta[1]== "basto": 
        pila_basto.push(carta)
    else:
        pila_copa.push(carta)

print("Cartas de oro:")
pila_oro.show()
print("Cartas de espada:")
pila_espada.show()
print("Cartas de basto:")
pila_basto.show()
print("Cartas de copa:")
pila_copa.show()


lista_oro = []

while pila_oro.size() > 0:
    lista_oro.append(pila_oro.pop())

lista_oro.sort(key=lambda carta: carta[0])

for carta in lista_oro:
    pila_oro.push(carta)

print("Cartas de oro ordenadas:")
pila_oro.show()

