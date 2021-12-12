from Graph import State
class DFS :
    def dfs(self, G, target):
        nodes = G.getNodes()
        for node in nodes :
            if node.getState() == State.UNVISITED :
                result = self.dfsVisit(G, node, target)
                if result :
                    return True

        return False

    def dfsVisit(self, G, node, target):
        if node.data == target :
            return True

        node.setState = State.VISITING

        neighbours = node.getNeighbours()

        for neighbour in neighbours :
            if neighbour.getState() == State.UNVISITED :
                if self.dfsVisit(G, neighbour, target) :
                    return True

        node.setState = State.VISITED
        return False




