a = int(input("Enter the value of a: "))
b = int(input("Enter the value of a: "))

try:
    print(a/b)
    h = [10,20,30,40]
    print(h[55])
except (IndexError, ZeroDivisionError):
    print("Exception Occurred")

c = a*a
print(f"Square of a: {c}")