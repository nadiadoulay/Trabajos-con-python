from random import randint
from list_ import List

l=List()

for i in range(20):
    l.append(randint(0,50))


l.show()

print("La cantidad de elementos es: ",l.size())
