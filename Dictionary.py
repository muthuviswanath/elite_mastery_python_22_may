# dct = {"key":"value"}
# employee = {"muthu":{"salary":345345,"desig":"manager"},
#             "shreeya":{"salary":867645,"desig":"manager"},
#             "Roopa":{"salary":345345,"desig":"sales rep"}}



emp_dict = {}
size = int(input("Enter the size of nested dictionary: "))

for i in range(size):
    emp_name = input("Enter the name of the employee: ")

    emp_dict[emp_name] = {}
    salary = int(input("Enter the salary: "))
    designation = input("Enter the designation: ")
    emp_dict[emp_name]["salary"] = salary
    emp_dict[emp_name]["designation"] = designation

# printing original dictionary
print("The original dictionary is : \n" + str(emp_dict))

# Maximum Value in Nested Dictionary
# Using loop
result = {}
max = 0
for key,val in emp_dict.items():
   if isinstance(val,dict):
       if val["designation"] == "Manager":
           pass
if val["salary"] > max:
   max = val["salary"]

for key,val in emp_dict.items():
   if isinstance(val,dict):
       if val["designation"] == "Manager" and val["salary"] == max:
           result.update({key: val})
print(result)