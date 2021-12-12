import enum
import math
import threading


class State(enum.Enum):
    VISITING = 1
    NO_PATH = 2
    UNVISITED = 3


class BackTracking:
    def pathExists(self, arr):
        if arr == None or len(arr) == 0:
            return False

        memo = [[State.UNVISITED for i in range(len(arr[0]))] for j in range(len(arr))]

        return self.pathExistsHelper(arr, 0, 0, memo)

    def pathExistsHelper(self, arr, i, j, memo):
        if self.oob(arr, i, j) or arr[i][j] == 1:
            return False

        if i == len(arr) - 1 and j == len(arr[0]) - 1:
            return True

        if memo[i][j] != State.UNVISITED:
            return False

        memo[i][j] = State.VISITING

        paths = [(+1, 0), (0, +1), (0, -1), (-1, 0)]

        for k in paths:
            if self.pathExistsHelper(arr, i + k[0], j + k[1], memo):
                return True

        memo[i][j] = State.NO_PATH
        return False

    def oob(self, arr, i, j):
        if i >= len(arr) or j >= len(arr[0]) or i < 0 or j < 0:
            return True

    def wordBreak(self, arr, dict):
        if arr is None or len(arr) == 0:
            return None

        memo = [[State.UNVISITED for i in range(len(arr[0]))] for j in range(len(arr))]

        result = []

        if self.wordBreakHelper(arr, dict, 0, result, memo):
            return result

        return False

    def wordBreakHelper(self, arr, dict, startIndex, result, memo):
        if startIndex == len(arr):
            return True

        if memo == State.NO_PATH:
            return False

        for i in range(startIndex, len(arr)):
            ans = arr[startIndex: i + 1]
            if ans in dict:
                result.append(ans)
                if self.wordBreakHelper(arr, dict, i + 1, result, memo):
                    return True
                else:
                    result.pop()
                    memo[i + 1] = State.NO_PATH

        return False

    def sodokuSolver(self, arr):
        if arr is None or len(arr) == 0 :
            return None

        checker = BoardChecker(arr)

        return self.sodokuSolverHelper(arr, 0, 0, checker)

    def nextPair(self, i, j):
        if j == 8 :
            return (i + 1, 0)
        else :
            return (i, j+1)

    def sodokuSolverHelper(self, arr, i, j, checker):
        if i == len(arr) and j == len(arr) :
            return True

        pair = self.nextPair(i,j)
        if arr[i][j] != 0 :
            return self.sodokuSolver(self, arr, pair[0], pair[1], checker)

        for i in range(0,9) :
            if checker.canPlace(arr, i, j) :
                arr[i][j] = i
                checker.place(arr, i, j)

                if(self.sodokuSolver(arr, pair[0], pair[1], checker)) :
                    return True

                arr[i][j] = 0
                checker.remove(arr, i, j)

        return False







class BoardChecker :
    def __init__(self, board):
        self.rows = [[0 for i in len(board[0])] for j in len(board)]
        self.cols = [[0 for i in len(board[0])] for j in len(board)]
        self.squares = [[0 for i in len(board[0])] for j in len(board)]

        for i in range(len(board)) :
            for j in range(len(i)) :
                self.rows[i][board[i][j]-1] = True
                self.rows[j][board[i][j]-1] = True
                boxNumber = self.boxNumber(i, j)
                self.squares[boxNumber][board[i][j]-1] = True

    def boxNumber(self, i, j):
        return (i//3)*3 + j//3

    def canPlace(self, board, i, j):
        elem = board[i][j]
        if not self.rows[i][elem] and not self.cols[j][elem] and not self.squares[self.boxNumber(i, j), elem] :
            return True

    def place(self, board, i, j):
        elem = board[i][j]
        self.rows[i][elem] = True
        self.cols[j][elem] = True
        self.squares[self.boxNumber(i, j)][elem] = True

    def remove(self, board, i, j):
        elem = board[i][j]
        self.rows[i][elem] = False
        self.cols[j][elem] = False
        self.squares[self.boxNumber(i, j)][elem] = False



print(BackTracking().sodokuSolver([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
]))
