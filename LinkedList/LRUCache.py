
class Node :
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRU :
    def __init__(self, capacity):
        self.map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def addToLinkedList(self, node):
        if self.head is None :
            self.head = node
        else :
            node.prev = self.tail
            self.tail.next = node
        self.tail = node

    def removeFromLinkedList(self, node):
        if node.next is not None :
            node.next.prev = node.prev

        if node.prev is not None :
            node.prev.next = node.next

        if node == self.head :
            self.head = node.next

        if node == self.tail :
            self.tail = node.tail


    def mapSize(self):
        return len((self.map.keys()))

    def remove(self, Key):
        element = self.map.get(Key)
        if element is None :
            return None

        self.removeFromLinkedList(element)
        self.map.pop(Key)

    def add(self, key, value):
        node = Node(key, value)
        self.addToLinkedList(node)
        self.map[key] = node

    def read(self, Key):
        element = self.map.get(Key)
        if element is None :
            return None

        self.remove(Key)
        self.add(element.key, element.value)

        current = self.head
        while current is not None :
            print(Key,"Cc",current.value,self.head.value)
            current = current.next

        return element.value

    def write(self, Key, Value):
        if self.mapSize() == self.capacity :
            self.remove(self.head.key)

        self.add(Key, Value)




cache = LRU(3)


cache.write(1, "Kshitij")
cache.write(2, "Varun")
cache.write(3, "Vaibhav")
cache.write(4, "Prashant")
print(cache.read(2))