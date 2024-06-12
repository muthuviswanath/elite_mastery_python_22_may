class Humans:
    def __init__(self) -> None:
        self.name = "Modi"
        self.position = "Prime Minister"
    
    def display(self,name):
        self.name = name
        print(f"{self.name} is our {self.position}")

class Muthu(Humans):
    pass

m = Muthu()
print(m.name);print(m.position)
m.display("Shreeya")