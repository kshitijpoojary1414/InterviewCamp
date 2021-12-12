class Stack :
    def __init__(self, capacity):
        self.A = [None]*capacity
        self.s1 = -1
        self.s2 = capacity

    def push(self, stackNumber, value):
        if self.s1 == self.s2 :
            raise Exception('Stack is Full')

        if stackNumber not in (1,2) :
            raise Exception('Invalid stack number')

        if stackNumber == 1 :
            self.s1 += 1
            self.A[self.s1] = value
        else :
            self.s2 -= 1
            self.A[self.s2] = value


    def pop(self, stackNumber):
        if self.s1 == 0 or self.s2 == len(self.A)-1 :
            raise Exception('Stack is empty')

        if stackNumber not in (1,2) :
            raise Exception("Invalid Stack")

        if stackNumber == 1 :
            item = self.A[self.s1]
            self.s1 -= 1
        else :
            item = self.A[self.s2]
            self.s2 += 1
        return item


stack = Stack(10)
stack.push(1,2)
stack.push(1,3)
stack.push(1,4)
stack.push(1,5)
stack.push(1,6)
stack.push(2,9)
stack.push(2,10)
stack.push(2,11)
print(stack.pop(1))
print(stack.pop(2))

# stack.push(2,12)
# stack.push(2,13)