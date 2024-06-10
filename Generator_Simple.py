def counter():
    i = 1
    while i<= 10:
        yield f"Even - {i}"
        i += 1

my_lst = list(counter())
print(my_lst)
    