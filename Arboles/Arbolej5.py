from tree import BinaryTree
from random import randint

arbol = BinaryTree()

personajes = {
    "Ant-Man": True,
    "Black Panther": True,
    "Black Widow": True,
    "Captain America": True,
    "Captain Marvel": True,
    "Doctor Strage": True,
    "Falcon": True,
    "Hawkeye": True,
    "Hulk": True,
    "Iron Man": True,
    "Moon Knight": True,
    "Ms. Marvel": True,
    "Shang-Chi": True,
    "She-Hulk": True,
    "Spider-Man": True,
    "Star-Lord": True,
    "Thor": True,
    "Vision": True,
    "War Machine": True,
    "Wasp": True,
    "Wong": True,

    "Abomination": False,
    "Agatha Harkness": False,
    "Arishem": False,
    "Baron Zemo": False,
    "Dormammu": False,
    "Ego": False,
    "Gorr": False,
    "Green Goblin": False,
    "Hela": False,
    "Kang": False,
    "Killmonger": False,
    "Kingpin": False,
    "Loki": False,
    "Mysterio": False,
    "Red Skull": False,
    "Ronan": False,
    "Thanos": False,
    "Ultron": False,
    "Vulture": False,
    "Yellowjacket": False
}

for personaje in personajes:
    arbol.insert_node(personaje, personajes[personaje])

def listar_villanos(root):
    if root is not None:
        listar_villanos(root.left)
        if root.other_values == False:
            print(root.value)
        listar_villanos(root.right)

print("Villanos en el árbol:")
listar_villanos(arbol.root)


def Superheroes_con_C (root):
            if root is not None:
                Superheroes_con_C(root.left)
                if root.other_values == True and root.value.startswith('C'):
                    print(root.value)
                Superheroes_con_C(root.right)

print("Superhéroes que comienzan con 'C':")
Superheroes_con_C(arbol.root)

def contar_heroes(root):
    if root is None:
        return 0
    else:
        count = 1 if root.other_values == True else 0
        count += contar_heroes(root.left)
        count += contar_heroes(root.right)
        return count

print("Cantidad de superhéroes en el árbol:", contar_heroes(arbol.root))


def heroes_ordenados_descendente(root):
     if root is not None:
          heroes_ordenados_descendente(root.right)
          if root.other_values == True:
                 print(root.value)


print("Superhéroes ordenados de manera descendente:")
heroes_ordenados_descendente(arbol.root)