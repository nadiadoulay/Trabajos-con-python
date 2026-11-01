from stack import Stack

peliculas = [
    {"titulo": "Captain America: The Winter Soldier", "estudio": "Marvel Studios", "año": 2014},
    {"titulo": "Guardians of the Galaxy", "estudio": "Marvel Studios", "año": 2014},
    {"titulo": "X-Men: Days of Future Past", "estudio": "20th Century Fox", "año": 2014},
    {"titulo": "Interstellar", "estudio": "Warner Bros", "año": 2014},

    {"titulo": "Avengers: Age of Ultron", "estudio": "Marvel Studios", "año": 2015},
    {"titulo": "Mad Max: Fury Road", "estudio": "Warner Bros", "año": 2015},

    {"titulo": "Captain America: Civil War", "estudio": "Marvel Studios", "año": 2016},
    {"titulo": "Doctor Strange", "estudio": "Marvel Studios", "año": 2016},
    {"titulo": "Deadpool", "estudio": "20th Century Fox", "año": 2016},
    {"titulo": "Batman v Superman: Dawn of Justice", "estudio": "Warner Bros", "año": 2016},

    {"titulo": "Black Panther", "estudio": "Marvel Studios", "año": 2018},
    {"titulo": "Avengers: Infinity War", "estudio": "Marvel Studios", "año": 2018},
    {"titulo": "Ant-Man and the Wasp", "estudio": "Marvel Studios", "año": 2018},
    {"titulo": "Venom", "estudio": "Sony Pictures", "año": 2018}
]

Pila=Stack()
Pila_aux=Stack()
cont=0
for pelicula in peliculas:
    Pila.push(pelicula)


print ("Peliculas estrenadas en 2014:")
while Pila.size()>0:
    pelicula=Pila.pop()
    if pelicula["año"]==2014:
        print (pelicula["titulo"])
    if pelicula["año"]==2018:
        cont=cont+1
    Pila_aux.push(pelicula)


print ("Cantidad de peliculas estrenadas en el 2018:",cont)

print ("Peliculas de marvel estrenadas en el 2016:")

while Pila_aux.size()>0:
    pelicula=Pila_aux.pop()
    if pelicula ["estudio"]=="Marvel Studios" and pelicula["año"]==2016:
        print (pelicula["titulo"])

    Pila.push(pelicula)





