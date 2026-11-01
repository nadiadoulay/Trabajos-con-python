from stack import Stack

pila = Stack()
pila_aux = Stack()

pila.push("hola")
pila.push("como")
pila.push("estas")
pila.push("bien")

i = int(input("Ingrese la posición a eliminar (desde la cima): "))

contador = 0

while pila.size() > 0:
    value = pila.pop()

    if contador != i:
        pila_aux.push(value)

    contador += 1


while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print("Pila final:")
pila.show()