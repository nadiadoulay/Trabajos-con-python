from random import randint
from list_ import List

l = List()

for i in range(20):
    l.append(randint(1, 50))

print("Lista original:")
l.show()


def esPrimo(num):

    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


for num in l[:]:

    if esPrimo(num):
        l.delete_value(num)

print("\nLista sin números primos:")
l.show()

