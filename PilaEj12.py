from stack import Stack

pila = Stack()
pilaAux = Stack()

personajes = [
    "Luke Skywalker",
    "Darth Vader",
    "Han Solo",
    "Leia Organa",
    "Obi-Wan Kenobi",
    "Yoda",
    "Boba Fett",
    "Chewbacca",
    "R2-D2",
    "C-3PO"
]

for personaje in personajes:
    pila.push(personaje)

encontro_leia = False
encontro_boba = False

while pila.size() > 0:
    value = pila.pop()

    if value == "Leia Organa":
        encontro_leia = True
    elif value == "Boba Fett":
        encontro_boba = True

    pilaAux.push(value)

while pilaAux.size() > 0:
    pila.push(pilaAux.pop())


if encontro_leia:
    print("Leia Organa está en la pila")

if encontro_boba:
    print("Boba Fett está en la pila")

pila.show()