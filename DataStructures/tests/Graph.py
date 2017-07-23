import context
from Graph import Graph

g = Graph()
g.add_edge('a', 'b', 0)
g.add_edge('d', 'e', 0)
g.add_edge('c', 'a', 0)
g.add_edge('b', 'c', 0)
g.add_edge('d', 'g', 0)
g.add_edge('f', 'd', 0)
g.add_edge('e', 'f', 0)
g.add_edge('b', 'd', 0)
g.add_edge('f', 'g', 0)
dag, leaves= g.BFS('a')
print(dag.calculate_betweeness('a'))
print (dag.weights)



h = Graph()
h.add_edge('a', 'b', 0)
h.add_edge('a', 'c', 0)
h.add_edge('b', 'd', 0)
h.add_edge('c', 'd', 0)

dag, leaves= h.BFS('a')
dag.calculate_betweeness('a')
print (dag.weights)
