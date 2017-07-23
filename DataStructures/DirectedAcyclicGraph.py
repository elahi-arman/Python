from collections import namedtuple

class DAG():

    Edge = namedtuple('Edge', 'nextVertex weight')

    def __init__(self):
        self.vertices = {}
        self.leaves = {}
        self.weights = {}

    def add_edge(self, inVertex, outVertex, weight = 0):
        newEdge = DAG.Edge(nextVertex = outVertex , weight = weight)
        if inVertex not in self.vertices:
            self.add_vertex(inVertex)
        elif inVertex in self.leaves:
            del self.leaves[inVertex]

        if outVertex not in self.vertices:
            self.add_vertex(outVertex)
        elif outVertex in self.leaves:
            self.leaves[outVertex] /= 2

        self.vertices[inVertex].append(newEdge)

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []
            self.leaves[value] = 1

    def calculate_betweeness(self, node):
        if node in self.leaves:
            self.weights[node] = self.leaves[node]
            return self.leaves[node]
        else:
            weight = 1
            for child in self.vertices[node]:
                weight += self.calculate_betweeness(child.nextVertex)
            self.weights[node] = weight
            return weight
