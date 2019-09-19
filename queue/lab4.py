class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty!!!"

    def change_last_first(self):
        self.queue[0], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1], self.queue[0]

    def peek(self):
        if self.queue:
            return self.queue[0]
        return "Queue is empty!!!"

    def reverse(self):
        self.queue.reverse()

    def clear(self):
        self.queue = []

    def check(self, element):
        return (element in self.queue)
    