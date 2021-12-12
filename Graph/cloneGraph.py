from Graph import *
class cloneGraph :
    def cloneGraph(self, root):
        rootCopy = Node(root.data)
        map = {
            root : rootCopy
        }
        self.dfsVisit(root, map)

        return rootCopy

    def dfsVisit(self, root, map):
        root.setState(State.VISITING)
        neighbours = root.getNeighbours()

        for neighbour in neighbours :
            if map.get(neighbour) is None :
                map[neighbour] = Node(neighbour.data)

            rootCopy = map[root]
            neighbourCopy = map[neighbour]
            rootCopy.addNeighbour(neighbourCopy)

            if neighbour.getState == State.UNVISITED :
                self.dfsVisit(self, neighbour, map)

        root.setState(State.VISITED)