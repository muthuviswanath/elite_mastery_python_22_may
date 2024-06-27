a = int(input("Enter the value of a: "))
b = int(input("Enter the value of a: "))

try:
    if (b==0):
        raise
    else:
        print(a/b)
except IndexError:
    print("Index error")
except ZeroDivisionError:
    print("Cannot perform division. Error with input")