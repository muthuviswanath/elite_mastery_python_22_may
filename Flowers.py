
class Flower:
    
    def __init__(self) -> None:
        self.nectar = Nectar()

    def produce(self):
        return self.nectar

class Nectar:
    pass

class HoneyBees:

    def __init__(self, nectar) -> None:
        print(id(nectar))
        self.honey = Honey()
        print("Converted the nectar into Honey")
        print(id(self.honey))

    def produce(self):
        return self.honey
class Honey:
    pass


f = Flower()
nectar = f.produce()
print("Nectar Produced by the flower: ")
print(id(nectar))

print("Nectar  consumed by Honeybee")
hbee = HoneyBees(nectar)
honey = hbee.produce()
print(f"Honey consumed by the humans {id(honey)}")
