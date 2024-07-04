class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def traversal(node):
    current = node
    while current is not None:
        print(current.data, end=" ")
        current = current.next

def search(node,data):
    current = node
    found = 0
    while current is not None:
        if current.data == data:
            print(f"{current.data} is found in the linked list")
            found += 1
        current = current.next
    if found == 0:
        print(f"{data} is not found")

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

first.next = second
second.next = third
third.next = fourth

traversal(first)
search(first,360)