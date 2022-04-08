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

Doublelist.push(12)
Doublelist.push(13)
Doublelist.push(14)
Doublelist.push(15)
Doublelist.push(16)

Doublelist.listprint(Doublelist.head)