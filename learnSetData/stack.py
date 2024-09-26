# Реализовать стек с помощью списка.

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def __len__(self):
        return len(self.stack)
    def peak(self):
        return self.stack[-1]

stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(len(stack))
print(stack.peak())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())