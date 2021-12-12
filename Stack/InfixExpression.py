from Stack import Stack
class Expression :
    def __init__(self):
       self.operator = Stack()
       self.operand = Stack()
       self.postfix = Stack()

    def isOperand(self, character):
        if '0' <= (character) <= '9':
            return True
        return False

    def isOperator(self, character):
        if character in set(['+','-','/','*']) :
            return True
        return False

    def precedence(self, operator):
        if operator == '+' :
            return 2
        elif operator =='-' :
            return 2
        elif operator == '/':
            return 3
        elif operator == '*':
            return 3
        else :
            return 0

    def process(self):
        self.operand.printStack()
        operand1 = int(self.operand.pop())
        operand2 = int(self.operand.pop())

        operator = self.operator.pop()

        result = 0
        if operator == '+' :
            result = operand2 + operand1
        elif operator == '-':
            result = operand2 - operand1
        elif operator == '/':
            result = operand2 / operand1
        elif operator == '*':
            result = operand2 * operand1

        self.operand.push(int(result))
        return

    def infix(self, expression):
        for i in expression :
            if self.isOperand(i) :
                self.operand.push(i)
            elif self.isOperator(i):
                while not self.operator.isEmpty() and self.precedence(self.operator.peek()) >= self.precedence(i) :
                    self.process()
                self.operator.push(i)
            elif i == "(" :
                self.operator.push(i)
            elif i == ")" :
                while not self.operator.isEmpty() and self.operator.peek() != '(' :
                    self.process()
                self.operator.pop()
        while not self.operator.isEmpty() :
            self.process()

        return self.operand.pop()



print(Expression().infix('1+5'))
