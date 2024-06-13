class Animal:
    leg_count = None

    def __init__(self,leg_count):
        self.leg_count = leg_count
        print(self.leg_count)

    def reproduction(self):
        print(f"leg count: {self.leg_count}")
        print("Gives birth")

class Bird:
    wings = None

    def __init__(self, wings):
        self.wings = wings
        print(self.wings)
    
    
    def ability(self):
        print(f"Wings: {self.wings}")
        print("Fly")

class Unicorn(Animal,Bird):

    def __init__(self,opt):
        pass
    def __init__(self,leg,wings):
        self.leg_count = leg
        self.wings = wings

uni = Unicorn(2,"Yes")
uni.reproduction()
uni.ability()