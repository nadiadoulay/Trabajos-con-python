from cola import Queue

cola = Queue()

letras = ["h", "o", "l", "a", "x", "y", "e", "m"]

for letra in letras:
    cola.arrive(letra)

print("Cola original:")
cola.show()

size = cola.size()

for i in range(size):

    letra = cola.attention()

    if letra not in "aeiouAEIOU":
        cola.arrive(letra)

print("Cola sin vocales:")
cola.show()