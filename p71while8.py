while True:
    print("Enter 1 to add")
    print("Enter 2 to Subtract")
    print("Enter 3 to Multiply")
    print("Enter 4 to Divide")
    print("Enter 5 to exit")

    opt=int(input("Enter Option"))

    
    if opt==1:
        n1=int(input("Enter Nuumber =>"))
        n2=int(input("Enter Nuumber =>"))
        print("Answer =",n1+n2)
    elif opt==2:
        n1=int(input("Enter Nuumber =>"))
        n2=int(input("Enter Nuumber =>"))
        print("Answer =",n1-n2)
    elif opt==3:
        n1=int(input("Enter Nuumber =>"))
        n2=int(input("Enter Nuumber =>"))
        print("Answer =",n1*n2)
    elif opt==4:
        n1=int(input("Enter Nuumber =>"))
        n2=int(input("Enter Nuumber =>"))
        print("Answer =",n1/n2)
    elif opt==5:
      break

