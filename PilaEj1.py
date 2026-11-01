from random import randint
from stack import Stack

pila= Stack()

for i in range(10):
    pila.push(randint(1,10))


pila.show()

search_value = int(input('ingrese un numero para contar ocurrencias '))
counter=0

while pila.size()>0:
    value=pila.pop()
    if value==search_value:
        counter+=1

print(f"El valor {search_value} se encuentra {counter} veces en la pila")
