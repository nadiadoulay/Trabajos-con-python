from stack import Stack

pila=Stack()
pilaaux=Stack()

texto= input ("Ingrese una palabra: ")

for i in range(len(texto)):
    pila.push(texto[i])

print("Palabra invertida:")

while pila.size() > 0:
    print(pila.pop(), end="")