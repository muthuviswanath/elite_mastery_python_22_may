# Declaration of Instance Variables:
#    1. Inside the constructor using self keyword
#    2. Inside the instance method using self keyword
#    3. Outside the class by using the object reference variable

class Mouse:

    def __init__(self):
        #    1. Inside the constructor using self keyword
        self.no_of_buttons = 2
    
    def display(self):
        #    2. Inside the instance method using self keyword
        self.manufacturer = "Zebronics"
    
m = Mouse()
#    3. Outside the class by using the object reference variable
m.type = "Wireless Mouse"


mse = Mouse()
print(mse.no_of_buttons)

print(mse.manufacturer)
print(mse.type)


