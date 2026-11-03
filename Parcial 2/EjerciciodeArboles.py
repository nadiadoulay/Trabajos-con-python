from tree import BinaryTree

import json

with open("pokemonData.json", "r", encoding="utf-8") as archivo:
    pokemones = json.load(archivo)

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()




for pokemon in pokemones:
    arbol_nombre.insert_node(pokemon["nombre"], pokemon)
    arbol_numero.insert_node(pokemon["numero"], pokemon)
    for tipo in pokemon["tipos"]:
        arbol_tipo.insert_node(tipo, pokemon)



def mostrar_por_numero(raiz):
    if raiz is not None:
        mostrar_por_numero(raiz.left)
        print(raiz.value, "-", raiz.other_values["nombre"])
        mostrar_por_numero(raiz.right)

print("BUSQUEDA POR NUMERO")
numero = int(input("Ingrese el numero del Pokemon que desea buscar: "))


pokemon = arbol_numero.search(numero)

print()
if pokemon is not None:
    print(pokemon.other_values)
else:
    print("No se encontro el Pokemon")

print("BUSQUEDA POR NOMBRE")
nombre = input("Ingrese el nombre o parte del nombre: ")

arbol_nombre.search_coincidence(nombre)

print()

print("POKEMONS POR TIPO")

for tipo in ["Fantasma", "Fuego", "Acero", "Eléctrico"]:
    print(f"\nPokemons de tipo {tipo}:")
    arbol_tipo.names_by_type(tipo)
print()

print("POKEMONS ORDENADOS POR NUMERO:")
mostrar_por_numero(arbol_numero.root)

print()
print("POKEMONS ORDENADOS POR NOMBRE:")
arbol_nombre.inorden()

print()

print("POKEMONS ORDENADOS POR NIVEL (NOMBRE):")
arbol_nombre.by_level()

print()

print("POKEMONS DEBILES FRENTE A JOLTEON:")
arbol_nombre.search_weakness("Eléctrico")

print()

print("POKEMONS DEBILES FRENTE A LYCANROC:")
arbol_nombre.search_weakness("Roca")

print()

print("POKEMONS DEBILES FRENTE A TYRANTRUM:")
arbol_nombre.search_weakness("Roca")
arbol_nombre.search_weakness("Dragón")

print()

print("CANTIDAD DE POKEMONS POR TIPO")
arbol_tipo.count_by_type()

print()

print("CANTIDAD DE POKEMONS CON MEGAEVOLUCION")
print(arbol_numero.count_flag("mega"))

print()

print("CANTIDAD DE POKEMONS CON FORMA GIGAMAX")
print(arbol_numero.count_flag("gigamax"))

