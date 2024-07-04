class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data,end =" ")
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data,end =" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
    
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data,end =" ")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
print("In Order Traversal")
root.in_order_traversal()
print()
print("Pre Order Traversal")
root.pre_order_traversal()
print()
print("Post Order Traversal")
root.post_order_traversal()


    