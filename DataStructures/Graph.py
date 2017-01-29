import sys
from collections import namedtuple

class Graph():

    Edge = namedtuple('Edge', 'nextVertex weight')

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
            murr

        Raises:
            KeyError - starting node could not be found
        """

        leaves, dirtyNodes = ({}, {})
        upEdges, queue = ([], [])
        dag = Graph()

        try:
            queue.append(start)
            dirtyNodes[start] = 1
        except KeyError:
            print ('Could not find starting node: {}'.format(start), file=sys.stderr)
            return []

        for node in queue:
            dag.addVertex(node)
            weight = dirtyNodes[node] + 1
            notDirtyNeighbors = []

            for edge in self.vertices[node]:
                if edge.nextVertex not in dirtyNodes:
                    print ('Processing {} with weight {}'.format(node, weight))
                    notDirtyNeighbors.append(edge.nextVertex)
                elif dirtyNodes[edge.nextVertex] == weight:
                    dag.addDirectedEdge(node, edge.nextVertex)
                    upEdges.append((edge.nextVertex, node))

            queue.extend(notDirtyNeighbors)

            for neighbor in notDirtyNeighbors:
                dirtyNodes[neighbor] = weight
                dag.addDirectedEdge(node, neighbor)
                upEdges.append((neighbor, node))

        for vertex in self.vertices:
            num_occurrences = len([v for v in upEdges if v[0] == vertex])
            if len(dag.vertices[vertex]) == 0:
                leaves[vertex] =  1/num_occurrences

        return (dag, leaves)

    # should go into directed_acyclic_graph class
    def calculate_betweeness(self, node, leaves):
        if node in leaves:
            return leaves[node]
        else:
            weight = 0
            for child in self.vertices[node]:
                weight += self.calculate_betweeness(child.nextVertex, leaves)
            return weight + 1
