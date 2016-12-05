from collections import namedtuple

class Graph():

    Edge = namedtuple('Edge', 'nextVertex weight')

    def __init__(self):
        self.vertices = {}

    def addEdge(self, v1, v2, weight):
        v1_to_v2 = Graph.Edge(nextVertex = v2, weight = weight)
        v2_to_v1 = Graph.Edge(nextVertex = v1, weight = weight)

        if v1 not in self.vertices:
            self.addVertex(v1)

        if v2 not in self.vertices:
            self.addVertex(v2)

        self.vertices[v1].append(v1_to_v2)
        self.vertices[v2].append(v2_to_v1)

    def addVertex(self, value):
        self.vertices[value] = []
