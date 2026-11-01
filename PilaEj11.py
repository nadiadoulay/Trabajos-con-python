from stack import Stack

pila = Stack()
contador= 0
letras = ["a", "b", "e", "k", "i", "m", "o", "z", "u", "p", "r", "t"]

for letra in letras:
    pila.push(letra)
  
while pila.size()>0:
    value= pila.pop()
    if value in ["a", "e", "i", "o", "u"]:
        contador += 1

print("El número de vocales es: ", contador)