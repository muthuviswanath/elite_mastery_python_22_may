import os
os.getcwd()

os.chdir("D:\\Elite_Python_May2024\\FileHandling\\")
my_file = open("Task.txt")
print(my_file.read())
print(my_file.tell())

for ln in open("Task.txt"):
    print(ln, end='')
    
print()
your_file = open("Task.txt")
print(your_file.readline())
your_file.seek(5)
print(your_file.readlines())


