class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class double_linked:
    def __init__(self):
        self.head = None

    #Adding the elements
    def push(self, newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode

    def listprint(self, node):
        while node:
            print(node.data),
            last = node
            node = node.next

Doublelist = double_linked()
items = [12,13,14,15,16]
for i in items:
    Doublelist.push(i)


Doublelist.listprint(Doublelist.head)