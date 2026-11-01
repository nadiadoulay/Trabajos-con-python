
from stack import Stack
invertida = ""
pila=Stack()


texto= input ("Ingrese una palabra: ")

for i in range(len(texto)):
    pila.push(texto[i])

while pila.size()>0:
   invertida += pila.pop()


if texto==invertida:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")