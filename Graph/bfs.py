from collections import deque
from Graph import *
class BFS :
    def bfs(self, G, target) :
        nodes = G.getNodes()
        for node in nodes :
            if node.getState() == State.UNVISITED :
                if self.bfsVisit(node, target) :
                    return True
        return False

    def bfsVisit(self, start, target):
        queue = deque()
        queue.append(start)
        start.setState(State.VISITING)
        while len(queue)>0 :
            node = queue.popleft()
            neighbours = node.neighbours

            if node.data == target:
                return True

            for neighbour in neighbours :
                if neighbour.getState == State.UNVISITED :
                    neighbour.setState(State.VISITING)
                    queue.append(neighbour)

            node.setState(State.VISITED)
        return False
