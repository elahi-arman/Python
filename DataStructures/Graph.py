import sys
from collections import namedtuple

class Graph():

    Edge = namedtuple('Edge', 'nextVertex weight')
    DirtyVertex = namedTuple('DirtyVertex', 'vertex weight')

    def __init__(self):
        self.vertices = {}

    def addEdge(self, v1, v2, weight = 0):
        v1_to_v2 = Graph.Edge(nextVertex = v2, weight = weight)
        v2_to_v1 = Graph.Edge(nextVertex = v1, weight = weight)

        if v1 not in self.vertices:
            self.addVertex(v1)

        if v2 not in self.vertices:
            self.addVertex(v2)

        self.vertices[v1].append(v1_to_v2)
        self.vertices[v2].append(v2_to_v1)

    def addDirectedEdge(self, inVertex, outVertex, weight = 0):
        newEdge = Graph.Edge(nextVertex = outVertex , weight = weight)
        if inVertex not in self.vertices:
            self.addVertex(inVertex)

        if outVertex not in self.vertices:
            self.addVertex(outVertex)

        self.vertices[inVertex].append(newEdge)

    def addVertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []

    def BFS(self, start):
        """
        Creates a BFS DAG and returns list of triples (in, out, weight)

        Positional Arguments:
            start - key in vertex

        Return:
            weights - list of triples (in, out, weight)

        Raises:
            KeyError - starting node could not be found
        """

        dirtyNodes = []
        queue = []
        dag = Graph()

        try:
            queue.append(start)
        except KeyError:
            print ('Could not find starting node: {}'.format(start), file=sys.stderr)
            return []

        for node in queue:
            # enqueue the neighbors
            print ('Processing {}'.format(node))
            dag.addVertex(node)
            dirtyNodes.append(node)
            notDirtyNeighbors = [edge.nextVertex for edge in self.vertices[node] if edge.nextVertex not in dirtyNodes]

            queue.extend(notDirtyNeighbors)

            for neighbor in notDirtyNeighbors:
                dag.addDirectedEdge(node, neighbor)

        print (dag)
