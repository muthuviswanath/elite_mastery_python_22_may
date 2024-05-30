# colors= ['red','green','blue']
# myfav = ['idly','vada',[1,2,3,4,5],'cricket']
# print(myfav[2][2])
# print(colors[-1])
# print(colors[1:])
# print(colors[:-2])
# print(colors[::-1])

# # Operations

# lst = ['a','b','b','c']
# print(lst*2)
# numlst = [1,2,3,4,5]
# print(numlst*5)

# print(lst[2] * 3)

# print(34 in numlst)

# for i in range(len(numlst)):
#     print(numlst[i], end=' ')

# for ele in numlst:
#     print(ele)

# #List Comprehension

# ls = [1,2,3,4,5]
# for i in range(len(ls)):
#     print( ls[i] * 5)

# #Create a new list
# multiples = [5**i for i in range(1,6)]
# print(multiples)

# Fun
# len()
# max()
# min()
# sum()
# sorted()
# list()
# any()
# all()

lst = [2,5,3,7,1,8]

# Methods of List

# append() - To add elements to the existing list
# insert() - To insert an element at a specific index. If  invalid index give, it just appends
# remove() - To remove
# pop() - To pop
# clear() - To clear the entire list
# index() - To retireve the index value of an element
# count() - To display the repeated element count
# sort() - To permanently sort the list
# reverse() - To print the list in reverse order

lst.append("item")
print(lst)

lst.insert(100,'Tel')
print(lst[7])

print(lst)
lst.remove('Tel')
print(lst)

lst.insert(100,'Tel')
lst.insert(100,'Max')
lst.insert(100,'Tel')
lst.insert(100,'Tel')
print(lst)
lst.remove('Tel')
print(lst)

lst.pop(2)
print(lst)

lst.remove(2)
print(lst)

print(lst.count('Tel'))
