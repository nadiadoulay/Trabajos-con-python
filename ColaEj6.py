from cola import Queue
from random import randint

cola = Queue()
cont= 0
for i in range(20):
    cola.arrive(randint(1,10))

buscar = int(input("Ingrese el número a buscar: "))


size = cola.size()

for i in range(size):
    if cola.move_to_end() == buscar:
        cont += 1

print(f"El número {buscar} se encontró {cont} veces en la cola.")