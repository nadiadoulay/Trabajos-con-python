from tree import BinaryTree, Node
from Archivo import Archivo
from list_ import List

arbol = BinaryTree()

personajes = [
    ["Luke Skywalker", 172, 77],
    ["Yoda", 66, 17],
    ["Boba Fett", 183, 78],
    ["Darth Vader", 202, 136],
    ["Leia Organa", 150, 49],
    ["Han Solo", 180, 80],
    ["Chewbacca", 228, 112],
    ["R2-D2", 96, 32],
    ["C-3PO", 167, 75],
    ["Obi-Wan Kenobi", 182, 77],
    ["Anakin Skywalker", 188, 84],
    ["Padmé Amidala", 165, 45],
    ["Mace Windu", 188, 84],
    ["Palpatine", 173, 75],
    ["Finn", 178, 73],
    ["Poe Dameron", 176, 80],
    ["Rey", 170, 54],
    ["Kylo Ren", 189, 87],
    ["Jabba the Hutt", 175, 1358],
    ["Darth Maul", 175, 80]
]

archivo = Archivo("personajes.dat")
archivo.abrir()

for personaje in personajes:
    nrr = archivo.guardar(personaje)
    arbol.insert_node(personaje[0], nrr)

archivo.cerrar()

def cargar_pj (nombre,altura,peso):
    personaje = [nombre, altura, peso]
    archivo.abrir()
    nrr= archivo.guardar(personaje)
    archivo.cerrar()
    arbol.insert_node(nombre, nrr)

cargar_pj("Ahsoka Tano", 168, 54)

def modificar_pj(nombre, altura, peso):

    nodo = arbol.search(nombre)

    if nodo is not None:
        personaje = [nombre, altura, peso]

        archivo.abrir()
        archivo.modificar(nodo.other_values, personaje)
        archivo.cerrar()

modificar_pj("Ahsoka Tano", 170, 54)


def dar_de_baja(nombre):

    nodo = arbol.search(nombre)

    if nodo is not None:
        arbol.delete_node(nombre)

dar_de_baja("Ahsoka Tano")


print("Determinar si Yoda y Boba Fett están en el árbol y mostrar sus datos:")
nodo = arbol.search("Yoda")

if nodo is not None:
    archivo.abrir()
    personaje = archivo.leer(nodo.other_values)
    archivo.cerrar()
    print(personaje)

nodo = arbol.search("Boba Fett")

if nodo is not None:
    archivo.abrir()
    personaje = archivo.leer(nodo.other_values)
    archivo.cerrar()
    print(personaje)


personajes_mas_1m = []

def recorrer(root):
    if root is not None:
        recorrer(root.left)

        archivo.abrir()
        personaje = archivo.leer(root.other_values)
        archivo.cerrar()

        if personaje[1] > 100:
            personajes_mas_1m.append(personaje)

        recorrer(root.right)

recorrer(arbol.root)

print("Personajes con altura mayor a 1m:")

for personaje in personajes_mas_1m:
    print(personaje)

personajes_menos_75kg = []

def recorrer(root):
    if root is not None:
        recorrer(root.left)

        archivo.abrir()
        personaje = archivo.leer(root.other_values)
        archivo.cerrar()

        if personaje[2] < 75:
            personajes_menos_75kg.append(personaje)

        recorrer(root.right)

recorrer(arbol.root)

print("Personajes que pesan menos de 75 kg:")

for personaje in personajes_menos_75kg:
    print(personaje)