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
