class CircularQueue():

    def __init__(self,size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear= -1

    # add items inside the queue
    def enqueue(self, items):

        if (self.rear +1) % self.size == self.front:
            print("The Circular queue is full \n")
        elif self.front== -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = items
            # print("queue", self.queue[self.rear])
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = items
            # print("queue", self.queue[self.rear])
            
    # pop out the elements from queue
    def dequeue(self):
        if self.front == -1:
            print("The Circular queue is empty \n")
        elif self.front == self.front:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            # print("queue", temp)
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            # print("queue", temp)
            return temp 

    def printCircularQueue(self):
        if self.front == -1:
            print("No element in the circular queue")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

# Driver code 
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
# print("Queue elements", )
obj.printCircularQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCircularQueue()