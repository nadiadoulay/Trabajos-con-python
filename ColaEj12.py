from cola import Queue

cola1 = Queue()
cola2 = Queue()
cola= Queue()

datos1 = [1, 4, 7, 10, 13, 15]
datos2 = [2, 3, 5, 8, 9, 11, 14]

for dato in datos1:
    cola1.arrive(dato)

for dato in datos2:    
    cola2.arrive(dato)


while cola1.size()>0 and cola2.size()>0:
    if cola1.on_front()<cola2.on_front():
        cola.arrive(cola1.attention())
    else:
       cola.arrive(cola2.attention())

while cola1.size() > 0:
    cola.arrive(cola1.attention())

while cola2.size() > 0:
    cola.arrive(cola2.attention())

cola.show()


