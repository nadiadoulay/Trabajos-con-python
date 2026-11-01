from graph import Graph

g = Graph(is_dir=False)


g.add_vertex('Cocina')
g.add_vertex('Comedor')
g.add_vertex('Cochera')
g.add_vertex('Quincho')
g.add_vertex('Baño 1')
g.add_vertex('Baño 2')
g.add_vertex('Habitación 1')
g.add_vertex('Habitación 2')
g.add_vertex('Sala de estar')
g.add_vertex('Terraza')
g.add_vertex('Patio')

g.add_edge(4, 'Cocina', 'Comedor')
g.add_edge(8, 'Cocina', 'Quincho')
g.add_edge(6, 'Cocina', 'Patio')
g.add_edge(9, 'Cocina', 'Baño 1')
g.add_edge(7, 'Cocina', 'Sala de estar')
 
g.add_edge(5, 'Comedor', 'Sala de estar')
g.add_edge(12, 'Comedor', 'Cochera')
g.add_edge(6, 'Comedor', 'Baño 1')
 
g.add_edge(3, 'Habitación 1', 'Baño 1')
g.add_edge(10, 'Habitación 1', 'Sala de estar')
g.add_edge(4, 'Habitación 1', 'Habitación 2')
 
g.add_edge(3, 'Habitación 2', 'Baño 2')
g.add_edge(10, 'Habitación 2', 'Terraza')
 
g.add_edge(5, 'Baño 1', 'Sala de estar')
g.add_edge(9, 'Sala de estar', 'Terraza')
 
g.add_edge(5, 'Baño 2', 'Terraza')
g.add_edge(9, 'Baño 2', 'Patio')
 
g.add_edge(5, 'Cochera', 'Patio')
g.add_edge(6, 'Cochera', 'Quincho')
g.add_edge(4, 'Quincho', 'Patio')

min_tree = g.kruskal('Cocina')

print(min_tree)

peso_total = 0

for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)

print(f'Se necesitan los siguientes metros de cable para conectar los ambientes: {peso_total}')

paths = g.dijkstra('Habitación 1')

destination = 'Sala de estar'
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

print(f'el camino mas corto desde la habitacion 1 hasta la sala de estar es {"-".join(camino_completo)} con {peso_total} metros de cable')