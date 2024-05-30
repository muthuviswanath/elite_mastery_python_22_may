people = {}
size = int(input("enter the num of people:"))
for i in range(size):
    person_name = input("enter the person name:")
    weight = float(input("enter the weight:"))
    height = float(input("enter the height:"))
    people[person_name] = {}
    people[person_name]["weight"] = weight
    people[person_name]["height"] = height
print("People List")
print(people)


overweight = {}
underweight = {}
fit = {}
bmi = 0
for key,val in people.items():
    bmi = (val['weight'])/(val['height']**2) * 10000
    if bmi < 18.5:
        underweight.update({key:"Underweight"})
    elif 18.5 <= bmi <24.9:
        fit.update({key:"Fit"})
    else:
        overweight.update({key:"Overweight"})

print("Underweight Candidates: ")
print(underweight)
print("Overweight Candidates: ")
print(overweight)
print("Fit Candidates: ")
print(fit)