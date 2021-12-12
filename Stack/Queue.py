#Enqueue O(1)
class Queue :
    def __init__(self):
        self.StackA = []
        self.StackB = []

    def enqueue(self, value):
        self.StackB.append(value)

    def flush(self):
        while len(self.StackB) != 0 :
            self.StackA.append(self.StackB.pop())

    def dequeue(self):
        if len(self.StackA) == 0 :
            self.flush()
        if len(self.StackA) == 0 :
            raise Exception('Queue is empty')
        return self.StackA.pop()
