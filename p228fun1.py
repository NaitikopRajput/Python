def add():
    v1=int(input("Enter Number 1 =>"))
    v2=int(input("Enter Number 2 =>"))
    print("Add = ",v1+v2)

def table():
    v1=int(input("Enter Number =>"))
    for x in range(1,11):
        print(v1,"X",x,"=",v1*x)

def odev():
    v1=int(input("Enter Number =>"))
    if v1%2==0:
        print(v1,"is even")
    else:
        print(v1,"is odd")

def povneg():
    v1=int(input("Enter Number =>"))
    if v1<0:
        print(v1,"is negative number.")
    else: 
        print(v1,"is positive number.")

def tri():
    h=int(input("Enter Height of triange =>"))
    b=int(input("Enter Base of triange =>"))
    print("Area of Trianle =",h*b*0.5)


def cir():
    rad=int(input("Enter radius of circle =>"))
    print("Area of circle =",rad*rad*0.5)

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)











































num = int(input("Enter Number =>"))
print("Factorial of",num,"is",factorial(num))

def primeno():
    num-int(input("Enter Number =>"))
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

print("Press 1 for adding two numbers")
print("Press 2 for knowing table of any Number")
print("Press 3 for knowing the number is odd or even")
print("Press 4 for knowing the number is posetive and negative")
print("Press 5 for knowing the triangle area")
print("Press 6 for knowing the circle area")
print("Press 7 for knowing the factorial of any number")
print("Press 8 for knowing the number is prinme number or not")

opt=int(input("Enter option =>"))

if opt==1:
    add()
elif opt==2:
    table()
elif opt==3:
    povneg()
elif opt==4:
    tri()
elif opt==5:
    cir()
elif opt==6:
    factorial()
elif opt==7:
    primeno()
else:
    print("Wrong option")


