from stack import Stack

print("hola")
pila5= Stack()
pila7= Stack()
pilaAux7= Stack()
pilaAux5 = Stack()

episodio5 = [
    "Luke Skywalker",
    "Darth Vader",
    "Han Solo",
    "Leia Organa",
    "Yoda",
    "Lando Calrissian",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "Boba Fett"
]

episodio7 = [
    "Rey",
    "Finn",
    "Kylo Ren",
    "Han Solo",
    "Leia Organa",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "Luke Skywalker",
    "BB-8"
]

for personaje in episodio5:
    pila5.push(personaje)

for personaje in episodio7:
    pila7.push(personaje)


while pila5.size()>0:
    personaje5=pila5.pop()

    while pila7.size()>0:
        personaje7=pila7.pop()

        if personaje5==personaje7:
            print(f"Personaje común: {personaje5}")

        pilaAux7.push(personaje7)


    while pilaAux7.size() > 0:
        pila7.push(pilaAux7.pop())

    pilaAux5.push(personaje5)


while pilaAux5.size() > 0:
    pila5.push(pilaAux5.pop())