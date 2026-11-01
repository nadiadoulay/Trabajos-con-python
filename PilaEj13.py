from stack import Stack

pila = Stack()
pilaAux = Stack()

trajes = [
    ("Mark I", "Iron Man", "Destruido"),
    ("Mark II", "Iron Man", "Dañado"),
    ("Mark III", "Iron Man", "Impecable"),
    ("Mark IV", "Iron Man 2", "Impecable"),
    ("Mark V", "Iron Man 2", "Dañado"),
    ("Mark VI", "Iron Man 2", "Impecable"),
    ("Mark VII", "The Avengers", "Dañado"),
    ("Mark XLII", "Iron Man 3", "Destruido"),
    ("Mark XLIII", "Avengers: Age of Ultron", "Impecable"),
    ("Mark XLIV", "Avengers: Age of Ultron", "Dañado"),  # Hulkbuster
    ("Mark XLV", "Avengers: Age of Ultron", "Impecable"),
    ("Mark XLVI", "Capitan America: Civil War", "Dañado"),
    ("Mark XLVII", "Spider-Man: Homecoming", "Impecable"),
    ("Mark L", "Avengers: Infinity War", "Dañado"),
    ("Mark LXXXV", "Avengers: Endgame", "Destruido")
]
for traje in trajes:
    pila.push(traje)

existe = False
while pila.size() > 0:
    traje = pila.pop()

    if traje[0]== "Mark XLIV":
        print("El traje Mark XLIV aparece en la película", traje[1])

    if traje[2] == "Dañado":
        print("El traje", traje[0], "está dañado")

    if traje[2] == "Impecable" or traje[2] == "Dañado":
        pilaAux.push(traje)
    elif traje[2] == "Destruido":
        print("El traje", traje[0], "está destruido")

    if traje[0] == "Mark LXXXV" and traje[1] == "Avengers: Infinity War":
        existe = True
        print("El traje Mark LXXXV aparece en la película Avengers: Infinity War")
        
    if traje[1] == "Spider-Man: Homecoming" or traje[1] == "Capitan America: Civil War":
        print("En esa película aparece:", traje[0])

if not existe:
            pilaAux.push(("Mark LXXXV", "Avengers: Infinity War", "Impecable"))



while pilaAux.size() > 0:
    pila.push(pilaAux.pop())

print("Pila final:")
pila.show()