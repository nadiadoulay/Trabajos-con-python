from graph import Graph

g = Graph(is_dir=False)

g.add_vertex("Red Hat", "Notebook")
g.add_vertex("Debian", "Notebook")
g.add_vertex("Arch", "Notebook")

g.add_vertex("Manjaro", "PC")
g.add_vertex("Fedora", "PC")
g.add_vertex("Ubuntu", "PC")
g.add_vertex("Mint", "PC")
g.add_vertex("Parrot", "PC")

g.add_vertex("Guarani", "Servidor")
g.add_vertex("MongoDB", "Servidor")
g.add_vertex("Router 1", "Router")
g.add_vertex("Router 2", "Router")
g.add_vertex("Router 3", "Router")

g.add_vertex("Switch 1", "Switch")
g.add_vertex("Switch 2", "Switch")

g.add_vertex("Impresora", "Impresora")


g.add_edge(37,'Router 1','Router 2')
g.add_edge(43,'Router 1','Router 3')
g.add_edge(29,'Router 1','Switch 1')
g.add_edge(25,'Router 2','Red Hat')
g.add_edge(9,'Router 2','Guarani')
g.add_edge(50,'Router 2','Router 3')
g.add_edge(61,'Router 3','Switch 2')
g.add_edge(40,'Switch 2','Manjaro')
g.add_edge(12,'Switch 2','Parrot')
g.add_edge(3,'Switch 2','Fedora')
g.add_edge(5,'Switch 2','MongoDB')
g.add_edge(56,'Switch 2','Arch')
g.add_edge(17,'Switch 1','Debian')
g.add_edge(18,'Switch 1','Ubuntu')
g.add_edge(80,'Switch 1','Mint')
g.add_edge(22,'Switch 1','Impresora')

g.delete_edge('Switch 1', 'Impresora')
g.add_edge(22,'Switch 2','Impresora')

print("RECORRIDO EN PROFUNDIDAD")

g.deep_show("Red Hat")
g.deep_show("Debian")
g.deep_show("Arch")


print("RECORRIDO EN AMPLITUD")

g.amplitude_show("Red Hat")
g.amplitude_show("Debian")
g.amplitude_show("Arch")


paths = g.dijkstra('Manjaro')

destination = 'Impresora'
peso_total = None
camino_completo = []

while paths.size() > 0:
    value = paths.pop()

    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]

        camino_completo.append(value[0])
        destination = value[2]

camino_completo.reverse()

print(f'el camino mas corto desde Manjaro a la impresora es: {"-".join(camino_completo)} con un costo de {peso_total}')

paths = g.dijkstra('Red Hat')

destination = 'Impresora'
peso_total = None
camino_completo = []

while paths.size() > 0:
    value = paths.pop()

    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]

        camino_completo.append(value[0])
        destination = value[2]

camino_completo.reverse()

print(f'el camino mas corto desde Red Hat a la impresora es: {"-".join(camino_completo)} con un costo de {peso_total}')

paths = g.dijkstra('Fedora')

destination = 'Impresora'
peso_total = None
camino_completo = []

while paths.size() > 0:
    value = paths.pop()

    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]

        camino_completo.append(value[0])
        destination = value[2]

camino_completo.reverse()

print(f'el camino mas corto desde Fedora a la impresora es: {"-".join(camino_completo)} con un costo de {peso_total}')

min_tree = g.kruskal('Switch 1')

print(min_tree)

peso_total = 0

for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)

print(f'peso total: {peso_total}')


pcs = ['Manjaro', 'Fedora', 'Ubuntu', 'Mint', 'Parrot']

peso_menor = None
pc_menor = None

for pc in pcs:
    paths = g.dijkstra(pc)

    destination = 'Guarani'
    peso_total = None

    while paths.size() > 0:
        value = paths.pop()

        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]

            destination = value[2]

    if peso_total is not None:
        if peso_menor is None or peso_total < peso_menor:
            peso_menor = peso_total
            pc_menor = pc

print(f'La PC con el camino más corto hasta Guaraní es {pc_menor} con un costo de {peso_menor}')


pcs = ['Debian','Ubuntu', 'Mint']

peso_menor = None
pc_menor = None

for pc in pcs:
    paths = g.dijkstra(pc)

    destination = 'MongoDB'
    peso_total = None

    while paths.size() > 0:
        value = paths.pop()

        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]

            destination = value[2]

    if peso_total is not None:
        if peso_menor is None or peso_total < peso_menor:
            peso_menor = peso_total
            pc_menor = pc

print(f'La PC con el camino más corto hasta MongoDB es {pc_menor} con un costo de {peso_menor}')

