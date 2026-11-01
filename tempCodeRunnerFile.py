from list_ import List
from cola import Queue
from super_heroes_data import superheroes


class Superheroe:
     def __init__(self, name,alias, real_name, short_bio, first_appearance, is_villain):
        self.name=name
        self.alias=alias
        self.real_name=real_name
        self.short_bio=short_bio
        self.first_appearance=first_appearance
        self.is_villain=is_villain

     def __str__(self):
        return f"{self.name}-{self.alias}-{ self.real_name}-{self.short_bio}-{self.first_appearance}-{self.is_villain}"

#Criterios
def by_name(item):
      return item.name
def by_real_name(item):
      return item.real_name
def by_first_appearance(item):
      return item.first_appearance


listaHeroes=List()
listaHeroes.add_criterion ('name',by_name)
listaHeroes.add_criterion ('real_name',by_real_name)
listaHeroes.add_criterion ('first_appearance',by_first_appearance)

for heroe in superheroes:
      listaHeroes.append(Superheroe(
            heroe['name'],
            heroe['alias'],
            heroe['real_name'],
            heroe['short_bio'],
            heroe['first_appearance'],
            heroe['is_villain'],
      ))

#Consigna1
print ("Listado ordenado ascendentemente por los nombres de los personajes:")
listaHeroes.sort_by_criterion('name')
listaHeroes.show()

print()

#Consigna2
TheThing=listaHeroes.search("The Thing","name")
if TheThing is not None:
     print ("The Thing se encuentra en la posicion:",TheThing)
else:
     print ("The Thing no se encuentra en la lista:")

RocketRaccoon=listaHeroes.search("Rocket Raccoon","name")
if RocketRaccoon is not None:
     print ("Rocket Raccoon se encuentra en la posicion:",RocketRaccoon)
else:
     print ("Rocket Raccoon no se encuentra en la lista:")

print()

#Consigna3
print("Villanos de la lista:")
for heroe in listaHeroes:
    if heroe.is_villain:
        print(heroe)

print()

#Consigna4
cola = Queue()
colaAux = Queue()

for heroe in listaHeroes:
    if heroe.is_villain:
      cola.arrive(heroe)

tam=cola.size()

print("Villanos aparecidos antes de 1980:")
for i in range(tam):
     per=cola.attention()
     if per.first_appearance<1980:
          print(per)
     colaAux.arrive(per)

while colaAux.size() > 0:
    cola.arrive(colaAux.attention())

print()

#Consigna5
print("Superhéroes que comienzan con Bl, G, My y W:")

for heroe in listaHeroes:
    if heroe.name.startswith(("Bl", "G", "My", "W")):
        print(heroe)

print()

#Consigna6
print ("Listado ordenado ascendentemente por los nombres reales de los personajes:")
listaHeroes.sort_by_criterion('real_name')
listaHeroes.show()

print()

#Consigna7
print ("Listado de los superheroes ordenados por fecha de aparicion:")
listaHeroes.sort_by_criterion('first_appearance')
listaHeroes.show()

print()

#Consigna8
for heroe in listaHeroes:
     if heroe.name=="Ant Man":
          heroe.real_name="Scott Lang"

print()

#Consigna9
print ("Personajes en cuya biografia aparece time-traveling o suit:")
for heroe in listaHeroes:
     if "time-traveling" in heroe.short_bio.lower() or "suit" in heroe.short_bio.lower():
          print (heroe.name)

print()

#Consigna10
electro=listaHeroes.delete_value("Electro", "name")
if electro is not None:
     print("Electro eliminado")
else:
     print("Electro no estaba en la lista")
print(electro)

BaronZemo=listaHeroes.delete_value("Baron Zemo", "name")
if BaronZemo is not None:
     print("Baron Zemo eliminado")
else:
     print("Baron Zemo no estaba en la lista")
print(BaronZemo)
