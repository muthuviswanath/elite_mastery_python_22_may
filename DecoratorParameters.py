def ops(a,b):
    return (a+b)

def decor(func):
    def wrapper(a,b):
        return func(a,b)
    return wrapper

res = decor(ops)
final_out = res(10,20)
print(final_out)