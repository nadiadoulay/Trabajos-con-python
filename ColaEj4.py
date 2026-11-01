from cola import Queue
from random import randint

cola = Queue()

for i in range(10):
    cola.arrive(randint(1, 20))


print("Cola original:")
cola.show()


def esPrimo(numero):

    if numero < 2:
        return False


    for i in range(2, numero):

        if numero % i == 0:
            return False
        
    return True

size = cola.size()


for i in range(size):

    numero = cola.attention()


    if esPrimo(numero):
        cola.arrive(numero)

print("Cola solo con números primos:")
cola.show()