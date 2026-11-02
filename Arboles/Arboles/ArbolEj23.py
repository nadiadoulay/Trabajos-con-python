from tree import BinaryTree
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()



arbol = BinaryTree()


criaturas = [
    ("Ceto", []),
    ("Tifón", ["Zeus"]),
    ("Equidna", ["Argos Panoptes"]),
    ("Dino", []),
    ("Pefredo", []),
    ("Enio", []),
    ("Escila", []),
    ("Caribdis", []),
    ("Euríale", []),
    ("Esteno", []),
    ("Medusa", ["Perseo"]),
    ("Ladón", ["Heracles"]),
    ("Águila del Cáucaso", []),
    ("Quimera", ["Belerofonte"]),
    ("Hidra de Lerna", ["Heracles"]),
    ("León de Nemea", ["Heracles"]),
    ("Esfinge", ["Edipo"]),
    ("Dragón de la Cólquida", []),
    ("Cerbero", []),
    ("Cerda de Cromión", ["Teseo"]),
    ("Ortro", ["Heracles"]),
    ("Toro de Creta", ["Teseo"]),
    ("Jabalí de Calidón", ["Atalanta"]),
    ("Carcinos", []),
    ("Gerión", ["Heracles"]),
    ("Cloto", []),
    ("Láquesis", []),
    ("Átropos", []),
    ("Minotauro de Creta", ["Teseo"]),
    ("Harpías", []),
    ("Argos Panoptes", ["Hermes"]),
    ("Aves del Estínfalo", []),
    ("Talos", ["Medea"]),
    ("Sirenas", []),
    ("Pitón", ["Apolo"]),
    ("Cierva de Cerinea", []),
    ("Basilisco", []),
    ("Jabalí de Erimanto", [])
]

for criatura, derrotado_por in criaturas:
    arbol.insert_node(criatura, {
        "derrotado_por": derrotado_por,
        "descripcion": "",
        "capturada": None
    })


print("Criaturas en inorden y quienes las derrotaron:")
arbol.inorden_creatures()


print("Cargar descripcion de una criatura:")
arbol.cargar_descripcion()

print("Informacion de Talos:")
arbol.show_creature("Talos")

print("Los 3 heroes o dioses que mas criaturas derrotaron:")
arbol.top_defeaters()

print("Criaturas derrotadas por Heracles:")
arbol.creatures_defeated_by("Heracles")

print("Criaturas que no han sido derrotadas:")
arbol.creatures_not_defeated()

print("Capturar criaturas con Heracles:")

arbol.capture_creature("Cerbero", "Heracles")
arbol.capture_creature("Toro de Creta", "Heracles")
arbol.capture_creature("Cierva de Cerinea", "Heracles")
arbol.capture_creature("Jabalí de Erimanto", "Heracles")

nombre = input("Ingrese el nombre o parte del nombre de la criatura: ")
arbol.search_coincidence(nombre)

print("Eliminar Basilisco y Sirenas:")

arbol.delete_node("Basilisco")
arbol.delete_node("Sirenas")

criatura = arbol.search("Aves del Estínfalo")

if criatura is not None:
    criatura.other_values["derrotado_por"].append("Heracles")

criatura = arbol.search("Ladón")

if criatura is not None:
    datos = criatura.other_values
    arbol.delete_node("Ladón")
    arbol.insert_node("Dragón Ladón", datos)

print("Listado de criaturas por nivel:")
arbol.by_level()

print("Criaturas capturadas por Heracles:")
arbol.creatures_captured_by("Heracles")