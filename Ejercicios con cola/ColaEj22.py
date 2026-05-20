from cola import Queue

cola = Queue()


personajes = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Peter Parker", "Spider-Man", "M"),
    ("Wanda Maximoff", "Scarlet Witch", "F"),
    ("Bruce Banner", "Hulk", "M"),
    ("Stephen Strange", "Doctor Strange", "M"),
    ("Sam Wilson", "Falcon", "M"),
    ("Shuri", "Black Panther", "F")
]

for personaje in personajes:
    cola.arrive(personaje)

    size= cola.size()

for i in range(size):
    personaje=cola.attention()
    if personaje[1]=="Capitana Marvel":
        print("El nombre de Capitana Marvel es:", personaje[0])
    cola.arrive(personaje)

print("Personajes femeninos:")
for i in range(size):
    personaje=cola.attention()
    if personaje[2]=="F":
        print(personaje[1])
    cola.arrive(personaje)

print("Nombres de los personajes masculinos:")
for i in range(size):
    personaje=cola.attention()
    if personaje[2]=="M":
        print(personaje[0])
    cola.arrive(personaje)

for i in range(size):
    personaje=cola.attention()
    if personaje[0]=="Scott Lang":
        print("El nombre de superheroe de Scott Lang es:", personaje[1])
    cola.arrive(personaje)

print("Personajes que comienzan con 'S':")
for i in range(size):
    personaje=cola.attention()
    if personaje[0][0] == "S" or personaje[1][0] == "S":
        print(personaje)
    cola.arrive(personaje)

encontrado = False
for i in range(size):
    personaje=cola.attention()
    if personaje[0]=="Carol Danvers":
        encontrado = True
    cola.arrive(personaje)

if encontrado:
    print("Carol Danvers se encuentra en la cola y su nombre de superhéroe es Capitana Marvel.")
