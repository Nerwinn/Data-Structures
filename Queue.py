"""Queue - a FIFO (First In-First Out) data structure. 
Deque - is a double-ended queue, but we can use it for queue.
use append() to enqueue an item, and popleft() to dequeue an item."""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if (len(self.queue)<1):
            return None
        return self.queue.pop()

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.dequeue()
print(q.display())
