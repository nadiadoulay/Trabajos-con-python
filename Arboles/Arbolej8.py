from tree import BinaryTree

arbol=BinaryTree()

arbol.insert_node(8)
arbol.insert_node(3)
arbol.insert_node(12)
arbol.insert_node(1)
arbol.insert_node(5)
arbol.insert_node(15)

def minimo(arbol):

    if arbol.root is None:
        return None

    nodo = arbol.root

    while nodo.left is not None:
        nodo = nodo.left

    return nodo.value

def maximo(arbol):

    if arbol.root is None:
        return None

    nodo = arbol.root

    while nodo.right is not None:
        nodo = nodo.right

    return nodo.value

print(minimo(arbol))
print(maximo(arbol))