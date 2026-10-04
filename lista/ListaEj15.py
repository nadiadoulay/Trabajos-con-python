from list_ import List


class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - Nivel: {self.nivel} - Tipo: {self.tipo} - Subtipo: {self.subtipo}"


class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = List()

    def __str__(self):
        return (
            f"{self.nombre} - Torneos ganados: {self.torneos_ganados} - "
            f"Batallas ganadas: {self.batallas_ganadas} - "
            f"Batallas perdidas: {self.batallas_perdidas}"
        )


def by_nombre_entrenador(item):
    return item.nombre


entrenadores = List()
entrenadores.add_criterion("nombre", by_nombre_entrenador)


# ENTRENADOR 1
ash = Entrenador("Ash", 5, 20, 85)

ash.pokemons.append(Pokemon("Pikachu", 70, "Electrico", ""))
ash.pokemons.append(Pokemon("Charizard", 80, "Fuego", "Volador"))
ash.pokemons.append(Pokemon("Bulbasaur", 55, "Planta", "Veneno"))
ash.pokemons.append(Pokemon("Pikachu", 70, "Electrico", ""))

entrenadores.append(ash)


# ENTRENADOR 2
misty = Entrenador("Misty", 2, 15, 65)

misty.pokemons.append(Pokemon("Starmie", 60, "Agua", "Psiquico"))
misty.pokemons.append(Pokemon("Wingull", 45, "Agua", "Volador"))
misty.pokemons.append(Pokemon("Psyduck", 50, "Agua", ""))

entrenadores.append(misty)


# ENTRENADOR 3
brock = Entrenador("Brock", 4, 10, 70)

brock.pokemons.append(Pokemon("Onix", 65, "Roca", "Tierra"))
brock.pokemons.append(Pokemon("Tyrantrum", 78, "Roca", "Dragon"))
brock.pokemons.append(Pokemon("Geodude", 48, "Roca", "Tierra"))

entrenadores.append(brock)


# ENTRENADOR 4
cynthia = Entrenador("Cynthia", 8, 5, 95)

cynthia.pokemons.append(Pokemon("Garchomp", 90, "Dragon", "Tierra"))
cynthia.pokemons.append(Pokemon("Roserade", 75, "Planta", "Veneno"))
cynthia.pokemons.append(Pokemon("Terrakion", 85, "Roca", "Lucha"))

entrenadores.append(cynthia)


# ENTRENADOR 5
gary = Entrenador("Gary", 3, 18, 60)

gary.pokemons.append(Pokemon("Blastoise", 80, "Agua", ""))
gary.pokemons.append(Pokemon("Arcanine", 72, "Fuego", ""))
gary.pokemons.append(Pokemon("Exeggutor", 68, "Planta", "Psiquico"))

entrenadores.append(gary)


# a. cantidad de Pokémon de un determinado entrenador

nombre_entrenador = input("Ingrese el entrenador: ")

pos = entrenadores.search(nombre_entrenador, "nombre")

if pos is not None:
    print("Cantidad de Pokemons:", entrenadores[pos].pokemons.size())
else:
    print("Entrenador no encontrado")


# b. entrenadores que ganaron más de tres torneos

print("\nEntrenadores con más de tres torneos ganados:")

for entrenador in entrenadores:
    if entrenador.torneos_ganados > 3:
        print(entrenador.nombre)


# c. Pokémon de mayor nivel del entrenador con más torneos ganados

entrenador_mayor = entrenadores[0]

for entrenador in entrenadores:
    if entrenador.torneos_ganados > entrenador_mayor.torneos_ganados:
        entrenador_mayor = entrenador

pokemon_mayor = entrenador_mayor.pokemons[0]

for pokemon in entrenador_mayor.pokemons:
    if pokemon.nivel > pokemon_mayor.nivel:
        pokemon_mayor = pokemon

print("\nEntrenador con más torneos:", entrenador_mayor.nombre)
print("Pokemon de mayor nivel:", pokemon_mayor)


# d. mostrar todos los datos de un entrenador y sus Pokémon

nombre_entrenador = input("\nIngrese entrenador para mostrar sus datos: ")

pos = entrenadores.search(nombre_entrenador, "nombre")

if pos is not None:
    entrenador = entrenadores[pos]

    print(entrenador)

    print("Pokemons:")
    for pokemon in entrenador.pokemons:
        print(pokemon)
else:
    print("Entrenador no encontrado")


# e. porcentaje de batallas ganadas mayor al 79 %

print("\nEntrenadores con porcentaje de victorias mayor al 79%:")

for entrenador in entrenadores:

    total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas

    porcentaje = entrenador.batallas_ganadas * 100 / total_batallas

    if porcentaje > 79:
        print(entrenador.nombre, "-", round(porcentaje, 2), "%")


# f. entrenadores con Pokémon fuego/planta o agua/volador

print("\nEntrenadores con Pokemon fuego/planta o agua/volador:")

for entrenador in entrenadores:

    encontrado = False

    for pokemon in entrenador.pokemons:

        if (
            pokemon.tipo == "Fuego" and pokemon.subtipo == "Planta"
        ) or (
            pokemon.tipo == "Agua" and pokemon.subtipo == "Volador"
        ):
            encontrado = True

    if encontrado:
        print(entrenador.nombre)


# g. promedio de nivel de Pokémon de un entrenador

nombre_entrenador = input("\nIngrese entrenador para calcular promedio de nivel: ")

pos = entrenadores.search(nombre_entrenador, "nombre")

if pos is not None:

    entrenador = entrenadores[pos]

    suma = 0

    for pokemon in entrenador.pokemons:
        suma += pokemon.nivel

    promedio = suma / entrenador.pokemons.size()

    print("Promedio de nivel:", round(promedio, 2))

else:
    print("Entrenador no encontrado")


# h. cuántos entrenadores tienen determinado Pokémon

pokemon_buscado = input("\nIngrese nombre del Pokemon: ")

cantidad = 0

for entrenador in entrenadores:

    encontrado = False

    for pokemon in entrenador.pokemons:

        if pokemon.nombre == pokemon_buscado:
            encontrado = True

    if encontrado:
        cantidad += 1

print("Cantidad de entrenadores que tienen ese Pokemon:", cantidad)


# i. entrenadores que tienen Pokémon repetidos

print("\nEntrenadores con Pokemon repetidos:")

for entrenador in entrenadores:

    repetido = False

    for i in range(entrenador.pokemons.size()):

        for j in range(i + 1, entrenador.pokemons.size()):

            if entrenador.pokemons[i].nombre == entrenador.pokemons[j].nombre:
                repetido = True

    if repetido:
        print(entrenador.nombre)


# j. entrenadores que tengan Tyrantrum, Terrakion o Wingull

print("\nEntrenadores con Tyrantrum, Terrakion o Wingull:")

for entrenador in entrenadores:

    encontrado = False

    for pokemon in entrenador.pokemons:

        if pokemon.nombre in ("Tyrantrum", "Terrakion", "Wingull"):
            encontrado = True

    if encontrado:
        print(entrenador.nombre)


# k. determinar si entrenador X tiene Pokémon Y

nombre_entrenador = input("\nIngrese entrenador: ")
nombre_pokemon = input("Ingrese Pokemon: ")

pos = entrenadores.search(nombre_entrenador, "nombre")

if pos is not None:

    entrenador = entrenadores[pos]

    encontrado = False

    for pokemon in entrenador.pokemons:

        if pokemon.nombre == nombre_pokemon:

            encontrado = True

            print("\nDatos del entrenador:")
            print(entrenador)

            print("\nDatos del Pokemon:")
            print(pokemon)

    if not encontrado:
        print("El entrenador no tiene ese Pokemon")

else:
    print("Entrenador no encontrado")