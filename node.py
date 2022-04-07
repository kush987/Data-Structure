# Creation of Node
class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None

#Data
e1 = Node('code')
e2 = Node('with')
e3 = Node('Kushal')
e4 = Node('learn')
e5 = Node('more')
# next 

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

value = e1

while value:
    print(value.dataval)
    value = value.nextval
print("******Program complete******")
