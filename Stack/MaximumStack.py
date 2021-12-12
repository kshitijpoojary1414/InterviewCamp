class Stack :
    def __init__(self):
        stack = []

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
        if (self.isEmpty(self.stack)) :
            raise Exception('Empty')
        return self.stack[-1]

class MaximumStack:
    def __init__(self):
        self.stack = Stack()
        self.maxStack = Stack()

    def push(self, value):
        self.maxStack.push(value)

        if self.maxStack.isEmpty() or self.maxStack.peek() <= value :
            self.maxStack.push(value)

        return True

    def pop(self):
        if self.stack.isEmpty() :
            raise Exception("Empty")
        value = self.stack.pop()
        if self.maxStack.peek() == value :
            self.maxStack.pop()
        return value

    def max(self):
        if self.maxStack.isEmpty() :
            raise Exception('Empty')

        return self.maxStack.peek()




