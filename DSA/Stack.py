def create_stack():
    stack = []
    return stack

def is_stack_empty(stack):
    return len(stack)==0

def push(stack, element):
    stack.append(element)
    print(f"Added the element {element} into the stack")

def pop(stack):
    if is_stack_empty(stack):
        print("Cannot delete element from empty stack")

    return stack.pop()

my_stack = create_stack()
push(my_stack,12)
push(my_stack,14)
push(my_stack,15)
push(my_stack,12)
print(my_stack)
print("Elements after popping")
pop_ele = pop(my_stack)

print(my_stack)
print(f"The popped element from the stack is: {pop_ele}")
