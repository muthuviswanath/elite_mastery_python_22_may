colors= ['red','green','blue']
myfav = ['idly','vada',[1,2,3,4,5],'cricket']
print(myfav[2][2])
print(colors[-1])
print(colors[1:])
print(colors[:-2])
print(colors[::-1])

# Operations

lst = ['a','b','b','c']
print(lst*2)
numlst = [1,2,3,4,5]
print(numlst*5)

print(lst[2] * 3)

print(34 in numlst)

for i in range(len(numlst)):
    print(numlst[i], end=' ')

for ele in numlst:
    print(ele)

#List Comprehension

ls = [1,2,3,4,5]
for i in range(len(ls)):
    print( ls[i] * 5)

#Create a new list
multiples = [5**i for i in range(1,6)]
print(multiples)

#
# len()
# max()
# min()
# sum()
# sorted()
# list()
# any()
# all()

lst = [2,5,3,7,1,8]
print(sorted(lst))
print(lst)

lst.sort()
print(lst)