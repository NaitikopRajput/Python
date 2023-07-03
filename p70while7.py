while True:
    print("Press 1 to know the sqare of numbers")
    print("press 2 to know the cube of numbers")
    print("press 3 for exit")
    op=int(input("Enter Option =>"))

    if op==1:
        n1=int(input("Enter Number =>"))
        print(n1,"--",n1*n1)
    elif op==2:
        n1=int(input("Enter Number =>"))
        print(n1,"--",n1*n1*n1)
    elif op==3:
        break
    else:
        print(" Wrong Opt ")