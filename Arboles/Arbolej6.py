from tree import BinaryTree
from cola import Queue

arbol_nombre = BinaryTree()
arbol_ranking = BinaryTree()
arbol_especie = BinaryTree()

jedis = [
    {
        "name": "Yoda",
        "species": "Unknown",
        "birth_year": 896,
        "lightsaber_color": ["Green"],
        "ranking": ["Jedi Master"],
        "master": []
    },
    {
        "name": "Luke Skywalker",
        "species": "Human",
        "birth_year": 19,
        "lightsaber_color": ["Green", "Blue"],
        "ranking": ["Jedi Knight", "Jedi Master"],
        "master": ["Yoda", "Obi-Wan Kenobi"]
    },
    {
        "name": "Obi-Wan Kenobi",
        "species": "Human",
        "birth_year": 57,
        "lightsaber_color": ["Blue"],
        "ranking": ["Jedi Master"],
        "master": ["Qui-Gon Jinn"]
    },
    {
        "name": "Anakin Skywalker",
        "species": "Human",
        "birth_year": 41,
        "lightsaber_color": ["Blue"],
        "ranking": ["Jedi Knight"],
        "master": ["Obi-Wan Kenobi"]
    },
    {
        "name": "Ahsoka Tano",
        "species": "Togruta",
        "birth_year": 36,
        "lightsaber_color": ["Green", "White"],
        "ranking": ["Padawan"],
        "master": ["Anakin Skywalker"]
    },
    {
        "name": "Ki-Adi-Mundi",
        "species": "Cerean",
        "birth_year": 92,
        "lightsaber_color": ["Blue"],
        "ranking": ["Jedi Master"],
        "master": []
    },
    {
        "name": "Plo Koon",
        "species": "Kel Dor",
        "birth_year": 382,
        "lightsaber_color": ["Yellow"],
        "ranking": ["Jedi Master"],
        "master": []
    },
    {
        "name": "Mace Windu",
        "species": "Human",
        "birth_year": 72,
        "lightsaber_color": ["Purple"],
        "ranking": ["Jedi Master"],
        "master": []
    }
]

class Jedi:
    def __init__(self,name,species,birth_year,lightsaber_color,ranking,master):
        self.name=name
        self.species=species
        self.birth_year=birth_year
        self.lightsaber_color=lightsaber_color
        self.ranking=ranking
        self.master=master

for jedi in jedis:
    dato= Jedi(
        jedi["name"],
        jedi["species"],
        jedi["birth_year"],
        jedi["lightsaber_color"],
        jedi["ranking"],
        jedi["master"]
    )
        

arbol_nombre.insert_node(dato.name,dato)
arbol_ranking.insert_node(dato.ranking[0],dato)
arbol_especie.insert_node(dato.species,dato)

print("Inorden por nombre:")
arbol_nombre.inorden()

print("\nInorden por ranking:")
arbol_ranking.inorden()

print("Por nivel de ranking:")
arbol_ranking.by_level()

print("Por nivel de especie:")
arbol_especie.by_level()

nodo= arbol_nombre.search("Yoda")
if nodo is not None:
    jedi=nodo.other_values
    print(f"Nombre: {jedi.name}")
    print(f"Especie: {jedi.species}")
    print(f"Año: {jedi.birth_year}")
    print(f"Sable: {jedi.lightsaber_color}")
    print(f"Ranking: {jedi.ranking}")
    print(f"Maestro: {jedi.master}")

nodo2= arbol_nombre.search("Luke Skywalker")
if nodo2 is not None:   
    jedi=nodo2.other_values
    print(f"Nombre: {jedi.name}")
    print(f"Especie: {jedi.species}")
    print(f"Año: {jedi.birth_year}")
    print(f"Sable: {jedi.lightsaber_color}")
    print(f"Ranking: {jedi.ranking}")
    print(f"Maestro: {jedi.master}")

print("Jedis Masters:")

def mostrar_masters(nodo):
    if nodo is None:
        return
    
    mostrar_masters(nodo.left)
    
    jedi = nodo.other_values
    if "Jedi Master" in jedi.ranking:
        print(f"Nombre: {jedi.name}")
        print(f"Especie: {jedi.species}")
        print(f"Año: {jedi.birth_year}")
        print(f"Sable: {jedi.lightsaber_color}")
        print(f"Ranking: {jedi.ranking}")
        print(f"Maestro: {jedi.master}")
        print("-" * 30)
    
    mostrar_masters(nodo.right)
mostrar_masters(arbol_ranking.root)

def mostrar_lightsaber_color(nodo, color_buscado):
    if nodo is None:
        return

    mostrar_lightsaber_color(nodo.left, color_buscado)

    jedi = nodo.other_values
    if color_buscado in jedi.lightsaber_color:
        print(f"Nombre: {jedi.name}")
        print(f"Especie: {jedi.species}")
        print(f"Año: {jedi.birth_year}")
        print(f"Sable: {jedi.lightsaber_color}")
        print(f"Ranking: {jedi.ranking}")
        print(f"Maestro: {jedi.master}")
        print("-" * 30)

    mostrar_lightsaber_color(nodo.right, color_buscado)

print("Jedis con sable verde:")
mostrar_lightsaber_color(arbol_nombre.root, "Green")

def listar_jedi_con_maestros_en_archivo(arbol_nombres):
    def recorrer(nodo):
        if nodo is None:
            return
        
        recorrer(nodo.left)

        jedi = nodo.other_values
        
        if jedi.master: 
            todos_existen = True
            
            for maestro in jedi.master:
                nodo_maestro = arbol_nombres.search(maestro)
                if nodo_maestro is None:
                    todos_existen = False
                    break
            
            if todos_existen:
                print(f"Nombre: {jedi.name}")
                print(f"Maestros: {jedi.master}")
                print(f"Especie: {jedi.species}")
                print("-" * 30)
        
        recorrer(nodo.right)
    
    print("Jedi cuyos maestros están en el archivo:")
    recorrer(arbol_nombres.root)

def mostrar_jedis_togruta(arbol_especies):
    def recorrer(nodo):
        if nodo is None:
            return
        
        recorrer(nodo.left)

        jedi = nodo.other_values
        
        if jedi.species == "Togruta":
            print(f"Nombre: {jedi.name}")
            print(f"Especie: {jedi.species}")
            print(f"Año: {jedi.birth_year}")
            print(f"Sable: {jedi.lightsaber_color}")
            print(f"Ranking: {jedi.ranking}")
            print(f"Maestro: {jedi.master}")
            print("-" * 30)
        
        recorrer(nodo.right)
    
    print("Jedis de la especie Togruta:")
    recorrer(arbol_especies.root)

def mostrar_jedis_cerean(arbol_especies):
    def recorrer(nodo):
        if nodo is None:
            return
        
        recorrer(nodo.left)

        jedi = nodo.other_values
        
        if jedi.species == "Cerean":
            print(f"Nombre: {jedi.name}")
            print(f"Especie: {jedi.species}")
            print(f"Año: {jedi.birth_year}")
            print(f"Sable: {jedi.lightsaber_color}")
            print(f"Ranking: {jedi.ranking}")
            print(f"Maestro: {jedi.master}")
            print("-" * 30)
        
        recorrer(nodo.right)
    
    print("Jedis de la especie Cerean:")
    recorrer(arbol_especies.root)

mostrar_jedis_togruta(arbol_especie)
mostrar_jedis_cerean(arbol_especie)

def listar_jedi_por_nombre(arbol_nombres):
    def recorrer(nodo):
        if nodo is None:
            return
        
        recorrer(nodo.left)
        
        jedi = nodo.other_values
        nombre = jedi.name
        
    
        if nombre.startswith('A') or '-' in nombre:
            print(f"Nombre: {nombre}")
            print(f"Especie: {jedi.species}")
            print(f"Año: {jedi.birth_year}")
            print(f"Sable: {jedi.lightsaber_color}")
            print(f"Ranking: {jedi.ranking}")
            print(f"Maestro: {jedi.master}")
            print("-" * 30)
        
        recorrer(nodo.right)
    
    print("Jedis que empiezan con 'A' o tienen '-' en el nombre:")
    recorrer(arbol_nombres.root)