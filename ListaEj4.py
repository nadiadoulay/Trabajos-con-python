from random import randint
from list_ import List

l=List()

for i in range(100):
    l.append(randint(1,100))

l.show()

valor=int(input("Ingrese el valor que desea agregar: "))
posicion=int(input("Ingrese la posición donde desea agregar el valor: "))   

l.insert(posicion, valor)

print("Lista después de insertar el valor: ")
l.show()