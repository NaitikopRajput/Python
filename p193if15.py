age=int(input("Enter age =>"))
gender=input("Enter gender =>")

if age>=18 and age <30 and gender=="M":
    print("You Wage per day is 700")
elif age>=18 and age <30 and gender=="F":
    print("You Wage per day is 750")
elif age>30 and age<40 and gender=="M":
    print("You Wage per day is 800")
elif age>30 and age<40 and gender=="F":
    print("You Wage per day is 850")

