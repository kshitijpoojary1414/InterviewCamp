class Solution :
    def printCombos(self, arr, k):
        buffer = [0] * k
        self.result = []
        self.printCombosHelper(arr, buffer, 0, 0, 1)
        return self.result


    def printCombosHelper(self, arr, buffer, startIndex, bufferIndex, k):
        if bufferIndex == len(buffer) or k <= 0:
            return
        if startIndex == len(arr):
            return
        self.result.append(buffer[:bufferIndex])

        for i in range(startIndex, len(arr)):
            print(i, bufferIndex, arr[i])
            buffer[bufferIndex] = arr[i]

            if arr[i] %2 != 0 :
              k -= 1
            self.printCombosHelper(arr, buffer, i + 1, bufferIndex + 1, k)

print(Solution().printCombos([1,2,3,4],4))
