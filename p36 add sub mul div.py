print("Enter number 1 to add two numbers")
print("Enter number 2 to subtract two numbers")
print("Enter number 3 to multiply two numbers")
print("Enter number 4 to divide two numbers")
op=int(input("Enter option =>"))

if op==1:
    no1=int(input("Enter number 1"))
    no2=int(input("Enter number 2"))
    print("Addition of both number =",no1+no2)
elif op==2:
    no1 = int(input("Enter number 1"))
    no2 = int(input("Enter number 2"))
    print("Subtraction of both number =", no1-no2)
elif op==3:
    no1 = int(input("Enter number 1"))
    no2 = int(input("Enter number 2"))
    print("Multiplication of both number =", no1*no2)
elif op==4:
    no1 = int(input("Enter number 1"))
    no2 = int(input("Enter number 2"))
    print("Division of both number =", no1/no2)
else:
    print("Wrong option")