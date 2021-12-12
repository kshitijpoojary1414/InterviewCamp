import math
import threading


class Recursion:

    def getAllCharacters(self, number):
        map = {
            2 : ["A","B","C"],
            3 : ["D","E","F"],
            4 : ["G","H", "I"],
            5 : ["J", "K", "L"],
            6 : ["M", "N", "O"],
            7 : ["P","Q", "R", "S"],
            8 : ["T", "U", "V"],
            9 : ["W", "X", "Y", 'Z']
        }

        if number in map :
            return map[number]

        return []
    # Question
    '''(Level: Medium) Print all combinations of length n.'''

    # Approach
    '''
        1. Termination Cases
        2. Find candidates that go into buffer
        3. Place each candidate into buffer
        4. Recurse to next buffer index 
    '''

    def printCombos(self, arr, size):
        buffer = [0] * size
        self.result = []
        self.printCombosHelper(arr, buffer, 0, 0)
        return self.result

    def printCombosHelper(self, arr, buffer, startIndex, bufferIndex):
        if bufferIndex == len(buffer):
            self.result.append(buffer[::])
            return
        if startIndex == len(arr):
            return

        for i in range(startIndex, len(arr)):
            print(i, bufferIndex, arr[i])
            buffer[bufferIndex] = arr[i]
            self.printCombosHelper(arr, buffer, i + 1, bufferIndex + 1)

    def phoneNumberMnemonic(self, number):
        buffer = [None]*len(str(number))
        self.result = []
        arr = [int(i) for i in str(number)]
        self.findMnemonic(arr, buffer, 0, 0)
        return self.result

    def findMnemonic(self, arr, buffer, startIndex, bufferIndex):
        if bufferIndex == len(buffer) or startIndex == len(arr):
            self.result.append(''.join(buffer[:bufferIndex]))
            return

        charArray = self.getAllCharacters(arr[startIndex])

        if len(charArray) == 0  :
            self.findMnemonic(arr, buffer, startIndex + 1, bufferIndex)

        for i in charArray :
            buffer[bufferIndex] = i
            self.findMnemonic(arr, buffer, startIndex+1, bufferIndex + 1)

    def printSubsets(self, arr):
        self.result = []

        buffer = [0]*len(arr)
        self.printSubsetsHelper(arr, buffer, 0, 0)
        return self.result

    def printSubsetsHelper(self, arr, buffer, startIndex, bufferIndex):
        self.result.append(buffer[:bufferIndex])

        if bufferIndex == len(buffer) or startIndex == len(arr) :
            return

        for i in range(startIndex, len(arr)) :
            buffer[bufferIndex] = arr[i]
            self.printSubsetsHelper(arr, buffer, i + 1, bufferIndex + 1)

    def printPermutations(self, arr, size):
        self.result = []
        buffer = [0]*size
        isInBuffer = [False] * len(arr)
        self.findPermutations(arr, buffer, 0, isInBuffer)
        return self.result

    def findPermutations(self, arr, buffer, bufferIndex, isInBuffer):
        if bufferIndex == len(buffer) :
            self.result.append(buffer[::])
            return

        for i in range(0, len(arr)) :
            if not isInBuffer[i] :
                buffer[bufferIndex] = arr[i]
                isInBuffer[i] = True
                self.findPermutations(arr, buffer, bufferIndex + 1, isInBuffer)
                isInBuffer[i] = False

    def coinCombinations(self, arr, target):
        self.result = []
        buffer = []
        self.findAllCombinations(arr, buffer, 0, target, 0)
        return self.result

    def findAllCombinations(self, arr, buffer, startIndex, target, currentSum):
        if currentSum > target:
            return

        if currentSum == target :
            self.result.append(buffer[::])
            return

        for i in range(startIndex, len(arr)) :
            buffer.append(arr[i])
            currentSum += arr[i]
            self.findAllCombinations(arr, buffer, i, target, currentSum)
            buffer.pop()
            currentSum -= arr[i]


print(Recursion().coinCombinations([1,2,5],5))
