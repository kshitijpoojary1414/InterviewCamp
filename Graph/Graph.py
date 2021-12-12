import enum


class Graph :
    def __init__(self):
        self.nodes =[]

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes


class State(enum.Enum) :
    VISITING= 1
    VISITED = 2
    UNVISITED = 3


class Node :
    def __init__(self, data):
        self.data = data
        self.neighbours = []
        self.state = State.UNVISITED
        self.neighbours = []

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def addNeighbour(self, node):
        self.neighbours.append(node)

    def getNeighbours(self):
        return self.neighbours

    