class Muthu:
    
    def __init__(self) -> None:
        self.brain = Brain()
    
    def perform_action(self):
        self.brain.think()

class Brain:
    
    def think(self):
        print("Muthu is thinking whether to Resign because of coffee or not")

muthu = Muthu()
muthu.perform_action()
del muthu
