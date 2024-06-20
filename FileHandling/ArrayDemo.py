import array
numarray = array.array('i',[1,2,3,4,5])
print(numarray)

print(array.typecodes)
print(numarray.typecode)
print(numarray.itemsize)
numarray.append(10)
print(numarray)
numarray.append(10)
print(numarray)
numarray.append(10)
print(numarray)
print(numarray.count(10))
my_favnum = [100,200,300,400,500]
my_fav_people = (22,33,44,55,66)
my_diction = {234,567}
numarray.extend(my_favnum)
print(numarray)
numarray.extend(my_fav_people)
print(numarray)
numarray.extend(my_diction)
print(numarray)
numarray.fromlist([5,10,15,20,25])
print(numarray)
unicode_array = array.array('u','\u0C86')
print(unicode_array)
print(numarray.index(400))
numarray.insert(11,999999)
print(numarray)
#  removes the element at the index value
numarray.pop(11)
print(numarray)
#  removes the element at the last
numarray.pop()
print(numarray)
numarray.remove(10)
print(numarray)
numarray.reverse()
print(numarray)
lstarr = numarray.tolist()
print(type(numarray))
print(type(lstarr))

# iterating the arrays
# printing the array elements based on the index value:
print(numarray[5])
print(numarray[5:11])

shreeya_array = array.array('i',[3,9,12])
temp_arr = numarray+shreeya_array
print(temp_arr)

#Arithmetic Operations on array
print(temp_arr * 2)

for i in temp_arr:
    print(i*2, end=" ")
print()
print(numarray[3:0:-1])

