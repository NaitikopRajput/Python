print("Enter 1 if you want to take xerox")
print("Enter 2 if you want to use typewriter ")
print("Enter 3 if you want to do Both")
op=int(input("Enter Option =>"))
totalxerox=0
typetotal=0
if op==1:
    print("If you want to print more than 50 pages then it will cost 5 rupees")
    print("If you want to print less than 50 pages then it will cost 7 rupees")
    xerox=int(input("How much pages you want to xerox ?"))
    if xerox<50:
        print("bill = ",xerox*7)
        totalxerox=xerox*7
    else:
        print("bill =",xerox*5)
        totalxerox=xerox*5
elif op==2:
    print("if you want to type more than 50 pages you have to pay 5 rupees")
    print("if you want to type less than 50 pages you have to pay 7 rupees")
    type=int(input("How much page you want to type ?"))
    if type<50:
        print("Your bill is",type*7)
        typetotal = type * 7
    else:
        typetotal=type*5
        print("Your bill is", type * 7)
elif op==3:
            value1=0
            value2=0
            print("if you want to type more than 50 pages you have to pay 5 rupees")
            print("if you want to type less than 50 pages you have to pay 7 rupees")
            print("---------------------------------------------------------------")
            print("If you want to print more than 50 pages then it will cost 5 rupees")
            print("If you want to print less than 50 pages then it will cost 7 rupees")
            print("---------------------------------------------------------------")
            xerox = int(input("How much pages you want to xerox ?"))
            print("------------------------------------------------")
            type = int(input("How much page you want to type ?"))
            if xerox<50:
                print("this is your total for xerox",xerox*7)
                value1=xerox*7
            else:
                print("this is your total for xerox",xerox*5)
                value1=xerox*5
            if type < 50:
                    print("this is your total for xerox", type*7)
                    value1 = type*7
            else:
                    print("this is your total for xerox", type*5)
                    value2 = type*5
            print("your total is ",value1+value2)