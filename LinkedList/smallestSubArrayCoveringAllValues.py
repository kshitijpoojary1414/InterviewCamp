class Node :
    def __init__(self, Key, value, next=None, prev=None ):
        self.key = Key
        self.value = value
        self.next = next
        self.prev = prev

class subArray :
    def __init__(self, capacity=None):
        self.head = None
        self.tail = None
        self.map = {}
        self.key = None
        self.value = None
        self.capacity = capacity

    def mapSize(self):
        return len(self.map.keys())

    def appendToLinkedList(self, node):
        if self.head is None :
            self.head = node
        else :
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def removeFromLinkedList(self, node):
        if node.next is not None :
            node.next.prev = node.prev

        if node.prev is not None :
            node.prev.next = node.next

        if self.head == node :
            self.head = node.next

        if self.tail == node :
            self.tail = node.prev

    def add(self, Key, value):
        node = Node(Key, value)
        self.appendToLinkedList(node)
        self.map[Key] = node

    def remove(self, Key):
        node = self.map.get(Key)
        if node is None :
            return None
        self.removeFromLinkedList(node)
        del self.map[Key]

    def lengthOfSubArray(self):
        head = self.head.value
        tail = self.tail.value

        return tail - head

    def update(self, Key, Value):
        element = self.map.get(Key)

        if element is not None :
            self.remove(Key)

        self.add(Key, Value)
        print(self.map, self.head.value,self.tail.value)


        if self.capacity == self.mapSize() :
            return self.lengthOfSubArray()
        return float('inf')

def returnLowestSubstr(doc, words):
    wordSet = set(words)
    docArray = doc.split(' ')
    minimum = float('inf')
    indices = [None, None]
    word = ""
    start = 0
    cache = subArray(len(words))
    for i in range(len(doc)) :

        if doc[i] != ' ' and i != len(doc)-1:
            word += doc[i]
        else :
            if i == len(doc)-1:
                word += doc[i]
            print(word, word in wordSet)
            if word in wordSet:
                ans = cache.update(word,start)
                if ans < minimum :
                    minimum = ans
                    indices = [start,i-1]
            start = i + 1
            word = ""
    return indices

print(returnLowestSubstr('I am graeat',["I","am"]))

