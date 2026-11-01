from list_ import List

l = List()

personajes = [
    ["Luke Skywalker", 172, 19, "M", "Humano", "Tatooine", [4, 5, 6, 7, 8, 9]],
    ["Leia Organa", 150, 19, "F", "Humano", "Alderaan", [4, 5, 6, 7, 8, 9]],
    ["Han Solo", 180, 32, "M", "Humano", "Corellia", [4, 5, 6, 7]],
    ["Darth Vader", 202, 45, "M", "Humano", "Tatooine", [3, 4, 5, 6]],
    ["Chewbacca", 228, 200, "M", "Wookiee", "Kashyyyk", [3, 4, 5, 6, 7, 8, 9]],
    ["Yoda", 66, 900, "M", "Desconocida", "Desconocido", [1, 2, 3, 5, 6]],
    ["R2-D2", 96, 66, "M", "Droide", "Naboo", [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ["C-3PO", 167, 112, "M", "Droide", "Tatooine", [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ["BB-8", 67, 10, "M", "Droide", "Desconocido", [7, 8, 9]],
    ["Rey", 170, 19, "F", "Humano", "Jakku", [7, 8, 9]],
    ["Finn", 178, 23, "M", "Humano", "Desconocido", [7, 8, 9]],
    ["Poe Dameron", 176, 32, "M", "Humano", "Yavin IV", [7, 8, 9]],
    ["Padmé Amidala", 165, 27, "F", "Humano", "Naboo", [1, 2, 3]],
    ["Jar Jar Binks", 196, 25, "M", "Gungan", "Naboo", [1, 2, 3]],
    ["Maz Kanata", 124, 1000, "F", "Desconocida", "Takodana", [7, 8, 9]],
]


for personaje in personajes:
    l.append(personaje)

print("Personajes femeninos:")
for personaje in l:
    if personaje[3] == "F":
        print(personaje[0])

print ("Personajes Droide que aparecen en los primeros 6 episodios:")

for personaje in l:
    if personaje[4]== "Droide" and 1 in personaje[6] or 2 in personaje[6] or 3 in personaje[6] or 4 in personaje[6] or 5 in personaje[6] or 6 in personaje[6]:
        print(personaje[0])

for personaje in l:
    if personaje[0]=="Darth Vader" or personaje[0]=="Han Solo":
        print(personaje)

print("Personajes que aparecen en los episodios 4, 5, 6 y 7:")
for personaje in l:
    if 4 in personaje[6] and 5 in personaje[6] and 6 in personaje[6] and 7 in personaje[6]:
        print(personaje)

pjMasViejo = l[0]

print("Personajes mayores a 850:")
for personaje in l:
    if personaje[2]>850:
        print(personaje[0])
        if personaje[2]>pjMasViejo[2]:
            pjMasViejo=personaje

print("El personaje más viejo es:", pjMasViejo[0], "con una edad de", pjMasViejo[2], "años.")


for personaje in l:
    if personaje[6]==[4,5,6]:
        l.delete_value(personaje)
print("Lista después de eliminar personajes que aparecen solo en los episodios 4, 5 y 6")
l.show()

for personaje in l:
    if personaje[4]=="Humano" and personaje[5]=="Alderaan":
        print(personaje[0], "es un humano que nació en Alderaan.")

print ("Personajes cuya altura es menor a 70 cm")
for personaje in l:
    if personaje[1]<70:
        print(personaje[0], "mide", personaje[1], "cm.")

for personaje in l:
    if personaje[0]=="Chewbacca":
        print ("Episodios en los que aparece Chewbacca:", personaje[6])
        print(personaje)

