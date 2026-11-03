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
