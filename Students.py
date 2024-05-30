students = {}
size = int(input("enter the num of students:"))
for i in range(size):
    stu_name = input("enter the student name:")
    course = input("enter the course name he/she opted for:")
    course_fees = int(input("enter the fees of the course:"))
    students[stu_name] = {}
    students[stu_name]["course"] = course
    students[stu_name]["fees"] = course_fees
    
print("students_dictionary:")
print(students)
result = {}
for key,val in students.items():
    if isinstance(val,dict):
        if val["course"] == "python":
            result.update({key:val})
print (result)