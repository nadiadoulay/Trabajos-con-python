from tree import BinaryTree

arbol=BinaryTree()

arbol.insert_node(8)
arbol.insert_node(3)
arbol.insert_node(12)
arbol.insert_node(1)
arbol.insert_node(5)
arbol.insert_node(15)
arbol.insert_node(7)
arbol.insert_node(10)
arbol.insert_node(16)
arbol.insert_node(20)
arbol.insert_node(18)

print("cantidad de nodos:")
print(arbol.contar_nodos())

print("Cantidad de hojas:")
print(arbol.contar_hojas())

print("Padre del nodo 7:")
print(arbol.padre(7))

print("altura del arbol:")
print(arbol.altura())