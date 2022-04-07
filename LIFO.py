def create_stack():
    stack = []
    return stack


#checking the stack is empty
def check_empty(stack):
    return len(stack) == 0

# add the items into a stack
def push(stack, item):
    stack.append(item)
    print("New item is push into a stack: " + item)

# delete the items into a stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"

    return stack.pop()

stack = create_stack()


#items that are push and pop from the stack
items = [1,2,3,4,5]
for i in items:
    push(stack, str(i))

print("Stack items: ", stack)
print("Popping the stack item: ", pop(stack))
print("stack after poping the items", str(stack))