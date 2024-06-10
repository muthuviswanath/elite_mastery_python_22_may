def decor(func):

    def wrap():
        print("==================")
        func()
        print("==================")
    return wrap

def greet():
    print("Hello Shreeya")


def display():
    a = 10
    b = 20
    print("Sum of a and b is: ", (a+b))

f_call = decor(greet)
f_call()
f_call = decor(display)
f_call()