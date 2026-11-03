from graph import Graph

g = Graph(is_dir=False)

#vertices
g.add_vertex("Luke Skywalker")
g.add_vertex("Darth Vader")
g.add_vertex("Yoda")
g.add_vertex("Boba Fett")
g.add_vertex("C3PO")
g.add_vertex("Leia")
g.add_vertex("Rey")
g.add_vertex("Kylo Ren")
g.add_vertex("Chewbacca")
g.add_vertex("Han Solo")
g.add_vertex("R2D2")
g.add_vertex("BB8")
g.add_vertex("ObiWan Kenobi")
g.add_vertex("Anakin Skywalker")
g.add_vertex("Palpatine")
g.add_vertex("Padmé Amidala")
g.add_vertex("QuiGon Jinn")
g.add_vertex("Finn")
g.add_vertex("Poe Dameron")
g.add_vertex("Jabba the Hutt")
g.add_vertex("Lando Calrissian")
g.add_vertex("Dooku")
g.add_vertex("Jar Jar Binks")
g.add_vertex("Wicket")

#aristas
g.add_edge(6, "Luke Skywalker", "C3PO")
g.add_edge(6, "Luke Skywalker", "R2D2")
g.add_edge(6, "Luke Skywalker", "Leia")
g.add_edge(6, "Luke Skywalker", "Chewbacca")
g.add_edge(5, "Luke Skywalker", "Han Solo")
g.add_edge(3, "Luke Skywalker", "Darth Vader")
g.add_edge(3, "Luke Skywalker", "Yoda")
g.add_edge(9, "C3PO", "R2D2")
g.add_edge(7, "C3PO", "Leia")
g.add_edge(7, "C3PO", "Chewbacca")
g.add_edge(5, "C3PO", "Han Solo")
g.add_edge(3, "C3PO", "Rey")
g.add_edge(3, "C3PO", "BB8")
g.add_edge(6, "Leia", "Chewbacca")
g.add_edge(5, "Leia", "Han Solo")
g.add_edge(7, "Leia", "R2D2")
g.add_edge(3, "Leia", "Rey")
g.add_edge(3, "Leia", "Kylo Ren")
g.add_edge(3, "Rey", "Kylo Ren")
g.add_edge(3, "Rey", "BB8")
g.add_edge(3, "Rey", "Chewbacca")
g.add_edge(3, "Rey", "R2D2")
g.add_edge(3, "Kylo Ren", "Chewbacca")
g.add_edge(3, "Kylo Ren", "BB8")
g.add_edge(3, "Kylo Ren", "R2D2")
g.add_edge(3, "BB8", "Chewbacca")
g.add_edge(3, "BB8", "R2D2")
g.add_edge(5, "Han Solo", "Chewbacca")
g.add_edge(5, "Han Solo", "R2D2")
g.add_edge(2, "Han Solo", "Boba Fett")
g.add_edge(5, "Yoda", "C3PO")
g.add_edge(5, "Yoda", "R2D2")
g.add_edge(3, "Yoda", "Darth Vader")
g.add_edge(2, "Yoda", "Anakin Skywalker")
g.add_edge(2, "Yoda", "ObiWan Kenobi")
g.add_edge(3, "ObiWan Kenobi", "Anakin Skywalker")
g.add_edge(3, "Anakin Skywalker", "Padmé Amidala")
g.add_edge(2, "Yoda", "Dooku")
g.add_edge(1, "QuiGon Jinn", "ObiWan Kenobi")
g.add_edge(2, "Han Solo", "Jabba the Hutt")
g.add_edge(3, "Poe Dameron", "Finn")
g.add_edge(3, "Poe Dameron", "BB8")
g.add_edge(3, "Finn", "BB8")
g.add_edge(3, "Jar Jar Binks", "Padmé Amidala")
g.add_edge(2, "Darth Vader", "Boba Fett")


print()


print("Arbol de expansion minimo desde C-3PO:")
min_tree = g.kruskal('C3PO')

print(min_tree)

peso_total = 0

for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)

print(f'con un peso total: {peso_total}')

print()
print("Arbol de expansion minimo desde Yoda:")
min_tree = g.kruskal('Yoda')

print(min_tree)

peso_total = 0

for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)

print(f'con un peso total: {peso_total}')

print()
print("Arbol de expansion minimo desde Leia:")
min_tree = g.kruskal('Leia')

print(min_tree)

peso_total = 0

for edge in min_tree.split(';'):
    origin, destination, weight = edge.split('-')
    peso_total += int(weight)

print(f'con un peso total: {peso_total}')

print()
print("Los 3 arboles de expansion minima tienen el mismo peso total, ya que el grafo es no dirigido, por lo que el arbol de expansion minimo es unico.")
print()

max_episodios = 0

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_episodios:
            max_episodios = edge.weight

print(f'el numero maximo de episodios compartidos es: {max_episodios}')
print('pares de personajes que lo comparten:')

pares = []
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == max_episodios:
            if vertex.value < edge.destination:
                pares.append(f'{vertex.value} - {edge.destination}')

for par in pares:
    print(par)

print()
paths = g.dijkstra('C3PO')

destination = 'R2D2'
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

print(f'el camino mas corto desde C-3PO a R2-D2 es: {" - ".join(camino_completo)} con un costo de {peso_total}')


print()
paths = g.dijkstra('Yoda')

destination = 'Darth Vader'
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

print(f'el camino mas corto desde Yoda a Darth Vader es: {" - ".join(camino_completo)} con un costo de {peso_total}')

print()
print('personajes que aparecieron en los 9 episodios:')

en_nueve = []
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == 9:
            if vertex.value not in en_nueve:
                en_nueve.append(vertex.value)

for personaje in en_nueve:
    print(personaje)