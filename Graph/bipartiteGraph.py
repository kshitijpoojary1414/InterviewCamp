from Graph import *
from Graph2 import *
from collections import deque


class Bipartite:
    def bipartiteGraph(self, G):
        nodes = G.getNodes()

        for node in nodes:
            node.level = -1
            node.setState(State.UNVISITED)
        oddList, evenList = [], []
        for node in nodes:
            if node.getState() == State.UNVISITED:
                res = self.bfsBipartite(G, node)
                print(res)
                if res is None:
                    return False
                oddList += res[0]
                evenList += res[1]
        return [oddList, evenList]

    def bfsBipartite(self, G, node):
        queue = deque()
        queue.append(node)
        node.setState(State.VISITING)
        node.level = 0
        oddList, evenList = [], []

        while len(queue) > 0:
            node = queue.popleft()

            neighbours = node.getNeighbours()

            if node.level % 2 == 0:
                evenList.append(node.data)
            else:
                oddList.append(node.data)
            print(node, node.data, node.level)
            for neighbour in neighbours:
                if neighbour.getState() == State.UNVISITED:
                    queue.append(neighbour)
                    neighbour.setState(State.VISITING)
                    neighbour.level = node.level + 1

                elif neighbour.level == node.level:
                    print('False')
                    return None

            node.setState(State.VISITED)
        return [oddList, evenList]

    def createGraph(self):
        G = Graph2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.addNeighbour(node2)
        node1.addNeighbour(node4)
        node2.addNeighbour(node3)
        node3.addNeighbour(node5)


        nodes = [node1, node2, node3, node4, node5]

        for i in nodes:
            G.addNode(i)
        print(self.bipartiteGraph(G))
        return G


print(Bipartite().createGraph())
