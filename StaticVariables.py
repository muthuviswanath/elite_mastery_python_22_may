# The value of the variable remains the same for the entire class and if modified, it
# is applicable for all the objects in the class going forward

# Where to create the static variable:
# 1. Inside the constructor using the class name
# 2. Inside the instance method using class name
# 3. Inside the classmethod (annotated method) using class name or cls variable 
# 4. Inside the static method (annotated method) using class name

class Laptop:
    price = 10000
    def __init__(self):
        # 1. Inside the constructor using the class name
        Laptop.model = "Lenovo Thinkpad"

    def display(self):
        # 2. Inside the instance method using class name
        Laptop.ram_size = "64 GB"
    
    @classmethod
    def show(cls):
        # 3. Inside the classmethod (annotated method) using class name or cls variable 
        Laptop.screen_size = "15 inches"
        cls.color = "Slate Grey"
    
    @staticmethod
    def running():
        # 4. Inside the static method (annotated method) using class name
        Laptop.price = 56433.56


lenovo = Laptop()

print(Laptop.model)
lenovo.display()
print(Laptop.ram_size)
Laptop.show()
print(Laptop.screen_size)
print(Laptop.color)
lenovo.running()
print(lenovo.price)

dell = Laptop()
Laptop.price = 99999
print(f"price of dell laptop: {dell.price}")
print(f"price of dell laptop: {lenovo.price}")


    
