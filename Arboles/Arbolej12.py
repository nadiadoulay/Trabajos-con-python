from tree import BinaryTree
from cola import Queue
from list_ import List

arbol = BinaryTree()

arbol.insert_node(50)
arbol.insert_node(30)
arbol.insert_node(70)
arbol.insert_node(20)
arbol.insert_node(40)
arbol.insert_node(60)
arbol.insert_node(80)
arbol.insert_node(10)
arbol.insert_node(25)
arbol.insert_node(35)
arbol.insert_node(45)
arbol.insert_node(55)
arbol.insert_node(65)
arbol.insert_node(75)
arbol.insert_node(90)

arbol.insert_node(5)
arbol.insert_node(15)
arbol.insert_node(22)
arbol.insert_node(28)
arbol.insert_node(32)
arbol.insert_node(38)
arbol.insert_node(42)
arbol.insert_node(48)
arbol.insert_node(52)
arbol.insert_node(58)
arbol.insert_node(62)
arbol.insert_node(68)
arbol.insert_node(72)
arbol.insert_node(78)
arbol.insert_node(85)
arbol.insert_node(95)

arbol.by_level()

bosque = []

def cortar_nodos_por_nivel(arbol, nivel):
    def cortar_nodos(root, nivel_actual):
        if root is None:
            return

        if nivel_actual == nivel:
            bosque.append(root)
            return

        cortar_nodos(root.left, nivel_actual + 1)
        cortar_nodos(root.right, nivel_actual + 1)

    cortar_nodos(arbol.root, 1)


cortar_nodos_por_nivel(arbol, 3)

def contar_nodos(root):
    if root is None:
        return 0
    return 1 + contar_nodos(root.left) + contar_nodos(root.right)


arbol_con_mas_nodos = 0

print("Cantidad de nodos en cada arbol del bosque:")

for arbol in bosque:
    cantidad = contar_nodos(arbol)
    print(arbol.value, ":", cantidad)

    if cantidad > arbol_con_mas_nodos:
        arbol_con_mas_nodos = cantidad

def preorden(root):
    if root is not None:
        print(root.value)
        preorden(root.left)
        preorden(root.right)

print("preorden de cada arbol del bosque:")

for arbol in bosque:
    print("Arbol", arbol.value)
    preorden(arbol)


arbol_con_mas_nodos = None
mayor_cantidad = 0

for arbol in bosque:
    cantidad = contar_nodos(arbol)

    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        arbol_con_mas_nodos = arbol

print("Arbol con mayor cantidad de nodos:")
print(arbol_con_mas_nodos.value)

def es_completo(root):
    cola = Queue()
    cola.arrive(root)
    encontrado_vacio = False

    while cola.size() > 0:
        nodo = cola.attention()

        if nodo.left is not None:
            if encontrado_vacio:
                return False
            cola.arrive(nodo.left)
        else:
            encontrado_vacio = True

        if nodo.right is not None:
            if encontrado_vacio:
                return False
            cola.arrive(nodo.right)
        else:
            encontrado_vacio = True

    return True

print("Arboles completos:")

for arbol in bosque:
    if es_completo(arbol):
        print(arbol.value)

