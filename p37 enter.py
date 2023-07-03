print("Enter number 1 to find area of triangle")
print("Enter 2 to find circumference of circle")

op=int(input("Enter Option =>"))

if op==1:
    height=int(input("Enter height of triangle =>"))
    base=int(input("Enter base of triangle =>"))
    print("Area of triangle =",height*base*0.5)
elif op==2:
    radius=int(input("Enter radius of circle =>"))
    print("Circumference of the circle is =",radius*3.14*2)
elif op==3:
    number=int(input("Enter number"))
    if number<0:
        print("it is a negative value")
    else:
        print("It is a posetive value")
else:
    print("Wrong option")