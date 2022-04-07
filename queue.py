# First in First out 
class Queue:
    def __init__(self):
        self.queue = []
        

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print("Display the Queue: ", self.queue )

    def size(self):
        return len(self.queue)

q = Queue()
item = [2,5,6,7,8,9]

for i in item:
    q.enqueue(i)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

q.display()
q.dequeue()
q.display()