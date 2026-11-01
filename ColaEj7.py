from cola import Queue
from random import randint

cola = Queue()

for i in range(10):
    cola.arrive(randint(1, 10))

print ("cola:")
cola.show()

posicion=int(input("Ingrese la posición del elemento a eliminar: "))

size=cola.size()

for i in range(size):
    valor = cola.attention()
    if i != posicion:
        cola.arrive(valor)


print("Cola después de eliminar el elemento en la posición", posicion, ":")
cola.show()