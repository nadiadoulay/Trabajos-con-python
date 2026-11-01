from cola import Queue
from random import randint
from stack import Stack

cola = Queue()
pila = Stack()

palabra= input("Ingrese una palabra: ")

for letra in palabra:
    cola.arrive(letra)
    pila.push(letra)

palindromo = True

while cola.size()>0:
    letraCola = cola.attention()
    letraPila = pila.pop()
    if letraCola != letraPila:
        palindromo = False
if palindromo:
    print("La palabra es un palíndromo")
else:    print("La palabra no es un palíndromo")