#Fill a list with the squares of n natural numbers
# where 1<=n<=10


lst = []
for i in range(1,11):
    lst.append(i**2)

print(lst)

numlist = [n**2 for n in range (1,11)]
print(numlist)

lst = [num for num in range(1,100) if num % 3 ==0 and num %5 == 0 ]
print(lst)

# fill the list with all possible odd numbers from 1 till 100
# take another empty list and use list comprehension such that all the prime numbers
# of the previous list is added to the new list