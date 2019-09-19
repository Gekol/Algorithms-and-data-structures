class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return ("Stack is empty!!!")

    def peek(self):
        if self.stack:
            return self.stack[len(self.stack) - 1]
        return "Stack is empty!!!"

    def change_last_first(self):
        self.stack[0], self.stack[len(self.stack) - 1] = self.stack[len(self.stack) - 1], self.stack[0]

    def reverse(self):
        self.stack.reverse()

    def clear(self):
        self.stack = []

    def check(self, elem):
        return (elem in self.stack)


