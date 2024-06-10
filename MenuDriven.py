while True:
    print("1. Create Tuple")
    print("2. Modify Tuple Elements")
    print("3. Exit")
    choice = int(input("Enter your Choice[1/2/3]: "))
    if choice == 1:
        list_count = int(input("Enter the number of lists to be created"))
        for i in range (1,list_count+1):
            items = int(input(f"Enter the number of values to be stored in the {i} List: "))
            temp_lst = []
            for j in range (items):
                item = input("Enter the items: ")
                temp_lst.append(item)
        my_tup = tuple(temp_lst)
    print(my_tup)
