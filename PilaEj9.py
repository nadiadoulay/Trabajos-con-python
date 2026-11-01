from stack import Stack

pila = Stack()
factorial=1
numero= int(input("Ingrese el numero del cual se quiere saber el factorial"))

for i in range(1,numero+1):
    pila.push(i)

while pila.size() > 0:
    aux= pila.pop()
    factorial=factorial*aux


print("El factorial del numero es:",factorial)
