from tree import BinaryTree
from random import randint

arbol= BinaryTree()

for i in range(1000):
    num = randint(1, 1000)
    arbol.insert_node(num)

print("preorden:")
arbol.preorden()

print("inorden:")
arbol.inorden()

print("postorden:")
arbol.postorden()

numero=input("¿que numero desea buscar?")

aux=arbol.search(int(numero))

if aux is not None:
    print("el numero se encuentra en el arbol")
else:
    print("el numero no se encuentra en el arbol")

num1= input("Ingrese el primer numero a eliminar: ")
num2= input("Ingrese el segundo numero a eliminar: ")
num3= input("Ingrese el tercer numero a eliminar: ")

arbol.delete_node(int(num1))
arbol.delete_node(int(num2))
arbol.delete_node(int(num3))

def altura(root):

    if root is None:
        return 0

    izq = altura(root.left)
    der = altura(root.right)

    if izq > der:
        return izq + 1
    else:
        return der + 1

altura_izq = altura(arbol.root.left)
altura_der = altura(arbol.root.right)

print("Altura subárbol izquierdo:", altura_izq)
print("Altura subárbol derecho:", altura_der)

ocurrencia= input("Ingrese el numero que desea buscar la cantidad de ocurrencias: ")

def contar_ocurrencias(root, buscado):

    if root is None:
        return 0

    contador = 0

    if root.value == buscado:
        contador = 1

    return contador + contar_ocurrencias(root.left, buscado) + contar_ocurrencias(root.right, buscado)

cantidad = contar_ocurrencias(arbol.root, int(ocurrencia))

print("Cantidad de ocurrencias:", cantidad)

par=0
impar=0

def contar_par_impar(root):
    if root is None:
        return 0, 0  # (pares, impares)

    pares_izq, impares_izq = contar_par_impar(root.left)
    pares_der, impares_der = contar_par_impar(root.right)

    par = 1 if root.value % 2 == 0 else 0
    impar = 1 if root.value % 2 != 0 else 0

    total_pares = pares_izq + pares_der + par
    total_impares = impares_izq + impares_der + impar

    return total_pares, total_impares


pares, impares = contar_par_impar(arbol.root)

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)




