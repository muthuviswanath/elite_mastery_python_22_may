import array
narr = array.array("i",[1,2,3,4,5,6,7,8,9,10])
# f_array = int(input("Enter the size of first array"))
# print(f"Elements of First Array:\n {narr[:f_array]}")
# print(f"Elements of Second Array:\n {narr[f_array:]}")


def split_arr(arr,n):

    if(len(arr) >= n):
        lst = []
        for i in range (1,n+1):
            elem = int(input(f"Enter the element to be store in array {i}:  "))
            for j in range(elem):
                lst[i] = arr[:elem]

a = [1,2,3,4,5,6,7]
split_arr(a,2)
        


n = int(input("Enter the elements for the first array: "))
split_arr(narr,n)