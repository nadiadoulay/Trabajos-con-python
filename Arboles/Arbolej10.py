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

valor = int(input("Ingrese el nivel del arbol que desea determinar si es completo: "))

valoresperado=2**valor

print("El nivel del arbol deberia tener",valoresperado,"nodos para ser completo")

cantidad_real= arbol.contar_nodos_nivel(valor)

print("El nivel del arbol tiene",cantidad_real,"nodos")
