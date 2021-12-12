from collections import deque
from Graph import *
class LevelOrderTraversal :
    def queueApproach(self, root):
        currentQueue = deque()
        currentQueue.append(root)
        nextQueue = deque()
        root.setState(State.VISITED)
        level = []
        while len(currentQueue) > 0:
            node = currentQueue.popleft()
            neighbours = node.getNeighbours()

            level.append(node.data)

            for neighbour in neighbours :
                if neighbour.getState() == State.UNVISITED :
                    neighbour.setState(State.VISITING)
                    nextQueue.append(neighbour)
            node.setState(State.VISITED)

            if len(currentQueue) == 0 :
                currentQueue = nextQueue
                nextQueue = deque()
                print(level)

    def markerApproach(self, root):
        currentQueue = deque()
        currentQueue.append(root)
        root.setState(State.VISITED)
        marker = Node(None)
        currentQueue.append(marker)
        level = []
        while len(currentQueue) > 0:
            node = currentQueue.popleft()

            if node == marker :
                if len(currentQueue) > 0 :
                    currentQueue.append(marker)
                print(level)
                level = []
                continue

            level.append(node.data)

            neighbours = node.getNeighbours()

            for neighbour in neighbours :
                if neighbour.getState() == State.UNVISITED :
                    neighbour.setState(State.VISITING)
                    currentQueue.append(neighbour)

            node.setState(State.VISITED)


