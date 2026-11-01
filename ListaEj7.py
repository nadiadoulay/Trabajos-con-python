from random import randint
from list_ import List

l1=List()
l2=List()
l3=List()
l4=List()
coincidencias=0

for i in range(10):
    l1.append(randint(0,20))

for i in range(10):
    l2.append(randint(0,20))

print("Lista 1:")
l1.show()

print("Lista 2:")
l2.show()

for elemento in l1:
    l3.append(elemento)

for elemento in l2:
    l3.append(elemento)

print("Lista 3 (concatenación de lista 1 y lista 2):")
l3.show()

for elemento in l1:
    if elemento not in l4:
        l4.append(elemento)

for elemento in l2:
    if elemento not in l4:
        l4.append(elemento)

print("Lista 4 (elementos únicos de lista 1 y lista 2):")
l4.show()

for elemento in l1:
    if elemento in l2:
        coincidencias += 1

print("Cantidad de elementos que coinciden entre lista 1 y lista 2:", coincidencias)

l5 = List()

for elemento in l1:
    l5.append(elemento)
while l5.size() > 0:
    print("Eliminado:", l5[0])
    l5.delete_value(l5[0])

print 

