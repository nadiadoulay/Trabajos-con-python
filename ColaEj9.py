from cola import Queue
from random import randint

cola = Queue()  
contNegativos = 0

for i in range(12):
    cola.arrive (randint (-10,10))

num = cola.attention( )
minimo = num
maximo = num

cola.arrive(num)


for i in range(12):
    num= cola.attention( )
    if num < 0:
        contNegativos += 1
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
    cola.arrive(num)

rango = maximo - minimo

print("Cantidad de numeros negativos: ", contNegativos)
print("El numero minimo es: ", minimo)
print("El numero maximo es: ", maximo)
print("El rango es: ", rango)







