marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

total_percentage=100*(marks1+marks2+marks3)/300

if(total_percentage>=40 and marks1>=33 and marks2>=32 and marks3>=32):
    print("You are passed",total_percentage)
else:
    print("Try again next year!",total_percentage)

