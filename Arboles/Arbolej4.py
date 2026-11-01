from tree import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range(20):
    num = randint(1, 50)
    arbol.insert_node(num)


def hijo_derecho(root):
    return root.right


def hijo_izquierdo(root):
    return root.left


derecho = hijo_derecho(arbol.root)
izquierdo = hijo_izquierdo(arbol.root)

print("Hijo derecho:", derecho.value)
print("Hijo izquierdo:", izquierdo.value)