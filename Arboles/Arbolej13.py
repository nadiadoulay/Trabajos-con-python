from tree import BinaryTree, Node

arbol = BinaryTree()

arbol.root = Node("¿La misión es intergaláctica?")
arbol.root.left = Node("¿Es una misión en equipo?")
arbol.root.left.left = Node("Guardianes de la Galaxia")
arbol.root.left.right = Node("Capitana Marvel")
arbol.root.right =Node ("¿Es una misión de destrucción?")
arbol.root.right.left = Node ("¿Se necesita destruir ejércitos completos?")
arbol.root.right.left.left = Node("Thor")
arbol.root.right.left.right = Node("Hulk")
arbol.root.right.right = Node("¿Es una misión de recuperación?")
arbol.root.right.right.left = Node("¿Requiere infiltrarse con personas del lugar?")
arbol.root.right.right.left.left = Node("Black Widow")
arbol.root.right.right.left.right = Node("¿Debe pasar desapercibido?")
arbol.root.right.right.left.right.left = Node("Ant-Man")
arbol.root.right.right.left.right.right = Node("Capitán América")
arbol.root.right.right.right = Node("¿Es una misión de defensa?")
arbol.root.right.right.right.left = Node("Iron Man")
arbol.root.right.right.right.right = Node("¿Se requiere decidir rápidamente la próxima acción y moverse entre lugares?")
arbol.root.right.right.right.right.left = Node("Doctor Strange")
arbol.root.right.right.right.right.right = Node("Spider-Man")

def determinar_heroe(arbol):
    aux = arbol.root

    while aux.left is not None or aux.right is not None:
        print(aux.value)
        respuesta = input("¿Sí o no? ")

        if respuesta.lower() == "si":
            aux = aux.left
        else:
            aux = aux.right

    return aux.value

print("Héroe seleccionado:", determinar_heroe(arbol))
