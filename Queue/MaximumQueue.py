from collections import  deque
class MaxQueue :
    def __init__(self):
        self.queue = deque()
        self.mQueue = deque()

    def enqueue(self, value):
        while len(self.mQueue) > 0 and self.mQueue[0] < value :
            self.mQueue.popleft()
        self.mQueue.appendleft(value)
        self.queue.appendleft(value)

    def dequeue(self):
        element = self.queue.pop()
        if len(self.mQueue) and self.mQueue[-1] == element :
            self.mQueue.pop()
        return element

    def max(self):
        print(self.mQueue, self.queue)
        if(len(self.mQueue) == 0) :
            raise Exception('Queue is empty')
        return self.mQueue[-1]


def maxWindow(arr, window) :
    if arr is None or len(arr) == 0 :
        return False

    queue = MaxQueue()
    length = 0
    result =[]
    for i in arr :
        print(i,length)
        if length == window :
            queue.dequeue()
            length -= 1

        queue.enqueue(i)
        length += 1

        if length == window :
            result.append(queue.max())

    return result

class Solution:
    def numIslands(self, grid) :
        if grid is None or len(grid) == 0 :
            return False

        count = 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == '1' :
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def oob(self, grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j<0 :
            return True
        return False

    def dfs(self, grid, i, j):
        if self.oob(grid,i,j) :
            return
        if grid[i][j] == '0' :
            return
        grid[i][j] = '0'
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for k in directions :
            print(k,i,j)
            self.dfs(grid, k[0]+i, k[1] + j)
        return



print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))


