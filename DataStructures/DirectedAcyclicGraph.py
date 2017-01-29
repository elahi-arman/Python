from collections import namedtuple

class DAG():

    Edge = namedtuple('Edge', 'nextVertex weight')

    def __init__(self):
        self.vertices = {}

    def add_edge(self, inVertex, outVertex, weight = 0):
        newEdge = Graph.Edge(nextVertex = outVertex , weight = weight)
        if inVertex not in self.vertices:
            self.addVertex(inVertex)

        if outVertex not in self.vertices:
            self.addVertex(outVertex)

        self.vertices[inVertex].append(newEdge)

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []

    # should go into directed_acyclic_graph class
    def calculate_betweeness(self, node):
        if node in leaves:
            return leaves[node]
        else:
            weight = 0
            for child in self.vertices[node]:
                weight += self.calculate_betweeness(child.nextVertex, leaves)
            return weight + 1
