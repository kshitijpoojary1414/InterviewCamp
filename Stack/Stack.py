class Stack :
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if(len(self.stack) == 0) :
            raise Exception("Empty")
        return self.stack.pop()

    def isEmpty(self):
        if(len(self.stack) == 0) :
            return True
        return False

    def peek(self):
        if (self.isEmpty()) :
            raise Exception('Empty')
        return self.stack[-1]

    def printStack(self):
        print(self.stack)
