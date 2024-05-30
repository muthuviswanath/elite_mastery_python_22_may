# It is applicable for the entire class and n number of copies will be created for
# n number of objects.

class DisplayUnit:
    dimension = "1920 x 1080 px"
    cost = 20000

    def __init__(self):
        print(self.dimension)

    def display(self):
        self.cost = 23000
        print(self.dimension)

d = DisplayUnit()
d.display()
print(d.dimension)
print(d.cost)

e = DisplayUnit()
print(e.dimension)
print(e.cost)
