from cola import Queue

personajes = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Bruce Banner", "superheroe": "Hulk", "genero": "M"},
    {"personaje": "Thor Odinson", "superheroe": "Thor", "genero": "M"},
    {"personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Black Panther", "genero": "F"}
]

cola= Queue()
colaAux=Queue()

for personaje in personajes:
    cola.arrive(personaje)

tam=cola.size()

for i in range(tam):
    p=cola.attention()
    if p["superheroe"]=="Capitana Marvel":
        print ("El nombre de Capitana marvel es:",p["personaje"])
    colaAux.arrive(p)

print ("Heroes femeninos:")
for i in range(tam):
    p=colaAux.attention()
    if p["genero"]=="F":
        print(p["superheroe"])
    cola.arrive(p)

print ("Heroes masculinos:")
for i in range(tam):
    p=cola.attention()
    if p["genero"]=="M":
        print(p["personaje"])
    colaAux.arrive(p)

for i in range(tam):
    p=colaAux.attention()
    if p["personaje"]=="Scott Lang":
        print ("El nombre de heroe de Scott Lang es:",p["superheroe"])
    cola.arrive(p)    

print("Personajes o superheroes que comienzan con S:")

for i in range(tam):
    p = cola.attention()

    if p["personaje"].startswith("S") or p["superheroe"].startswith("S"):
        print(p)

    print("Personajes o superheroes que comienzan con S:")

for i in range(tam):
    p = cola.attention()

    if p["personaje"].startswith("S") or p["superheroe"].startswith("S"):
        print(p)
    colaAux.arrive(p)

    
for i in range(tam):
    p=colaAux.attention()
    if p["personaje"]=="Carol Danvers":
        print ("El nombre de heroe de Carol Danvers es:",p["superheroe"])
    cola.arrive(p)