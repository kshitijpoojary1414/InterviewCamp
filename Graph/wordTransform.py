from collections import deque
class WordTransform :
    dictionary = set(['COB','COG','DOG'])

    def createPatternWordMap(self,):
        map = {}
        for word in self.dictionary :
            for index in range(len(word)) :
                pattern = word[0:index] + '*' + word[index+1:]
                if map.get(pattern) is None :
                    map[pattern] = [word]
                else :
                    map[pattern].append(word)
        return map
    
    def wordTransform(self, start, end):
        patternWordMap = self.createPatternWordMap()
        result = []
        queue = deque()
        queue.append(start)
        visitedWords = {start : 0}

        while len(queue) > 0 :
            word = queue.popleft()

            if word == end :
                return visitedWords.get(word)+1

            neighbours = self.getNeighbours(word, patternWordMap)

            for neighbour in neighbours :
                if neighbour not in visitedWords :
                    visitedWords[neighbour] = visitedWords[word] + 1
                    queue.append(neighbour)

        print(result,visitedWords,patternWordMap)
        return False

    def getNeighbours(self, word, map):
        neighbours = []
        for index in range(len(word)) :
            pattern = word[0:index] + '*' + word[index + 1:]

            values = map.get(pattern)
            if values is not None :
                neighbours = neighbours + values

        return neighbours

print(WordTransform().wordTransform('CAB','DOG'))