from collections import namedtuple
from DirectedAcyclicGraph import DAG as DAG

class Graph():

    class Edge():
        """Edge class represented by the vertices and weights. Easily printable and comparable."""
        def __init__(self, startVertex, nextVertex, weight=0):
            self.startVertex = startVertex
            self.nextVertex = nextVertex
            self.weight = weight

        def __str__(self):
            return '{}->{}({})'.format(self.startVertex, self.nextVertex, self.weight)

        def __eq__(self, other):
            return ((self.startVertex == other.startVertex and self.nextVertex == other.nextVertex)
                    or (self.startVertex == other.nextVertex and self.nextVertex == other.startVertex))

    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = ''
        for vertex, edges in self.vertices.items():
            string += '{}\t{}\n'.format(vertex, ['{}'.format(edge) for edge in edges])
        return string

    def add_edge(self, v1, v2, weight = 0):
        """Add edge and vertices (if they don't exist) into the graph."""
        v1_to_v2 = Graph.Edge(startVertex = v1, nextVertex = v2, weight = weight)
        v2_to_v1 = Graph.Edge(startVertex = v2, nextVertex = v1, weight = weight)

        if v1 not in self.vertices:
            self.add_vertex(v1)

        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].append(v1_to_v2)
        self.vertices[v2].append(v2_to_v1)

    def add_vertex(self, value):
        """Add a vertex into the graph if it doesn't already exist."""
        if value not in self.vertices:
            self.vertices[value] = []

    def delete_edge(self, startVertex, nextVertex):
        temp_edge = Graph.Edge(startVertex, nextVertex, 0)
        if startVertex in self.vertices:
            for edge in self.vertices[startVertex]:
                if edge == temp_edge:
                    del edge

        if nextVertex in self.vertices:
            for edge in self.vertices[nextVertex]:
                if edge == temp_edge:
                    del edge

    def flatten_edges(self):
        with_duplicates =  [edge for vertex in self.vertices for edge in self.vertices[vertex]]
        no_duplicates = []
        for edge in with_duplicates:
            exists = False
            for edg in no_duplicates:
                if edge == edg:
                    exists = True

            if not exists:
                no_duplicates.append(edge)

        return no_duplicates

    def BFS(self, start):
        """
        Creates a BFS DAG and returns list of triples (in, out, weight)

        Positional Arguments:
            start - key in vertex

        Return:
            [] if start does not exist

        """

        leaves, dirtyNodes = ({}, {})
        upEdges, queue = ([], [])
        dag = DAG()

        try:
            queue.append(start)
            dirtyNodes[start] = 1
        except KeyError:
            return []

        for node in queue:
            dag.add_vertex(node)
            weight = dirtyNodes[node] + 1
            notDirtyNeighbors = []

            for edge in self.vertices[node]:
                if edge.nextVertex not in dirtyNodes:
                    notDirtyNeighbors.append(edge.nextVertex)
                elif dirtyNodes[edge.nextVertex] == weight:
                    dag.add_edge(node, edge.nextVertex)
                    upEdges.append((edge.nextVertex, node))

            queue.extend(notDirtyNeighbors)

            for neighbor in notDirtyNeighbors:
                dirtyNodes[neighbor] = weight
                dag.add_edge(node, neighbor)
                upEdges.append((neighbor, node))

        return dag

    def determine_clusters(edges):
        """Does a BFS through all vertices in graph to determine all possible paths."""
        clusters = []     # keep one extra list to have lazy indexing
        dirty_vertices = {}
        for edge in edges:
            start = edge.startVertex
            end = edge.nextVertex
            if start in dirty_vertices and end in dirty_vertices:
                # they both already belong to same cluster
                if dirty_vertices[start] == dirty_vertices[end]:
                    continue
                # need to merge clusters
                else:
                    start_cluster = dirty_vertices[start]
                    end_cluster = dirty_vertices[end]
                    for vertex, cluster in dirty_vertices.items():
                        if cluster == end_cluster:
                            dirty_vertices[vertex] = start_cluster
                    clusters[start_cluster].extend(clusters[end_cluster])
                    clusters.pop(end_cluster)
                    continue
            # add one new vertex into cluster
            if start in dirty_vertices and end not in dirty_vertices:
                dirty_vertices[end] = dirty_vertices[start]
                clusters[dirty_vertices[start]].append(end)
            elif end in dirty_vertices and start not in dirty_vertices:
                dirty_vertices[start] = dirty_vertices[end]
                clusters[dirty_vertices[end]].append(start)
            #add new cluster
            else:
                clusters.append([start, end])
                dirty_vertices[start] = len(clusters) - 1
                dirty_vertices[end] = len(clusters) - 1

        return clusters
