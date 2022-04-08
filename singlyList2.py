#Add Node at the Begining of the list 
#Add Node at the End of the list
#<<<-----Solution------>>>#

class Node:
    def __init__(self,dataval) -> None:
        self.dataval = dataval
        self.nextval = None

class Linkedlist:
    def __init__(self):
        self.headval = None
    

    def AtBegin(self, newdata): # Add node at the begining of the list
        self.newNode = Node(newdata)     

        #  Update the new nodes next val to existing node
        self.newNode.nextval = self.headval
        self.headval= self.newNode

    def AtEnd(self, newdata): #Add node at the End of list
        self.newNode1 = Node(newdata)
        if self.headval is None:
            self.headval = self.newNode1
            return
        self.last = self.headval
        while self.last.nextval:
            self.last = self.last.nextval
        self.last.nextval = self.newNode1

    # def Inbtw(self, mid, newdata):
    #     newNode = Node(newdata)
    #     if mid is None:
    #         print("The node is absent")
    #         return
        
    #     newNode.nextval = mid.nextval
    #     mid.nextval = self.last.nextval


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

list.AtBegin("Sun")

list.AtEnd("Sat")
# list.Inbtw(list.headval.nextval,"Fri")


list.printVal()