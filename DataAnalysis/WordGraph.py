from collections import defaultdict

class WordGraph:

    '''

    Based on the paper by Francois Rousseau and Michalis Vazirgiannis, the WordGraph analyzes the number of contexts a word comes from, thus creating a accurate represetnation of the importance of a word

    The chosen representation is an adjacency list because working with words, by Zipf's Law, the heavy tailed distribution of words in a document will create a sparse matrix, therefore wasting a lot of space.

    The underlying graph data structure is adapted from: http://stackoverflow.com/a/30747003
    '''

    def __init__(self, connections=None):
        self._graph = defaultdict(set)

        if connections is not None:
            self.add_edges(connections)

    def add_edges(self, edges):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in edges:
            self._graph[node1].add(node2)
            self._graph[node2].add(node1)


    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
