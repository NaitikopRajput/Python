experience=int(input("Enter How Much Experience You Have =>"))
salary=float(input("What Is You Salary =>"))

if experience>10:
    print("You Will Get '10%' Bonus In Your Salary")
    print("Your Salary Is now => ",salary*0.10)
elif experience>=6 and experience<=10:
    print("You Will Get '8%' Bonus In Your Salary")
    print("Your Salary Is now => ",salary*0.8)
elif experience<6:
    print("You Will Get '5%' Bonus In Your Salary")
    print("Your Salary Is now: ",salary*0.5)

