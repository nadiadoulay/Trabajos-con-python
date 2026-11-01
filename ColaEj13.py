from cola import Queue
from random import choice

cola = Queue()
colaDigitos = Queue()
colaCaracteres = Queue()
letras=0

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?#@$%"

for i in range(50000):
    cola.arrive(choice(caracteres))

cola.show()

while cola.size()>0:
    elemento = cola.attention()
    if elemento == "0" or elemento == "1" or elemento == "2" or elemento == "3" or elemento == "4" or elemento == "5" or elemento == "6" or elemento == "7" or elemento == "8" or elemento == "9":
        colaDigitos.arrive(elemento)
    else:
        colaCaracteres.arrive(elemento)


hayPregunta = False
hayNumeral = False

size=colaCaracteres.size()
for i in range(size):
    elemento = colaCaracteres.attention()
    if elemento.isalpha():
        letras+=1
    if elemento == "?":
        hayPregunta = True
    if elemento == "#":
        hayNumeral = True
colaCaracteres.arrive(elemento)

print("Cantidad de letras: ",letras)
print("¿Hay signos de pregunta? ",hayPregunta)
print("¿Hay signos numeral? ",hayNumeral)





