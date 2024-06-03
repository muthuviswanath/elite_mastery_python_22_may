
student = {}
n = int(input("Enter the number of recordsto be stored"))
for i in range(n):
    name = input("Enter the student name")
    score = int(input("Enter the score"))
    student.update({name:score})
outstanding = {}
exceeds_expectations={}
acceptable={}
fail={}
for key,value in student.items():
    if student[key] > 90:
        outstanding.update({key:"Outstanding"})
    elif 80 < student[key] <=90:
        exceeds_expectations.update({key:"exceeds expectations"})
    elif 70 < student[key] <=80:
        acceptable.update({key:"acceptable"})
    else:
        fail.update({key:"fail"})

print(outstanding)
print(exceeds_expectations)
print(acceptable)
print(fail)