class ArraysAndStrings2 :
    def maxDiff(self, arr):
        minSoFar = float('inf')
        maxDiff = 0
        for i in arr :
            if minSoFar > i :
                minSoFar = i

            diff = i - minSoFar

            if maxDiff < diff :
                maxDiff = diff
        return maxDiff

    #2 trades allowed

    def maxDiff2Trades(self, arr):
        bestTillI = [None]*len(arr)
        bestFromI = [None]*len(arr)

        minimumSoFar = float('inf')
        maxDiff = 0
        for i in range(len(arr)) :
            minimumSoFar = min(arr[i],minimumSoFar)
            maxDiff = max(maxDiff,arr[i]-minimumSoFar)
            print(arr[i], minimumSoFar,maxDiff)
            bestTillI[i] = maxDiff

        maxSoFar = float('-inf')
        maxDiff = 0
        for i in range(len(arr)-1,-1,-1):
            maxSoFar = max(arr[i],maxSoFar)
            maxDiff = max(maxDiff, maxSoFar-arr[i])
            bestFromI[i] = maxDiff
        maxDiff = 0

        for i in range(len(arr)-1) :
            maxDiff = max(maxDiff,bestTillI[i] + bestFromI[i+1] if i+1 < len(arr) else 0)

        return maxDiff

    def performMove(self, matrix, r1, r2, c1, c2, offset):
        temp = matrix[r1][c1+offset]
        matrix[r1][c1+offset] = matrix[r2-offset][c1]
        matrix[r2-offset][c1] = matrix[r2][c2-offset]
        matrix[r2][c2-offset] = matrix[r1+offset][c2]
        matrix[r1+offset][c2] = temp

        return

    def printLayer(self, matrix, layer, rows, cols):
        print(layer, cols)
        for i in range(layer, cols) :
            print(matrix[layer][i])

        for i in range(layer, rows) :
            print(matrix[i][cols])

        for i in range(cols,layer,-1) :
            print(matrix[rows][i])

        for i in range(rows, layer,-1) :
            print(matrix[i][layer])


    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) <= 0 :
            return None

        rows = len(matrix)-1
        cols = len(matrix[0])-1

        for i in range(len(matrix)//2) :
            self.printLayer(matrix, i, rows, cols)
            rows = rows - 1
            cols = cols - 1


        for i in matrix :
            print(i)

        return matrix



print(ArraysAndStrings2().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))