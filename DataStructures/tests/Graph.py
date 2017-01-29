import context
from Graph import Graph

g = Graph()
g.addEdge('a', 'b', 0)
g.addEdge('d', 'e', 0)
g.addEdge('c', 'a', 0)
g.addEdge('b', 'c', 0)
g.addEdge('d', 'g', 0)
g.addEdge('f', 'd', 0)
g.addEdge('e', 'f', 0)
g.addEdge('b', 'd', 0)
g.addEdge('f', 'g', 0)
dag, leaves= g.BFS('a')
print(dag.calculate_betweeness('a', leaves))



h = Graph()
h.addEdge('a', 'b', 0)
h.addEdge('a', 'c', 0)
h.addEdge('b', 'd', 0)
h.addEdge('c', 'd', 0)

dag, leaves= h.BFS('a')
print(dag.calculate_betweeness('a', leaves))
