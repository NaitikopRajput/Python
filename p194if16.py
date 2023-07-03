ser=int(input("From how much years you are working =>"))
salary=int(input("Enter Your Salary =>"))
bonus=salary//20

if ser>5:
    print("You salary is now =",salary+bonus)
else:
    print("You salary remains =",salary)