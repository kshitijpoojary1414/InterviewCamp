from Graph import *
from Graph2 import *
class TopologicalSort :

    def topoSort(self, G):
        nodes =  G.getNodes()
        self.stack = []
        for node in nodes :
            if node.getState() == State.UNVISITED:
                self.dfsVisit(G, node)
        return self.stack

    def dfsVisit(self, G, node) :
        node.setState(State.VISITING)
        neighbours = node.getNeighbours()

        for neighbour in neighbours :
            if neighbour.getState() == State.UNVISITED :
                self.dfsVisit(G, neighbour)

        node.setState(State.VISITED)
        self.stack.append(node)
        return

    def createGraph(self):
        G = Graph2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.addNeighbour(node2)
        node1.addNeighbour(node4)
        node2.addNeighbour(node4)
        node2.addNeighbour(node3)
        node2.addNeighbour(node5)
        node3.addNeighbour(node5)

        nodes = [node1,node2,node3,node4,node5]

        for i in nodes :
            G.addNode(i)
        print("dIAMERE",self.detectingCycle(G))
        return G

    def diameterOfAGraph(self, G) :
        stack = self.topoSort(G)
        maximum = 0

        while len(stack) > 0  :
            node = stack.pop()
            neighbours = node.getNeighbours()
            maximum = max(maximum, node.longestPath)
            for neighbour in neighbours :

                if neighbour.longestPath < node.longestPath + 1 :
                    neighbour.longestPath = node.longestPath + 1

        return maximum

    def detectingCycle(self, G):
        nodes = G.getNodes()
        for node in nodes:
            if node.getState() == State.UNVISITED :
                if self.dfsDetectCycle(G, node) :
                    return True

        return False

    def dfsDetectCycle(self, G, start):
        start.setState(State.VISITING)
        neighbours = start.getNeighbours()

        for neighbour in neighbours :
            neighbourState = neighbour.getState()

            if neighbourState == State.UNVISITED :
                if self.dfsDetectCycle(G, neighbour) :
                    return True
            elif neighbourState == State.VISITING :
                return True

        start.setState(State.VISITED)
        return False







TopologicalSort().createGraph()

