from stack import Stack

pilaAux = Stack()
pila = Stack()
contador=0
dioses = ["Zeus", "Hera", "Poseidon", "Ares", "Apolo", "Artemisa"]

for dios in dioses:
    pila.push(dios)

i=int(input("En que posicion quiere agregar a Atenea"))

while pila.size() > 0:
    valor = pila.pop()

    if contador == i:
        pilaAux.push("Atenea")

    pilaAux.push(valor)
    contador += 1

if contador <= i:
    pilaAux.push("Atenea")

while pilaAux.size() > 0:
    pila.push(pilaAux.pop())

print("Pila final:")
pila.show()

