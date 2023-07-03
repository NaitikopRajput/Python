print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter option =>"))

if op==1:
    number=int(input("Enter Number one =>"))
    print("Sqare of number is =",number*number)
elif op==2:
    number = int(input("Enter Number one =>"))
    print("Cube of number is =",number*number*number)
else:
    print("Wrong option")