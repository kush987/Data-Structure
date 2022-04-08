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

    def insert(self, prev, newVal):
        if prev is None:
            return
        newNode = Node(newVal)
        newNode.next = prev.next
        prev.next = newNode
        newNode.prev = prev
        if newNode.next != None:
            newNode.next.prev = newNode

    def listprint(self, node):
        while node != None:
            print(node.data),
            last = node
            node = node.next

d = double_linked()
d.push("Cat")
d.push("Dog")
d.push("Bird")
d.insert(d.head.next, "Horse")
d.listprint(d.head)