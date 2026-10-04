from list_ import List

superheroes = [
    {
        "nombre": "Linterna Verde",
        "anio_aparicion": 1940,
        "casa": "DC",
        "biografia": "Heroe que utiliza un anillo de poder para crear construcciones de energia."
    },
    {
        "nombre": "Wolverine",
        "anio_aparicion": 1974,
        "casa": "Marvel",
        "biografia": "Mutante con garras de adamantium y factor de curacion acelerado."
    },
    {
        "nombre": "Dr. Strange",
        "anio_aparicion": 1963,
        "casa": "DC",
        "biografia": "Hechicero supremo que protege la Tierra mediante las artes misticas."
    },
    {
        "nombre": "Iron Man",
        "anio_aparicion": 1963,
        "casa": "Marvel",
        "biografia": "Millonario que combate el crimen usando una armadura tecnologica."
    },
    {
        "nombre": "Batman",
        "anio_aparicion": 1939,
        "casa": "DC",
        "biografia": "Vigilante de Gotham que utiliza un traje con multiples herramientas."
    },
    {
        "nombre": "Superman",
        "anio_aparicion": 1938,
        "casa": "DC",
        "biografia": "Kriptoniano con fuerza sobrehumana y capacidad de volar."
    },
    {
        "nombre": "Flash",
        "anio_aparicion": 1956,
        "casa": "DC",
        "biografia": "Velocista capaz de moverse a velocidades extraordinarias."
    },
    {
        "nombre": "Star-Lord",
        "anio_aparicion": 1976,
        "casa": "Marvel",
        "biografia": "Lider de los Guardianes de la Galaxia y experto piloto."
    },
    {
        "nombre": "Capitana Marvel",
        "anio_aparicion": 1968,
        "casa": "Marvel",
        "biografia": "Heroina con poderes cosmicos y gran resistencia."
    },
    {
        "nombre": "Mujer Maravilla",
        "anio_aparicion": 1941,
        "casa": "DC",
        "biografia": "Princesa amazona experta en combate y estrategia."
    },
    {
        "nombre": "Black Widow",
        "anio_aparicion": 1964,
        "casa": "Marvel",
        "biografia": "Espia entrenada en combate cuerpo a cuerpo."
    },
    {
        "nombre": "Black Panther",
        "anio_aparicion": 1966,
        "casa": "Marvel",
        "biografia": "Rey de Wakanda que utiliza un traje de vibranium."
    },
    {
        "nombre": "Moon Knight",
        "anio_aparicion": 1975,
        "casa": "Marvel",
        "biografia": "Justiciero nocturno con multiples personalidades."
    },
    {
        "nombre": "Shazam",
        "anio_aparicion": 1940,
        "casa": "DC",
        "biografia": "Heroe que obtiene poderes magicos al pronunciar una palabra."
    }
]

class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia
    
    def __str__(self):
        return f"{self.nombre} ({self.casa}) - {self.anio_aparicion}: {self.biografia}"
    
def by_nombre(item):
    return item.nombre

def by_anio_aparicion(item):
    return item.anio_aparicion

lista_superheroes = List()
lista_superheroes.add_criterion('nombre', by_nombre)
lista_superheroes.add_criterion('anio_aparicion', by_anio_aparicion)

for hero in superheroes:
    lista_superheroes.append(
        Superheroe(
            hero['nombre'],
            hero['anio_aparicion'],
            hero['casa'],
            hero['biografia']
        )
    )

lista_superheroes.show()

heroe_eliminado = lista_superheroes.delete_value("Linterna Verde", criterion='nombre')
print(f"\nHeroe eliminado: {heroe_eliminado}\n")

wolverine = lista_superheroes.search("Wolverine", "nombre")

if wolverine is not None:
    print(
        "Año de aparición de Wolverine:",
        lista_superheroes[wolverine].anio_aparicion
    )
else:
    print("Wolverine no encontrado")

dr_strange= lista_superheroes.search ("Dr. Strange", "nombre")
if dr_strange is not None:
   lista_superheroes[dr_strange].casa = "Marvel"
   print(lista_superheroes[dr_strange])


print("Superhéroes cuya biografía menciona traje o armadura:")

for hero in lista_superheroes:
    if "traje" in hero.biografia.lower() or "armadura" in hero.biografia.lower():
        print(hero.nombre)

print("Superheroes aparecidos antes de 1963:")
for hero in lista_superheroes:
    if hero.anio_aparicion<1963:
        print(hero.nombre, hero.casa)

capitanaMarvel= lista_superheroes.search("Capitana Marvel","nombre")
MujerMaravilla= lista_superheroes.search("Mujer Maravilla","nombre")

if capitanaMarvel is not None:
    print("Estudio al que pertenece capitana marvel:",lista_superheroes[capitanaMarvel].casa)
else:
    print ("Capitana marvel no encontrada")

if MujerMaravilla is not None:
    print("Estudio al que pertenece Mujer Maravilla:",lista_superheroes[MujerMaravilla].casa)
else:
    print ("Mujer Maravilla no encontrada")

Flash= lista_superheroes.search("Flash","nombre")
StarLord= lista_superheroes.search("Star-Lord","nombre")

if Flash is not None:
    print("Informacion de Flash:",lista_superheroes[Flash])
else:
    print ("Flash no encontrado")

if StarLord is not None:
    print("Informacion de Star lord:",lista_superheroes[StarLord])
else:
    print ("Star lord no encontrado")

Marvel=0
dc=0

for hero in lista_superheroes:
    if hero.casa=="Marvel":
        Marvel=Marvel+1
    if hero.casa=="DC":
        dc=dc+1

print("Cantidad de heroes que hay en marvel:",Marvel)
print("Cantidad de heroes que hay en DC:",dc)

for hero in lista_superheroes:
    if hero.nombre.startswith(("B", "M", "S")):
        print(hero.nombre)