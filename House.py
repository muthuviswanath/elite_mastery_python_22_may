class House:

    color = None
    size = None

    def __init__(self,color,size):
        self.color = color
        self.size = size
    
    def display(self):
        pass

class MuthuHouse(House):

    def __init__(self, color, size):
        self.color = color + " Color"
        self.size = size + " BHK"
    
    def display(self):
        print(f" Muthu's house is {self.color} and he lives in {self.size}")
    
    def share(self):
        print("We share everything in the house and life")

class RoopaHouse(MuthuHouse):
    pass


rhouse = RoopaHouse('Pink','4')
rhouse.display()
rhouse.share()