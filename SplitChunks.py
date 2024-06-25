import array
def array_chunker():
    # Example usage:
    arr = array.array("i",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    arr_count = int(input("Enter the number of arrays you want to split it into: "))
    remaining_arr = arr_count - 1
    arr_len = len(arr)
    remaining = arr_len
    chunker_list = []

    if arr_len > arr_count:
        for i in range(1, arr_count + 1):
            element_count = int(input(f"Enter the number of elements to be stored in array {i}: "))
            remaining -= element_count
            if remaining >= remaining_arr:
                chunk = arr[sum(len(chunk) for chunk in chunker_list):sum(len(chunk) for chunk in chunker_list) + element_count]
                chunker_list.append(chunk)
                remaining_arr -= 1
            else:
                print("Not Possible to split the arrays")
                break
    else:
        print("Cannot split")

    for chunk in chunker_list:
        print(f"[{', '.join(str(x) for x in chunk)}]")
    # print(chunker_list)

array_chunker()