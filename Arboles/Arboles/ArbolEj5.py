from tree import BinaryTree
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()



arbol = BinaryTree()

arbol.insert_node("Black Panther", {"is_villain": False})
arbol.insert_node("Black Widow", {"is_villain": False})
arbol.insert_node("Captain America", {"is_villain": False})
arbol.insert_node("Captain Marvel", {"is_villain": False})
arbol.insert_node("Doctor Strangee", {"is_villain": False})
arbol.insert_node("Drax", {"is_villain": False})
arbol.insert_node("Falcon", {"is_villain": False})
arbol.insert_node("Hulk", {"is_villain": False})
arbol.insert_node("Iron Man", {"is_villain": False})
arbol.insert_node("Loki", {"is_villain": True})
arbol.insert_node("Nebula", {"is_villain": True})
arbol.insert_node("Scarlet Witch", {"is_villain": False})
arbol.insert_node("Spider-Man", {"is_villain": False})
arbol.insert_node("Star-Lord", {"is_villain": False})
arbol.insert_node("Thanos", {"is_villain": True})
arbol.insert_node("Thor", {"is_villain": False})
arbol.insert_node("Ultron", {"is_villain": True})
arbol.insert_node("Vision", {"is_villain": False})
arbol.insert_node("Winter Soldier", {"is_villain": False})
arbol.insert_node("Wong", {"is_villain": False})



print ("villanos ordenados alfabeticamente:")
arbol.inorden_villain()

print ("Heroes que comienzan con la letra C:")
arbol.inorden_hero_star_with("C")

print ("Cantidad de heroes en el arbol:")
print(arbol.count_heroes())

nombre = input("Dr Strange esta mal cargado, ingrese su nombre aproximado para modificar: ")

arbol.proxy_search(nombre)

arbol.split_tree(arbol_heroes, arbol_villanos)

print ("Heroes ordenados de manera descendente:")
arbol.postorden_hero()

print("Cantidad de superhéroes:")
print(arbol_heroes.count_nodes())

print("Cantidad de villanos:")
print(arbol_villanos.count_nodes())

print("Superhéroes ordenados alfabéticamente:")
arbol_heroes.inorden()

print("Villanos ordenados alfabéticamente:")
arbol_villanos.inorden()
