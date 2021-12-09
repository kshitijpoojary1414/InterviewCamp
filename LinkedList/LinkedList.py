class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


    def append(self, node):
       if self.head is None :
           self.head = node
       else :
           self.tail.next = node
       self.tail = node


    def printLinkedList(self):
        current = self.head
        while (current is not None):
            print(current.data)
            current = current.next

    def getNthNode(self, n):
        if self.head is None :
            raise Exception("No Element at this index ")

        current = self.head
        for i in range(n):
            current = current.next
            if current is None:
                raise Exception("No Element at this index ")
        return current

    def generateListFromArray(self, arr):
        startIndex = 0
        if self.head is None :
            self.head = Node(arr[0])
            startIndex = 1

        current = self.head
        for i in range(startIndex, len(arr)) :
            current.next = Node(arr[i])
            current = current.next
        self.tail = current

