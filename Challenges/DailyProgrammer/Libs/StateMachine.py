from collections import namedtuple

class StateMachine():

    Vertex = namedtuple('Vertex', 'value outEdges' )
    Edge = namedtuple('Edge', 'nextState condition')

    def __init__(self, maxStates):
        self.vertices = [0] * maxStates
        self.currentState = 0

    def addEdge(self, inVertex, outVertex, condition):
        newEdge = StateMachine.Edge(nextState=outVertex, condition=condition)
        self.vertices[inVertex].outEdges.append(newEdge)

    def addVertex(self, value):
        node = StateMachine.Vertex(value=value, outEdges=[])
        self.vertices[value] = node

    def advance(self, condition):
        for edge in self.vertices[self.currentState].outEdges:
            if condition == edge.condition:
                self.currentState = edge.nextState
                return

        self.currentState = -1
