from cola import Queue

cola = Queue()

semaforo= [("rojo", 15), 
          ("amarillo",3), 
          ("verde",5)]

for s in semaforo:
    cola.arrive(s)

for i in range (6):
    semaforo= cola.on_front()
    print(f"El semaforo esta en {semaforo[0]} por {semaforo[1]} segundos")
    cola.move_to_end()



