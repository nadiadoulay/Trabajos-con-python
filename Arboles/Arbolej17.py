from tree import BinaryTree

pokemones = [
    ["Bulbasaur", 1, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"]],
    ["Ivysaur", 2, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"]],
    ["Venusaur", 3, ["Planta", "Veneno"], ["Fuego", "Hielo", "Volador", "Psíquico"]],
    ["Charmander", 4, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Charmeleon", 5, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Charizard", 6, ["Fuego", "Volador"], ["Agua", "Eléctrico", "Roca"]],
    ["Squirtle", 7, ["Agua"], ["Eléctrico", "Planta"]],
    ["Wartortle", 8, ["Agua"], ["Eléctrico", "Planta"]],
    ["Blastoise", 9, ["Agua"], ["Eléctrico", "Planta"]],
    ["Caterpie", 10, ["Bicho"], ["Fuego", "Volador", "Roca"]],
    ["Pikachu", 25, ["Eléctrico"], ["Tierra"]],
    ["Raichu", 26, ["Eléctrico"], ["Tierra"]],
    ["Sandshrew", 27, ["Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Sandslash", 28, ["Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Vulpix", 37, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Ninetales", 38, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Jigglypuff", 39, ["Normal", "Hada"], ["Veneno", "Acero"]],
    ["Zubat", 41, ["Veneno", "Volador"], ["Eléctrico", "Hielo", "Psíquico", "Roca"]],
    ["Psyduck", 54, ["Agua"], ["Eléctrico", "Planta"]],
    ["Golduck", 55, ["Agua"], ["Eléctrico", "Planta"]],
    ["Growlithe", 58, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Arcanine", 59, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Geodude", 74, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Graveler", 75, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Golem", 76, ["Roca", "Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Ponyta", 77, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Slowpoke", 79, ["Agua", "Psíquico"], ["Eléctrico", "Planta", "Bicho", "Fantasma", "Siniestro"]],
    ["Magnemite", 81, ["Eléctrico", "Acero"], ["Fuego", "Lucha", "Tierra"]],
    ["Magneton", 82, ["Eléctrico", "Acero"], ["Fuego", "Lucha", "Tierra"]],
    ["Farfetch'd", 83, ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"]],
    ["Doduo", 84, ["Normal", "Volador"], ["Eléctrico", "Hielo", "Roca"]],
    ["Grimer", 88, ["Veneno"], ["Tierra", "Psíquico"]],
    ["Gengar", 94, ["Fantasma", "Veneno"], ["Tierra", "Psíquico", "Fantasma", "Siniestro"]],
    ["Drowzee", 96, ["Psíquico"], ["Bicho", "Fantasma", "Siniestro"]],
    ["Voltorb", 100, ["Eléctrico"], ["Tierra"]],
    ["Electrode", 101, ["Eléctrico"], ["Tierra"]],
    ["Cubone", 104, ["Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Marowak", 105, ["Tierra"], ["Agua", "Planta", "Hielo"]],
    ["Koffing", 109, ["Veneno"], ["Tierra", "Psíquico"]],
    ["Rhyhorn", 111, ["Tierra", "Roca"], ["Agua", "Planta", "Hielo"]],
    ["Chansey", 113, ["Normal"], ["Lucha"]],
    ["Scyther", 123, ["Bicho", "Volador"], ["Fuego", "Eléctrico", "Hielo", "Volador", "Roca"]],
    ["Magikarp", 129, ["Agua"], ["Eléctrico", "Planta"]],
    ["Lapras", 131, ["Agua", "Hielo"], ["Eléctrico", "Planta", "Lucha", "Roca"]],
    ["Eevee", 133, ["Normal"], ["Lucha"]],
    ["Vaporeon", 134, ["Agua"], ["Eléctrico", "Planta"]],
    ["Jolteon", 135, ["Eléctrico"], ["Tierra"]],
    ["Flareon", 136, ["Fuego"], ["Agua", "Tierra", "Roca"]],
    ["Dratini", 147, ["Dragón"], ["Hielo", "Dragón", "Hada"]],
    ["Dragonite", 149, ["Dragón", "Volador"], ["Hielo", "Roca", "Dragón", "Hada"]],
]

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemones:
    arbol_nombre.insert_node(pokemon[0], pokemon)

for pokemon in pokemones:
    arbol_numero.insert_node(pokemon[1], pokemon)

for pokemon in pokemones:
    for tipo in pokemon[2]:
        arbol_tipo.insert_node(tipo, pokemon)


numero = int(input("Ingrese el número del Pokémon: "))

nodo = arbol_numero.search(numero)

if nodo is not None:
    print(nodo.other_values)
else:
    print("Pokémon no encontrado")


nombre = input("Ingrese el nombre o parte del nombre: ").lower()

def buscar_proximidad(root):
    if root is not None:
        buscar_proximidad(root.left)

        if nombre in root.value.lower():
            print(root.other_values)

        buscar_proximidad(root.right)

buscar_proximidad(arbol_nombre.root)

def mostrar_tipo(root, tipo):
    if root is not None:
        mostrar_tipo(root.left, tipo)

        if root.value == tipo:
            print(root.other_values)

        mostrar_tipo(root.right, tipo)

print("Pokemones de tipo agua:")
mostrar_tipo(arbol_tipo.root, "Agua")

print("Pokemones de tipo fuego:")
mostrar_tipo(arbol_tipo.root, "Fuego")

print("Pokemones de tipo planta:")
mostrar_tipo(arbol_tipo.root, "Planta")

print("Pokemones de tipo eléctrico:")
mostrar_tipo(arbol_tipo.root, "Eléctrico")


print("Orden ascendente por número:")
arbol_numero.inorden()

print("Orden ascendente por nombre:")
arbol_nombre.inorden()

print("Listado por nivel por nombre:")
arbol_nombre.by_level()

print("Pokemones con debilidades a Jolteon, Lycanroc y Tyrantrum;")
def mostrar_debilidades(root):
    if root is not None:
        mostrar_debilidades(root.left)

        pokemon = root.other_values

        if ("Eléctrico" in pokemon[3] or
            "Roca" in pokemon[3] or
            "Dragón" in pokemon[3]):
            print(pokemon)

        mostrar_debilidades(root.right)

mostrar_debilidades(arbol_nombre.root)

tipos = {}

for pokemon in pokemones:
    for tipo in pokemon[2]:
        if tipo in tipos:
            tipos[tipo] += 1
        else:
            tipos[tipo] = 1

for tipo, cantidad in tipos.items():
    print(tipo, cantidad)