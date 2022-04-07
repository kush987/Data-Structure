#####Linked List#####

class Node:
    def __init__(self,dataval) -> None:
        self.dataval = dataval
        self.nextval = None

class Linkedlist:
    def __init__(self):
        self.headval = None
    
    def printVal(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval
            

list = Linkedlist()

list.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
e4 = Node('Thu')

list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4

list.End("Fri")

list.printVal()