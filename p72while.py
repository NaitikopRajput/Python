while True:
    print("Enter (+) to Add")
    print("Enter (-) to Subtraction")
    print("Enter (*) to Multiply")
    print("Enter (/) to Divide")
    print("Enter (e) to")

    opt=input("Enter Option =>")

    if opt=="+":
        n1=int(input("Enter Number =>"))
        n2=int(input("Enter Number =>"))
        print("Ans =",n1+n2)
    elif opt=="-":
        n1=int(input("Enter Number =>"))
        n2=int(input("Enter Number =>"))
        print("Ans =",n1-n2)
    elif opt=="*":
        n1=int(input("Enter Number =>"))
        n2=int(input("Enter Number =>"))
        print("Ans =",n1*n2)
    elif opt=="/":
        n1=int(input("Enter Number =>"))
        n2=int(input("Enter Number =>"))
        print("Ans =",n1+n2)
    elif opt=="e":
        break
    else:
        print("Wrong")