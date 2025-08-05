marks=int(input("Enter your marks:"))

if(marks<=100 and marks>=90):
    grade="A++"

elif(marks<90 and marks>=80):
    grade="A"

elif(marks<80 and marks>=70):
    grade = "B"


print(grade)