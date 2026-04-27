from stack import Stack

personajes = [
    ("Iron Man", 10),
    ("Captain America", 9),
    ("Thor", 8),
    ("Hulk", 7),
    ("Black Widow", 8),
    ("Hawkeye", 6),
    ("Spider-Man", 6),
    ("Doctor Strange", 6),
    ("Black Panther", 5),
    ("Captain Marvel", 3),
    ("Scarlet Witch", 7),
    ("Vision", 5),
    ("Falcon", 6),
    ("Winter Soldier", 6),
    ("Star-Lord", 5),
    ("Gamora", 5),
    ("Drax", 5),
    ("Rocket Raccoon", 5),
    ("Groot", 4),
    ("Nebula", 5),
    ("Ant-Man", 5),
    ("Wasp", 3),
    ("Loki", 6),
    ("Shuri", 3),
    ("Okoye", 3),
    ("Mantis", 4),
    ("Yondu", 2),
    ("War Machine", 7)
]

pila = Stack()
posicion = 1
pilaAuxiliar = Stack()

for personaje in personajes:
    pila.push(personaje)

while pila.size()>0:
    personaje = pila.pop()
    if personaje[0] == "Rocket Raccoon":
        print(f"Posición de Rocket Raccoon: {posicion}")
    if personaje[0] == "Groot":
        print(f"Posición de Groot: {posicion}")
    if personaje[1]>5:
        print(f"{personaje[0]} aparece en {personaje[1]} películas")
    if personaje[0]== "Black Widow":
        print(f"{personaje[0]} aparece en {personaje[1]} películas")
    if personaje[0][0] in ["C", "D", "G"]:
        print(f"Personajes que empiezan con C, D o G: {personaje[0]}")
    posicion += 1

    pilaAuxiliar.push(personaje)


while pilaAuxiliar.size()>0:
    pila.push(pilaAuxiliar.pop())