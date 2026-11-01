from cola import Queue

cola = Queue() 

personajes = [
    ("Luke Skywalker", "Tatooine"),
    ("Leia Organa", "Alderaan"),
    ("Han Solo", "Corellia"),
    ("Yoda", "Dagobah"),
    ("Darth Vader", "Tatooine"),
    ("Chewbacca", "Kashyyyk"),
    ("R2-D2", "Naboo"),
    ("C-3PO", "Tatooine"),
    ("Obi-Wan Kenobi", "Stewjon"),
    ("Jar Jar Binks", "Naboo"),
    ("Boba Fett", "Kamino"),
    ("Anakin Skywalker", "Tatooine"),
    ("Padmé Amidala", "Naboo"),
    ("Ewok", "Endor"),
    ("Lando Calrissian", "Socorro"),
]

for personaje in personajes:
    cola.arrive(personaje)

size= cola.size()

for i in range(size):
    personaje = cola.attention()
    if personaje [1] == "Alderaan" or personaje [1]=="Tatooine" or personaje [1]=="Endor":
        print ("Personaje: ", personaje[0], "Planeta: ", personaje[1])
    cola.arrive(personaje)

for i in range(size):
    personaje = cola.attention()
    if personaje [0] == "Luke Skywalker" or personaje [0]=="Han Solo":
        print ("El planeta natal de ", personaje[0], " es: ", personaje[1])
    cola.arrive(personaje)


nuevo_personaje = ("Mace Windu", "Haruun Kal")

for i in range(size):

    personaje = cola.attention()

    if personaje[0] == "Yoda":
        cola.arrive(nuevo_personaje)

    cola.arrive(personaje)


    eliminar = False

for i in range(size):

    personaje = cola.attention()

    if eliminar:
        print("Eliminado:", personaje[0])
        eliminar = False

    else:


        cola.arrive(personaje)

        if personaje[0] == "Jar Jar Binks":
            eliminar = True


