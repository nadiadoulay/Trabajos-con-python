from cola import Queue

cola = Queue()  
colaAux = Queue()
contador=0


notificaciones = [
    ("08:15", "Facebook", "Juan comentó tu foto"),
    ("09:20", "Instagram", "Nuevo seguidor"),
    ("10:05", "Twitter", "Aprendiendo Python con pilas"),
    ("10:40", "WhatsApp", "Hola, ¿cómo estás?"),
    ("11:10", "Facebook", "Tienes una nueva solicitud"),
    ("11:50", "Twitter", "Python es un gran lenguaje"),
    ("12:00", "Instagram", "Te mencionaron en una historia"),
    ("12:30", "Twitter", "Estoy practicando estructuras de datos en Python"),
    ("13:15", "WhatsApp", "Reunión a las 14"),
    ("13:45", "Facebook", "Nuevo mensaje recibido"),
    ("14:10", "Twitter", "Colas y pilas en Python"),
    ("14:50", "Instagram", "Tu publicación recibió likes"),
    ("15:20", "Twitter", "Python facilita muchas tareas"),
    ("15:40", "WhatsApp", "¿Ya terminaste el ejercicio?"),
    ("16:05", "Facebook", "Recordatorio de evento"),
    ("16:30", "Instagram", "Nueva historia disponible"),
    ("17:00", "Twitter", "Programar en Python es divertido"),
    ("17:25", "WhatsApp", "Nos vemos luego"),
    ("18:10", "Facebook", "Nuevo comentario en tu publicación"),
    ("19:00", "Twitter", "Python y algoritmos")
]

for notificacion in notificaciones:
    cola.arrive(notificacion)


size = cola.size()

for i in range(size):

    notificacion = cola.attention()

    if notificacion[1] != "Facebook":
        cola.arrive(notificacion)

for i in range(size):

    notificacion = cola.attention()

    if notificacion[1] == "Twitter" and "Python" in notificacion[2]:
        print(notificacion)

    cola.arrive(notificacion)

for i in range(size):

    notificacion = cola.attention()

    if "11:43" <= notificacion[0] <= "15:57":
        colaAux.arrive(notificacion)
        contador += 1

    cola.arrive(notificacion)

print("Cantidad de notificaciones:", contador)


    