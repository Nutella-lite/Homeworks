# Реализовать очередь с помощью списка.

class Queue:
    def __init__(self):
        self.queue = []
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def __len__(self):
        return len(self.queue)
    def peak(self):
        return self.queue[0]

queue = Queue()
print(queue.is_empty())
queue.push(1)
queue.push(2)
queue.push(3)
print(len(queue))
print(queue.peak())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.is_empty())